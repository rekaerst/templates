import sys
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream, QIODevice
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QAction, QDialog, QMainWindow, QTextEdit, qApp, QLabel,
    QBoxLayout, QInputDialog, QLineEdit, QFileDialog)


class Skeletion(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.filename = ""

    def initUI(self):
        new_icon = QIcon.fromTheme("document-new", QIcon("new.png"))
        open_icon = QIcon.fromTheme("document-open", QIcon("open.png"))
        save_icon = QIcon.fromTheme("document-save")
        quit_icon = QIcon.fromTheme("application-quit", QIcon("quit.png"))

        file_menu = self.menuBar().addMenu("&File")
        file_menu.setMinimumWidth(200)

        new_act = QAction("&New", self)
        new_act.setShortcut("CTRL+N")
        open_act = QAction("&Open", self)
        open_act.setShortcut("CTRL+O")
        save_act = QAction("&Save", self)
        save_act.setShortcut("CTRL+S")
        save_as_act = QAction("Save &As", self)
        save_as_act.setShortcut("CTRL+SHIFT+S")
        quit_act = QAction("&Quit", self)
        quit_act.setShortcut("CTRL+Q")

        file_menu.addAction(new_act)
        file_menu.addAction(open_act)
        file_menu.addAction(save_act)
        file_menu.addAction(save_as_act)
        file_menu.addSeparator()
        file_menu.addAction(quit_act)

        help_menu = self.menuBar().addMenu("&Help")
        help_menu.setMinimumWidth(200)

        about_act = QAction("&About", self)

        help_menu.addAction(about_act)

        toolbar = self.addToolBar("main toolbar")
        toolbar.addAction(new_icon, "New").triggered.connect(self.newfile)
        toolbar.addAction(open_icon, "Open").triggered.connect(self.openfile)
        toolbar.addAction(save_icon, "Save").triggered.connect(self.savefile)
        toolbar.addAction(quit_icon, "Quit").triggered.connect(qApp.quit)

        self.edit = QTextEdit(self)
        self.setCentralWidget(self.edit)

        self.statusBar().showMessage("Ready")

        new_act.triggered.connect(self.newfile)
        open_act.triggered.connect(self.openfile)
        save_act.triggered.connect(self.savefile)
        save_as_act.triggered.connect(self.saveasfile)
        quit_act.triggered.connect(qApp.quit)

        about_act.triggered.connect(self.about)

    @pyqtSlot()
    def openfile(self):
        self.filename = QFileDialog.getOpenFileName(self)[0]
        f = QFile(self.filename)
        if not f.open(QIODevice.ReadOnly):
            self.statusBar().showMessage("Cannot open file!")
            return
        fin = QTextStream(f)
        self.edit.setText(fin.readAll())
        self.statusBar().showMessage(f"Opend {self.filename}")
        f.close()

    @pyqtSlot()
    def newfile(self):
        self.edit.setText("")
        self.filename = ""
        self.statusBar().showMessage("Ready")

    @pyqtSlot()
    def saveasfile(self):
        self.filename = QInputDialog.getText(
            self, "Save", "file name", QLineEdit.Normal, "")[0]
        self.savefile()

    @pyqtSlot()
    def savefile(self):
        if len(self.filename) == 0:
            self.filename = QInputDialog.getText(
                self, "Save", "file name", QLineEdit.Normal, "")[0]
        f = QFile(self.filename)
        if not f.open(QIODevice.WriteOnly):
            self.statusBar().showMessage("Cannot write file!")
            return
        fout = QTextStream(f)
        fout.setCodec("UTF-8")
        fout << self.edit.toPlainText() << "\n"
        f.close()
        self.statusBar().showMessage("File saved")

    @pyqtSlot()
    def about(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("about")
        dialog.resize(320, 160)
        layout = QBoxLayout(QBoxLayout.TopToBottom, dialog)
        layout.addWidget(QLabel("""
   A text editor created by rekaerst

   Copyright rekaerst 2021
   rekaerst@outlook.com
"""))
        dialog.exec()


def main():
    app = QApplication(sys.argv)

    window = Skeletion()
    window.resize(600, 400)
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
