#!/usr/bin/python2


import sys, re, argparse, fileinput
from operator import itemgetter
def prnt(list):
	print "DATA\nPARTID\t\tDESCRIPTION\t\tFOOTPRINT\t\tQUANTITY"
	for line in list:
		print line['pid'] + "\t\t" + line['des'] + "\t\t" + line['fpr'] + "\t\t" + line['qua']
	return


def added(str):
	x=str.strip().split('::')
	y.append({'pid' : x[0], 'des' : x[1], 'fpr' : x[2], 'qua' : x[3]})
	print "added item " + str
	return
def removed(str):
	x=str.strip().split('::')
	for entry in y:
		if entry[x[0]]==x[1]:
			y.remove(entry)
	print "removed all occurences of " + str
def enterItem(str):
	x=str.strip().split('::')
	for entry in y:
		try:
			if entry[x[0]]==x[1]:
				entry[x[2]] = x[3]
		except KeyError:
			print "Descriptor does not exist"
			return
	print "set " + x[2] + " as " + x[3] + " in all occurences of " + x[0] + "::" + x[1]
	return
def fnd(str,list):
	x=str.strip().split('::')
	prnt([z for z in list if z[x[0]] == x[1]])
	return
def wrt(str):
	try:
		writeFile = open(args.f[0], 'w')
		for line in y:
			writeFile.write(line['pid'] + "::" + line['des'] + "::" + line['fpr'] + "::" + line['qua']+ "\n")
		writeFile.close()
	except:
		print "didnt work"
	return


def sorted(str):
	x=str.strip().split('::')
	try:
		if len(x) > 1:
			fnd(str.strip().split(x[0] + "::", 1)[1], sorted(y, key=itemgetter(x[0])))
		else:
			prnt(sorted(y, key=itemgetter(x[0])))
	except KeyError:
		print "Descriptor does not exist"
		return
	return
		
total = 1
y = []

parser = argparse.ArgumentParser(description='Manage an electronics inventory')
parser.add_argument('-f', action='store', nargs = 1, default = sys.stdin)
args = parser.parse_args()
thefile = open(args.f[0], 'r')
print args.f[0]
for line in thefile:
	added(line);
thefile.close()
prnt(y)
for line in iter(sys.stdin.readline, ''):
	if re.match('(?:added>).+$', line):
		print(re.fndall('(?<=added>).+$', line))
		added(re.fndall('(?<=added>).+$', line)[0])
	if line.strip() == 'print':
		prnt(y)
	if line.strip() == 'save':
		wrt('test')
	if re.match('(?:removed>).+$', line):
		print(re.fndall('(?<=removed>).+$', line))
		removed(re.fndall('(?<=removed>).+$', line)[0])
	if re.match('(?:enterItem>).+$', line):
		print(re.fndall('(?<=enterItem>).+$', line))
		enterItem(re.fndall('(?<=enterItem>).+$', line)[0])
	if re.match('(?:print>sort>).+$', line):
		print(re.fndall('(?<=print>sort>).+$', line))
		sorted(re.fndall('(?<=print>sort>).+$', line)[0])
	if re.match('(?:^sort>).+$', line):
		print(re.fndall('(?<=^sort>).+$', line))
		sorted(re.fndall('(?<=^sort>).+$', line)[0])



