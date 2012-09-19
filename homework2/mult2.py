#!/usr/bin/python2

import sys
from sys import argv



import argparse
import fileinput

parser = argparse.ArgumentParser(description='Process some numbers.')

parser = argparse.ArgumentParser(description = "Process multiple files")
parser.add_argument('--ignore-blank',dest = 'ignoreblanks',action='store_const',const = file_ignore_blanks, default = error_menu,help='multiplication of two files')
parser.add_argument('--ignore-non-numeric',dest = 'ignorenonnumerics',action='store_const',const = file_ignore_bad, default = error_menu,help='multiplication of two files')
args.ignoreblanks(argv)
args.ignorenonnumerics(argv)


#def 'ignoreblanks'
#def 'ignorenonnumerics' 

args = parser.parse_args()
print(args.accumulate(args.integers))

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








