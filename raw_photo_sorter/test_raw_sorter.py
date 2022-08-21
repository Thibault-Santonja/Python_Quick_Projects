from unittest import TestCase
import io
import os

from raw_photo_sorter.raw_sorter import *


class Test(TestCase):
    def test_get_file_number(self):
        self.assertEqual(get_files_number(["IMG_0000.cr2"]), {"0000": "cr2"})
        self.assertEqual(get_files_number(["random_name_1234.jpg"]), {"1234": "jpg"})

    def test_get_unused_raws_in_folder(self):
        raws_and_jpg_list = {
            "jpg": ["random_name_1234.jpg"],
            "raw": ["IMG_0000.cr2", "IMG_1234.cr2"]
        }
        self.assertEqual(get_unused_raws_in_folder(raws_and_jpg_list), {"0000": "cr2"})

    def test_get_raws_and_jpg(self):
        file_list = ["random_name_1234.jpg", "IMG_0000.cr2", "IMG_1234.cr2"]
        raws_and_jpg_list = {
            "jpg": ["random_name_1234.jpg"],
            "raw": ["IMG_0000.cr2", "IMG_1234.cr2"]
        }
        self.assertEqual(get_raws_and_jpg(file_list), raws_and_jpg_list)

    def test_get_files(self):
        res = get_files(".")
        self.assertTrue('README.md' in res)

    def test_sort_raws_in_folders_failed(self):
        captured_output = io.StringIO() 
        sys.stdout = captured_output
        sort_raws_in_folders(['random_path/'])
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\nINFO: analyse random_path/\nERROR: Path not found: random_path/\n")

    def test_sort_raws_in_folders(self):
        self.assertEqual(sort_raws_in_folders(['raw_photo_sorter/']), None)
        self.assertEqual(os.rmdir('raw_photo_sorter/unused_raw/'), None)
        with self.assertRaises(FileNotFoundError):
            os.rmdir('raw_photo_sorter/unused_raw/')
