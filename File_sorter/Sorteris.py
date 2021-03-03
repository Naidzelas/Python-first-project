from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
import os
import glob
import shutil

t = 100

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.direct = {
            "HTML": [".html5", ".html", ".htm", ".xhtml"],
            "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
                       ".heif", ".psd"],
            "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
                       ".qt1", ".mpg", ".mpeg", ".3gp"],
            "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                          ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                          ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                          ".pptx"],
            "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                         ".dmg", ".rar", ".xar", ".zip"],
            "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
                      ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
            "PLAINTEXT": [".txt", ".in", ".out"],
            "PDF": [".pdf"],
            # "PYTHON": [".py"],
            "XML": [".xml"],
            "EXE": [".exe"],
            "SHELL": [".sh"],
            "LIDAR": [".las", ".laz"],
            "DWG": [".dwg", ".DXF"]
        }

        MainWindow.setObjectName("File sorter")

        # Code that does not allow the app frame move and is fixed to its size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(469, 156))
        MainWindow.setMaximumSize(QtCore.QSize(469, 156))


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # First button variable
        self.createfolders = QtWidgets.QPushButton(self.centralwidget)
        self.createfolders.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.createfolders.setObjectName("createfolders")
        self.createfolders.clicked.connect(self.create)
        self.createfolders.clicked.connect(self.loop)


        # Second button variable
        self.sortfiles = QtWidgets.QPushButton(self.centralwidget)
        self.sortfiles.setGeometry(QtCore.QRect(240, 10, 221, 61))
        self.sortfiles.setObjectName("sortfiles")
        self.sortfiles.clicked.connect(self.sort)
        self.sortfiles.clicked.connect(self.loop)


        # Button for choosing the directory
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(430, 80, 31, 21))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.open_dialog)


        # Progress bar that needs to be connected to sorter function
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 110, 461, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Text field for info
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(10, 80, 411, 21))
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def loop(self):
        count = 0
        while count < 100:
            count += 1
            #time.sleep(0.5)
            self.progressBar.setValue(count)

    def create(self):
        for entry in self.direct:
            if not entry in os.listdir(self.parent_dir):
                path = os.path.join(self.parent_dir, entry)
                os.mkdir(path)

    def sort(self):
        self.parent_dir = self.file_name
        for key, value in self.direct.items():
            for spread in value:
                f = spread[1:]
                for move in os.listdir(self.parent_dir):
                    self.add = glob.glob('*.' + f)
                    print(self.add)
                    
                    #for spread_again in add:
                        #self.new_path = os.path.join(self.parent_dir, spread_again)
                        #self.old_path = os.path.join(self.parent_dir, key)
                        #shutil.move(self.new_path, self.old_path)
                        #print(spread_again)


    def open_dialog(self):
        self.file_name = QFileDialog.getExistingDirectory()
        self.parent_dir = self.file_name
        self.textEdit.setText(self.file_name)
        print(self.parent_dir)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("File Sorter", "File Sorter"))
        self.createfolders.setText(_translate("MainWindow", "CREATE FOLDERS"))
        self.sortfiles.setText(_translate("MainWindow", "SORT FILES"))
        self.toolButton.setText(_translate("MainWindow", "..."))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())