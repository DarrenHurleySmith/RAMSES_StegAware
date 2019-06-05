# Swagger API Reference: https://ramses.treelogic.com/ramses-1.0.0/swagger-ui.html#!/steganography45controller/getResultbyIdUsingGET
# Integration Guide: https://docs.google.com/document/d/1ilqehwkQdfhgymgvWMyZFWwp0jc_wfLF3CDrXCfzAlk/edit#

import stegtool_swagger_wrapper as swag
import stegtool_utils as utils
import json
import time
import getpass
import csv
import base64
import random
import subprocess
import pyexifinfo as p
import os
import pandas as pd
from pathlib import Path

from OurSecret.OurSecret import ourSecret
from Pixelknot.PixelKnot import pKnot
from BDV.BDVScanner import BDV
from OmniHide.OmniHide import omniHide


def authenticate(usr,pswrd):
	token = ""
	return token

		
def run_tool(idir, odir, v_algo, i_algo, rec):
	seshId = str(random.getrandbits(128))

	with open(str(odir) + '/' + str(seshId) + '_stegResults.csv', mode='w') as results_file:
		csvwriter = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csvwriter.writerow(['Filename', 'Steganography Present', 'Steganography Algorithm', 'Signature'])

	with open(str(odir) + '/' + str(seshId) + '_metaData.csv', mode='w') as meta_file:
		csvwriter = csv.writer(meta_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csvwriter.writerow(['Filename', 'file type', 'file size', 'file modify date', 'file access date', 'dimensions'])

	if rec == False:
		for r, d, f in os.walk(idir):
			for file in f:
				filename = r + '/' + file
				with open(str(odir) + '/' + str(seshId) + '_stegResults.csv', mode='a') as results_file:
					csvwriter = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

					for algo in v_algo:
						if algo == 'OurSecret':
							ourSecret(filename, csvwriter)
						if algo == 'BDV':
							BDV(filename, csvwriter)
						if algo == 'OmniHide':
							omniHide(filename)

					for algo in i_algo:
						if algo == 'PixelKnot':
							pKnot(filename, csvwriter)

				metadata(filename, odir, seshId)

	elif rec == True:
		for filename in Path(idir).glob('**/*.*'):
			with open(str(odir) + '/' + str(seshId) + '_stegResults.csv', mode='a') as results_file:
				csvwriter = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

				for algo in v_algo:
					if algo == 'OurSecret':
						ourSecret(filename, csvwriter)
					if algo == 'BDV':
						BDV(filename, csvwriter)
					if algo == 'OmniHide':
						omniHide(filename, csvwriter)

				for algo in i_algo:
					if algo == 'PixelKnot':
						pKnot(filename, csvwriter)

			metadata(filename, odir, seshId)

	results_merge(odir, seshId)

	print('Testing complete, please find results in ' + str(odir))


def metadata(f, odir, seshId):
	if '.jpg' or '.JPG' or '.jpeg' or '.JPEG' or '.png' or '.PNG' or '.MP4' or '.mp4' in f:
		# print(f)
		with open(str(odir) + '/' + str(seshId) + '_metaData.csv', mode='a') as meta_file:
			csvwriter = csv.writer(meta_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

			m = p.get_json(f)
			csvwriter.writerow([f, m[0]['File:FileType'], m[0]['File:FileSize'], m[0]['File:FileModifyDate'], m[0]['File:FileAccessDate'], m[0]['Composite:ImageSize']])


def results_merge(odir, seshId):
	a = pd.read_csv(str(odir) + '/' + str(seshId) + '_metaData.csv')
	b = pd.read_csv(str(odir) + '/' + str(seshId) + '_stegResults.csv')
	merged = a.merge(b, on='Filename')
	merged.to_csv(str(odir) + '/' + str(seshId) + '_Results.csv', index=False)
	# doesn't work yet, keep looking at ways to drop duplicates that do not have Steg
	# df = pd.read_csv(str(odir) + '/' + str(seshId) + '_Results.csv').drop_duplicates(keep='first').reset_index()
	# df.to_csv(str(odir) + '/' + str(seshId) + '_Results.csv', index=False)