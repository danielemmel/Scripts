A small script that allows merging all files and subdirectories of a directory into a singular directory.

To use it, simply put it into the directory of which you wish to merge all resources into one directory. 
Make sure you have at least Python 3.8 installed (this is the version on which I build and tested the script).
By default, the script will only merge .mp3 files in the output directory. However, that can be customized.
Furthermore, the script only merges subdirectories to a depth of one, meaning that only direct subdirectories of the one in which the script is executed are considered.

To execute it merging only .mp3 files, simply open the command line in the input folder and execute
```bash
python3 DirectoryMerger.py
```
The script will then query you for the name of the output directory that all .mp3 files should be merged into. Make sure this is a directory that does not already exist.

You can also pass the output directory name directly on the command line. Assuming the output dir should be named Foo, simply execute 
```bash
python3 DirectoryMerger.py Foo
```

Lastly, you can naturally also customize the files extensions that should be considered during the merge. This can be done over the command line; simply pass the desired file extension
name after the name of the new output directory.
```bash
# consider .mp3, .txt and .png files during the merge
python3 DirectoryMerger.py Foo mp3 txt png
```
You can also change the default extensions that are considered directly in the code if you wish. Simply search the line
```python3
def merge_to_dir(output_dir, file_extensions=frozenset({'.mp3'})):
```
and change the value of the `file_extensions` parameter.
```python3
# use .txt, .png and .py files in merge as default
def merge_to_dir(output_dir, file_extensions=frozenset({'.txt', '.png', '.py'})):
```
