# base imports
from os import listdir, makedirs, path
from shutil import copy2
from typing import List

# library imports
from PIL import Image, ExifTags
from PIL.Image import Exif
from filetype import is_image


def main():
    in_path: str = "./testdata/"
    out_path: str = "./testdata/out/"
    file_name: str
    file_exif: Exif
    file_date: List[str]
    file_ending: str

    # check whether the input path exists
    if not path.exists(in_path):
        return

    # generate the output path if it doesn't exist
    makedirs(out_path, exist_ok=True)

    for file in listdir(in_path):
        if path.isfile(in_path + file) and is_image(in_path + file):
            # get image exif data
            file_exif = Image.open(in_path + file).getexif()

            # set file_name (in case date time exif isn't present, the old file name will stay)
            file_name = file

            # check if the date time exif data exists
            if ExifTags.Base.DateTime in file_exif:
                # build new file name
                file_date = file_exif[ExifTags.Base.DateTime].replace(":", " ").split()
                file_ending = file.split(".")[-1].lower()
                file_name = file_date[0] + file_date[1] + file_date[2] + "_" + file_date[3] + file_date[4] + file_date[5] + "." + file_ending

            # copy the old file to the out path
            copy2(in_path + file, out_path + file_name)


if __name__ == '__main__':
    main()
