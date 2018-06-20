import shutil, os

os.chdir('/home/harvey/Documents/shared_projects/file_management/')

# shutil.copytree('./test1/', './test3/')

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    print('The current folder is {folder}'.format(folder=folderName))

    for subfolder in subfolders:
        print('The current subfolder is ' + subfolder)
    for filename in filenames:
        print('It contains the file ' + filename)
