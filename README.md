### Made with **1LunchMan**

## What's a Control Surface?
[Control Surfaces](https://help.ableton.com/hc/en-us/articles/209774285-Using-Control-Surfaces) are scripts made by Ableton to open their users to control Ableton using their Midi devices.<br>
It opens to some super neat integrations, such as the Ableton Push, or to Akai APC.

## The FlKey is just a Launchkey MK3, can't I just use its Remove Script?
The [FlKey](https://novationmusic.com/flkey) is a *0.9*:1 [Launchkey MK3](https://novationmusic.com/launchkey-mk3), with the main difference (appart from the color and buttons decals) being the firmware.<br>
The FlKey have different IDs, making it not working by default with the Launchkey MK3 Control Surface.

**This repo is heavily [based](https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/tree/main/Launchkey_MK3) on decompiled MK3 control surface**, with some tweaks in the \_\_init__.py and midi.py to tweak some IDs (as well as fixing the files, as decompiled files aren't supposed to work on the go).

## Installation
Head to the latest [Release](https://github.com/MeblIkea/FlKey_Surface-Control/releases/), and download *FlKey.zip*.<br>
Just have to unzip it in a Control Surface directory *(see below the most convenient)*.

### Installation path:
(if `Remote Scripts` doesn't exist, you can create the directory by yourself)<br>
Windows: `C:\Users\%username%\Documents\Ableton\User Library\Remote Scripts`<br>
MacOS: `Macintosh HD/Users/[username]/Music/Ableton/User Library/Remote Scripts`

#### *So, it's supposed to look like:*
User Library<br>
├─  Remote Scripts<br>
│  ├─ FlKey<br>
│  │  ├─ \_\_init__.py<br>
│  │  ├─ flkey.py<br>
│  │  ├─ ...

Then, you just have to close and re-open Ableton, <br>
Head to the Settings -> Midi -> [Bind your FlKey to the Control Surface](https://help.ableton.com/hc/en-us/articles/209774285-Using-Control-Surfaces).

## *Usage*
*See this tutorial for the base Control Surface*<br>
https://www.youtube.com/watch?v=DJjB_mWpfak

### <i>If you need help or suggestions, open an issue</i>
