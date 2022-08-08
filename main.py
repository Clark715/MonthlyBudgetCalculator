
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5 import uic
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # LINK GUI
        uic.loadUi('budgetui.ui', self)

# //LINK GUI PIECES//

        # LABELS
        self.explain_l = self.findChild(QLabel, 'label_9')
        self.income_l = self.findChild(QLabel, 'label')
        self.home_l = self.findChild(QLabel, 'label_2')
        self.utilities_l = self.findChild(QLabel, 'label_3')
        self.food_l = self.findChild(QLabel, 'label_4')
        self.trans_l = self.findChild(QLabel, 'label_5')
        self.debt_l = self.findChild(QLabel, 'label_6')
        self.personal_l = self.findChild(QLabel, 'label_7')
        self.other_l = self.findChild(QLabel, 'label_8')

        # LINE EDITS
        self.income_edit = self.findChild(QLineEdit, 'lineEdit')
        self.home_edit = self.findChild(QLineEdit, 'lineEdit_2')
        self.utilities_edit = self.findChild(QLineEdit, 'lineEdit_3')
        self.food_edit = self.findChild(QLineEdit, 'lineEdit_4')
        self.trans_edit = self.findChild(QLineEdit, 'lineEdit_5')
        self.debt_edit = self.findChild(QLineEdit, 'lineEdit_6')
        self.personal_edit = self.findChild(QLineEdit, 'lineEdit_7')
        self.other_edit = self.findChild(QLineEdit, 'lineEdit_8')

        # PUSH BUTTONS
        self.go_button = self.findChild(QPushButton, 'pushButton_2')
        self.exit_button = self.findChild(QPushButton, 'pushButton')

        # BUTTON ACTIONS
        self.exit_button.clicked.connect(self.exitapp)
        self.go_button.clicked.connect(self.user_input)

        # SHOW WINDOW
        self.show()


# //FUNCTIONS//


    # 'EXIT' BUTTON PRESSED
    def exitapp(self):

        self.close()


    # 'GO' BUTTON PRESSED
    def user_input(self):

        try:
            # CONVERT INCOME & EXPENSES TO FLOATS / SHOW RESULTS
            income = self.income_edit.text()
            income_float = float(income)


            num_list = [self.home_edit, self.utilities_edit, self.food_edit, self.trans_edit,
                        self.debt_edit, self.personal_edit, self.other_edit]
            le_text = [n.text() for n in num_list]

            for i in range(len(le_text)):
                if le_text[i] == '':
                    le_text[i] = 0

            nums_final = list(map(float, le_text))

            print('Income: ' + str(round(income_float)), 'Expenses: ' + str(nums_final))

            expenses_total = sum(nums_final)
            leftover_total = income_float - expenses_total

            print('Total expenses: ' + str(expenses_total) + '\nLeftover: ' + str(leftover_total))

            QMessageBox.about(self, 'Done!', 'Based on a monthly income of $' + str(round(income_float)) + ', you are left '
                                             'with $' + str(round(leftover_total)) + ' after all your expenses totaling $' +
                                             str(round(expenses_total)) + '.')

        except:
            QMessageBox.about(self, 'Error', 'Something went wrong. Please make sure you are using numbers and '
                                             'decimals only without letters or special characters.')
            print('Invalid inputs / Something went wrong')
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    UIMain = MainWindow()
    app.exec_()
