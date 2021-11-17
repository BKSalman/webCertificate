import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *

from PyQt5.uic import loadUi

import sqlite3

from threading import Thread

from CertificateGenerator import generateCertificate, sendEmail

connection = sqlite3.connect("Data.sqlite")
cur = connection.cursor()
class mainApp(QMainWindow):
    def __init__(self):
        super(mainApp, self).__init__()
        loadUi("CertificationUI.ui", self)
        self.PageOneBtn.clicked.connect(self.page1)
        self.PageTwoBtn.clicked.connect(self.page2)
        self.tableWidget.setColumnWidth(0, 20)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 300)
        self.loaddata()
        self.AddBtn.clicked.connect(self.saveInfo)
        self.RemoveBtn.clicked.connect(self.removeinfo)
        self.OMK3NDYBtn.clicked.connect(self.omk3ndy)
        self.omk3ndystate = 0
        qpixmap = QtGui.QPixmap("UI/OMK3NDY.png")
        self.OMK3NDYPic.setPixmap(qpixmap)
        self.OMK3NDYPic.setHidden(True)
        # Certificate = generateCertificate()
        self.CreateBtn.clicked.connect(generateCertificate)
        self.EmailBtn.clicked.connect(sendEmail)
        # self.PageOneBtn.setStyleSheet("background:#22272d;")

        # with open('Data3.csv', 'r', encoding='UTF-8') as f:

        #     threads = []

        #     for i, studentData in enumerate(f):
        #         if i == 0: continue

        #         thread = Thread(target=generateCertificate, args=(studentData,))
        #         threads.append(thread)
        #         thread.start()

        #     for thread in threads: 
        #         thread.join() # wait for completion

    def omk3ndy(self):
        if self.omk3ndystate == 0:
            self.omk3ndystate = 1
            self.OMK3NDYPic.setHidden(False)
        elif self.omk3ndystate == 1:
            self.omk3ndystate = 0
            self.OMK3NDYPic.setHidden(True)
        

    def createCertificate(self):
        Names = []
        Id = []
        sqlquery = "SELECT Name FROM People;"
        names = cur.execute(sqlquery)
        sqlquery = "SELECT ID FROM People;"
        IDs = cur.execute(sqlquery)
        for i in names:
            Names += i
        for i in IDs:
            Id += i



    def loaddata(self):
        
        sqlquery = "SELECT * FROM People;"

        Count = "SELECT COUNT(*) FROM People"
        for i in cur.execute(Count):
            c = i
        
        self.tableWidget.setRowCount(c[0])
        
        tablerow = 0
        for row in cur.execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow += 1


    def page1(self):
        self.stackedWidget.setCurrentWidget(self.page)

    def page2(self):
        self.stackedWidget.setCurrentWidget(self.page_2)

    def saveInfo(self):
        connection = sqlite3.connect("Data.sqlite")
        cur = connection.cursor() 
        Id = self.IdLine.text()
        cur.execute("SELECT ID FROM People WHERE ID=?",(Id,))
        if cur.fetchone() is not None:
            return
        Pre = self.PreMenu.currentText()
        Name = self.NameLine.text()
        Email = self.EmailLine.text()
        cur.execute("INSERT INTO People (Pre, ID, Name, Email) Values(?,?,?,?);",(Pre,Id,Name,Email))
        connection.commit()

        self.loaddata()

    def removeinfo(self):
        connection = sqlite3.connect("Data.sqlite")
        cur = connection.cursor()
        currentrow = self.tableWidget.currentRow()
        if currentrow >= 0:
            primary = self.tableWidget.item(currentrow, 1).text()
            cur.execute(f"DELETE FROM People WHERE ID=\"{primary}\" ;")
            connection.commit()
            self.tableWidget.removeRow(currentrow)
            self.loaddata()

app = QApplication(sys.argv)
mainwindow = mainApp()
mainwindow.show()
app.exec_()