# this script goes throw the full folder and randly splits images into
# a test and a training set
import glob
whiteList = ['*.jpg', '*.png','*.bmp','*.gif']
def getFiles():
	imageFiles = []
	for ext in whiteList:
		imageFiles.extend(glob.glob(ext))
	return imageFiles

from random import sample
from copy import copy
def randomSplit(mySet,n):
    mySet = set(mySet)
    set2 = sample(mySet,n)
    set1 = mySet.difference(set2)
    return (set1,set2) 


import os
os.chdir("train")
folders = os.listdir()
for folder in folders:
	os.chdir(folder)
	newFolder = "../../validation/" + folder 
	os.mkdir(newFolder)
	
	files = getFiles()
	f0,f1 = randomSplit(files,64)
	
	for filename in f1:
		newFile = newFolder + "/" + filename
		os.rename(filename,newFile)
	os.chdir("../")
