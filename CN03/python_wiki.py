#!/usr/bin/env python3

import argparse
import requests
import time
import sys


parser = argparse.ArgumentParser()

parser.add_argument("-f", "--fname", help = "Enter file name ", default="default_log.txt")
parser.add_argument("word", nargs="+")

args=parser.parse_args()


word=args.word[0]
n = len(args.word)
i = 1 

while i<n:
	word+="_"+args.word[i]
	i += 1


url = "https://en.wikipedia.org/wiki/" + word

response = requests.get(url)

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush() 

sys.stdout.write("#"*10+"33%\r")
time.sleep(1)
sys.stdout.write("#"*30+"66%\r")
time.sleep(1.3)
sys.stdout.write("#"*60+"100%")
print()
print(url)




if response.status_code == 200:
	with open(args.fname, 'a') as f:
		f.write(url)
		f.write("\n")
	print("log is saved in", args.fname)

else:
	print("Enter valid word to search")
	
