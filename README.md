# 🏞️ Image Renamer
Remember that time you went on holiday with some friends and after sharing your photos with each other ended up in
having a quite random set of differently named images? While your Android phone chose an actually reasonable format of
naming the image `yyyymmdd_HHMMSS`, the one person in your group that uses an iPhone uploads their photos named 
`IMG_xxxx` and that other persons photos taken using a Google Pixel are named `PXL_yyyymmdd_HHMMSSxxx`. What a mess!

And this is where Image Renamer comes to its turn. With Image Renamer you can easily rename all images to a 
consistent and reasonable naming format.

Currently, this is just a simple Python script with a CLI. The future plans would be to add a simple GTK UI.

## Usage

### Requirements
This script requires Python, just use a somewhat modern Python version (lets say above 3.9) and it'll probably work.

You will need to install some requirements, just run `pip install -r requirements.txt`.

### CLI

On linux you can directly run the file `./src/image_renamer.py`, otherwise run `python3 src/image_renamer.py `.

```txt
usage: image_renamer.py [-h] [-v] [-s SOURCE] [-o OUTPUT] [-f FORMAT]

Rename images based on their Exif data

options:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -s SOURCE, --source SOURCE
                        specify the source folder (folder containing the input images)
  -o OUTPUT, --output OUTPUT
                        specify the data output folder (where the renamed files will be saved)
  -f FORMAT, --format FORMAT
                        format of the new image name (eg. yyyymmdd_HHMMSS -> 20241101_181154)
                                yyyy    year (four digit, eg. 2024)
                                yy      year (two digit, eg 24)
                                mm      month (eg. 11)
                                dd      day (eg. 01)
                                HH      hour (eg. 18)
                                MM      minute (eg. 11)
                                SS      second (eg. 54)
```

## Version
### v1.0.0
- CLI added
- base functionality
- allow for custom naming format