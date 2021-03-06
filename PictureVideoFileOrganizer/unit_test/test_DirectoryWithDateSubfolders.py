from PictureVideoFileOrganizer import DirectoryWithDateSubfolders
from os import listdir


class TestDirectoryWithDateSubfolders:
    def test_constructor(self):
        source_dir_test = "./PictureVideoFileOrganizer/unit_test/source_dir/Digital Camera"
        picture_destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures"
        movie_destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/"
        test_dir = DirectoryWithDateSubfolders(source_dir_test, picture_destination_dir_test, movie_destination_dir_test)

        assert test_dir.directory_path == "./PictureVideoFileOrganizer/unit_test/source_dir/Digital Camera/"
        assert test_dir.picture_destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/"
        assert test_dir.movie_destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/"
        assert len(test_dir.directories) == 9
        assert test_dir.files_copied == 0
        assert test_dir.files_not_copied == 0
        assert test_dir.files_with_date_found == 0
        assert test_dir.files_without_date_found == 0

    def test_copy(self):
        source_dir_test = "./PictureVideoFileOrganizer/unit_test/source_dir/Digital Camera"
        picture_destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures"
        movie_destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/"
        test_dir = DirectoryWithDateSubfolders(source_dir_test, picture_destination_dir_test, movie_destination_dir_test)
        test_dir.copy_files_to_destination_directory()

        assert test_dir.directory_path == "./PictureVideoFileOrganizer/unit_test/source_dir/Digital Camera/"
        assert test_dir.picture_destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/"
        assert test_dir.movie_destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/"
        assert len(test_dir.directories) == 9
        assert test_dir.files_copied == 28
        assert test_dir.files_not_copied == 1
        assert test_dir.files_with_date_found == 29
        assert test_dir.files_without_date_found == 0

        test_files = {
            "IMG_0035.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2014-08-02/",
            "IMG_0957.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2014-08-02/",
            "IMG_0958.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2014-08-02/",
            "IMG_6917.MOV" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/2014-08-02/",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-02-28/",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-02-28/",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-02-28/",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-02 Blaa",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-02 Blaa",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-02 Blaa",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-02",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-02",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-02",
            "IMG_0035.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-04 Blaa2 ",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-04 Blaa2 ",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-04 Blaa2 ",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-04 Blaa2 ",
            "IMG_6917.MOV" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/2015-08-04 Blaa2 ",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-06",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-06",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-06",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-03",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-03",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-03",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-05",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-05",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-05",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-07 Blaa3",
            "IMG_6917.MOV" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/2015-08-07 Blaa3"
        }

        for key, value in test_files.items():
            assert (key in listdir(value))

    def test_copy_second_time(self):
        source_dir_test = "./PictureVideoFileOrganizer/unit_test/source_dir/Digital Camera"
        picture_destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures"
        movie_destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/"
        test_dir = DirectoryWithDateSubfolders(source_dir_test, picture_destination_dir_test, movie_destination_dir_test)
        test_dir.copy_files_to_destination_directory()

        assert test_dir.directory_path == "./PictureVideoFileOrganizer/unit_test/source_dir/Digital Camera/"
        assert test_dir.picture_destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/"
        assert test_dir.movie_destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/"
        assert len(test_dir.directories) == 9
        assert test_dir.files_copied == 0
        assert test_dir.files_not_copied == 29
        assert test_dir.files_with_date_found == 29
        assert test_dir.files_without_date_found == 0

        test_files = {
            "IMG_0035.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2014-08-02/",
            "IMG_0957.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2014-08-02/",
            "IMG_0958.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2014-08-02/",
            "IMG_6917.MOV" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/2014-08-02/",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-02-28/",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-02-28/",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-02-28/",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-02 Blaa",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-02 Blaa",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-02 Blaa",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-02",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-02",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-02",
            "IMG_0035.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-04 Blaa2 ",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-04 Blaa2 ",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-04 Blaa2 ",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-04 Blaa2 ",
            "IMG_6917.MOV" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/2015-08-04 Blaa2 ",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-06",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-06",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-06",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-03",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-03",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-03",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-05",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-05",
            "IMG_6785.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-05",
            "IMG_6782.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-07 Blaa3",
            "IMG_6917.MOV" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/2015-08-07 Blaa3"
        }

        for key, value in test_files.items():
            assert (key in listdir(value))
