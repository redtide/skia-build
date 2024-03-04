# general

- Delete patches directory?
- Arm64 builds on Linux: it's not clear if runners can't make them yet,
  eventually we need a Docker container.
- Clang builds on Windows: there is an issue somewhere with GN configuration.

## script/archive.py

Fix if wrong file name and/or files in the list.

## script/build.py

Check if the original options can be useful and then remove the multiline comment.

## script/check_release.py

This file checks if the artifact being built is already present in the release,
if any was made already previously, in which case generate an error and make
the build to fail.

If the above is not desiderable for our purpose in some way,
either change the logic or delete the file
and remove the related references in the workflow file.

Otherwise pass the repo slug from the CI workflow as parameter instead of hardcoding it.

## checkout.py and common.py

At first glance seems OK.

## notes

- `actions/upload-artifact` has been replaced by `xresloader/upload-to-github-release`
  because it doesn't upload single files like the `.md5`, only zips.
