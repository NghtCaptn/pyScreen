import sys, string, os, subprocess, urllib3, json, time
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
print("**********************************************************************")
print("*                            pyScreen 0.1                            *")
print("**********************************************************************")


'''
define screen shot function
'''

def screenShot(source, encode):
	i = 1
	j = 10
	while i <= 6:
		ts = round(time.mktime(time.localtime()))
		sourceScreen = subprocess.check_call("ffmpeg.exe -ss 00:{3}:00 -t 1 -i {0} -vframes 1 source-{2}-{1}.png".format(source, ts, i, j))
		encodeScreen = subprocess.check_call("ffmpeg.exe -ss 00:{3}:00 -t 1 -i {0} -vframes 1 encode-{2}-{1}.png".format(encode, ts, i, j))
		i += 1
		j += 5
	print("Screenshots Generated Successfully!")

source = input("Enter your Source Location: ")
type(source)
encode = input("Enter your Encode Location: ")
type(encode)

screenShot(source, encode)




