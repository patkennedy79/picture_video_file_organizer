from os import listdir
from os.path import isfile, join
from PictureFile import PictureFile
from VideoFile import VideoFile


""" Purpose: This method returns the extension of a file assuming that the
             extension is only 3 characters in length.
    Example: Input - 'img_0303.jpg', Output - '.jpg'
"""
def get_file_extension(filename):
    return str(filename)[len(filename)-4:len(filename)]


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
        self.directory_path = directory_path
        self.picture_destination_directory = picture_destination_directory
        self.movie_destination_directory = movie_destination_directory
        self.files = [ f for f in listdir(self.directory_path) if isfile(join(self.directory_path,f)) ]
        self.files.sort()

    def print_details(self):
        print "Directory details:"
        print "    Directory path: %s" % self.directory_path
        print "    Picture Destination directory: %s" % self.picture_destination_directory
        print "    Movie Destination directory: %s" % self.movie_destination_directory
        print "    Number of files in directory: %s" % len(self.files)

    def copy_files_to_destination_directory(self):
        for file in self.files:
            if get_file_extension(file).lower() == ".jpg":
                current_file = PictureFile(file, self.directory_path, self.picture_destination_directory)
                current_file.copy_to_destination_directory()
                current_file.print_details()
            elif get_file_extension(file).lower() == ".mov":
                current_file = VideoFile(file, self.directory_path, self.movie_destination_directory)
                current_file.copy_to_destination_directory()
                current_file.print_details()
            else:
                print "file extension not found"
