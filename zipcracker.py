import zipfile
def zcracker( zipFile, wordList):
	password = None
	zipFile = zipfile.ZipFile(zipFile)
	with open(wordList, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				zipFile.extractall(pwd=password)
				print " Password Found: { %s }" % password
			except:
				pass
					
def main():
	
	file = ("output.txt")
	zfile = "myzip.zip"
	zcracker(zfile , file)
	
main()