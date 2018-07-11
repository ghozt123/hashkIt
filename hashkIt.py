#! /usr/bin/python2.7

""" 

hashkIt.py: Core module

Version: 1.0.0
Author: wil.tor
License: https://opensource.org/licenses/GPL-3.0

"""

import os 
import sys
import hashlib
import argparse

global res

# Colors ...
W = '\033[0m'   # white
R = '\033[31m'  # red
O = '\033[33m'  # orange
G = '\033[32m'  # green		
B = '\033[34m'  # blue
C = '\033[36m'  # cyan

header = C + """.__                  .__     __   .___  __   
|  |__ _____    _____|  |__ |  | _|   |/  |_ 
|  |  \\__  \  /  ___/  |  \|  |/ /   \   __|
|   Y  \/ __ \_\___ \|   Y  \    <|   ||  |  
|___|  (____  /____  >___|  /__|_ \___||__|  
     \/     \/     \/     \/     \/   
""" + O + "Developed by wil.tor in 2018\n"+ W + "Small hash module written for multiple " + G + "hash operations\n"  # header

def get_res(hashtype, cleartext): 
	if hashtype == "md5":
		res = hashlib.md5(cleartext)
		print(B+"[+] Hash format ==> "+W+"{}".format(res.hexdigest()))
	elif hashtype == "sha1":
		res = hashlib.sha1(cleartext)
		print(B+"[+] Hash format ==> "+W+"{}".format(res.hexdigest()))
	elif hashtype == "sha256":
		res = hashlib.sha256(cleartext)
		print(B+"[+] Hash format ==> "+W+"{}".format(res.hexdigest()))
	elif hashtype == "sha512":
		res = hashlib.sha512(cleartext)
		print(B+"[+] Hash format ==> "+W+"{}".format(res.hexdigest()))
	elif hashtype == "sha384":
		res = hashlib.sha384(cleartext)
		print(B+"[+] Hash format ==> "+W+"{}".format(res.hexdigest()))
	elif hashtype == "sha224":
		res = hashlib.sha224(cleartext)
		print(B+"[+] Hash format ==> "+W+"{}".format(res.hexdigest()))
	else:
		print(C+"[-] Unknown hash format, try again"+W)
		exit(1) 

if __name__ == "__main__":
	os.system("clear")
	print(header)
	parser = argparse.ArgumentParser()
	parser.add_argument("--hash", type=str, help="text to hash operation ==>")
	parser.add_argument("--hashtype", type=str, help="hash type for hash clear text ==>")
	args = parser.parse_args()

	if args.hash:
		if args.hashtype:
			get_res(args.hashtype, args.hash)
	else:
		print(C+"[-] Please, specify the hash_type and give the clear_text"+W)
		sys.exit(1)
