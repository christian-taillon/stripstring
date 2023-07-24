# stripstring.py

Author: Christian Taillon

Description:
This script takes a regular expression and a directory as input and renames all files in the directory by removing parts of the file name that match the regular expression.

## Example Usage

To use this script, run the following command:

```bash
python stripstring.py "foo.*" -d /path/to/directory
```

Here, `"foo.*"` is the regular expression you want to remove from the file names, and `/path/to/directory` is the directory where the files are located.

## How it Works

1. The script takes the regular expression and directory as command-line arguments using `argparse`.
2. It walks through the directory and looks for files whose names match the regular expression.
3. For each matched file, the script removes the matching part of the filename and builds a list of files to rename.
4. The script then prompts the user to confirm the renaming operation.
5. If the user confirms, the script renames the files accordingly, using `os.rename()`.
6. If any error occurs during the renaming process, the script notifies the user of the error.

**Note:** Make sure to use the script with caution, as renaming files is irreversible and can potentially lead to data loss.

Please ensure you have a proper backup of your files before using this script.

## Requirements

- Python 3.x

## Command-Line Arguments

- `strip_string`: The regular expression to remove from file names.
- `-d` or `--directory`: The directory where the script will operate.

## Example

Suppose you have the following files in the directory:

```
/path/to/directory/
    foo.txt
    foo_hello.txt
    bar.jpg
    sample.txt
```

Running the script with the command:

```bash
python stripstring.py "foo.*" -d /path/to/directory
```

will result in:

```
The following files will be renamed:
/path/to/directory/foo_hello.txt -> /path/to/directory/hello.txt
Do you want to proceed? [y/N]: y
Renamed file /path/to/directory/foo_hello.txt to /path/to/directory/hello.txt
```

After the operation, the directory will contain the following files:

```
/path/to/directory/
    bar.jpg
    hello.txt
    sample.txt
```

Please use the script responsibly and always double-check the regular expression before confirming the renaming operation.
