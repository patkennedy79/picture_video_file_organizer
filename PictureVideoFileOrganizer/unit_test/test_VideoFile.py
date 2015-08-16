from PictureVideoFileOrganizer import VideoFile


class TestVideoFile:
    def test_constructor(self):
        source_dir_test = "./PictureVideoFileOrganizer/unit_test/source_dir"
        destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/"
        test_file = VideoFile("IMG_6917.MOV", source_dir_test, destination_dir_test)

        assert test_file.filename == "IMG_6917.MOV"
        assert test_file.source_directory == "./PictureVideoFileOrganizer/unit_test/source_dir/"
        assert test_file.destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/2015-08-09/"
        assert test_file.file_size == 0
        assert test_file.copy_successful == False
        assert test_file.date_created == "2015-08-09"

    def test_copy(self):
        source_dir_test = "./PictureVideoFileOrganizer/unit_test/source_dir/"
        destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/"
        test_file = VideoFile("IMG_6917.MOV", source_dir_test, destination_dir_test)
        test_file.copy_to_destination_directory()

        assert test_file.filename == "IMG_6917.MOV"
        assert test_file.source_directory == "./PictureVideoFileOrganizer/unit_test/source_dir/"
        assert test_file.destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/2015-08-09/"
        assert test_file.file_size == 0
        assert test_file.copy_successful == True
        assert test_file.date_created == "2015-08-09"

    def test_copy_second_time(self):
        source_dir_test = "./PictureVideoFileOrganizer/unit_test/source_dir/"
        destination_dir_test = "./PictureVideoFileOrganizer/unit_test/destination_dir/"
        test_file = VideoFile("IMG_6917.MOV", source_dir_test, destination_dir_test)
        test_file.copy_to_destination_directory()

        assert test_file.filename == "IMG_6917.MOV"
        assert test_file.source_directory == "./PictureVideoFileOrganizer/unit_test/source_dir/"
        assert test_file.destination_directory == "./PictureVideoFileOrganizer/unit_test/destination_dir/2015-08-09/"
        assert test_file.file_size == 0
        assert test_file.copy_successful == False
        assert test_file.date_created == "2015-08-09"
