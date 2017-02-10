#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PyQt4.QtGui  import *
from PyQt4.QtCore import *
import sys

class SimplePyQtGUIKit:
    def QuitApp(self):
        QApplication.quit()

    @classmethod
    def GetFilePath(self,caption="Open File",filefilter="",isApp=False):
        u"""
            "Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)"
        """

        if not isApp:
          app = QApplication(sys.argv)
        files=QFileDialog.getOpenFileNames(caption=caption,filter=filefilter)

        strlist=[]
        for file in files:
            strlist.append(str(file))

        return strlist


    @classmethod
    def GetCheckButtonSelect(self, selectList, title="Select", msg="",app=None):
        """
        Get selected check button options

        title: Window name
        mag: Label of the check button
        return selected dictionary
            {'sample b': False, 'sample c': False, 'sample a': False}
        """
 
        if app is None:
          app = QApplication(sys.argv)
        win = QWidget()
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = QWidget(scrollArea)
        scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 247))
        scrollArea.setWidget(scrollAreaWidgetContents)
        layout=QGridLayout()
        verticalLayoutScroll = QVBoxLayout(scrollAreaWidgetContents)
        layoutIndex=0

        if msg is not "":
            label = QLabel(msg)
            layout.addWidget(label,layoutIndex,0)
            layoutIndex=layoutIndex+1

        checkboxs=[]
        for select in selectList:
            checkbox=QCheckBox(select)
            verticalLayoutScroll.addWidget(checkbox)
            layoutIndex=layoutIndex+1
            checkboxs.append(checkbox)

        layout.addWidget(scrollArea)
        btn=QPushButton("OK")
        btn.clicked.connect(app.quit)
        layout.addWidget(btn,layoutIndex,0)
        layoutIndex=layoutIndex+1


        win.setLayout(layout)
        win.setWindowTitle(title)
        win.show()
        app.exec_()

        result={}
        for (checkbox, select) in zip(checkboxs, selectList):
            result[select]=checkbox.isChecked()

        return result

if __name__ == '__main__':
    #  print "GetCheckButtonSelect"
    #  optList=SimplePyQtGUIKit.GetCheckButtonSelect(["sample a","sample b","sample c"], title="Select sample", msg="Please select sample")
    #  print optList
    filePath=SimplePyQtGUIKit.GetFilePath(caption=u"Select files",filefilter="*py")
    print filePath


