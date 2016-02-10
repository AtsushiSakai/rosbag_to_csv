#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from SimplePyQtGUIKit import SimplePyQtGUIKit
from PyQt4 import QtGui
import rosbag
import rospy
import subprocess
from optparse import OptionParser
from datetime import datetime
import uuid

def message_to_csv(stream, msg, flatten=False):
    """
    stream: StringIO
    msg: message
    """
    try:
        for s in type(msg).__slots__:
            val = msg.__getattribute__(s)
            message_to_csv(stream, val, flatten)
    except:
        msg_str = str(msg)
        if msg_str.find(",") is not -1:
            if flatten:
                msg_str = msg_str.strip("(")
                msg_str = msg_str.strip(")")
                msg_str = msg_str.strip(" ")
            else:
                msg_str = "\"" + msg_str + "\""
        stream.write("," + msg_str)

def message_type_to_csv(stream, msg, parent_content_name=""):
    """
    stream: StringIO
    msg: message
    """
    try:
        for s in type(msg).__slots__:
            val = msg.__getattribute__(s)
            message_type_to_csv(stream, val, ".".join([parent_content_name,s]))
    except:
        stream.write("," + parent_content_name)

seq = 0
nowtime = datetime.now().strftime("%Y%m%d-%H%M%S")



def format_csv_filename(form, topic_name):
    global seq
    if form==None:
        return "Convertedbag.csv"
    ret = form.replace('%t', topic_name.replace('/','-'))
    ret=ret[1:]
    return ret
 
def bag_to_csv(options, fname):
    try:
        bag = rosbag.Bag(fname)
        streamdict= dict()
        stime = None
        if options.start_time:
            stime = rospy.Time(options.start_time)
        etime = None
        if options.end_time:
            etime = rospy.Time(options.end_time)
    except Exception as e:
        rospy.logfatal('failed to load bag file: %s', e)
        exit(1)

    try:
        for topic, msg, time in bag.read_messages(topics=options.topic_names,
                                                  start_time=stime,
                                                  end_time=etime):
            if streamdict.has_key(topic):
                stream = streamdict[topic]
            else:
                stream = open(format_csv_filename(options.output_file_format, topic),'w')
                streamdict[topic] = stream
                # header
                if options.header:
                    stream.write("time")
                    message_type_to_csv(stream, msg)
                    stream.write('\n')

            stream.write(datetime.fromtimestamp(time.to_time()).strftime('%Y/%m/%d/%H:%M:%S.%f'))
            message_to_csv(stream, msg, flatten=not options.header)
            stream.write('\n')
        [s.close for s in streamdict.values()]
    except Exception as e:
        rospy.logwarn("fail: %s", e)
    finally:
        bag.close()


def GetTopicList(path):
    bag = rosbag.Bag(path)
    topics = bag.get_type_and_topic_info()[1].keys()
    types=[]
    for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
        types.append(bag.get_type_and_topic_info()[1].values()[i][0])

    results=[]    
    for to,ty in zip(topics,types):
        results.append(to)

    #  print "GetTopicList result:"
    #  print results
    return results

def main(options):
    app = QtGui.QApplication(sys.argv)

    #GetFilePath
    files=SimplePyQtGUIKit.GetFilePath(isApp=True,caption="Select bag file",filefilter="*bag")
    #  print files
    if len(files)<1:
        print("Please select a bag file")
        sys.exit()

    topics=GetTopicList(files[0])
    selected=SimplePyQtGUIKit.GetCheckButtonSelect(topics,app=app,msg="Select topics which you want to keep")

    options.output_file_format="%t.csv"
    bag_to_csv(options,files[0])

    print("Converting....")
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_data, stderr_data = p.communicate()

    QtGui.QMessageBox.information(QtGui.QWidget(), "Message", "Finish Convert!!")

if __name__ == '__main__':
    print "rosbag_to_csv start!!"
    rospy.init_node('rosbag_to_csv', anonymous=True)
    parser = OptionParser(usage="%prog [options] bagfile")
    parser.add_option("-a", "--all", dest="all_topics",
            action="store_true",
            help="exports all topics", default=False)
    parser.add_option("-t", "--topic", dest="topic_names",
            action="append",
                      help="white list topic names", metavar="TOPIC_NAME")
    parser.add_option("-O", "--output", dest="output_file_format",
                      help="output file names format\n%t: topic name\n%s: sequential number\n%d: datetime (now)\n%u: uuid\ne.g.: -O jskbag-$t-$d.csv", metavar="DESTINATION")
    parser.add_option("-s", "--start-time", dest="start_time",
                      help="start time of bagfile", type="float")
    parser.add_option("-e", "--end-time", dest="end_time",
                      help="end time of bagfile", type="float")
    parser.add_option("-n", "--no-header", dest="header",
                      action="store_false", default=True,
                      help="no header / flatten array value")
    (options, args) = parser.parse_args()


    main(options)
