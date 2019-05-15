# DiffDrive GUI and READER


## Requirements
install tkinter and its dependencies for the GUI.

## [writer.py](https://github.com/lobolanja/RTIConnectorAndGazebo/blob/master/python/DiffDriveInterface/writerer.py) 
It is a simple GUI to control the Differential Drive Robot.
Keep in mind that the buttons are incremental, I mean,
if you press a button several times, the speed will increase.



## [reader.py](https://github.com/lobolanja/RTIConnectorAndGazebo/blob/master/python/DiffDriveInterface/reader.py)
Script that receive the information related with the Differential Drive Robot status and show it in a terminal.

## How To Run
 
1. [Run Gazebo and differential Drive World](https://github.com/rticommunity/gazebo-dds-plugins/blob/master/src/diff_drive/README.md)

2. Run the Reader:
    You will start to see in the terminal the Differential Drive Robot status.

3. Run the Writer: 
    You will see a simple interface with 4 buttons to play with the Differential Drive 
    Robot.

