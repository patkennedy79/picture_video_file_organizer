from PictureFile import PictureFile
from VideoFile import VideoFile
from Directory import Directory
from DirectoryWithDateSubfolders import DirectoryWithDateSubfolders
from datetime import datetime

"""
Set the source directories where the files (pictures and videos) will be
 copied from.
"""
#source_directories = {
#    "Patrick_iPhone5s" : '/Users/patrickkennedy/Pictures/Patrick_iPhone5s/Camera Roll',
#    "Colleen_iPhone5"  : '/Users/patrickkennedy/Pictures/Colleen_iPhone5/Camera Roll',
#    "iPad"             : '/Users/patrickkennedy/Pictures/iPad',
#    "Digital_Camera"   : '/Users/patrickkennedy/Pictures/Digital_Camera',
#    "Patrick GalaxyS3" : '/Users/patrickkennedy/Pictures/Patrick_GalaxyS3'
#}
source_directories = {
    "Patrick_iPhone5s" : '/Users/patrickkennedy/Pictures/Patrick_iPhone5s/Camera Roll',
    "Colleen_iPhone5"  : '/Users/patrickkennedy/Pictures/Colleen_iPhone5/Camera Roll'
}
"""
Set the destination directories where the pictures will be stored and where
 the videos will be stored.
"""
pictures_destination_directory = '/Users/patrickkennedy/Pictures/test_dir'
videos_destination_directory = '/Users/patrickkennedy/Movies/test_dir'

print ("Picture/Video File Organizer Application...")

#Set the start time
start_time = datetime.now()

for key, value in source_directories.items():
    print "... Processing files from %s" % key
    current_directory = Directory(value, pictures_destination_directory, videos_destination_directory)
    current_directory.copy_files_to_destination_directory()
    current_directory.print_details()

#Set the end time
end_time = datetime.now()
elapsed_time = end_time - start_time
print "Elapsed time: %s" % elapsed_time
