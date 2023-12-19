# Form implementation generated from reading ui file 'UserWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        UserWindow.setObjectName("UserWindow")
        UserWindow.resize(1000, 650)
        UserWindow.setMinimumSize(QtCore.QSize(1000, 650))
        font = QtGui.QFont()
        font.setPointSize(18)
        UserWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=UserWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(40, 44, 52);\n"
"\n"
"font-family:\"Segoe UI\";")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Left_Frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.Left_Frame.setMinimumSize(QtCore.QSize(70, 0))
        self.Left_Frame.setMaximumSize(QtCore.QSize(70, 16777215))
        self.Left_Frame.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.Left_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Left_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Left_Frame.setLineWidth(0)
        self.Left_Frame.setObjectName("Left_Frame")
        self.btn_exit_user = QtWidgets.QPushButton(parent=self.Left_Frame)
        self.btn_exit_user.setGeometry(QtCore.QRect(10, 10, 50, 50))
        self.btn_exit_user.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_exit_user.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_exit_user.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_exit_user.setStyleSheet("QPushButton{\n"
"background-color: rgb(40, 44, 52);\n"
"border: 2px solid rgb(40, 44, 52);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:rgb(192, 218, 255);\n"
"background-color: rgb(43, 51, 67);  \n"
"border: 2px solid rgb(33, 37, 43);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(192, 218, 255);\n"
"background-color: rgb(40, 44, 52); \n"
"border: 2px solid rgb(192, 218, 255);\n"
"border-radius: 15px;\n"
"}")
        self.btn_exit_user.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/cil-account-logout.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_exit_user.setIcon(icon)
        self.btn_exit_user.setObjectName("btn_exit_user")
        self.horizontalLayout.addWidget(self.Left_Frame)
        self.Right_Frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.Right_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Right_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Right_Frame.setObjectName("Right_Frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Right_Frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Frame = QtWidgets.QFrame(parent=self.Right_Frame)
        self.Top_Frame.setMinimumSize(QtCore.QSize(0, 576))
        self.Top_Frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Top_Frame.setStyleSheet("background-color: rgb(40, 44, 52);\n"
"")
        self.Top_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Top_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Top_Frame.setLineWidth(0)
        self.Top_Frame.setObjectName("Top_Frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.Top_Frame)
        self.horizontalLayout_10.setContentsMargins(40, 40, 40, 40)
        self.horizontalLayout_10.setSpacing(40)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame = QtWidgets.QFrame(parent=self.Top_Frame)
        self.frame.setMinimumSize(QtCore.QSize(300, 300))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("background-color: rgb(33, 37, 43);\n"
"border: 2px solid rgb(33, 37, 43);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.H_lay_Firstname = QtWidgets.QHBoxLayout()
        self.H_lay_Firstname.setObjectName("H_lay_Firstname")
        self.label_Firstname = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_Firstname.setFont(font)
        self.label_Firstname.setStyleSheet("color: rgb(192, 218, 255);")
        self.label_Firstname.setObjectName("label_Firstname")
        self.H_lay_Firstname.addWidget(self.label_Firstname)
        self.edit_Firstname = QtWidgets.QTextEdit(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_Firstname.sizePolicy().hasHeightForWidth())
        self.edit_Firstname.setSizePolicy(sizePolicy)
        self.edit_Firstname.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.edit_Firstname.setFont(font)
        self.edit_Firstname.setStyleSheet("color: rgb(192, 218, 255);\n"
"border: 2px solid rgb(78, 175, 255);  \n"
"border-radius: 15px;\n"
"")
        self.edit_Firstname.setObjectName("edit_Firstname")
        self.H_lay_Firstname.addWidget(self.edit_Firstname)
        self.verticalLayout_2.addLayout(self.H_lay_Firstname)
        self.H_lay_Lastname = QtWidgets.QHBoxLayout()
        self.H_lay_Lastname.setObjectName("H_lay_Lastname")
        self.label_Lastname = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_Lastname.setFont(font)
        self.label_Lastname.setStyleSheet("color: rgb(192, 218, 255);")
        self.label_Lastname.setObjectName("label_Lastname")
        self.H_lay_Lastname.addWidget(self.label_Lastname)
        self.edit_Lastname = QtWidgets.QTextEdit(parent=self.frame)
        self.edit_Lastname.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.edit_Lastname.setFont(font)
        self.edit_Lastname.setStyleSheet("color: rgb(192, 218, 255);\n"
"border: 2px solid rgb(78, 175, 255);  \n"
"border-radius: 15px;\n"
"")
        self.edit_Lastname.setObjectName("edit_Lastname")
        self.H_lay_Lastname.addWidget(self.edit_Lastname)
        self.verticalLayout_2.addLayout(self.H_lay_Lastname)
        self.H_lay_age = QtWidgets.QHBoxLayout()
        self.H_lay_age.setObjectName("H_lay_age")
        self.label_age = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_age.setFont(font)
        self.label_age.setStyleSheet("color: rgb(192, 218, 255);")
        self.label_age.setObjectName("label_age")
        self.H_lay_age.addWidget(self.label_age)
        self.edit_age = QtWidgets.QTextEdit(parent=self.frame)
        self.edit_age.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.edit_age.setFont(font)
        self.edit_age.setStyleSheet("color: rgb(192, 218, 255);\n"
"border: 2px solid rgb(78, 175, 255);  \n"
"border-radius: 15px;\n"
"")
        self.edit_age.setObjectName("edit_age")
        self.H_lay_age.addWidget(self.edit_age)
        self.verticalLayout_2.addLayout(self.H_lay_age)
        self.H_lay_phone = QtWidgets.QHBoxLayout()
        self.H_lay_phone.setObjectName("H_lay_phone")
        self.label_phone = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_phone.setFont(font)
        self.label_phone.setStyleSheet("color: rgb(192, 218, 255);")
        self.label_phone.setObjectName("label_phone")
        self.H_lay_phone.addWidget(self.label_phone)
        self.edit_phone = QtWidgets.QTextEdit(parent=self.frame)
        self.edit_phone.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.edit_phone.setFont(font)
        self.edit_phone.setStyleSheet("color: rgb(192, 218, 255);\n"
"border: 2px solid rgb(78, 175, 255);  \n"
"border-radius: 15px;\n"
"")
        self.edit_phone.setObjectName("edit_phone")
        self.H_lay_phone.addWidget(self.edit_phone)
        self.verticalLayout_2.addLayout(self.H_lay_phone)
        self.H_lay_mark = QtWidgets.QHBoxLayout()
        self.H_lay_mark.setObjectName("H_lay_mark")
        self.label_mark = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_mark.setFont(font)
        self.label_mark.setStyleSheet("color: rgb(192, 218, 255);")
        self.label_mark.setObjectName("label_mark")
        self.H_lay_mark.addWidget(self.label_mark)
        self.edit_mark = QtWidgets.QTextEdit(parent=self.frame)
        self.edit_mark.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.edit_mark.setFont(font)
        self.edit_mark.setStyleSheet("color: rgb(192, 218, 255);\n"
"border: 2px solid rgb(78, 175, 255);  \n"
"border-radius: 15px;\n"
"")
        self.edit_mark.setObjectName("edit_mark")
        self.H_lay_mark.addWidget(self.edit_mark)
        self.verticalLayout_2.addLayout(self.H_lay_mark)
        self.H_lay_desription = QtWidgets.QHBoxLayout()
        self.H_lay_desription.setObjectName("H_lay_desription")
        self.label_description = QtWidgets.QLabel(parent=self.frame)
        self.label_description.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(192, 218, 255);")
        self.label_description.setObjectName("label_description")
        self.H_lay_desription.addWidget(self.label_description)
        self.edit_description = QtWidgets.QTextEdit(parent=self.frame)
        self.edit_description.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.edit_description.setFont(font)
        self.edit_description.setStyleSheet("color: rgb(192, 218, 255);\n"
"border: 2px solid rgb(78, 175, 255);  \n"
"border-radius: 15px;\n"
"")
        self.edit_description.setObjectName("edit_description")
        self.H_lay_desription.addWidget(self.edit_description)
        self.verticalLayout_2.addLayout(self.H_lay_desription)
        self.H_lay_data = QtWidgets.QHBoxLayout()
        self.H_lay_data.setObjectName("H_lay_data")
        self.label_data = QtWidgets.QLabel(parent=self.frame)
        self.label_data.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_data.setFont(font)
        self.label_data.setStyleSheet("color: rgb(192, 218, 255);")
        self.label_data.setObjectName("label_data")
        self.H_lay_data.addWidget(self.label_data)
        self.dateEdit_user = QtWidgets.QDateEdit(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_user.sizePolicy().hasHeightForWidth())
        self.dateEdit_user.setSizePolicy(sizePolicy)
        self.dateEdit_user.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.dateEdit_user.setFont(font)
        self.dateEdit_user.setStyleSheet("color: rgb(192, 218, 255);\n"
"background-color: rgb(40, 44, 52);\n"
"border: 2px solid rgb(43, 51, 67); \n"
"border-radius: 15px;")
        self.dateEdit_user.setObjectName("dateEdit_user")
        self.H_lay_data.addWidget(self.dateEdit_user)
        self.verticalLayout_2.addLayout(self.H_lay_data)
        self.horizontalLayout_10.addWidget(self.frame)
        self.Info_Frame = QtWidgets.QFrame(parent=self.Top_Frame)
        self.Info_Frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Info_Frame.setStyleSheet("background-color: rgb(33, 37, 43);\n"
"border: 2px solid rgb(33, 37, 43);\n"
"border-radius: 15px;")
        self.Info_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Info_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Info_Frame.setObjectName("Info_Frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Info_Frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_Firstname_edit = QtWidgets.QLabel(parent=self.Info_Frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_Firstname_edit.setFont(font)
        self.label_Firstname_edit.setStyleSheet("color: rgb(192, 218, 255);")
        self.label_Firstname_edit.setObjectName("label_Firstname_edit")
        self.verticalLayout_4.addWidget(self.label_Firstname_edit)
        self.label_Lastname_edit = QtWidgets.QLabel(parent=self.Info_Frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_Lastname_edit.setFont(font)
        self.label_Lastname_edit.setStyleSheet("color: rgb(192, 218, 255);")
        self.label_Lastname_edit.setObjectName("label_Lastname_edit")
        self.verticalLayout_4.addWidget(self.label_Lastname_edit)
        self.label_age_edit = QtWidgets.QLabel(parent=self.Info_Frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_age_edit.setFont(font)
        self.label_age_edit.setStyleSheet("color: rgb(192, 218, 255);")
        self.label_age_edit.setObjectName("label_age_edit")
        self.verticalLayout_4.addWidget(self.label_age_edit)
        self.label_phone_edit = QtWidgets.QLabel(parent=self.Info_Frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_phone_edit.setFont(font)
        self.label_phone_edit.setStyleSheet("color: rgb(192, 218, 255);")
        self.label_phone_edit.setObjectName("label_phone_edit")
        self.verticalLayout_4.addWidget(self.label_phone_edit)
        self.horizontalLayout_10.addWidget(self.Info_Frame)
        self.verticalLayout.addWidget(self.Top_Frame)
        self.Bot_Frame = QtWidgets.QFrame(parent=self.Right_Frame)
        self.Bot_Frame.setMinimumSize(QtCore.QSize(300, 0))
        self.Bot_Frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Bot_Frame.setStyleSheet("background-color: rgb(40, 44, 52);\n"
"")
        self.Bot_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Bot_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Bot_Frame.setLineWidth(0)
        self.Bot_Frame.setObjectName("Bot_Frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Bot_Frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Holow_L_Frame = QtWidgets.QFrame(parent=self.Bot_Frame)
        self.Holow_L_Frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Holow_L_Frame.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.Holow_L_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Holow_L_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Holow_L_Frame.setObjectName("Holow_L_Frame")
        self.horizontalLayout_2.addWidget(self.Holow_L_Frame)
        self.Save_Frame = QtWidgets.QFrame(parent=self.Bot_Frame)
        self.Save_Frame.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.Save_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Save_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Save_Frame.setObjectName("Save_Frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Save_Frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_save = QtWidgets.QPushButton(parent=self.Save_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_save.setStyleSheet("QPushButton{\n"
"color:rgb(192, 218, 255);\n"
"background-color: rgb(33, 37, 43);;  \n"
"border: 2px solid rgb(33, 37, 43);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:rgb(192, 218, 255);\n"
"background-color: rgb(43, 51, 67);  \n"
"border: 2px solid rgb(33, 37, 43);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(192, 218, 255);\n"
"background-color: rgb(33, 37, 43);;  \n"
"border: 2px solid rgb(192, 218, 255);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout_3.addWidget(self.btn_save, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout_2.addWidget(self.Save_Frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Holow_R_Frame = QtWidgets.QFrame(parent=self.Bot_Frame)
        self.Holow_R_Frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Holow_R_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Holow_R_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Holow_R_Frame.setObjectName("Holow_R_Frame")
        self.horizontalLayout_2.addWidget(self.Holow_R_Frame)
        self.verticalLayout.addWidget(self.Bot_Frame)
        self.horizontalLayout.addWidget(self.Right_Frame)
        UserWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserWindow)
        QtCore.QMetaObject.connectSlotsByName(UserWindow)

    def retranslateUi(self, UserWindow):
        _translate = QtCore.QCoreApplication.translate
        UserWindow.setWindowTitle(_translate("UserWindow", "MainWindow"))
        self.label_Firstname.setText(_translate("UserWindow", "имя"))
        self.label_Lastname.setText(_translate("UserWindow", "фамилия"))
        self.label_age.setText(_translate("UserWindow", "возраст"))
        self.label_phone.setText(_translate("UserWindow", "номер телефона"))
        self.label_mark.setText(_translate("UserWindow", "марка машины"))
        self.label_description.setText(_translate("UserWindow", "описание\n"
"проблемы"))
        self.label_data.setText(_translate("UserWindow", "дата"))
        self.label_Firstname_edit.setText(_translate("UserWindow", "имя"))
        self.label_Lastname_edit.setText(_translate("UserWindow", "фамилия"))
        self.label_age_edit.setText(_translate("UserWindow", "возраст"))
        self.label_phone_edit.setText(_translate("UserWindow", "номер телефона"))
        self.btn_save.setText(_translate("UserWindow", "сохранить"))