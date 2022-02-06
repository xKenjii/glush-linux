# Glush source for Linux

### Installation

Glush requires any version of Python 3 to be installed and present in the bin folder under python3

Installing git & git-core.
> sudo apt-get install git git-core

Clone this repository.
> sudo git clone https://github.com/xKenjii/glush-linux.git

Move the Glush source code to a more reliable and static location.
> sudo mv glush-linux /etc

Before we can add Glush as a cronjob we need to configure our settings, open config.json
> sudo nano /etc/config.json

Change YOUR-API-KEY-HERE to the API Key provided in your Dashboard, and set your Device Name however you please.
Save the config file with Ctrl + X followed by Y + Enter to confirm our changes.

Open the crontab editor.
> sudo crontab -e

Add the following line to the bottom of the file.
> */3 * * * * cd /etc/glush-linux && /usr/bin/python3 /etc/glush-linux/main.py

Save file with Ctrl + X followed by Y + Enter to confirm our changes.
