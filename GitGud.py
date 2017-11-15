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
			w.write("Please enter y or n: ")
			w.flush()


def gud(r, w):
	w.write("Gud commit! Add a comment (or leave blank): ")
	w.flush()
	line = r.readline()

	# if line != "\n":
	# 	print("You gave me: \"" + line[:-1] + "\"")
	# else:
	# 	print("You gave me nothing!")

	#TODO: sanitize commit messages?


	commitArgs = ["git", "commit"]
	if line != "\n":
		commitArgs += ["-m", line[:-1]]

	argv = commitArgs
	subprocess.run(argv)


def rekt(r, w):
	w.write("Are you sure you wish to git rekt? Y/N: ")
	w.flush()
	answer = confirmYN(r, w)
	if answer:
		subprocess.run(["git", "reset", "--hard", "HEAD"])

def spooked():
	print('spooked')

def halp():
	print('halp')

