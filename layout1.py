from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QSpinBox, QGroupBox, QHBoxLayout, QButtonGroup, QVBoxLayout, QPushButton, QRadioButton
from PyQt5.QtCore import Qt

btn_menu = QPushButton("Меню")

btn_rest = QPushButton("Відпочити")
spin = QSpinBox()
spin.setValue(30)

quest_lb = QLabel("яблуко")
rbGroupbox = QGroupBox("Варіанти відповідей:")
btn_ok = QPushButton("Відповісти")
button_group = QButtonGroup()

rb1 = QRadioButton("1")
rb2 = QRadioButton("2")
rb3 = QRadioButton("3")
rb4 = QRadioButton("4")
button_group.addButton(rb1)
button_group.addButton(rb2)
button_group.addButton(rb3)
button_group.addButton(rb4)

rbuttons = [rb1, rb2, rb3, rb4]

main_line_quizz = QVBoxLayout()
line1_quizz = QHBoxLayout()

main_box_line = QHBoxLayout()
box_line1 = QVBoxLayout()
box_line2 = QVBoxLayout()
box_line1.addWidget(rb1)
box_line1.addWidget(rb2)
box_line2.addWidget(rb3)
box_line2.addWidget(rb4)
main_box_line.addLayout(box_line1)
main_box_line.addLayout(box_line2)
rbGroupbox.setLayout(main_box_line)

#rbGroupbox.hide()

ansGroupbox = QGroupBox("Результат тесту:")
main_box2_line = QVBoxLayout()
result_lb = QLabel("Правильно")
right_ans_lb = QLabel("apple")
main_box2_line.addWidget(result_lb)
main_box2_line.addWidget(right_ans_lb)
ansGroupbox.setLayout(main_box2_line)
ansGroupbox.hide()

line1_quizz.addWidget(btn_menu)
line1_quizz.addStretch(1)
line1_quizz.addWidget(btn_rest)
line1_quizz.addWidget(spin)
line1_quizz.addWidget(QLabel("хвилин"))

main_line_quizz.addLayout(line1_quizz, stretch=1)
main_line_quizz.addWidget(quest_lb, alignment = Qt.AlignCenter)
main_line_quizz.addWidget(rbGroupbox, stretch=1)
main_line_quizz.addWidget(ansGroupbox, stretch=1)
main_line_quizz.addWidget(btn_ok, stretch=1)






