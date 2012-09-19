#!/usr/bin/python2

import argparse
import fileinput

parser = argparse.ArgumentParser(description='Process some numbers.')
args = parser.parse_args()

condition = 1
ans = 1
while(condition == 1):

	try:
		x = raw_input()
		y = float(x)
		ans = y * ans

	except EOFError:
		print "^D"
		if ans != 1:
			print ans
		condition = 0

	except ValueError:
		if x == '':
			print ans
			ans = 1
			continue
		else:
			print "could not convert string to float: ", x
			condition = 0
