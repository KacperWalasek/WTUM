import io
from tkinter import *

from algorithms.knearest_algorithm import KNearestAlgorithm
from algorithms.svm_algorithm import SVMAlgorithm
from data_classes import Entity
from data_preparation.data_extraction import extract_data
from flow.prepare_sets import prepare_sets
from flow.train_algorithm import train_algorithm
from flow.validate import validate
from interface.show_picture import show_pictures
from PIL import Image, ImageDraw #needs 'Pillow' to work
import joblib


def init_pixels(pixels):
    for i in range(28):
        pixels[i] = [0] * 28


def show_interface():
    pixels = [None] * 28
    init_pixels(pixels)

    canvas_width = 280
    canvas_height = 280
    image1 = Image.new("RGB", (canvas_width, canvas_height), "#FFFFFF")
    draw = ImageDraw.Draw(image1)

    def button_press():
        algorithm1 = joblib.load('trained-svm.pkl')
        algorithm2 = joblib.load('trained-k-nearest.pkl')
        for i in range(0, 28):
            for j in range(0, 28):
                pixels[j][i] = 255 - image1.getpixel((5+i*10, 5+j*10))[0]
        #image1.show()
        #show_pictures([[Entity('1', pixels), '1']])
        resultSVM['text'] = algorithm1.predict([extract_data(Entity('-1', pixels))])
        resultKN['text'] = algorithm2.predict([extract_data(Entity('-1', pixels))])

        w.delete("all")
        init_pixels(pixels)
        draw.rectangle([(0, 0), (280, 280)], fill="#FFFFFF")

    def paint(event):
        black = "#000000"
        x, y = int(event.x/10), int(event.y/10)
        if x > 27 or y > 27 or x < 0 or y < 0:
            return
        pixels[y][x] = 255
        r = 10
        x1, y1 = (event.x - r), (event.y - r)
        x2, y2 = (event.x + r), (event.y + r)
        w.create_oval(x1, y1, x2, y2, fill=black)
        draw.ellipse([(x1, y1), (x2, y2)], fill=black)

    def train_alg_button_press():
        algSVM = SVMAlgorithm()
        algKN = KNearestAlgorithm()
        print('preparing data...')
        training_set, validation_set = prepare_sets()
        print('training SVM algorithm...')
        train_algorithm(algSVM, training_set)
        print('saving SVM algorithm')
        joblib.dump(algSVM, 'trained-svm.pkl', compress=3)
        print('training k-nearest algorithm...')
        train_algorithm(algKN, training_set)
        print('saving k-nearest algorithm')
        joblib.dump(algKN, 'trained-k-nearest.pkl', compress=3)
        print('done')

    def test_alg_button_press():
        print('preparing data...')
        training_set, validation_set = prepare_sets()
        algSVM = joblib.load('trained-svm.pkl')
        algKN = joblib.load('trained-k-nearest.pkl')
        print('testing svm algorithm...')
        print('result: ', validate(algSVM, validation_set)*100, '%')
        print('testing k-nearest algorithm...')
        print('result: ', validate(algKN, validation_set)*100, '%')

    master = Tk()
    master.title("Wpisz cyfre")

    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
    w.pack(expand=YES, fill=BOTH)
    w.bind("<B1-Motion>", paint)

    button = Button(master, text="Rozpoznaj", command=button_press)
    button.pack(side=BOTTOM)

    button2 = Button(master, text="Trenuj algorytmy", command=train_alg_button_press)
    button2.pack(side=BOTTOM)

    button3 = Button(master, text="Testuj algorytmy", command=test_alg_button_press)
    button3.pack(side=BOTTOM)

    resultKN = Label(master, text="")
    resultKN.pack(side=BOTTOM)

    label1 = Label(master, text="Rozpoznana liczba przez K-nearest: ")
    label1.pack(side=BOTTOM)

    resultSVM = Label(master, text="")
    resultSVM.pack(side=BOTTOM)

    label2 = Label(master, text="Rozpoznana liczba przez SVM: ")
    label2.pack(side=BOTTOM)

    mainloop()