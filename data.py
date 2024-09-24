from random import shuffle
questions = []
class Question():
    def __init__(self, text, true, false1, false2, false3):
        self.text = text
        self.true = true
        self.false1 = false1
        self.false2 = false2
        self.false3 = false3
        questions.append(self)

    def show_question(self, lb, rbuttons):
        lb.setText(self.text)   
        rbuttons[0].setText(self.true)
        rbuttons[1].setText(self.false1)
        rbuttons[2].setText(self.false2)
        rbuttons[3].setText(self.false3)
    
Question("В якому році почалась 1 світова війна?:", "1914", "1915", "1916", "1917")
Question("Хто придумав лампочку?:", "Томас Едіссон", "Майкл Джордан", "Я", "Альберт Енштейн")
Question("Хто перший ступив на місяць?:", "Ніл Армстронг", "Олдрин", "Фреді Меркурі", "Я")
Question("Коли вийшла перша яастина фільму Вартові галактики?:", "2014", "2021", "2004", "2018")



