from unittest import TestCase

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
