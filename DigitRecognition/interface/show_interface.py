from tkinter import *

from data_classes import Entity
from data_preparation.data_extraction import extract_data
from interface.show_picture import show_pictures


def init_pixels(pixels):
    for i in range(28):
        pixels[i] = [0] * 28


def show_interface(algorithmSvm, algorithmKN):
    pixels = [None] * 28
    init_pixels(pixels)

    canvas_width = 280
    canvas_height = 280

    def test_button_press():
        print(algorithmSvm.predict([extract_data(Entity('-1', pixels))]))
        master.destroy()
        show_pictures([[Entity('-1', pixels), '']])

    def button_press():
        result_svm['text'] = algorithmSvm.predict([extract_data(Entity('-1', pixels))])[0]
        result_kn['text'] = algorithmKN.predict([extract_data(Entity('-1', pixels))])[0]
        w.delete("all")
        init_pixels(pixels)

    def paint(event):
        black = "#000000"
        x, y = int(event.x/10), int(event.y/10)
        pixels[y][x] = 255
        x1, y1 = (event.x - 10), (event.y - 10)
        x2, y2 = (event.x + 10), (event.y + 10)
        w.create_oval(x1, y1, x2, y2, fill=black)

    master = Tk()
    master.title("Wpisz cyfre")
    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
    w.pack(expand=YES, fill=BOTH)
    w.bind("<B1-Motion>", paint)

    button = Button(master, text="Rozpoznaj", command=button_press)
    button.pack(side=BOTTOM)

    result_svm = Label(master)
    result_svm.pack(side=BOTTOM)

    label_svm = Label(master, text="Rozpoznana liczba przez SVM: ")
    label_svm.pack(side=BOTTOM)

    result_kn = Label(master)
    result_kn.pack(side=BOTTOM)

    label_kn = Label(master, text="Rozpoznana liczba przez k-nearest: ")
    label_kn.pack(side=BOTTOM)
    mainloop()