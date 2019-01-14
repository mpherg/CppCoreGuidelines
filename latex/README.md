# Build a PDF of C++ Core Guidelines
Create a printable book of the C++ Core Guidelines, complete with a list of contributors based on Git commits.

## Requirements
- Make
- Docker

## How To Run

    make

Ding! You now have a CppCoreGuidelines.pdf!

You can also do standard make-like things, such as `make clean`. If you are changing source and rebuilding, you'll want to clean first using this nice one-liner:

    make clean all

## What It Does
1. If it doesn't already exist, builds a Docker image called `cppcoreguidelines` that includes all the necessary tools for building a PDF of the C++ Core Guidelines. This image is based on Fedora 30 with the following packages installed:
    - texlive 2018 with all the appropriate fonts
    - pandoc
    - git
    - make
    - python
2. Builds the C++ Core Guidelines PDF file using pandoc and latex in a `cppcoreguidelines` Docker container.
3. There is no step 3.
