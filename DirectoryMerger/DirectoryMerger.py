import os
import sys
from re import match
from shutil import copy2
from sys import argv


def merge_to_dir(output_dir, file_extensions=frozenset({'.mp3'})):
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, output_dir)
    os.makedirs(output_dir, exist_ok=True)

    for entry in os.listdir(current_dir):
        if os.path.join(current_dir, entry) == output_dir:
            continue
        # copy specific file extensions only
        if os.path.isfile(entry) and any([entry.endswith(ext) for ext in file_extensions]):
            copy2(os.path.join(current_dir, entry), output_dir)
        elif os.path.isdir(entry):
            for val in os.listdir(os.path.join(current_dir, entry)):
                # copy specific file extensions only
                if any([val.endswith(ext) for ext in file_extensions]):
                    copy2(os.path.join(current_dir, entry, val), output_dir)


def main(output_dir=None, extensions=None):
    if output_dir is None:
        output_dir = input("Please input the name of the Directory that should be created:\n")

    # make sure new name does not contain weird chars
    if not match(r'^[A-Za-z0-9_\-]+$', output_dir):
        sys.exit("Invalid Directory name: Only alphanumeric chars, underscores and hyphens allowed")
    if output_dir in os.listdir(os.getcwd()):
        sys.exit("Name must be of a directory that does not exist yet!")

    if extensions is None:
        merge_to_dir(output_dir)
    else:
        merge_to_dir(output_dir, extensions)


if __name__ == '__main__':
    if len(argv) > 1:
        extension_set = set()
        for extension in argv[2:]:
            extension_set.add(extension)
        main(argv[1], extension_set)
    else:
        main()
