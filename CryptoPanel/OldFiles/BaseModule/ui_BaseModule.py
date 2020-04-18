from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Widgets import uni_Widget


class ui_BasePanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_BasePanel, self).__init__()
        self.BaseMode = 1
        self.BaseTextInputPath = ''
        self.BaseTextOutputPath = ''
        self.BaseCipherInputPath = ''
        self.BaseCipherOutputPath = ''

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.BaseMainLayout = QtWidgets.QVBoxLayout()
        self.BaseMainLayout.setObjectName("BaseMainLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Base64Button = uni_Widget.ICTFEButton(self)
        self.Base64Button.setMinimumSize(QtCore.QSize(120, 45))
        self.Base64Button.setMaximumSize(QtCore.QSize(120, 45))
        self.Base64Button.setObjectName("Base64Button")
        self.horizontalLayout.addWidget(self.Base64Button)
        self.Base32Button = uni_Widget.ICTFEButton(self)
        self.Base32Button.setMinimumSize(QtCore.QSize(120, 45))
        self.Base32Button.setMaximumSize(QtCore.QSize(120, 45))
        self.Base32Button.setObjectName("Base32Button")
        self.horizontalLayout.addWidget(self.Base32Button)
        self.Base16Button = uni_Widget.ICTFEButton(self)
        self.Base16Button.setMinimumSize(QtCore.QSize(120, 45))
        self.Base16Button.setMaximumSize(QtCore.QSize(120, 45))
        self.Base16Button.setObjectName("Base16Button")
        self.horizontalLayout.addWidget(self.Base16Button)
        self.Base85Button = uni_Widget.ICTFEButton(self)
        self.Base85Button.setMinimumSize(QtCore.QSize(120, 45))
        self.Base85Button.setMaximumSize(QtCore.QSize(120, 45))
        self.Base85Button.setObjectName("Base85Button")
        self.horizontalLayout.addWidget(self.Base85Button)
        self.Base85RFCButton = uni_Widget.ICTFEButton(self)
        self.Base85RFCButton.setMinimumSize(QtCore.QSize(120, 45))
        self.Base85RFCButton.setMaximumSize(QtCore.QSize(120, 45))
        self.Base85RFCButton.setObjectName("Base85RFCButton")
        self.horizontalLayout.addWidget(self.Base85RFCButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.BaseEButton = uni_Widget.ICTFEButton(self)
        self.BaseEButton.setMinimumSize(QtCore.QSize(200, 45))
        self.BaseEButton.setMaximumSize(QtCore.QSize(200, 45))
        self.BaseEButton.setObjectName("BaseEButton")
        self.horizontalLayout.addWidget(self.BaseEButton)
        self.BaseMainLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BaseTableTips = uni_Widget.ICTFELabel(self)
        self.BaseTableTips.setObjectName("BaseTableTips")
        self.horizontalLayout_2.addWidget(self.BaseTableTips)
        self.BaseTableBox = uni_Widget.ICTFELineBox(self)
        self.BaseTableBox.setObjectName("BaseTableBox")
        self.horizontalLayout_2.addWidget(self.BaseTableBox)
        self.BaseEncButton = uni_Widget.ICTFEButton(self)
        self.BaseEncButton.setMinimumSize(QtCore.QSize(120, 45))
        self.BaseEncButton.setMaximumSize(QtCore.QSize(120, 45))
        self.BaseEncButton.setObjectName("BaseEncButton")
        self.horizontalLayout_2.addWidget(self.BaseEncButton)
        self.BaseDecButton = uni_Widget.ICTFEButton(self)
        self.BaseDecButton.setMinimumSize(QtCore.QSize(120, 45))
        self.BaseDecButton.setMaximumSize(QtCore.QSize(120, 45))
        self.BaseDecButton.setObjectName("BaseDecButton")
        self.horizontalLayout_2.addWidget(self.BaseDecButton)
        self.BaseMainLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BaseTextInputButton = uni_Widget.ICTFEButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaseTextInputButton.sizePolicy().hasHeightForWidth())
        self.BaseTextInputButton.setSizePolicy(sizePolicy)
        self.BaseTextInputButton.setMinimumSize(QtCore.QSize(120, 45))
        self.BaseTextInputButton.setMaximumSize(QtCore.QSize(120, 45))
        self.BaseTextInputButton.setObjectName("BaseTextInputButton")
        self.horizontalLayout_3.addWidget(self.BaseTextInputButton)
        self.BaseTextOutputButton = uni_Widget.ICTFEButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaseTextOutputButton.sizePolicy().hasHeightForWidth())
        self.BaseTextOutputButton.setSizePolicy(sizePolicy)
        self.BaseTextOutputButton.setMinimumSize(QtCore.QSize(120, 45))
        self.BaseTextOutputButton.setMaximumSize(QtCore.QSize(120, 45))
        self.BaseTextOutputButton.setObjectName("BaseTextOutputButton")
        self.horizontalLayout_3.addWidget(self.BaseTextOutputButton)
        self.BaseTextEvalCheckBox = uni_Widget.ICTFECheckBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaseTextEvalCheckBox.sizePolicy().hasHeightForWidth())
        self.BaseTextEvalCheckBox.setSizePolicy(sizePolicy)
        self.BaseTextEvalCheckBox.setMinimumSize(QtCore.QSize(120, 45))
        self.BaseTextEvalCheckBox.setMaximumSize(QtCore.QSize(120, 45))
        self.BaseTextEvalCheckBox.setObjectName("BaseTextEvalCheckBox")
        self.horizontalLayout_3.addWidget(self.BaseTextEvalCheckBox)
        self.BaseDoNotLoadFileCheckBox = uni_Widget.ICTFECheckBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaseDoNotLoadFileCheckBox.sizePolicy().hasHeightForWidth())
        self.BaseDoNotLoadFileCheckBox.setSizePolicy(sizePolicy)
        self.BaseDoNotLoadFileCheckBox.setMinimumSize(QtCore.QSize(120, 45))
        self.BaseDoNotLoadFileCheckBox.setMaximumSize(QtCore.QSize(120, 45))
        self.BaseDoNotLoadFileCheckBox.setObjectName("BaseDoNotLoadFileCheckBox")
        self.horizontalLayout_3.addWidget(self.BaseDoNotLoadFileCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.BaseTextBox = uni_Widget.ICTFETextBox(self)
        self.BaseTextBox.setObjectName("BaseTextBox")
        self.verticalLayout.addWidget(self.BaseTextBox)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.BaseCipherInputButton = uni_Widget.ICTFEButton(self)
        self.BaseCipherInputButton.setMinimumSize(QtCore.QSize(120, 45))
        self.BaseCipherInputButton.setMaximumSize(QtCore.QSize(120, 45))
        self.BaseCipherInputButton.setObjectName("BaseCipherInputButton")
        self.horizontalLayout_4.addWidget(self.BaseCipherInputButton)
        self.BaseCipherOutputButton = uni_Widget.ICTFEButton(self)
        self.BaseCipherOutputButton.setMinimumSize(QtCore.QSize(120, 45))
        self.BaseCipherOutputButton.setMaximumSize(QtCore.QSize(120, 45))
        self.BaseCipherOutputButton.setObjectName("BaseCipherOutputButton")
        self.horizontalLayout_4.addWidget(self.BaseCipherOutputButton)
        self.BaseTranslateButton = uni_Widget.ICTFEButton(self)
        self.BaseTranslateButton.setMinimumSize(QtCore.QSize(120, 45))
        self.BaseTranslateButton.setMaximumSize(QtCore.QSize(120, 45))
        self.BaseTranslateButton.setObjectName("BaseTranslateButton")
        self.horizontalLayout_4.addWidget(self.BaseTranslateButton)
        self.BaseAutoLoadCheckBox = uni_Widget.ICTFECheckBox(self)
        self.BaseAutoLoadCheckBox.setMinimumSize(QtCore.QSize(120, 45))
        self.BaseAutoLoadCheckBox.setMaximumSize(QtCore.QSize(120, 45))
        self.BaseAutoLoadCheckBox.setObjectName("BaseAutoLoadCheckBox")
        self.horizontalLayout_4.addWidget(self.BaseAutoLoadCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.BaseCipherBox = uni_Widget.ICTFETextBox(self)
        self.BaseCipherBox.setObjectName("BaseCipherBox")
        self.verticalLayout_2.addWidget(self.BaseCipherBox)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.BaseMainLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.BaseMainLayout)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Base64Button.setText(_translate("self", "Base64"))
        self.Base32Button.setText(_translate("self", "Base32"))
        self.Base16Button.setText(_translate("self", "Base16"))
        self.Base85Button.setText(_translate("self", "Base85ASC"))
        self.Base85RFCButton.setText(_translate("self", "Base85RFC"))
        self.BaseEButton.setText(_translate("self", "Base64隐写提取"))
        self.BaseTableTips.setText(_translate("self", "编码表:"))
        self.BaseEncButton.setText(_translate("self", "编码"))
        self.BaseDecButton.setText(_translate("self", "解码"))
        self.BaseTextInputButton.setText(_translate("self", "打开"))
        self.BaseTextOutputButton.setText(_translate("self", "另存为"))
        self.BaseTextEvalCheckBox.setText(_translate("self", "启用eval"))
        self.BaseDoNotLoadFileCheckBox.setText(_translate("self", "大文件"))
        self.BaseCipherInputButton.setText(_translate("self", "打开"))
        self.BaseCipherOutputButton.setText(_translate("self", "另存为"))
        self.BaseTranslateButton.setText(_translate("self", "交换"))
        self.BaseAutoLoadCheckBox.setText(_translate("self", "AutoLoad"))

        # end base panel