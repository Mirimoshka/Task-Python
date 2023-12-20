
from math import sqrt

def triangle(quad, word_instance): #Сжатие пирамиды из 4-х элементов 
    if quad.count(quad[0]) == 4:
        word_instance.NewWord += quad[0]
    else:                          #Если его не происходит, то процесс сжатия строки полностью останавливается
        word_instance.Stand = "Stop"

def level(Piece, NumTriangle, word_instance): #Выделение пирамид на каждых уровнях 
    for i in range(1, NumTriangle + 1):       #Цикл по количеству пирамид на уровне
        center = 2 * i - 2                    #Индекс, который содержит основу всех элементов пирамиды
        if i % 2 == 1:
            triangle(Piece[center] + Piece[center + 2 * NumTriangle - 1] + Piece[center + 2 * NumTriangle] +
                     Piece[center + 2 * NumTriangle + 1], word_instance)  #Выделение 4 элемента пирамиды, с вершиной вверх
        else:
            triangle(Piece[center - 1] + Piece[center + 1] + Piece[center] + Piece[center + 2 * NumTriangle],
                     word_instance)                                       #С вершиной вниз
        if word_instance.Stand == "Stop":
            break

def compression(word_instance): 
    BorderLevel = [0] #Массив для сохранения граничных значений уровня в общей пирамиде
    NumTriangle = 1   #Количество 4-х элементых пирамид на уровне
    for i in range(int(sqrt(len(word_instance.FullWord)) / 2)): #Цикл по числу уровней в пирамиде
        BorderLevel.append(i * 8 + 4 + BorderLevel[i])          
        level(word_instance.FullWord[BorderLevel[i]:BorderLevel[i + 1]], NumTriangle, word_instance) 
        NumTriangle += 2 
        if word_instance.Stand == "Stop":
            break

    if word_instance.Stand != "Stop" and len(word_instance.NewWord) >= 4:
        word_instance = Word(word_instance.NewWord)
        return compression(word_instance)
    else:
        return word_instance.FullWord

def opentxt():      #Открытие и чтение с файла, инициирование сжатия строки, запись и закрытие файла
  FileOpen= open('text.txt', "r")
  FirstWord = FileOpen.read()[::-1]
  FileOpen.close

  word_instance = Word(FirstWord)
  LastWord = compression(word_instance)[::-1]

  FileOpen= open('text.txt', "w")
  FileOpen.write(LastWord)
  FileOpen.close

class Word:                   #Класс для контроля строки
    def __init__(self, word):
        self.FullWord = word
        self.NewWord = ""
        self.Stand = "Normal"

opentxt()