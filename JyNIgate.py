'''
Created on 13.04.2015

@author: Stefan Richthofer
'''

listFileName = "JyNI-files.txt"
introFileName = "JyNI-copy-intro.txt"
defaultDest = "."
srcList = []
introTxt = []

def initSrcList():
	listFile = open(listFileName, 'r')
	lines = listFile.readlines()
	for line in lines:
		if not line[:3] == "// ":
			srcList.append(line[:-1])
	listFile.close()

def initIntro():
	global introTxt
	introFile = open(introFileName, 'r')
	introTxt = introFile.readlines()
	introFile.close()

def intro(fileName):
	result = []
	result.append(introTxt[0].replace("{srcfile}", fileName))
	result[1:] = introTxt[1:]
	return result

def spacesToTabs(line, indent = 4):
	count = 0
	while line[count] == ' ':
		count += 1
	return '\t'*(count/indent)+' '*(count%indent)+line[count:]

def convertFile(filePath, destPath):
	file = open(filePath, 'r')
	lines = file.readlines()
	file.close()
	destName = filePath.split("/")[-1]
	print "dest"
	print destName
	intr = intro(destName)
	dest = open(destPath, 'w')
	resultLines = intro(destName)
	resultLines.append("\n\n")
	JyNIIncluded = False
	for line in lines:
		line = spacesToTabs(line)
		if not JyNIIncluded and line.startswith("#include"):
			line = line.replace("Python.h", "JyNI.h")
			JyNIIncluded = True
		resultLines.append(line)
	resultLines.append("\n")
	print "resultLines"
	for line in resultLines:
		print line[:-1]
	dest.writelines(resultLines)
	dest.close()

def Cdest():
	return "../"+defaultDest+"/JyNI/JyNI-C/src/"

if __name__ == '__main__':
	initSrcList()
	initIntro()
	print "bla"
	print introTxt
	dest = "./test/"
	dest = Cdest()
	for line in srcList:
		if len(line) > 0 and not line[:3] == "// ":
			vals = line.split(" > ")
			#print vals
			#print "(("+line+"))"
			if len(vals) == 1:
				convertFile(vals[0], dest+vals[0])
			else:
				convertFile(vals[0], dest+vals[1])
	print "done"
