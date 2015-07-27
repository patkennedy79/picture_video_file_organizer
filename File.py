from os.path import isfile, isdir
from shutil import copy2

""" Purpose: This class defines a file that will be copied from its source
             directory to a destination directory, if the file does not exist
             in the destination directory already.

   Attributes:
       filename: name of the file with its extension, but without the directory
       source_directory: directory where the file exists without the trailing '/'
       destination_directory: directory where the file will be attempted to be
                              copied to without the trailing '/'
       file_size: size (in Bytes) of the file
       date_created: date (in format of "xx-yy-zz", such as "12-23-15" for
                     December 23rd, 2015)
       copy_successful: flag indicating if the copy from the source directory
                        to the destination directory was successful
"""
class File(object):
    # Constructor
    def __init__(self, filename, source_directory, destination_directory):
        self.filename = filename
        self.source_directory = source_directory
        self.destination_directory = destination_directory
        self.file_size = 0
        self.date_created = ""
        self.copy_successful = False

    def print_details(self):
        print "File details:"
        print "    Filename: %s" % self.filename
        print "    Source directory: %s" % self.source_directory
        print "    Destination directory: %s" % self.destination_directory
        print "    Date created: %s" % self.date_created
        print "    Copy successful: %s" % self.copy_successful

    def copy_to_destination_directory(self):
        # Check if the destination directory exists... if it does not, then
        #   create the directory
        if not isdir(self.destination_directory):
            print "Destination directory does NOT exist!"

            try:
                mkdir(self.destination_directory + "/" + date_created)
            except OSError as e:
                print "Exception: %s" % str(e)

        # Check if the file exists in the destination directory
        if not isfile(self.destination_directory + "/" + self.filename):
            print "File is NOT located in the destination directory!"
            print "Copying %s to %s/%s" % (self.filename, self.destination_directory, self.filename)

            try:
                copy2((self.source_directory + "/" + self.filename), self.destination_directory)
                self.copy_successful = True
            except OSError as e:
                print "Exception: %s" % str(e)
        else:
            print "File exists in the destination directory."
