# Sortag

Python script to sort your music library.
_________________________________

## Description
Sortag looks for `mp3/flac` files in a given directory, read the tags of those files and then move them to folders according with their metadata. The first folder is named after `ALBUMARTIST`( or `ARTIST` if first fails), and sub-folders are named after `ALBUM`.

## Example
```bash
>  tree ./test
./test
├── 02 - Dreams.mp3
├── 09 - Landslide.mp3
└── 12 - Play Dead.mp3

0 directories, 3 files

> python sortag.py ./test
Scanning...
3 songs found
3/3 tags are correct
Sorting...
Done

> tree ./test/
./test/
├── Bjork
│   └── Debut
│       └── 12 - Play Dead.mp3
└── Fleetwood Mac
    ├── Rumours
    │   └── 02 - Dreams.mp3
    └── The Dance
        └── 09 - Landslide.mp3

5 directories, 3 files
```
