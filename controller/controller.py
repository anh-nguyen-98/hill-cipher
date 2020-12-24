import functools

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow

from model.main import Model



class Controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.connect_signals()

    def set_alphabet_type(self):
        if self.view.ecp_type_alpha26.isChecked():
            self.alphabet_type = self.view.ecp_type_alpha26.text()

        elif self.view.ecp_type_alpha36.isChecked():
            self.alphabet_type = self.view.ecp_type_alpha36.text()

        elif self.view.dcp_type_alpha26.isChecked():
            self.alphabet_type = self.view.dcp_type_alpha26.text()

        elif self.view.dcp_type_alpha36.isChecked():
            self.alphabet_type = self.view.dcp_type_alpha36.text()

    def set_typePass(self):
        if self.view.ecp_pw_num_type.isChecked() or self.view.dcp_pw_num_type.isChecked():
            self.type_password = 0
        elif self.view.ecp_pw_alpha_type.isChecked() or self.view.dcp_pw_alpha_type.isChecked():
            self.type_password = 1


    def evaluate_password(self):

        if self.action == 0:
            password = self.view.ecp_pw_lineEdit.text().upper()
            if password == '':
                self.view.ecp_pw_status.setText('Please enter password')
            else:
                ret = self.model.evaluate_password(self.type_password, password, self.alphabet_type)
                if ret[0] == -1:
                    self.view.ecp_pw_status.setStyleSheet("color: rgb(248, 200, 83); font: 9pt MS Shell Dlg 2")
                    self.view.ecp_pw_status.setText('Your password is unsuccessfully set up. \nPlease check the number of characters again.'
                                                    ' Make sure that your password includes n^2 letters. ')

                elif ret[0] == 0:
                    self.view.ecp_pw_status.setStyleSheet("color: rgb(248, 200, 83); font: 9pt MS Shell Dlg 2")
                    if self.view.ecp_pw_num_type.isChecked():
                        if self.view.ecp_type_alpha26.isChecked():
                            self.view.ecp_pw_status.setText('Your password is unsuccessfully set up. \nPlease check the characters again. Suggested password: 5623')
                        elif self.view.ecp_type_alpha36.isChecked():
                            self.view.ecp_pw_status.setText(
                                'Your password is unsuccessfully set up. \nPlease check the characters again. Suggested password: 1372')
                    elif self.view.ecp_pw_alpha_type.isChecked():
                        if self.view.ecp_type_alpha26.isChecked():
                            self.view.ecp_pw_status.setText('Your password is unsuccessfully set up. \nPlease check the characters again. Suggested password: EFBC')
                        elif self.view.ecp_type_alpha36.isChecked():
                            self.view.ecp_pw_status.setText(
                                'Your password is unsuccessfully set up. \nPlease check the characters again. Suggested password: BDHC')

                else:
                    self.view.ecp_pw_status.setStyleSheet("color: rgb(0, 255, 0); font: 9pt MS Shell Dlg 2")
                    self.view.ecp_pw_status.setText('Your password is set up successfully.'
                    '\nYour password is ' + self.view.ecp_pw_lineEdit.text()+ '. Make sure: Password is known by your correspondent')

                    #create box to input plaintext

                    self.n = ret[1]
                    self.key = ret[2]
                    self.alphabet = ret[3]

                    self.view.ecp_continue_btn.setVisible(True)

        elif self.action == 1:
            password = self.view.dcp_pw_lineEdit.text().upper()
            if password == '':
                self.view.dcp_pw_status.setText('Please enter password')
            else:
                ret = self.model.evaluate_password(self.type_password, password, self.alphabet_type)
                if ret[0] == -1:
                    self.view.dcp_pw_status.setStyleSheet("color: rgb(248, 200, 83); font: 9pt MS Shell Dlg 2")
                    self.view.dcp_pw_status.setText(
                        'Your password is unsuccessfully set up. \nPlease check the number of characters again.'
                        ' Make sure that your password includes n^2 letters. ')

                elif ret[0] == 0:
                    self.view.dcp_pw_status.setStyleSheet("color: rgb(248, 200, 83); font: 9pt MS Shell Dlg 2")
                    if self.view.dcp_pw_num_type.isChecked():
                        if self.view.dcp_type_alpha26.isChecked():
                            self.view.dcp_pw_status.setText('Your password is unsuccessfully set up. \nPlease check the characters again. Suggested password: 5623')
                        elif self.view.dcp_type_alpha36.isChecked():
                            self.view.dcp_pw_status.setText(
                                'Your password is unsuccessfully set up. \nPlease check the characters again. Suggested password: 1372')
                    elif self.view.dcp_pw_alpha_type.isChecked():
                        if self.view.dcp_type_alpha26.isChecked():
                            self.view.dcp_pw_status.setText('Your password is unsuccessfully set up. \nPlease check the characters again. Suggested password: EFBC')
                        elif self.view.dcp_type_alpha36.isChecked():
                            self.view.dcp_pw_status.setText(
                                'Your password is unsuccessfully set up. \nPlease check the characters again. Suggested password: BDHC')
                    # self.view.dcp_pw_status.setText(
                    #     'Your password is unsuccessfully set up. \nPlease check the characters again.')
                else:
                    self.view.dcp_pw_status.setStyleSheet("color: rgb(0, 255, 0); font: 9pt MS Shell Dlg 2")
                    self.view.dcp_pw_status.setText('Your password is set up successfully.'
                                                    '\nYour password is ' + self.view.dcp_pw_lineEdit.text() + '. Make sure: Password is known by your correspondent')

                    # create box to input plaintext

                    self.n = ret[1]
                    self.key = ret[2]
                    self.alphabet = ret[3]

                    self.view.dcp_continue_btn.setVisible(True)


    def set_message(self):
        if self.action == 0:
            self.message = self.view.ecp_msg_lineEdit.text().upper()
        elif self.action == 1:
            self.message = self.view.dcp_msg_lineEdit.text().upper()
    #
    #
    def display_result(self):

        if self.action == 0:
            if self.message == '':
                self.view.ecp_ret_label.setText('Please enter message')

            ret = self.model.encipher(self.key, self.n, self.alphabet, self.message)
            self.view.ecp_ret_label.setText(ret)

        elif self.action == 1:
            if self.message == '':
                self.view.dcp_ret_label.setText('Please enter message')
            ret = self.model.decipher(self.key, self.n, self.alphabet,self.message)
            self.view.dcp_ret_label.setText(ret)

    def clear_form(self):

        self.view.ecp_type_alpha26.setChecked(False)
        self.view.ecp_type_alpha36.setChecked(False)
        self.view.ecp_pw_num_type.setChecked(False)
        self.view.ecp_pw_alpha_type.setChecked(False)
        self.view.ecp_pw_lineEdit.setText('')
        self.view.ecp_pw_status.setText('')
        self.view.ecp_msg_lineEdit.setText('')
        self.view.ecp_ret_label.setText('')
        self.view.ecp_continue_btn.setVisible(False)

        self.view.dcp_type_alpha26.setChecked(False)
        self.view.dcp_type_alpha36.setChecked(False)
        self.view.dcp_pw_num_type.setChecked(False)
        self.view.dcp_pw_alpha_type.setChecked(False)
        self.view.dcp_pw_lineEdit.setText('')
        self.view.dcp_pw_status.setText('')
        self.view.dcp_msg_lineEdit.setText('')
        self.view.dcp_ret_label.setText('')
        self.view.dcp_continue_btn.setVisible(False)




    def showHomePage(self):

        self.view.stackedWidget.setCurrentWidget(self.view.home_pg)

    def showAboutUsPage(self):
        self.view.stackedWidget.setCurrentWidget(self.view.about_us_pg)

    def showEncipherPage(self):
        self.action = 0
        self.clear_form()
        self.view.stackedWidget.setCurrentWidget(self.view.ecp_pg)

    def showEncipherPage2(self):
        self.clear_form()
        self.view.stackedWidget.setCurrentWidget(self.view.ecp_pg_2)

    def showDecipherPage(self):
        self.action = 1
        self.clear_form()
        self.view.stackedWidget.setCurrentWidget(self.view.dcp_pg)

    def showDecipherPage2(self):
        self.clear_form()
        self.view.stackedWidget.setCurrentWidget(self.view.dcp_pg_2)
    def showTeamPage(self):
        self.view.stackedWidget.setCurrentWidget(self.view.team_pg)


    def connect_signals(self):
        #deals with menu buttons
        self.view.stackedWidget.setCurrentWidget(self.view.home_pg)
        self.view.homebtn.clicked.connect(self.showHomePage)
        self.view.aboutusbtn.clicked.connect(self.showAboutUsPage)
        self.view.encipherbtn.clicked.connect(self.showEncipherPage)
        self.view.decipherbtn.clicked.connect(self.showDecipherPage)
        self.view.teambtn.clicked.connect(self.showTeamPage)

        #deals with home_pg btn:
        self.view.learnmore.clicked.connect(self.showAboutUsPage)

        #deals with aboutus_pg btn:
        self.view.ecp_btn_aboutus.clicked.connect(self.showEncipherPage)
        self.view.dcp_btn_aboutus.clicked.connect(self.showDecipherPage)


        #deals with encipher page:
        #alphabet type
        self.view.ecp_type_alpha26.toggled.connect(self.set_alphabet_type)
        self.view.ecp_type_alpha36.toggled.connect(self.set_alphabet_type)

        #pass type
        self.view.ecp_pw_num_type.toggled.connect(self.set_typePass)
        self.view.ecp_pw_alpha_type.toggled.connect(self.set_typePass)

        #pass input + check pass

        self.view.ecp_done_btn.clicked.connect(self.evaluate_password)

        self.view.ecp_continue_btn.clicked.connect(self.showEncipherPage2)


        #input plaitext
        self.view.ecp_msg_lineEdit.editingFinished.connect(self.set_message)
        self.view.ecp_encode_btn.pressed.connect(self.display_result)

        # deals with decipher page
        self.view.dcp_type_alpha26.toggled.connect(self.set_alphabet_type)
        self.view.dcp_type_alpha36.toggled.connect(self.set_alphabet_type)


        self.view.dcp_pw_num_type.toggled.connect(self.set_typePass)
        self.view.dcp_pw_alpha_type.toggled.connect(self.set_typePass)

        # pass input + check pass

        self.view.dcp_done_btn.clicked.connect(self.evaluate_password)

        self.view.dcp_continue_btn.clicked.connect(self.showDecipherPage2)

        # input ciphertext
        self.view.dcp_msg_lineEdit.editingFinished.connect(self.set_message)
        self.view.dcp_encode_btn.pressed.connect(self.display_result)


        #PUT THIS TO UI FILE
        # self.ecp_continue_btn.setVisible(False)
        # self.dcp_continue_btn.setVisible(False)
        # self.ecp_type_alpha26.setAutoExclusive(False)
        # self.ecp_type_alpha36.setAutoExclusive(False)
        # self.ecp_pw_num_type.setAutoExclusive(False)
        # self.ecp_pw_alpha_type.setAutoExclusive(False)
        #
        # self.dcp_type_alpha26.setAutoExclusive(False)
        # self.dcp_type_alpha36.setAutoExclusive(False)
        # self.dcp_pw_num_type.setAutoExclusive(False)
        # self.dcp_pw_alpha_type.setAutoExclusive(False)

