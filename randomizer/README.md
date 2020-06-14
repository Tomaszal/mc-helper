# Slot randomizer

Ever find yourself trying to build using a random palette? Want to mix up some mossy stone bricks in your regular stone bricks for that overgrown look? Well, this script has got you covered.

Every time you right click to place a block, the script will choose a random slot based on your provided weights and select it. Thus creating a random block placement pattern.

## Usage

An overlay icon will show up on the right of your monitor after launching the script. You can interact with it in three different ways:

* **Left-click** to toggle the randomizer on or off. The current state is indicated by the icon.
* **Right-click** to open slot weight adjustment dialog. Here you can set the weight (probability) of a slot to be selected. 0 means a slot will not be considered.
* **Middle-click** to exit the script.

## Prerequisites

Software:

* Qt5
* Python 3

Python libraries:

* PyQt5
* pynput

## Development notes

`dialog.py` is generated from `dialog.ui` , which can be edited using **Qt Designer**. It is crucial for the dialog UI to have 9 spin boxes named from `spinBox_s1` to `spinBox_s9` . To generate `dialog.py` run the following command: `pyuic5 dialog.ui > dialog.py` 
