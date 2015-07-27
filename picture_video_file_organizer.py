from PictureFile import PictureFile
from VideoFile import VideoFile

print ("Picture/Video File Organizer Application...")

file1 = PictureFile('IMG_4488.JPG', '/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/source_dir_test','/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/destination_dir_test')
file1.copy_to_destination_directory()
file1.print_details()

file2 = VideoFile('MVI_4487.MOV', '/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/source_dir_test','/Users/patrickkennedy/Documents/Workspace/picture_video_file_organizer/destination_dir_test')
file2.copy_to_destination_directory()
file2.print_details()
