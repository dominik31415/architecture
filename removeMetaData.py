import subprocess

outputFolders = [
"modern",
"artDeco",
"gothic",
"postmodern",
"classical",
"romanesque",
"brutalist",
"tudor",
"colonial",
"ottoman"
]

for folder in outputFolders:
	sendStr = "jhead -de \"train\\%s\\*.*\"" % folder
	subprocess.call(sendStr)

for folder in outputFolders:
	sendStr = "jhead -de \"validation\\%s\\*.*\"" % folder
	subprocess.call(sendStr)