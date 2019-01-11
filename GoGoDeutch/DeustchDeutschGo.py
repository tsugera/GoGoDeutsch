
from PyQt5.QtWidgets import  QHeaderView, QPushButton,QApplication, QComboBox, QTableWidget, QTableWidgetItem, QWizard, QWizardPage
from PyQt5 import uic

from PyQt5.QtCore import QSize, Qt



class MagicWizard(QWizard):
    def __init__(self, parent=None):
        super(MagicWizard, self).__init__(parent)
        self.addPage(Page1(self))
        self.addPage(Page2(self))
        self.addPage(Page3(self))
        self.addPage(Page4(self))
        self.addPage(Page5(self))
        self.setWindowTitle("GoGoDeutsch")
        self.resize(750, 600)


class Page1(QWizardPage):
    def __init__(self, parent=None):
        super(Page1, self).__init__(parent)
        uic.loadUi('3.ui', self)
        self.answer_label.setVisible(False)  # изначально делаем ответы невидимыми
        headline = [
            {"title": 'Auf Deutsch', "key": "D", "hidden": False, "width": 150},
            {"title": 'Auf Russisch', "key": "R", "hidden": False, "width": 150},

        ]

        data = [
            {"D": "die Sprache", "R": "a) песня"},
            {"D": "die Fremdsprache", "R": "b) язык"},
            {"D": "die Weltsprache", "R": "c) сочинение"},
            {"D": "die Muttersprache", "R": "d) урок"},
            {"D": "die Stunde", "R": "e) учебный материал"},
            {"D": "der Lehrstoff", "R": "f) иностранный язык"},
            {"D": "der Aufsatz", "R": "g) стихотворение"},
            {"D": "das Gedicht", "R": "h) правило"},
            {"D": "das Lied", "R": "i) мировой язык"},
            {"D": "die Regel", "R": "j) родной язык"},

        ]
        self.fill_table(table=self.tableWidget, headline=headline, data=data)
    def fill_table(self, table, headline, data):
        cnt = 0
        table.clearContents()
        table.setRowCount(0)
        head = []
        headline_strip = []

        for i in headline:
            if i['hidden'] == False:
                head.append(i['title'])
                headline_strip.append(i)

        table.setColumnCount(headline_strip.__len__())
        table.horizontalHeader().setMinimumSectionSize(0)
        for i, k in enumerate(headline_strip):
            if k['width'] == 'auto':
                table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
            else:
                table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Interactive)
                table.horizontalHeader().resizeSection(i, k['width'])

        table.setHorizontalHeaderLabels(head)

        for i in data:
            table.insertRow(cnt)

            for j, k in enumerate(headline_strip):
                if k['hidden'] == False:
                    cell = QTableWidgetItem()
                    cell.setText(str(i[k['key']]))
                    table.setItem(cnt, j, cell)
            cnt = cnt + 1
        table.setCurrentCell(0, 0)



class Page2(QWizardPage):
    def __init__(self, parent=None):
        super(Page2, self).__init__(parent)
        uic.loadUi('2_Fixed.ui', self)

        self.label_14.setVisible(False) #изначально делаем ответы невидимыми

        self.pushButton.clicked.connect(lambda: self.comboBox_5.setEnabled(False))
        self.pushButton.clicked.connect(lambda: self.comboBox.setEnabled(False))
        self.pushButton.clicked.connect(lambda: self.comboBox_4.setEnabled(False))
        self.pushButton.clicked.connect(lambda: self.comboBox_2.setEnabled(False))
        self.pushButton.clicked.connect(lambda: self.comboBox_6.setEnabled(False))
        self.pushButton.clicked.connect(lambda: self.comboBox_3.setEnabled(False))

class Page3(QWizardPage):
    def __init__(self, parent=None):
        super(Page3, self).__init__(parent)
        uic.loadUi('4.ui', self)
        self.answer_label.setVisible(False)  # изначально делаем ответы невидимыми
        self.answer_label_2.setVisible(False)
        headline = [
            {"title": 'Auf Deutsch', "key": "D", "hidden": False, "width": 150},
            {"title": 'Auf Russisch', "key": "R", "hidden": False, "width": 150},

        ]

        data = [
            {"D": "abschreiben", "R": "a)произносить"},
            {"D": "antworten", "R": "b)списывать"},
            {"D": "aufschreiben", "R": "c)отвечать"},
            {"D": "aussprechen", "R": "d)изучать, открывать"},
            {"D": "beschreiben", "R": "e)записывать "},
            {"D": "entdecken", "R": "f) описывать"},
            {"D": "ergänzen", "R": "g) слушать"},
            {"D": "erklären", "R": "h) дополнять"},
            {"D": "erzählen", "R": "i) исправлять"},
            {"D": "hören", "R": "j)объяснять"},
            {"D": "korrigieren", "R": "k)рассказывать"},
            {"D": "lernen", "R": "l)петь"},
            {"D": "nacherzählen", "R": "m)учить, учиться"},
            {"D": "singen", "R": "n)пересказывать"},
            {"D": "sprechen", "R": "o)упражняться, тренировать"},
            {"D": "üben", "R": "p)переводить"},
            {"D": "übersetzen", "R": "q)говорить"},
            {"D": "verstehen", "R": "r)повторять"},
            {"D": "vorlesen", "R": "s) понимать"},
            {"D": "wiederholen", "R": "t)читать вслух"},


        ]
        self.fill_table(table=self.tableWidget, headline=headline, data=data)
    def fill_table(self, table, headline, data):
        cnt = 0
        table.clearContents()
        table.setRowCount(0)
        head = []
        headline_strip = []

        for i in headline:
            if i['hidden'] == False:
                head.append(i['title'])
                headline_strip.append(i)

        table.setColumnCount(headline_strip.__len__())
        table.horizontalHeader().setMinimumSectionSize(0)
        for i, k in enumerate(headline_strip):
            if k['width'] == 'auto':
                table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
            else:
                table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Interactive)
                table.horizontalHeader().resizeSection(i, k['width'])

        table.setHorizontalHeaderLabels(head)

        for i in data:
            table.insertRow(cnt)

            for j, k in enumerate(headline_strip):
                if k['hidden'] == False:
                    cell = QTableWidgetItem()
                    cell.setText(str(i[k['key']]))
                    table.setItem(cnt, j, cell)
            cnt = cnt + 1
        table.setCurrentCell(0, 0)

class Page4(QWizardPage):
    def __init__(self, parent=None):
        super(Page4, self).__init__(parent)
        uic.loadUi('4_.ui', self)

        self.answer_label.setVisible(False) #изначально делаем ответы невидимыми
        self.answer_label_2.setVisible(False)
        self.answer_label_3.setVisible(False)
        self.answer_label_4.setVisible(False)


        self.pushButton.clicked.connect(lambda: self.comboBox.setEnabled(False))
        self.pushButton.clicked.connect(lambda: self.comboBox_2.setEnabled(False))
        self.pushButton.clicked.connect(lambda: self.comboBox_3.setEnabled(False))
        self.pushButton.clicked.connect(lambda: self.comboBox_4.setEnabled(False))
        self.pushButton.clicked.connect(lambda: self.comboBox_5.setEnabled(False))

class Page5(QWizardPage):
    def __init__(self, parent=None):
        super(Page5, self).__init__(parent)
        uic.loadUi('5.ui', self)

        

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    wizard = MagicWizard()
    wizard.show()
    sys.exit(app.exec_())