
# Raspberry Pi Practice Tracker  
Become a better musician by tracking your practice sessions. Because what gets measured gets managed.  
## What's This?  
This small piece of software can be installed on a Raspberry Pi or similar device.  
After completing the setup you can plug in your MIDI device and forget about it.   
Your practice sessions will automatically be tracked.  
  
![](practicetracker.png)  
  
## Setup
### Requirements
You will need a Raspberry Pi or similar, as well as an instrument with MIDI output and a cable to connect these two.

Dependencies: 
* python >= 3.9
* pipenv

### Installation
We will use `/home/pi/code/practicetracker` as our installation directory.
If you use another directory please change the paths in the files in the `/service` directory accordingly.

Change the current directory to `/home/pi/code` to get started:
```
$ mkdir -p /home/pi/code/  # Create the directory if it doesn't exist
$ cd /home/pi/code/
```
Clone this repository and change into the directory

```
$ git clone https://github.com/FelixAuer/practicetracker
$ cd practicetracker
```

Next steps [to be continued]:

Install pipenv stuff

run test.py to get port and set it

create database

copy services and set them up

tadaaa
