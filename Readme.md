## Synopsis

Python application to organizer picture and video files from multiple sources into a set of directories organized by date.

## What Does This Tool Do?
![Alt text](/Documentation/Picture and Video File Organizer.png?raw=true "Picture and Video File Organizer")

## Motivation

Given all of the different devices that take pictures and videos, it can be really difficult to properly organize all of these files.  This software tool was developed to organize the pictures and videos from multiple sources into a set of directories organized by date.

## How to Run

In the top-level file (picture_video_file_organizer.py), set the source and destination directories.  Run using:
    % python picture_video_file_organizer.py

## Key Python Modules Used

- ExifRead: extracts metadata from picture files
- hachoir-metadata: extracts metadata from video files

This application is written using Python 2.x, as the hachoir-metadata package can only be utilized with Python 2.x.

## Unit Testing

NOTE: These instructions are for setting up and running the unit tests on OS X.

Before attempting to run the unit tests, you need to make sure that the Python interpreter can find the PictureVideoFileOrganizer module.  The easiest way to make this happen is to set your PYTHONPATH to check the top-level directory of the module.  For example, I have my PYTHONPATH set in my ~/.profile file:
    PYTHONPATH="$PYTHONPATH:/Users/patrickkennedy/Documents/Workspace/PictureVideoFileOrganizer/"
    export PYTHONPATH
If you edit your ~/.profile file and want to implement it without restarting your terminal window, just "source ~/.profile".

1. Change directory to the top-level directory and clear all of the files in the unit test output directory:
    % ./unit_test_empty_destination_dir
2. Run the unit tests (usig py.test):
    % py.test
