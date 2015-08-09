from os import listdir
from os.path import isfile, join
from PictureFile import PictureFile
from VideoFile import VideoFile
from File import File


""" Purpose: This class defines a directory that contains any number of Files
             that will be copied from this directory to a destination directory.

   Attributes:
       directory_path: path of this directory without the trailing '/'
       destination_directory: directory where the file will be attempted to be
                              copied to without the trailing '/'
       files: list of Files that are contained in this directory
"""
class Directory(object):
    # Constructor
    def __init__(self, directory_path, picture_destination_directory, movie_destination_directory):
        self.directory_path = File.check_directory_name(directory_path)
        self.picture_destination_directory = File.check_directory_name(picture_destination_directory)
        self.movie_destination_directory = File.check_directory_name(movie_destination_directory)
        self.files = [ f for f in listdir(self.directory_path) if isfile(join(self.directory_path,f)) ]
        self.files.sort()
        self.files_copied = 0
        self.files_not_copied = 0
        self.files_with_date_found = 0
        self.files_without_date_found = 0

    def print_details(self):
        print "Directory details:"
        print "    Directory path: %s" % self.directory_path
        print "    Picture Destination directory: %s" % self.picture_destination_directory
        print "    Movie Destination directory: %s" % self.movie_destination_directory
        print "    Number of files in directory: %s" % len(self.files)
        print "      Files copied: %d, Files not copied: %d (sum: %d)" % (self.files_copied, self.files_not_copied, (self.files_copied + self.files_not_copied))
        print "      Files with date found: %d, Files without date found: %d (sum: %d)" % (self.files_with_date_found, self.files_without_date_found, (self.files_with_date_found + self.files_without_date_found))

    def copy_files_to_destination_directory(self):
        for file in self.files:
#            print file
            if file.lower().endswith('.jpg'):
                current_file = PictureFile(file, self.directory_path, self.picture_destination_directory)
                current_file.copy_to_destination_directory()
#                current_file.print_details()
            elif file.lower().endswith('.mov'):
                current_file = VideoFile(file, self.directory_path, self.movie_destination_directory)
                current_file.copy_to_destination_directory()
#                current_file.print_details()
            else:
                current_file = File(file, self.directory_path, self.movie_destination_directory)
#                print "file extension not found"

            if current_file.get_copy_successful():
                self.files_copied += 1
            else:
                self.files_not_copied += 1

            if current_file.get_date_found():
                self.files_with_date_found += 1
            else:
                self.files_without_date_found += 1
