from os import listdir, mkdir, chdir
from os.path import isfile, join, isdir
from shutil import copy2
from string import replace
from Directory import Directory
from File import File


""" Purpose: This class defines a directory that contains any number of
             directories that are named by date that will be copied from this
             directory to a destination directory.  For example, this would be
             the structure of the directory:
                - digital_camera_files
                  -- 2015_01_01
                  -- 2015_01_02
                  -- 2015_01_03
                  -- 2015_01_07
                  ...

   Attributes:
       directory_path: path of this directory
       destination_directory: directory where the file will be attempted to be
                              copied to without the trailing '/'
       files: list of Files that are contained in this directory

   Note:
     - The directories that are passed into the Constructor can either have a
       trailing '/' or not.  Within the Constructor, there is a check to ensure
       that a trailing '/' is included in the directory string.
"""
class DirectoryWithDateSubfolders(object):
    # Constructor
    def __init__(self, directory_path, picture_destination_directory, movie_destination_directory):
        self.directory_path = File.check_directory_name(directory_path)
        self.picture_destination_directory = File.check_directory_name(picture_destination_directory)
        self.movie_destination_directory = File.check_directory_name(movie_destination_directory)
        self.directories = [ folder for folder in listdir(self.directory_path) if isdir(join(self.directory_path,folder)) ]
        self.directories.sort()
        self.file_count = 0
        self.files_copied = 0
        self.files_not_copied = 0
        self.files_with_date_found = 0
        self.files_without_date_found = 0

    def print_details(self):
        print "Directory details:"
        print "    Directory path: %s" % self.directory_path
        print "    Picture Destination directory: %s" % self.picture_destination_directory
        print "    Movie Destination directory: %s" % self.movie_destination_directory
        print "    Number of directories in directory: %s" % len(self.directories)
        print "    Number of files in directory: %s" % self.file_count
        print "      Files copied: %d, Files not copied: %d (sum: %d)" % (self.files_copied, self.files_not_copied, (self.files_copied + self.files_not_copied))
        print "      Files with date found: %d, Files without date found: %d (sum: %d)" % (self.files_with_date_found, self.files_without_date_found, (self.files_with_date_found + self.files_without_date_found))

    def copy_files_to_destination_directory(self):
        for current_folder_original in self.directories:
            if current_folder_original.lower().startswith('20'):
                # Replace the character "_" with "-"
                current_folder = replace(current_folder_original, "_", "-")
                print "Digital Camera folder: ...%s..." % current_folder

                current_dir = Directory((self.directory_path + current_folder_original), self.picture_destination_directory, self.movie_destination_directory)
                current_dir.copy_files_to_destination_directory()
                current_dir.print_details

                self.file_count += len(current_dir.files)
                self.files_copied += current_dir.files_copied
                self.files_not_copied += current_dir.files_not_copied
                self.files_with_date_found += current_dir.files_with_date_found
                self.files_without_date_found += current_dir.files_without_date_found
