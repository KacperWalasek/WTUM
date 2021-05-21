from tkinter import *

from data_classes import Entity
from data_preparation.data_extraction import extract_data
from flow.prepare_sets import prepare_sets
from flow.train_algorithm import train_algorithm
from flow.validate import validate
from interface.show_picture import show_pictures
import joblib


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
        algorithm2 = joblib.load('trained-' + algorithm.name() + '.pkl')
        result['text'] = algorithm2.predict([extract_data(Entity('-1', pixels))])
        #result['text'] = algorithm.predict([extract_data(Entity('-1', pixels))])

        w.delete("all")
        init_pixels(pixels)

    def paint(event):
        black = "#000000"
        x, y = int(event.x/10), int(event.y/10)
        if x > 27 or y > 27 or x < 0 or y < 0:
            return
        pixels[y][x] = 255
        x1, y1 = (event.x - 10), (event.y - 10)
        x2, y2 = (event.x + 10), (event.y + 10)
        w.create_oval(x1, y1, x2, y2, fill=black)

    def train_alg_button_press():
        print('preparing data...')
        training_set, testing_set, validation_set = prepare_sets()
        print('training ' + algorithm.name() + ' algorithm...')
        train_algorithm(algorithm, training_set)
        print('saving algorithm')
        joblib.dump(algorithm, 'trained-' + algorithm.name() + '.pkl', compress=3)
        print('done')

    def test_alg_button_press():
        print('preparing data...')
        training_set, testing_set, validation_set = prepare_sets()
        algorithm2 = joblib.load('trained-' + algorithm.name() + '.pkl')
        print('testing ' + algorithm.name() + ' algorithm...')
        print('result: ', validate(algorithm2, validation_set)*100, '%')

    master = Tk()
    master.title("Wpisz cyfre")
    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
    w.pack(expand=YES, fill=BOTH)
    w.bind("<B1-Motion>", paint)

    button = Button(master, text="Rozpoznaj", command=button_press)
    button.pack(side=BOTTOM)

    button2 = Button(master, text="Trenuj algorytm " + algorithm.name(), command=train_alg_button_press)
    button2.pack(side=BOTTOM)

    button3 = Button(master, text="Testuj algorytm " + algorithm.name(), command=test_alg_button_press)
    button3.pack(side=BOTTOM)

    label = Label(master, text="Rozpoznana liczba: ")
    label.pack(side=BOTTOM)
    mainloop()