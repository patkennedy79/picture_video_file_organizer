from PictureFile import PictureFile
from VideoFile import VideoFile
from Directory import Directory
from DirectoryWithDateSubfolders import DirectoryWithDateSubfolders
from datetime import datetime

"""
Set the source directories where the files (pictures and videos) will be
 copied from.
"""
patrick_iphone_source_directory = '/Users/patrickkennedy/Pictures/Patrick_iPhone5s/Camera Roll'
colleen_iphone_source_directory = '/Users/patrickkennedy/Pictures/Colleen_iPhone5/Camera Roll'
ipad_source_directory = '/Users/patrickkennedy/Pictures/iPad'
digital_camera_source_directory = '/Users/patrickkennedy/Pictures/Digital_Camera'
patrick_galaxyS3_source_directory = '/Users/patrickkennedy/Pictures/Patrick_GalaxyS3'

"""
Set the destination directories where the pictures will be stored and where
 the videos will be stored.
"""
pictures_destination_directory = '/Users/patrickkennedy/Pictures/test_dir'
videos_destination_directory = '/Users/patrickkennedy/Movies/test_dir'

print ("Picture/Video File Organizer Application...")

#Set the start time
start_time = datetime.now()

dir1 = Directory(patrick_iphone_source_directory, pictures_destination_directory, videos_destination_directory)
dir1.copy_files_to_destination_directory()
dir1.print_details()

#Set the end time
end_time = datetime.now()
elapsed_time = end_time - start_time
print "Elapsed time: %s" % elapsed_time
