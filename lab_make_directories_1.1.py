#!/usr/bin/env python3

"""

Create a directory structure for new or existing collections.

Create a new directory structure based on the following structure:

    collection_folder
        item_folder
            content
                archive
                display
                raw

The collection_folder should have the following structure:

    ttu_pressr

The first three letters are an institution code (e.g. ttu for Texas Tech
University). The last six letters are a unique collection code.

The item_folder should have the following structure:

    ttu_pressr_000001

The six digit number is a unique item number for each item in the collections.

If the collection directory exists, add additional subdirectories.

"""

import os

base_dir = input('Enter location to save directory (e.g. C:\\Users\\christopher\\Desktop): ')
collection_code = input('Enter collection code (e.g. ttu_pressr): ')
item_number = input('Enter first item number (e.g. 1): ')
number_of_items = int(input('Enter number of item folders needed (e.g. 100): '))

collection_folder = os.path.join(base_dir, collection_code)
item_number = str(item_number).zfill(6)

if os.path.isdir(collection_folder):
    pass
else:
    os.mkdir(collection_folder)

for number in range(number_of_items):
    item_folder = os.path.join(collection_folder,
                               (collection_code + '_' + item_number))
    content_folder = os.path.join(item_folder, 'content')
    archive_folder = os.path.join(content_folder, 'archive')
    display_folder = os.path.join(content_folder, 'display')
    raw_folder = os.path.join(content_folder, 'raw')
    os.mkdir(item_folder)
    os.mkdir(content_folder)
    os.mkdir(archive_folder)
    os.mkdir(display_folder)
    os.mkdir(raw_folder)
    item_number = int(item_number)
    item_number += 1
    item_number = str(item_number).zfill(6)
