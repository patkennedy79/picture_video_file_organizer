from PictureFile import PictureFile
from VideoFile import VideoFile
from Directory import Directory
from DirectoryWithDateSubfolders import DirectoryWithDateSubfolders
from datetime import datetime

patrick_iphone_source_directory = '/Users/patrickkennedy/Pictures/Patrick_iPhone5s/Camera Roll'
test_source_directory = '/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/source_dir_test2'
test_source_directory2 = '/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/source_dir_test2/2015_06_13 Mommy Bday'
picture_destination_directory = '/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/destination_dir_test/Pictures'
movie_destination_directory = '/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/destination_dir_test/Movies'

print ("Picture/Video File Organizer Application...")

#Set the start time
start_time = datetime.now()

file1 = PictureFile('IMG_4488.JPG', '/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/source_dir_test',picture_destination_directory)
file1.copy_to_destination_directory()
file1.print_details()

file2 = VideoFile('MVI_4487.MOV', '/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/source_dir_test',movie_destination_directory)
file2.copy_to_destination_directory()
file2.print_details()

#file3 = PictureFile('IMG_6198.JPG', patrick_iphone_source_directory, picture_destination_directory)
#file3.copy_to_destination_directory()
#file3.print_details()

#file4 = PictureFile('IMG_6149.JPG', patrick_iphone_source_directory, picture_destination_directory)
#file4.copy_to_destination_directory()
#file4.print_details()

file5 = PictureFile('IMG_4193.JPG', test_source_directory2, picture_destination_directory)
file5.copy_to_destination_directory()
file5.print_details()

#dir1 = Directory('/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/source_dir_test', picture_destination_directory, movie_destination_directory)
#dir1.print_details()
#dir1.copy_files_to_destination_directory()

#dir2 = Directory(patrick_iphone_source_directory, picture_destination_directory, movie_destination_directory)
#dir2.print_details()
#dir2.copy_files_to_destination_directory()
#dir2.print_details()

dir3 = DirectoryWithDateSubfolders(test_source_directory, picture_destination_directory, movie_destination_directory)
dir3.copy_files_to_destination_directory()
dir3.print_details()

#Set the end time
end_time = datetime.now()
elapsed_time = end_time - start_time
print "Elapsed time: %s" % elapsed_time
