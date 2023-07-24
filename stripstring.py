"""
stripstring.py
Author: Christian Taillon
Description: This script takes a regular expression and a directory as input, and renames all files in the directory
by removing parts of the file name that match the regular expression.

Example usage: python stripstring.py "foo.*" -d /path/to/directory
"""

import argparse
import os
import re

def get_files_to_rename(strip_string, directory):
    pattern = re.compile(strip_string)
    files_to_rename = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            new_name = pattern.sub('', filename)
            if new_name != filename:
                files_to_rename.append((os.path.join(dirpath, filename), os.path.join(dirpath, new_name)))
    return files_to_rename

def prompt_user_confirmation(files_to_rename):
    print("The following files will be renamed:")
    for old_name, new_name in files_to_rename:
        print(f"{old_name} -> {new_name}")
    confirmation = input("Do you want to proceed? [y/N]: ")
    return confirmation.lower() in ['y', 'yes']

def rename_files(files_to_rename):
    for old_name, new_name in files_to_rename:
        try:
            os.rename(old_name, new_name)
            print(f"Renamed file {old_name} to {new_name}")
        except Exception as e:
            print(f"Failed to rename file {old_name}. Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove a pattern from all file names in a directory.')
    parser.add_argument('strip_string', help='The regular expression to remove from file names.')
    parser.add_argument('-d', '--directory', required=True, help='The directory to operate on.')

    args = parser.parse_args()

    files_to_rename = get_files_to_rename(args.strip_string, args.directory)
    if prompt_user_confirmation(files_to_rename):
        rename_files(files_to_rename)
    else:
        print("Operation aborted.")
