"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Colis, Neil Bradley V.]
Date: [09/27/26]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[a system that cleans up a messy folder by sorting files into subfolders based on their file extensions.
 Basically, the script looks at every file in a target directory]


============================================
KEY VOCABULARY
============================================
- os module: used to work with folders files and file paths
- shutil module: used to move and manage files
- file path: a path/location of a file on the computer
- directory: other term for file name
- extension: its a part of a file name that tells what type of file it is
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

folder = input("enter the folder path: ")

if os.path.exists(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file)[1].lower()

            if extension:
                folder_name = extension[1:].upper() + " Files"
                new_folder = os.path.join(folder, folder_name)

                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)

                shutil.move(file_path, os.path.join(new_folder, file))

    print("files sorted successfully")
else:
    print("folder does not exist")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I need to be careful with file paths since the target folder must exist before the program can run,
 and I also need to double‑check when moving files to avoid putting them in the wrong location.
============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
