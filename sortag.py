import taglib
import sys
from os import listdir,makedirs,path,rename

def is_song(file):
    return file.endswith(".mp3") or file.endswith(".flac")

def get_mp3_list(dir):
    return [file for file in listdir(dir) if is_song(file)]

def scan_folder(dir):
    print("Scanning...")
    results = dict()
    mp3_list = get_mp3_list(dir)
    total_songs = len(mp3_list)
    safe = 0
    print(str(total_songs)+" songs found")
    for mp3 in mp3_list:
        song = taglib.File(dir+"/"+mp3)
        if tag_is_safe(song):
            safe = safe + 1
            artist = get_artist(song)
            album = get_album(song)
            if not artist in results:
                results[artist] = dict()
            if not album in results[artist]:
                results[artist][album] = []
            results[artist][album].append(mp3)
    print(str(safe)+"/"+str(total_songs)+" tags are correct")
    return results

def create_folder(folder):
    if not path.exists(folder):
        makedirs(folder)

def tag_is_safe(song):
    has_album_artist = "ALBUMARTIST" in song.tags
    has_artist = "ARTIST" in song.tags
    has_album = "ALBUM" in song.tags
    return has_album_artist or has_artist and has_album

def get_artist(song):
    if "ALBUMARTIST" in song.tags:
        return song.tags["ALBUMARTIST"][0]
    else:
        return song.tags["ARTIST"][0]

def get_album(song):
    return song.tags["ALBUM"][0]

def sort(dir, results):
    print("Sorting...")
    for artist in results:
        artist_folder = dir+"/"+artist
        create_folder(artist_folder)
        for album in results[artist]:
            album_folder = artist_folder+"/"+album
            create_folder(album_folder)
            for song in results[artist][album]:
                song_dir = album_folder+"/"+song
                rename(dir+"/"+song,song_dir)
    print("Done")

args = sys.argv
if len(args) == 1:
    print("No args given")
elif len(args) > 2:
    print("Too many args given")
else:
    dir = path.abspath(sys.argv[1])
    print(dir)
    results = scan_folder(test_dir)
    sort(test_dir,results)
