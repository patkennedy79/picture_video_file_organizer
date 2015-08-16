from PictureVideoFileOrganizer import Directory
from os import listdir


class TestDirectory:
    def test_constructor(self):
        source_dir_test = "./PictureVideoFileOrganizer/unit_test/source_dir/Camera Roll"
        picture_destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures"
        movie_destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/"
        test_dir = Directory(source_dir_test, picture_destination_dir_test, movie_destination_dir_test)

        assert test_dir.directory_path == "./PictureVideoFileOrganizer/unit_test/source_dir/Camera Roll/"
        assert test_dir.picture_destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/"
        assert test_dir.movie_destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/"
        assert len(test_dir.files) == 8
        assert test_dir.files_copied == 0
        assert test_dir.files_not_copied == 0
        assert test_dir.files_with_date_found == 0
        assert test_dir.files_without_date_found == 0

    def test_copy(self):
        source_dir_test = "./PictureVideoFileOrganizer/unit_test/source_dir/Camera Roll"
        picture_destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures"
        movie_destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/"
        test_dir = Directory(source_dir_test, picture_destination_dir_test, movie_destination_dir_test)
        test_dir.copy_files_to_destination_directory()

        assert test_dir.directory_path == "./PictureVideoFileOrganizer/unit_test/source_dir/Camera Roll/"
        assert test_dir.picture_destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/"
        assert test_dir.movie_destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/"
        assert len(test_dir.files) == 8
        assert test_dir.files_copied == 8
        assert test_dir.files_not_copied == 0
        assert test_dir.files_with_date_found == 4
        assert test_dir.files_without_date_found == 4

        test_files = {
            "IMG_6084.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/no_date_available",
            "IMG_6272.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/no_date_available",
            "IMG_6285.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-07-17",
            "IMG_6296.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-07-17",
            "IMG_6367.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/no_date_available",
            "IMG_6385.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/no_date_available",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-06",
            "IMG_6784.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-06"
        }

        for key, value in test_files.items():
            assert (key in listdir(value))

    def test_copy_second_time(self):
        source_dir_test = "./PictureVideoFileOrganizer/unit_test/source_dir/Camera Roll"
        picture_destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures"
        movie_destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/"
        test_dir = Directory(source_dir_test, picture_destination_dir_test, movie_destination_dir_test)
        test_dir.copy_files_to_destination_directory()

        assert test_dir.directory_path == "./PictureVideoFileOrganizer/unit_test/source_dir/Camera Roll/"
        assert test_dir.picture_destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/"
        assert test_dir.movie_destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/Movies/"
        assert len(test_dir.files) == 8
        assert test_dir.files_copied == 0
        assert test_dir.files_not_copied == 8
        assert test_dir.files_with_date_found == 4
        assert test_dir.files_without_date_found == 4

        test_files = {
            "IMG_6084.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/no_date_available",
            "IMG_6272.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/no_date_available",
            "IMG_6285.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-07-17",
            "IMG_6296.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-07-17",
            "IMG_6367.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/no_date_available",
            "IMG_6385.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/no_date_available",
            "IMG_6781.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-06",
            "IMG_6784.JPG" : "./PictureVideoFileOrganizer/unit_test/destination_dir/Pictures/2015-08-06"
        }

        for key, value in test_files.items():
            assert (key in listdir(value))
