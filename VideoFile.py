from File import File
from datetime import datetime
from dateutil import tz
from hachoir_core.error import HachoirError
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_core.tools import makePrintable
from hachoir_metadata import extractMetadata
from hachoir_core.i18n import getTerminalCharset


""" Purpose: This class defines a video file, as distinguished by the "*.mov"
             file extension.  This class inherits from the File class.
"""
class VideoFile(File):
    # Constructor
    def __init__(self, filename, source_directory, destination_directory):
        # Call the Constructor of the super class
        super(VideoFile, self).__init__(filename, source_directory, destination_directory)

        # Set the timezone data for processing the movie files
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('America/Los_Angeles')

        filename, realname = unicodeFilename((self.source_directory + "/" + self.filename)), (self.source_directory + "/" + self.filename)
        parser = createParser(filename, realname)

        if not parser:
            print "ERROR... unable to parse file!"
        else:
            try:
                metadata = extractMetadata(parser)
            except (HachoirError, err):
                print "Metadata extraction error: %s" % unicode(err)
                metadata = None

        if not metadata:
            print "Unable to extract metadata"
        else:
            text = metadata.exportPlaintext()

            for line in text:
#                print line
                current_line  = str(line)[2:15]
                movie_creation_date_and_time_utc = str(line)[17:len(line)]

                if current_line == "Creation date":
                    print "Current line: %s" % current_line
                    print "Found match... %s" % movie_creation_date_and_time_utc

                    # Process the time extracted from the movie file by converting from
                    #  UTC time (Greenwich Mean Time) to the Pacific time zone
                    utc = datetime.strptime(movie_creation_date_and_time_utc, '%Y-%m-%d %H:%M:%S')
                    utc = utc.replace(tzinfo=from_zone)
                    movie_creation_date_and_time_pacific = utc.astimezone(to_zone)
                    print "Time/Date: %s" % movie_creation_date_and_time_pacific

                    # Extract the date from the processed Pacific time
                    movie_creation_date = str(movie_creation_date_and_time_pacific)[0:10]
                    self.date_created = movie_creation_date
                    print "Date: %s" % movie_creation_date
