from DirectoryWithDateSubfolders import DirectoryWithDateSubfolders


class TestDirectoryWithDateSubfolders:
    def test_constructor(self):
        source_dir_test = "./unit_test/source_dir/Digital Camera"
        picture_destination_dir_test = "./unit_test/destination_dir/Pictures"
        movie_destination_dir_test = "./unit_test/destination_dir/Movies/"
        test_dir = DirectoryWithDateSubfolders(source_dir_test, picture_destination_dir_test, movie_destination_dir_test)

        assert test_dir.directory_path == "./unit_test/source_dir/Digital Camera/"
        assert test_dir.picture_destination_directory == "./unit_test/destination_dir/Pictures/"
        assert test_dir.movie_destination_directory == "./unit_test/destination_dir/Movies/"
        assert len(test_dir.directories) == 9
        assert test_dir.files_copied == 0
        assert test_dir.files_not_copied == 0
        assert test_dir.files_with_date_found == 0
        assert test_dir.files_without_date_found == 0

    def test_copy(self):
        source_dir_test = "./unit_test/source_dir/Digital Camera"
        picture_destination_dir_test = "./unit_test/destination_dir/Pictures"
        movie_destination_dir_test = "./unit_test/destination_dir/Movies/"
        test_dir = DirectoryWithDateSubfolders(source_dir_test, picture_destination_dir_test, movie_destination_dir_test)
        test_dir.copy_files_to_destination_directory()

        assert test_dir.directory_path == "./unit_test/source_dir/Digital Camera/"
        assert test_dir.picture_destination_directory == "./unit_test/destination_dir/Pictures/"
        assert test_dir.movie_destination_directory == "./unit_test/destination_dir/Movies/"
        assert len(test_dir.directories) == 9
        assert test_dir.files_copied == 28
        assert test_dir.files_not_copied == 1
        assert test_dir.files_with_date_found == 29
        assert test_dir.files_without_date_found == 0

    def test_copy_second_time(self):
        source_dir_test = "./unit_test/source_dir/Digital Camera"
        picture_destination_dir_test = "./unit_test/destination_dir/Pictures"
        movie_destination_dir_test = "./unit_test/destination_dir/Movies/"
        test_dir = DirectoryWithDateSubfolders(source_dir_test, picture_destination_dir_test, movie_destination_dir_test)
        test_dir.copy_files_to_destination_directory()

        assert test_dir.directory_path == "./unit_test/source_dir/Digital Camera/"
        assert test_dir.picture_destination_directory == "./unit_test/destination_dir/Pictures/"
        assert test_dir.movie_destination_directory == "./unit_test/destination_dir/Movies/"
        assert len(test_dir.directories) == 9
        assert test_dir.files_copied == 0
        assert test_dir.files_not_copied == 29
        assert test_dir.files_with_date_found == 29
        assert test_dir.files_without_date_found == 0
