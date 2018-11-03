import subprocess, time, argparse, uuid
'''
MIT License

Copyright (c) 2018 NghtCaptn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

parser = argparse.ArgumentParser(prog='pyScreen.py', description='Script that generates screenshots for a video file using ffmpeg', usage='%(prog)s FILE PATH -t 1 or 2 -n for number of screen shots')
parser.add_argument('location', metavar='FULL PATH TO LOCATION', help='File Location')
parser.add_argument('-l', metavar='FULL PATH TO 2ND SOURCE FILE', help='2nd File Location',)
parser.add_argument('-t', help='denotes which config you want, 1 for single source 2 for double source', required=True)
parser.add_argument('-n', help='number of screen shots for single source', required=True)

print("**********************************************************************")
print("*                            pyScreen 0.1                            *")
print("**********************************************************************")


'''
define screen shot function
'''

def single(fileLocation, x):
	i = 0
	j = 10
	x = int(x)
	y = 0
	for i in range(x):
		if j <= 60:
			j = j - 60
			y = 1
		ts = str(uuid.uuid4().int)[:4]
		screen = subprocess.check_call("ffmpeg -ss {4}:{3}:00 -t 1 -i \"{0}\" -vframes 1 frame-{2}-{1}.png".format(fileLocation, ts, i, j, y))
		i += 1
		j += 5
	print("Screenshots generated Successfully!")

def encSor(source, encode, x):
	i = 0
	j = 10
	x = int(x)
	y = 0
	for i in range(x):
		if j <= 60:
			j = j - 60
			y = 1
		ts = str(uuid.uuid4().int)[:4]
		sourceScreen = subprocess.check_call("ffmpeg -ss {4}:{3}:00 -t 1 -i \"{0}\" -vframes 1 source-{2}-{1}.png".format(source, ts, i, j, y))
		encodeScreen = subprocess.check_call("ffmpeg -ss {4}:{3}:00 -t 1 -i \"{0}\" -vframes 1 encode-{2}-{1}.png".format(encode, ts, i, j, y))
		i += 1
		j += 5
	print("Screenshots Generated Successfully!")

args = parser.parse_args()


location1 = args.location
if args.t == "1":
	x = args.n
	single(location1, x)
	print("Screen Shots for single source created")

if args.t == "2":
	encSor(location1, args.l)




