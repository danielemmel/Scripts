A small script that given any path on Windows in double quotes will transform it into a valid WSL (Windows Subsystem for Linux) path pointing to the same directory.

To use it, simply call the script on your WSL with the Windows path (surrounded by double quotes to account for spaces in the name):

```shell
./convert.sh "C:\Users\SomeUser\Some Dir\Bar"
# output:
# "/mnt/c/Users/SomeUser/Some Dir/Bar"
```

The output can then be used to access to Windows directory from WSL, e.g. to `cd` into it and perform some operations there.
