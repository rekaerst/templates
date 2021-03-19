#!/usr/bin/python3

import sys
from faker import Faker

from PyQt5 import QtCore
from PyQt5.QtCore import QTranslator, pyqtSlot, Qt
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog, QDialogButtonBox, QHBoxLayout,
                             QLabel, QLineEdit, QMainWindow, QPushButton,
                             QVBoxLayout, QWidget)



class MainUI(QMainWindow):

    class inputDialog(QDialog):
        def __init__(self, parent):
            super().__init__(parent=parent)
            self.initUI()

        def initUI(self):
            self.setWindowTitle(QApplication.translate("MainUI", "New"))
            vbox = QVBoxLayout()

            hbox_lineedit = QHBoxLayout()
            hbox_lineedit.addWidget(QLabel(QApplication.instance().translate("inputDialog", "value")))

            self.lineedit = QLineEdit()
            self.lineedit.returnPressed.connect(self.accepted)
            hbox_lineedit.addWidget(self.lineedit)


            hbox_buttons = QHBoxLayout()
            btn_cancle = QPushButton(QApplication.instance().translate("Dialog", "Cancle"))
            btn_cancle.clicked.connect(self.rejected)
            hbox_buttons.addWidget(btn_cancle)

            btn_ok = QPushButton(QApplication.instance().translate("Dialog", "OK"))
            btn_ok.clicked.connect(self.accepted)
            hbox_buttons.addWidget(btn_ok)



            self.warning_label = QLabel(QApplication.instance().translate("Dialog", "Not a number. Please try again"))
            self.warning_label.setStyleSheet("QLabel { color : #ff4444; }")
            self.warning_label.hide()

            vbox.addLayout(hbox_lineedit)
            vbox.addLayout(hbox_buttons)
            vbox.addWidget(self.warning_label)
            self.setLayout(vbox)

        def accepted(self):
            try:
                self.parent().setResult(int(self.lineedit.text()))
                self.close()
            except:
                self.warning_label.show()

        def rejected(self):
            self.close()

    class RemoveDialog(QDialog):
        def __init__(self, parent):
            super().__init__(parent=parent)
            self.initUI()

        def initUI(self):
            self.setWindowTitle(QApplication.instance().translate("RemoveDialog", "Remove"))

            vbox = QVBoxLayout()

            warning = QLabel(QApplication.instance().translate("RemoveDialog", "Warning: This operation can cause data loss!"))

            hbox_buttons = QHBoxLayout()

            btn_cancle = QPushButton(QApplication.instance().translate("Dialog", "Cancle"))
            btn_cancle.clicked.connect(self.rejected)
            hbox_buttons.addWidget(btn_cancle)

            btn_ok = QPushButton(QApplication.instance().translate("Dialog", "OK"))
            btn_ok.clicked.connect(self.accepted)
            hbox_buttons.addWidget(btn_ok)

            vbox.addWidget(warning)
            vbox.addLayout(hbox_buttons)
            self.setLayout(vbox)

        def accepted(self):
            self.close()

        def rejected(self):
            self.close()

    def __init__(self):
        super(MainUI, self).__init__()
        self.trans = QTranslator(self)
        self._result = 0
        self.result = lambda: self._result

        self.initUI()


    def initUI(self):
        self.setWindowTitle("Hey Yo! You just looked at here!")
        self.resize(460,240)
        self.statusBar().setStyleSheet("QStatusBar { color : #aaaaff; }")
        centerWidget = QWidget()

        # Top level hbox
        hbox = QHBoxLayout()
        # sencond level vbox on the left
        vbox_l = QVBoxLayout()

        hbox_name = QHBoxLayout()
        self.label_name = QLabel()
        hbox_name.addWidget(self.label_name)
        self.le_name = QLineEdit()
        self.le_name.returnPressed.connect(self.get_dummy)
        hbox_name.addWidget(self.le_name)

        hbox_card_id = QHBoxLayout()
        self.label_card_id = QLabel()
        hbox_card_id.addWidget(self.label_card_id)
        self.le_card_id = QLineEdit()
        self.le_card_id.returnPressed.connect(self.get_dummy)
        hbox_card_id.addWidget(self.le_card_id)

        hbox_phone_number = QHBoxLayout()
        self.label_phone_number = QLabel()
        hbox_phone_number.addWidget(self.label_phone_number)
        self.le_phone_number = QLineEdit()
        self.le_phone_number.returnPressed.connect(self.get_dummy)
        hbox_phone_number.addWidget(self.le_phone_number)


        vbox_l.addLayout(hbox_name)
        vbox_l.addLayout(hbox_card_id)
        vbox_l.addLayout(hbox_phone_number)

        self.btn_dummy = QPushButton()
        self.btn_dummy.clicked.connect(self.get_dummy)
        vbox_l.addWidget(self.btn_dummy)

        self.btn_clear = QPushButton()
        self.btn_clear.clicked.connect(self.clear)
        vbox_l.addWidget(self.btn_clear)

        # second level vbox on the right
        # pack ui that serve modify add remove records functionality
        vbox_r = QVBoxLayout()

        self.btn_new = QPushButton()
        self.btn_new.clicked.connect(self.new)
        vbox_r.addWidget(self.btn_new)

        self.btn_save = QPushButton()
        self.btn_save.clicked.connect(self.save)
        vbox_r.addWidget(self.btn_save)

        self.btn_add = QPushButton()
        self.btn_add.clicked.connect(self.add)
        vbox_r.addWidget(self.btn_add)

        self.btn_remove = QPushButton()
        self.btn_remove.setStyleSheet("QPushButton { color : #ff4444; }")
        self.btn_remove.clicked.connect(self.remove)
        vbox_r.addWidget(self.btn_remove)

        self.combo = QComboBox()
        self.combo.currentIndexChanged.connect(self.change_lang)
        options = ([("English", ""), ("français", "eng-fr"), ("中文", "eng-chs")])
        for i, (text, lang) in enumerate(options):
            self.combo.addItem(text)
            self.combo.setItemData(i, lang)
        vbox_r.addWidget(self.combo)

        hbox.addLayout(vbox_l)
        hbox.addLayout(vbox_r)

        centerWidget.setLayout(hbox)
        self.setCentralWidget(centerWidget)
        self.retranslateUI()

    def setResult(self, n):
        self._result = n

    @ pyqtSlot()
    def get_dummy(self):
        f = Faker()
        self.le_name.setText(f.name())
        self.le_card_id.setText(f.numerify("#######"))
        self.le_phone_number.setText(f.phone_number())
        self.hint(self.msg_dummy)
        pass

    @ pyqtSlot()
    def clear(self):
        self.hint(self.msg_ready)
        self.clear_lineedits()

    @ pyqtSlot()
    def new(self):
        self.hint(self.msg_new)
        dialog = self.inputDialog(self)
        dialog.exec()
        self.hint(self.msg_result + str(self.result()))

    @ pyqtSlot()
    def save(self):
        self.hint(self.msg_save)

    @pyqtSlot()
    def add(self):
        self.hint(self.msg_add)

    @ pyqtSlot()
    def remove(self):
        self.warning(self.msg_remove)
        dialog = self.RemoveDialog(self)
        dialog.exec()

    @ pyqtSlot(int)
    def change_lang(self, index):
        data = self.combo.itemData(index)
        if data:
            self.trans.load(data)
            QApplication.instance().installTranslator(self.trans)
        else:
            QApplication.instance().removeTranslator(self.trans)

    def changeEvent(self, event) -> None:
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUI()
        super(MainUI, self).changeEvent(event)

    def hint(self, message: str):
        self.statusBar().setStyleSheet("QStatusBar { color : #aaaaff; }")
        self.statusBar().showMessage(message)

    def warning(self, message: str):
        self.statusBar().setStyleSheet("QStatusBar { color : #ff4444; }")
        self.statusBar().showMessage(message)

    def clear_lineedits(self):
        self.le_card_id.clear()
        self.le_name.clear()
        self.le_phone_number.clear()

    def retranslateUI(self):
        self.label_name.setText(QApplication.translate("MainUI", "name"))
        self.label_card_id.setText(QApplication.translate("MainUI", "card id"))
        self.label_phone_number.setText(QApplication.translate("MainUI", "phone number"))

        self.btn_dummy.setText(QApplication.translate("MainUI", "Get Dummy"))
        self.btn_clear.setText(QApplication.translate("MainUI", "Clear"))
        self.btn_new.setText(QApplication.translate("MainUI", "New"))
        self.btn_save.setText(QApplication.translate("MainUI", "Save"))
        self.btn_add.setText(QApplication.translate("MainUI", "Add"))
        self.btn_remove.setText(QApplication.translate("MainUI", "Remove"))

        self.msg_dummy = QApplication.translate("MainUI","Get Dummy clicked!")
        self.msg_new = QApplication.translate("MainUI", "New clicked!")
        self.msg_save = QApplication.translate("MainUI", "Save clicked!")
        self.msg_add = QApplication.translate("MainUI", "Add clicked!")
        self.msg_remove = QApplication.translate("MainUI", "Remove clicked!")
        self.msg_result = QApplication.translate("MainUI", "The result is ")

        self.msg_ready = QApplication.translate("MainUI", "Ready")
        self.hint(self.msg_ready)


def main(dbpath='./data.db'):
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)

    main_ui = MainUI()
    main_ui.show()

    r = app.exec()

    sys.exit(r)


if __name__ == '__main__':
    main()
    # I HOPE HOPE HOPE
