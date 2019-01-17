# RAMSES_StegAware
Multimedia steganalysis tool developed for the RAMSES platform

RAMSES StegAware

Copyright® University of Kent, Prof. Julio Hernandez-Castro, Dr. Darren Hurley-Smith, and Thomas Sloan. This work is funded by the Horizon 2020 RAMSES project.

Description
This forensic and steganalytic framework provides comprehensive analysis over image and video media and is part of the RAMSES platform. StegAware is a steganalysis tool for multimedia content (image and video) capable of detecting a diverse range of steganographic tools and techniques. The image steganalysis component of this framework uses the Java tool, StegExpose for LSB steganalysis and a series of signature detection methods. The video steganalytic feature of the tool uses signature steganalysis to cover a range of well-known video steganography tools. A feature for metadata forensics has been integrated to provide investigative details. In addition, the tool can integrate with the RAMSES platform and manage resources from its interface.

Quick Start Guide

The following steps can be used for a quick setup of the tool. 


1.0	$cd Desktop
1.1	$git clone https://github.com/UoK424/RAMSES_StegAware.git
1.2	Rename folder to “Ramses”
1.3	$sudo apt install libimage-exiftool-perl
1.4	$sudo apt install mp4v2-utils
1.5	$sudo apt install openjdk-11-jre-headless (or latest version)
1.6	$sudo apt install libdigest-sha3-perl
1.7	Set appropriate privileges for the Ramses directory and Ramses.sh script
1.8	Run the tool with $sudo python3 stegtool.py




*Refer to StegAware user manual for full details of the tool's setup and use.
