import argparse

def filenameOfPath(path):
	return path.split('/')[-1].rstrip()

parser = argparse.ArgumentParser()
parser.add_argument('inputFile1')
parser.add_argument('inputFile2')
args = parser.parse_args()


def buildSet(directory_files_list, selfduplicates_filenames_set, filenames_set):
	for file in directory_files_list:
		filename = filenameOfPath(file)

		if filename not in filenames_set:
			filenames_set.add(filename)
		else:
			selfduplicates_filenames_set.add(filename)

def printSelfduplicatesPaths(selfduplicates_filenames_set, directory_files_list):
	for selfduplicate_filename in selfduplicates_filenames_set:
		print('Duplicates of -> ' + selfduplicate_filename + ':')
		for path in directory_files_list:
			if selfduplicate_filename == filenameOfPath(path):
				print('    ' + path)


directory_1_scanfile_path = args.inputFile1
directory_2_scanfile_path = args.inputFile2

directory_1_input = open(directory_1_scanfile_path)
directory_2_input = open(directory_2_scanfile_path)

directory_1_files = []
directory_2_files = []

directory_1_selfduplicates_filenames = set()
directory_2_selfduplicates_filenames = set()

directory_1_filenames_set = set()
directory_2_filenames_set = set()


print('Checking for duplicate filenames on:')
print('1 - ' + directory_1_scanfile_path)
print('2 - ' + directory_2_scanfile_path)
print()

print('loading directory 1... ', end='')
for path in directory_1_input:
	directory_1_files.append(path.rstrip())
print('OK')

print('loading directory 1... ', end='')
for path in directory_2_input:
	directory_2_files.append(path.rstrip())
print('OK')


print('building set 1... ', end='')
buildSet(directory_1_files, directory_1_selfduplicates_filenames, directory_1_filenames_set)
print('OK')

print('building set 2... ', end='')
buildSet(directory_2_files, directory_2_selfduplicates_filenames, directory_2_filenames_set)
print('OK')

print('\n\n\n')
print('Directory 1 selfduplicates: ')
printSelfduplicatesPaths(directory_1_selfduplicates_filenames, directory_1_files)

print('\n\n\n')
print('Directory 2 selfduplicates: ')
printSelfduplicatesPaths(directory_2_selfduplicates_filenames, directory_2_files)

print('\n\n\n')
print('Directory 1 / Directory 2 duplicates: ')
for duplicate in directory_1_filenames_set.intersection(directory_2_filenames_set):
	print(duplicate)





