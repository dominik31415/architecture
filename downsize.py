import glob
whiteList = ['*.jpg', '*.png','*.bmp','*.gif']
def getFiles():
	imageFiles = []
	for ext in whiteList:
		imageFiles.extend(glob.glob(ext))
	return imageFiles

import os
from PIL import Image
newSize = (500,500)

os.chdir("train")
folders = os.listdir()
for folder in folders:
	print(folder)
	os.chdir(folder)
	newFolder = "../../train2/" + folder 
	os.mkdir(newFolder)	
	files = getFiles()	
	for filename in files:
		newFile = newFolder + "/" + filename
		try:
			im = Image.open(filename)
			width, height = im.size
			if width < 400 or height < 400:
				continue
			im.thumbnail(newSize, Image.ANTIALIAS)
			im.save(newFile)
		except IOError:
			print("cannot create thumbnail for '%s'" % filename)
	
	os.chdir("../")
	
	
os.chdir("../validation")
folders = os.listdir()
for folder in folders:
	print(folder)
	os.chdir(folder)
	newFolder = "../../validation2/" + folder 
	os.mkdir(newFolder)	
	files = getFiles()	
	for filename in files:
		newFile = newFolder + "/" + filename
		try:
			im = Image.open(filename)
			width, height = im.size
			if width < 400 or height < 400:
				continue
			im.thumbnail(newSize, Image.ANTIALIAS)
			im.save(newFile)
		except IOError:
			print("cannot create thumbnail for '%s'" % filename)
	
	os.chdir("../")
