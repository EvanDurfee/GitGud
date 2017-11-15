#!/usr/bin/env python3

import argparse
import sys

import subprocess


def confirmYN(r, w):
	while True:
		line = r.readline().lower()
		if "y\n" == line:
			return True
		elif "n\n" == line:
			return False
		else:
			print("Please enter y or n: ", end='', flush=True)


def gud(r, w):
	print('running gud...')
	print("Gud commit! Add comment (or leave blank): ", end='', flush=True)
	line = r.readline()
	if line != "\n":
		print("You gave me: \"" + line[:-1] + "\"")
	else:
		print("You gave me nothing!")

	#TODO: sanitize commit messages

	commitArgs = ["git", "commit"]
	if line != "\n":
		commitArgs += ["-m", line[:-1]]

	argv = commitArgs
	print(argv)
	subprocess.call(argv)




def rekt(r, w):
	print("Are you sure you wish to git rekt? Y/N: ", end='', flush=True)
	answer = confirmYN(r, w)
	if answer:
		subprocess.call(["git", "reset", "--HEAD"])

def spooked():
	print('spooked')

def help():
	print('halp')
	print(sys.argv[0])

