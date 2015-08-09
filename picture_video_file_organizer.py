from PictureFile import PictureFile
from VideoFile import VideoFile
from Directory import Directory
from DirectoryWithDateSubfolders import DirectoryWithDateSubfolders
from datetime import datetime

patrick_iphone_source_directory = '/Users/patrickkennedy/Pictures/Patrick_iPhone5s/Camera Roll'
picture_destination_directory = '/Users/patrickkennedy/Pictures/test_dir'
movie_destination_directory = '/Users/patrickkennedy/Movies/test_dir'

print ("Picture/Video File Organizer Application...")

#Set the start time
start_time = datetime.now()

dir1 = Directory(patrick_iphone_source_directory, picture_destination_directory, movie_destination_directory)
dir1.print_details()
dir1.copy_files_to_destination_directory()
dir1.print_details()

#Set the end time
end_time = datetime.now()
elapsed_time = end_time - start_time
print "Elapsed time: %s" % elapsed_time
