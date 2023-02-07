# rosbag_to_csv

A GUI tool to convert topics from a single rosbag file or multiple rosbag files at once to csv files

# Supported versions

* [`master` branch](https://github.com/AtsushiSakai/rosbag_to_csv/tree/master): Python3 (ROS Noetic, Python 3.8 or higher.)
* [`python2` branch](https://github.com/AtsushiSakai/rosbag_to_csv/tree/python2): Python2 (ROS Melodic)

# Install Dependencies and Build

## Python3

clone this repository

```
$ cd ~/catkin_ws/src  
$ git clone https://github.com/AtsushiSakai/rosbag_to_csv.git  
$ cd ~/catkin_ws && rosdep install -r --ignore-src --from-paths src
$ catkin_make
```

## Python2

clone this repository with `-b python2` option

```
$ cd ~/catkin_ws/src  
$ git clone -b python2 https://github.com/AtsushiSakai/rosbag_to_csv.git  
$ cd ~/catkin_ws && rosdep install -r --ignore-src --from-paths src
$ catkin_make
```

# How to use

## Start the node
```
$ rosrun rosbag_to_csv rosbag_to_csv.py
```

## Select a single bag file or multiple bag files with the GUI

![1](https://github.com/AtsushiSakai/rosbag_to_csv/wiki/1.png)

## Select topics to convert csv

You can select topics to save in csv files.

![2](https://github.com/AtsushiSakai/rosbag_to_csv/blob/master/images/pic1.png)

## Wait seconds....

A Message "Converting..." is displayed in the terminal.

## Finish convert

When the finish convert message dialog is shown,

![3](https://github.com/AtsushiSakai/rosbag_filter_gui/wiki/4.png)

CSV files are generated successfly in `~/.ros`.

![4](https://github.com/AtsushiSakai/rosbag_to_csv/blob/master/images/pic2.png)


The CSV file name is same as (the bag file name)_(each selected topic name).csv.

If You open the csv file with office software, you can see:

![5](https://github.com/AtsushiSakai/rosbag_to_csv/wiki/3.png)


# License

MIT
