# fitbit-utils

Helper scripts for the fitbit API.

## Usage

Before running a script make sure to install the requirements via pipenv

`pipenv install`

Execute scripts with pipenv. To open a shell with the pipenv environment use

`pipenv shell`

Use the `--help` argument on any script to find it's full options

Scrape nutrition info from a website and upload it as a custom food

`python3 -m fitbitutils.scrape <url>`

Get custom food

`python3 -m fitbitutils.getfood [options]`

Upload custom food

`python3 -m fitbitutils.createfood [options]`