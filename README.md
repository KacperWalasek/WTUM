# Digit Recognizer
Rozpoznawanie cyfr na bitmapach

## Compilation

Aby program dało się poprawnie skompilować i uruchomić potrzebujemy środowiska uruchomieniowego obsługującego język Python.

W naszym przypadku wykorzystywaliśmy najnowszą dostępną wersję (2021.1.1) IDE PyCharm Community oraz Python w wesji 3.8 i 3.9 dostępny na oficjalnej stronie www.python.org

Ponadto, aby uzyskać dostęp do używanych przez nas bibliotek konieczne jest zainstalowanie dodatkowych pakietów:

 - sklearn
 - scikit-learn
 - Pillow
 - mahotas
 - PySimpleGUI

## GUI explanation

Po skompilowaniu użytkownik powinien zobaczyć pustą planszę (280x280), na której może rysować, a także 3 przyciski:

 - Trenuj algorytmy
 - Testuj algorytmy
 - Rozpoznaj

Trenuj i testuj algorytmy robią dokładnie to, co sugeruje nazwa wykorzystując do tego odpowiednio podzielony zbiór danych.

Przycisk rozpoznaj ekstraktuje cechy narysowanego przez nas obrazka i próbuje zgadnąć co to za cyfra z wykorzystaniem wytenowanych wcześniej algorytmów (SVM i k-nearest neighbours).

Wytrenowany algorytm jest od razu zapisywany do pliku .pkl, dlatego nie ma potrzeby trenowania algorytmów po każdym uruchomieniu programu.
