from os import listdir, mkdir, chdir
from os.path import isfile, join, isdir
from shutil import copy2
from string import replace
from Directory import Directory


def check_directory_name(directory_name):
    if not directory_name.endswith('/'):
        return directory_name + '/'
    else:
        return directory_name

""" Purpose: This class defines a directory that contains any number of
             directories that are named by date that will be copied from this
             directory to a destination directory.

   Attributes:
       directory_path: path of this directory without the trailing '/'
       destination_directory: directory where the file will be attempted to be
                              copied to without the trailing '/'
       files: list of Files that are contained in this directory
"""
class DirectoryWithDateSubfolders(object):
    # Constructor
    def __init__(self, directory_path, picture_destination_directory, movie_destination_directory):
        self.directory_path = check_directory_name(directory_path)
        self.picture_destination_directory = check_directory_name(picture_destination_directory)
        self.movie_destination_directory = check_directory_name(movie_destination_directory)
        self.directories = [ folder for folder in listdir(self.directory_path) if isdir(join(self.directory_path,folder)) ]
        self.directories.sort()

    def print_details(self):
        print "Directory details:"
        print "    Directory path: %s" % self.directory_path
        print "    Picture Destination directory: %s" % self.picture_destination_directory
        print "    Movie Destination directory: %s" % self.movie_destination_directory
        print "    Number of directories in directory: %s" % len(self.directories)

    def copy_files_to_destination_directory(self):
        for current_folder_original in self.directories:
            if current_folder_original.lower().startswith('20'):
                # Replace the character "_" with "-"
                current_folder = replace(current_folder_original, "_", "-")
                print "Digital Camera folder: ...%s..." % current_folder

                # Change into the current folder
                current_source_directory = self.directory_path + current_folder_original
                chdir(current_source_directory)

                current_file_list = [ f for f in listdir(current_source_directory) if isfile(join(current_source_directory, f)) ]
                current_file_list.sort()

                for file in current_file_list:
                    if file.lower().endswith('.jpg'):
                        # Check if a directory exists in the pictures destination folder with the folder name
                        if not isdir(self.picture_destination_directory + current_folder):
                            print "Creating directory: %s" % (self.picture_destination_directory + current_folder)

                            try:
                                mkdir(self.picture_destination_directory + current_folder)
                            except OSError as e:
                                print "Exception: %s" % str(e)

                        # Check if the file exists in the destination directory
                        if not isfile(self.picture_destination_directory + current_folder + "/" + file):
                            # Copy the file to the destination directory
                            print "Copying %s to %s" % (file, (self.picture_destination_directory + current_folder + '/'))

                            try:
                                copy2((current_source_directory + "/" + file), (self.picture_destination_directory + current_folder + '/'))
                            except OSError as e:
                                print "Exception: %s" % str(e)

                    if file.lower().endswith('.mov'):
                        # Check if a directory exists in the movies destination folder with the folder name
                        if not isdir(self.movie_destination_directory + current_folder):
                            print "Creating directory: %s" % (self.movie_destination_directory + current_folder)

                            try:
                                mkdir(self.movie_destination_directory + current_folder)
                            except OSError as e:
                                print "Exception: %s" % str(e)

                        # Check if the file exists in the movies destination directory
                        if not isfile(self.movie_destination_directory + current_folder + "/" + file):
                            # Copy the file to the movies destination directory
                            print "Copying %s to %s" % (file, (self.movie_destination_directory + current_folder + '/'))

                            try:
                                copy2((current_source_directory + "/" + file), (self.movie_destination_directory + current_folder + '/'))
                            except OSError as e:
                                print "Exception: %s" % str(e)
