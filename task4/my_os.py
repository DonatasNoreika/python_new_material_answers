import os
import shutil


def list_directory(dirname=os.getcwd()):
    print(os.listdir(dirname))


def create_directory(directory_name):
    os.mkdir(directory_name)


def rename_file(old_name, new_name):
    os.rename(old_name, new_name)


def move_file(filename, new_location):
    shutil.move(filename, new_location)


def delete_file(filename):
    os.remove(filename)
