# Automated Skia builds

This repo is dedicated to building Skia binaries.

## Prebuilt binaries

Prebuilt binaries can be found [in releases].

## Building next version of Skia

Update `version` in [.github/workflows/build.yml].

## Building locally

```sh
python3 script/checkout.py --version m106-4100191c58
python3 script/build.py
python3 script/archive.py
```

To build a debug build:

```sh
python3 script/checkout.py --version m106-4100191c58
python3 script/build.py --build-type Debug
python3 script/archive.py --build-type Debug
```


[in releases]: https://github.com/cycfi/skia-build/releases
[.github/workflows/build.yml]: https://github.com/cycfi/skia-build/blob/master/.github/workflows/build.yml
