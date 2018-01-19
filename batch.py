# this is the main script to start scraping Bing for images
import subprocess

# used search words
searchStrings = [
"modern architecture",
"art deco buildings",
"gothic architecture",
"postmodern architecture",
"classical architecture",
"romanesque buildings",
"brutalist architecture",
"tudor architecture",
"french colonial architecture",
"ottoman architecture"
]

# target folders
outputFolders = [
"./modern",
"./artDeco",
"./gothic",
"./postmodern",
"./classical",
"./romanesque",
"./brutalist",
"./tudor",
"./colonial",
"./ottoman"
]

# i requested about 500 images per item
nImages = 500

for a,b in zip(searchStrings, outputFolders):
	sendStr = "python bbid.py -s \" %s \" -o %s --limit %d" %(a,b,nImages)
	subprocess.call(sendStr)
