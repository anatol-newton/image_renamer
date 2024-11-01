#!/usr/bin/env python3

# base imports
import logging
from argparse import ArgumentParser, Namespace
from os import listdir, makedirs, path, environ
from shutil import copy2
from typing import List

import argcomplete
# library imports
from PIL import Image, ExifTags
from PIL.Image import Exif
from filetype import is_image

__version__ = "0.0.1"


def main():
    parser = ArgumentParser(
        prog='image_renamer.py',
        description='Rename images based on their Exif data',
        epilog=f'Image Renamer v{__version__}')

    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true"
    )

    parser.add_argument(
        "--source",
        "-s",
        help="specify the source folder (folder containing the input images)",
        default=environ.get("IMAGERENAMER_SOURCE", "."),
    )

    parser.add_argument(
        "--output",
        "-o",
        help="specify the data output folder (where the renamed files will be saved)",
        default=environ.get("IMAGERENAMER_OUTPUT", "./out"),
    )

    argcomplete.autocomplete(parser)
    args: Namespace = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    in_path: str = path.abspath(args.source)
    out_path: str = path.abspath(args.output)
    logging.debug(f"source: \"{in_path}\", output: \"{out_path}\"")

    file_name: str
    file_exif: Exif
    file_date: List[str]
    file_ending: str

    # check whether the input path exists
    if not path.exists(in_path):
        logging.error(f"Given input path (\"{in_path}\") does not exist!")
        return

    # generate the output path if it doesn't exist
    makedirs(out_path, exist_ok=True)

    for file in listdir(in_path):
        logging.debug(f"checking file: \"{file}\"")
        if path.isfile(path.join(in_path, file)) and is_image(path.join(in_path, file)):
            logging.debug(f"image file detected: \"{file}\"")
            # get image exif data
            file_exif = Image.open(path.join(in_path, file)).getexif()

            # set file_name (in case date time exif isn't present, the old file name will stay)
            file_name = file

            # check if the date time exif data exists
            if ExifTags.Base.DateTime in file_exif:
                # build new file name
                file_date = file_exif[ExifTags.Base.DateTime].replace(":", " ").split()
                file_ending = file.split(".")[-1].lower()
                file_name = file_date[0] + file_date[1] + file_date[2] + "_" + file_date[3] + file_date[4] + file_date[
                    5] + "." + file_ending

            # copy the old file to the out path
            copy2(path.join(in_path, file), path.join(out_path, file_name))


if __name__ == '__main__':
    main()
