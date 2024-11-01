# 🏞️ Image Renamer
Remember that time you went on holiday with some friends and after sharing your photos with each other ended up in
having a quite random set of differently named images? While your Android phone chose an actually reasonable format of
naming the image `yyyymmdd_hhmmss`, the one person in your group that uses an iPhone uploads their photos named 
`IMG_xxxx` and that other persons photos taken using a Google Pixel are named `PXL_yyyymmdd_hhmmssxxx`. What a mess!

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
usage: image_renamer.py [-h] [-v] [--source SOURCE] [--output OUTPUT]

Rename images based on their Exif data

options:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  --source SOURCE, -s SOURCE
                        specify the source folder (folder containing the input images)
  --output OUTPUT, -o OUTPUT
                        specify the data output folder (where the renamed files will be saved)
```

## Version
### v0.0.1
- CLI added
- base functionality