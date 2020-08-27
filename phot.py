#!/usr/bin/env python3

import shutil, os, glob, send2trash
from pathlib import Path

print("""                                                                       
========================
=                      =
=  ###  #              =
=  # #  #          #   =
=  ###  ###  ###  ###  =
=  #    # #  # #   #   =
=  #    # #  ###   #   =
=                      =
========================
""")


def find_photos(sd_card_name):
    # There are two cameras, each one makes a different directory
    # Copy files from here
    if sd_card_name == "EL MC1":
        return f"/Volumes/{sd_card_name}/DCIM/100EOS5D"
    elif sd_card_name == "EL MC2":
        return f"/Volumes/{sd_card_name}/DCIM/100EOS5D"
    else:
        return f"/Volumes/{sd_card_name}/DCIM/100CANON"


def client_directory(client_name):        
    # Where files will be copied to.
    hd_dir = "/Volumes/ELAINE'S HD 2/SIMON STUDIOS"
    os.chdir(f"{hd_dir}")
    # Currently, only Big Thyme has sub-brands that requires moving into their sub-directory.
    if client_name == "1800 BIG THYME":
        sub_brand = input("Which sub brand is this for? ").upper()
        os.chdir(f"{hd_dir}/{client_name}/{sub_brand}/RAW")
        print(f"{client_name} already exists, so we don't need to make a new folder.")
    elif os.path.isdir(client_name):
        os.chdir(f"{hd_dir}/{client_name}/RAW")
        print(f"We are now in {client_name}'s folder.")
    else:
        os.makedirs(f"/{client_name}/RAW")
        os.chdir(f"{hd_dir}/{client_name}/RAW")
        print(f"{client_name} is a new client, so I created a new folder for you.")


def photo_shoot(date_of_shoot):
    cwd = os.getcwd()
    os.mkdir(date_of_shoot)
    print(f"Ok, a new folder labeled {date_of_shoot} was created under {client_name}.")
    return os.chdir(f"{cwd}/{date_of_shoot}")


def copy_file(copy_images):
    cwd = os.getcwd()
    photo_shoot_directory = photo_shoot(date_of_shoot)
    sd_dir = find_photos(sd_card_name)
    if copy_images == "Y":
        print("Copying files...")
        files = glob.iglob(os.path.join(sd_dir, "*.CR2"))
        for file in files:
            if os.path.isfile(file):
                shutil.copy2(file, cwd)
    else:
        print("Ok, bye!")
    #original_imgs = sum([len(files) for r, d, files in os.walk(sd_dir)])
    #copied_imgs = sum([len(files) for r, d, files in os.walk(photo_shoot_directory)])
    #print(f"Images found: {original_imgs}")
    #print(f"Images copied: {copied_imgs}")
    print("Done")
    print(" ")


def clear_sd_card(trash_files):
    sd_dir = find_photos(sd_card_name)
    if trash_files == "Y":
        print("Deleting files...")
        files = glob.iglob(os.path.join(sd_dir, "*.CR2"))
        for file in files:
            if os.path.isfile(file):
                send2trash.send2trash(file)
        print("Done")
    else:
        print("Ok, have a good day!")
        exit()


sd_card_name = input("Which memory card are the photos in? ").upper()
find_photos(sd_card_name)
client_name = input("Which client are you uploading images for? ").upper()
client_directory(client_name)
date_of_shoot = input("What day did you take these images?(ex.01-01-20) ")
photo_shoot(date_of_shoot)
copy_images = input("Do you want to copy over the images?(y/n) ").upper()
copy_file(copy_images)
trash_files = input("Do you want me to clear your memory card?(y/n) ").upper()
clear_sd_card(trash_files)