import sys
from collections import Counter
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(500, 500)
        self.setWindowTitle("Projet 2")


        # User Input
        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("Find Unique words")
        self.btnPress2 = QPushButton("Find Duplicate words")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)

        self.setLayout(layout)

        # Button event handler
        self.btnPress1.clicked.connect(self.press_btn1)
        self.btnPress2.clicked.connect(self.press_btn2)

        self.uniq_data = QLabel("Uniq words")
        layout.addWidget(self.uniq_data)

        self.show_text_one = QTextEdit()
        layout.addWidget(self.show_text_one)

        self.dupli_data = QLabel("Duplicate lines")
        layout.addWidget(self.dupli_data)

        self.show_text_two = QTextEdit()
        layout.addWidget(self.show_text_two)

    def press_btn1(self):
        """This function is edit the text of second text box which is display the duplicated lines."""
        find_dup = self.textEdit.toPlainText()
        new_dup = self.find_duplicates(find_dup)
        print(new_dup)
        self.show_text_two.setText(new_dup)

    def press_btn2(self):
        """This function is edit the text of first text box which is display the unique lines."""
        da = self.textEdit.toPlainText()
        new_data = self.find_uniq(da)
        print(new_data)
        self.show_text_one.setText(new_data)

    def find_uniq(self, lst):
        """This function takes string from text box and split the new lines and create a list.
        and return the unique lines only. It return string with new line characters."""
        wordlist = lst.split("\n")
        uniq_words = []
        duplicates = []
        for i in wordlist:
            if i not in uniq_words:
                uniq_words.append(i)
        dup_list = Counter(wordlist)
        for i, k in dup_list.items():
            duplicates.append(i)
        str_uniq_word = "\n".join(uniq_words)
        return str_uniq_word

    def find_duplicates(self, lst):
        """It takes string and use the counter function to find the words repeat and return the only duplicate words.
        It also return string with new line characters"""
        wordlist = lst.split("\n")
        duplicates = []
        dup_list = Counter(wordlist)
        for i, k in dup_list.items():
            if k >= 2:
                duplicates.append(i)
        str_dup = "\n".join(duplicates)
        return str_dup


def main():
    app = QApplication([])
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
