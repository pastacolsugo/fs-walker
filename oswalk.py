import os
import argparse
import hashlib
from colors import bcolors

quiet = False
# quiet = True

parser = argparse.ArgumentParser()
parser.add_argument('start_path')
parser.add_argument('file_type')
args = parser.parse_args()

extensions = {
    'jpeg' : ['jpg', 'jpeg'],
    'mp4' : ['mp4'],
    'mp3' : ['mp3'],
    'mkv' : ['mkv'],
    'all' : []
}
wanted_extensions = extensions[args.file_type]

skip_directories = ['Backups.backupdb']

def filetypeIsCorrect(file_extension):
    if len(wanted_extensions) == 0: 
        return True
    for extension in wanted_extensions:
        if file_extension == extension:
            return True
    return False

def getDirname(path):
    return path.split('/')[-1]

def walk(path):
    for dirpath, dirs, files in os.walk(path, topdown=True):
        # print(bcolors.OKGREEN + '### files' + bcolors.ENDC)
        for path in dirs:
            if getDirname(path) == skip_directories[0]:
                dirs.remove(skip_directories[0])
        if True:
            for file_name in files:
                # print(file_name.split('.')[-1].lower()) 
                file_extension = file_name.split('.')[-1].lower()
                if (filetypeIsCorrect(file_extension)):
                    print(os.path.join(dirpath, file_name))
        # print(bcolors.OKBLUE + '### dirs' + bcolors.ENDC)
        # for dir_name in dirs:
        #     print(os.path.join(dirpath, dir_name))

def walk2(path):
    walk_obj = os.walk(path, topdown=True)
    print(list(walk_obj))

if (not quiet):
    walk(args.start_path)
