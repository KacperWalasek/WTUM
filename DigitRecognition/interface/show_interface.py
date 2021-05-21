from tkinter import *

from data_classes import Entity
from data_preparation.data_extraction import extract_data
from interface.show_picture import show_pictures


def init_pixels(pixels):
    for i in range(28):
        pixels[i] = [0] * 28


def show_interface(algorithm):
    pixels = [None] * 28
    init_pixels(pixels)

    canvas_width = 280
    canvas_height = 280

    def test_button_press():
        print(algorithm.predict([extract_data(Entity('-1', pixels))]))
        master.destroy()
        show_pictures([[Entity('-1', pixels), '']])

    def button_press():
        result['text'] = algorithm.predict([extract_data(Entity('-1', pixels))])
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

    label = Label(master, text="Rozpoznana liczba: ")
    label.pack(side=BOTTOM)

    result = Label(master)
    result.pack(side=BOTTOM)

    mainloop()