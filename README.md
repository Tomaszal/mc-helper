# MC Helper

Ever find yourself trying to build using a random palette? Want to mix up some mossy stone bricks in your regular stone bricks for that overgrown look? Well, this app has got you covered.

Every time you right click to place a block, the app will choose a random slot based on your provided weights and select it. Thus creating a random block placement pattern.

## Using the app

An overlay icon will show up on the right of your monitor after launching the app. You can interact with it in three different ways:

* **Left-click** to toggle the randomizer on or off. The current state is indicated by the icon.
* **Right-click** to open slot weight adjustment dialog. Here you can set the weight (probability) of a slot to be selected. 0 means a slot will not be considered.
* **Middle-click** to exit the app.

## Planned features

* Configurable auto-clicker with a separate icon toggle.
* Settings window with ability to toggle overlay on / off.
* System tray icon (with status indication if possible).
* Ability to toggle modules on / off using keyboard shortcuts.

## Development notes

Install [pipenv](https://pipenv.pypa.io/en/latest/) and run the following command to setup the project:

``` 
pipenv install
```

To run the app:

``` 
pipenv run fbs run
```

To build the app executable:

``` 
pipenv run fbs freeze
```

To build the app installer:

``` 
pipenv run fbs installer
```

UI files can be edited using **Qt Designer**. To generate Python UI implementation run the following command:

```
pyuic5 src/main/ui/dialog.ui > src/main/python/ui/dialog.py
``` 
