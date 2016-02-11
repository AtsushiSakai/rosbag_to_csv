# rosbag_to_csv

A GUI tool to convert topics from a rosbag file to csv files

# Install

clone this repository

> $ git clone https://github.com/AtsushiSakai/rosbag_to_csv.git

# How to use

## Start the node

> $ rosrun rosbag_to_csv rosbag_to_csv.py

## Select a bag file with the GUI

![リンクテキスト](https://github.com/AtsushiSakai/rosbag_to_csv/wiki/1.png)

## Select topics to convert csv

You can select topics to save in csv files.

![リンクテキスト](https://github.com/AtsushiSakai/rosbag_to_csv/wiki/2.png)

## Wait seconds....

A Message "Converting..." is displayed in the terminal.

## Finish convert

When the finish convert message dialog is shown,

![リンクテキスト](https://github.com/AtsushiSakai/rosbag_filter_gui/wiki/4.png)

CSV files are generated successfly.

![リンクテキスト](https://github.com/AtsushiSakai/rosbag_to_csv/wiki/4.png)

The CSV file name is same as the each selected topic name.

If You open the csv file with office software, you can see:

![リンクテキスト](https://github.com/AtsushiSakai/rosbag_to_csv/wiki/3.png)


# License

MIT
