#!/usr/bin/env python3

from PyQt5 import QtCore, QtWidgets
import sys

class SimplePyQtGUIKit:
    def QuitApp(self):
        QtWidgets.QApplication.quit()

    @classmethod
    def GetFilePath(self,caption="Open File",filefilter="",isApp=False):
        u"""
            "Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)"
        """

        if not isApp:
          app = QtWidgets.QApplication(sys.argv)
        files=QtWidgets.QFileDialog.getOpenFileNames(caption=caption,filter=filefilter)

        strlist=[]
        for file in files:
            if type(file) == list:
                for f in file:
                    strlist.append(str(f))
            else:
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
          app = QtWidgets.QApplication(sys.argv)
        win = QtWidgets.QWidget()
        scrollArea = QtWidgets.QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = QtWidgets.QWidget(scrollArea)
        scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 247))
        scrollArea.setWidget(scrollAreaWidgetContents)
        layout=QtWidgets.QGridLayout()
        verticalLayoutScroll = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)
        layoutIndex=0

        if msg != "":
            label = QtWidgets.QLabel(msg)
            layout.addWidget(label,layoutIndex,0)
            layoutIndex=layoutIndex+1

        checkboxs=[]
        for select in selectList:
            checkbox=QtWidgets.QCheckBox(select)
            verticalLayoutScroll.addWidget(checkbox)
            layoutIndex=layoutIndex+1
            checkboxs.append(checkbox)

        layout.addWidget(scrollArea)
        btn=QtWidgets.QPushButton("OK")
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
    filePath=SimplePyQtGUIKit.GetFilePath(caption=u"Select files",filefilter="*py")
    print(f"{filePath=}")


