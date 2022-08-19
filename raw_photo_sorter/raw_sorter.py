import sys
import os
import stat
from typing import Dict, List


RAW_EXTENTIONS = ['.raw', '.3fr', '.arw', '.crw', '.cr2', '.cr3', '.dng', '.kdc',
                 '.mrw', '.nef', '.nrw', '.orf', '.ptx', '.pef', '.raf', '.R3D',
                 '.rw2', '.srw', '.x3f', '.CR2']


def create_unused_raw_folder_if_missing(path: str):
    if not os.path.exists(path + 'unused_raw'):
        os.makedirs(path + 'unused_raw', mode=0o777)
        os.chmod(path + 'unused_raw', stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO)
        print(path + 'unused_raw/ was created.')


def move_unused_raw(path: str, raw_list: Dict[str, str]) -> None:
    create_unused_raw_folder_if_missing(path)

    for raw_number, raw_extention in raw_list.items():
        old_path = path + '/IMG_' + raw_number + '.' + raw_extention
        new_path = path + '/unused_raw' + '/IMG_' + raw_number + '.' + raw_extention
        os.rename(os.path.join(old_path), os.path.join(new_path))


def get_files_number(files: List[str]) -> Dict[str, str]:
    files_number = {}

    for file in files:
        file_number = file.split('_')[-1]
        number, extention = file_number.split('.')
        files_number.update({number: extention})

    return files_number


def get_unused_raws_in_folder(raws_and_jpg_list: Dict[str, List[str]]) -> Dict[str, str]:
    raw_list : Dict[str, str] = get_files_number(raws_and_jpg_list['raw'])
    photo_list : Dict[str, str] = get_files_number(raws_and_jpg_list['jpg'])

    for photo in photo_list.keys():
        try:
            raw_list.pop(photo)
        except KeyError :
            print(f"WARNING: Unfound raw corresponding to this photo {photo}")

    return raw_list


def get_raws_and_jpg(files: List[str]) -> Dict[str, List[str]]:
    res = {"raw": [], "jpg": []}

    for file in files:
        _, extention = os.path.splitext(file)
        if extention in RAW_EXTENTIONS: 
            res['raw'].append(file)
        elif extention in ['.jpg']:
            res['jpg'].append(file)
        else:
            print(f'WARNING: Unknown file extension: {file + extention}')

    return res


def get_files(path: str) -> List[str]:
    return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]


def sort_raws_in_folder(path: str) -> None:
    files_list: List[str] = get_files(path)
    raws_and_jpg_list: Dict[str, List[str]] = get_raws_and_jpg(files_list)
    raw_list: Dict[str, str] = get_unused_raws_in_folder(raws_and_jpg_list)
    move_unused_raw(path, raw_list)


def sort_raws_in_folders(folders_paths: List[str]) -> None:
    for path in folders_paths:
        print(f"\nINFO: analyse {path}")
        if os.path.exists(path):
            sort_raws_in_folder(path)
        else:
            print("ERROR: Path not found: %s" % path)


if __name__ == '__main__':
    """
    This is a simple raw file sorter, to split my used raws to the unused ones.
    The unused are place in a new folder named `unused_raw`

    Example:
    `python raw_photo_sorter/raw_sorter.py E:/Media_Photos/2022/2022-07-16_Anniversaire/`

    would create `E:/Media_Photos/2022/2022-07-16_Anniversaire/unused_raw/` and put
    unused raws inside
    """

    folders_paths: List[str] = sys.argv[1:]

    sort_raws_in_folders(folders_paths)
