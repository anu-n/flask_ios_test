import os
#For the given path, get the List of all files in the directory tree 
	
def main():
	dirName = './flaskr';

	# Get the list of all files in directory tree at given path
	listOfFiles = list()
	for (dirpath, dirnames, filenames) in os.walk(dirName):
		listOfFiles += [os.path.join(dirpath, file) for file in filenames]

	# Print the files    
	for elem in listOfFiles:
		print(elem)
		
		os.system("git add " + elem)
		
		
if __name__ == '__main__':
	main()
