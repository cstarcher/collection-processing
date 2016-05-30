#!/usr/bin/env python3

"""

Rename processed files in a directory in preparation for move to metadata.

Rename files in the following directory structure:

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

Archive and raw folders must contain .tif files. Display folders may contain
multiple .jpg files and/or a single .pdf file.

If there are incorrect file types in a folder, this will be printed to the
console as 'Extra file: (file path).'

If a directory is missing that was specified in the input, it will be printed
to the console as 'Missing Folder: (item number)'

"""

import os
import os.path

base_dir = input('Enter location of files (e.g. J:\\Nathan\\ttu_pressr): ')
item_number = input('Enter item numbers to rename separated by commas (e.g. 1,5,10): ')

collection_code = base_dir[-10:]
item_number_list = item_number.split(',')

content_folder_name = 'content'
archive_folder_name = 'archive'
display_folder_name = 'display'
raw_folder_name = 'raw'

for item_number in item_number_list:
    item_number = str(item_number).zfill(6)
    item_folder_name = collection_code + '_' + item_number
    item_folder_path = os.path.join(base_dir, item_folder_name)
    content_folder_path = os.path.join(item_folder_path, content_folder_name)
    archive_folder_path = os.path.join(content_folder_path, archive_folder_name)
    display_folder_path = os.path.join(content_folder_path, display_folder_name)
    raw_folder_path = os.path.join(content_folder_path, raw_folder_name)
    if os.path.isdir(item_folder_path):
        page_number = '000001'
        page_number_jpg = page_number
        page_number_tif = page_number
        for file_name in os.listdir(archive_folder_path):
            if file_name.endswith('.tif'):
                os.rename(os.path.join(archive_folder_path, file_name),
                          os.path.join(archive_folder_path,
                          (collection_code + '_' + item_number + '_' + page_number + '.tif')))
                page_number = int(page_number)
                page_number += 1
                page_number = str(page_number).zfill(6)
            else:
                print('Extra file: ' + os.path.join(archive_folder_path, file_name))
        for file_name in os.listdir(display_folder_path):
            if file_name.endswith('.jpg'):
                os.rename(os.path.join(display_folder_path, file_name),
                          os.path.join(display_folder_path,
                          (collection_code + '_' + item_number + '_' + page_number_jpg + '.jpg')))
                page_number_jpg = int(page_number_jpg)
                page_number_jpg += 1
                page_number_jpg = str(page_number_jpg).zfill(6)
            elif file_name.endswith('.pdf'):
                os.rename(os.path.join(display_folder_path, file_name),
                          os.path.join(display_folder_path,
                          (collection_code + '_' + item_number + '.pdf')))
            else:
                print('Extra file: ' + os.path.join(display_folder_path, file_name))
        for file_name in os.listdir(raw_folder_path):
            if file_name.endswith('.tif'):
                os.rename(os.path.join(raw_folder_path, file_name),
                          os.path.join(raw_folder_path,
                          (collection_code + '_' + item_number + '_' + page_number_tif + '.tif')))
                page_number_tif = int(page_number_tif)
                page_number_tif += 1
                page_number_tif = str(page_number_tif).zfill(6)
            else:
                print('Extra file: ' + os.path.join(raw_folder_path, file_name))
    else:
        print('Missing folder: ' + item_number)
