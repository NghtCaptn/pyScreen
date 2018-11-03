# pyScreen
Create a set of screenshots of two video files to compare the two. User can select how many screen shots they want generated for their video files.

# Update 11/2/18 v1.0
Changed unique numbers for .png files, added more options such as chosing between screenshots for a single video file or screenshots for two video files.

## Prequisites 
You need to have ffmpeg installed AND included in your PATH system variable (if running Windows) or the binary finaly included within where pyScreen.py is stored. I have included a precompiled version of ffmpeg in the repository but it highly recommended to add include the location of ffmpeg to your system variable PATH.

## Install
Download the script and Prequisites if neccessary and simply run python pyScreen.py

## Usage
pyScreen has been rewritten and now uses a argumentative format for the user to execute commands within pyScreen.
```pyScreen.py [FILE NAME.MP4] [OPTIONS -l -t -n]```
pyScreen now allows the user to select whether they want to capture screen shots of a single video file or two files by setting the required parameter ```-t```. If the user ones to generate screen shots for a single video file then set ```-t 1``` or for screen shots of two video files set ```-t 2```. The user is also required to set the ```-n``` parameter which tells pyScreen how many screen shots to generate. When the user sets ```-t 2``` the ```-l``` parameter is required as it tells pyScreen the file location of 2nd video file.

## Examples
Generate Six Screen shots of ONE video file:
```python pyScreen.py "D:\Video File Here.mp4" -t 1 -n 6```

Generate 12 Screen Shots of TWO video files:
```python pyScreen.py "D:\Video File One.mp4" -t 2 - 12 -l "D:\Video File Two.mp4"```


