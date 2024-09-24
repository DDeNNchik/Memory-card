from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from random import shuffle

app = QApplication([])

from layout1 import *
from data import *

i = 0
points = 0

window = QWidget()
window.resize(600, 500)
window.setWindowTitle("Memory Card")
window.setLayout(main_line_quizz)
window.show()
shuffle(questions)
shuffle(rbuttons)
questions[i].show_question(quest_lb, rbuttons)

def click_ok():
    global i, points
    if btn_ok.text() == "Відповісти":
        if rbuttons[0].isChecked():
            result_lb.setText("Правильно")
            points += 1
        else:
            result_lb.setText("Неправильно")
        right_ans_lb.setText(rbuttons[0].text())
        rbGroupbox.hide()
        ansGroupbox.show()
        btn_ok.setText("Наступне завдання")
    else:
        if i < 3:
            button_group.setExclusive(False)
            for b in rbuttons:
                b.setChecked(False)
            button_group.setExclusive(True)
            i += 1
            shuffle(rbuttons)
            questions[i].show_question(quest_lb, rbuttons)
            rbGroupbox.show()
            ansGroupbox.hide()
            btn_ok.setText("Відповісти")
        else:
            msg = QMessageBox()
            msg.setText(str(points))
            msg.exec()


btn_ok.clicked.connect(click_ok)

app.exec()