import exifread

from File import File


""" Purpose: This class defines a picture file, as distinguished by the "*.jpg"
             file extension.  This class inherits from the File class.
"""
class PictureFile(File):
    # Constructor
    def __init__(self, filename, source_directory, destination_directory):
        # Call the Constructor of the super class
        super(PictureFile, self).__init__(filename, source_directory, destination_directory)

        # Open the picture file for reading the meta data (binary mode)
        f = open((self.source_directory + "/" + self.filename), 'rb')

        # Return Exif tags
        exif_tags = exifread.process_file(f)

        for tag in exif_tags.keys():
            if tag in ('EXIF DateTimeOriginal'):
                date_file = str(exif_tags[tag])
                photo_date = date_file[0:10]
                self.date_created = str.replace(photo_date, ":", "-")
                print "Picture created on %s" % self.date_created