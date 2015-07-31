from PictureFile import PictureFile
from VideoFile import VideoFile
from Directory import Directory

patrick_iphone_source_directory = '/Users/patrickkennedy/Pictures/Patrick_iPhone5s/Camera Roll'
picture_destination_directory = '/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/destination_dir_test/Pictures'
movie_destination_directory = '/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/destination_dir_test/Movies'

print ("Picture/Video File Organizer Application...")

#file1 = PictureFile('IMG_4488.JPG', '/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/source_dir_test','/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/destination_dir_test')
#file1.copy_to_destination_directory()
#file1.print_details()

#file2 = VideoFile('MVI_4487.MOV', '/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/source_dir_test','/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/destination_dir_test')
#file2.copy_to_destination_directory()
#file2.print_details()

#file3 = PictureFile('IMG_6198.JPG', patrick_iphone_source_directory, picture_destination_directory)
#file3.copy_to_destination_directory()
#file3.print_details()

#file4 = PictureFile('IMG_6149.JPG', patrick_iphone_source_directory, picture_destination_directory)
#file4.copy_to_destination_directory()
#file4.print_details()

#dir1 = Directory('/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/source_dir_test', picture_destination_directory, movie_destination_directory)
#dir1.print_details()
#dir1.copy_files_to_destination_directory()

dir2 = Directory(patrick_iphone_source_directory, picture_destination_directory, movie_destination_directory)
dir2.print_details()
dir2.copy_files_to_destination_directory()
