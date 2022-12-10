import tkinter as tk
import random
import math

# Vytvoření okna pro všechny úlohy
window = tk.Canvas(tk.Tk(), width=1920, height=1080)


def a():
    """
    Pomocí cyklu nakreslete 20 soustředných kružnic
    """
    offset = 0
    x_1 = 1920 // 2 - 200
    y_1 = 1080 // 2 - 200
    x_2 = 1920 // 2 + 200
    y_2 = 1080 // 2 + 200

    for i in range(20):
        # x_1 a y_1 se zvětšují
        # x_2 a y_2 se zmenšují (krajní body jdou blíž k sobě)
        window.create_oval(x_1 + offset, y_1 + offset, x_2 - offset, y_2 - offset)
        offset += 10

    window.pack()
    window.mainloop()


def b():
    """
    Pomocí obdélníků nakreslete tabulku se třemi sloupci a 20 řádky
    """
    # Doporučuji si nakraslit obrázek s jednotlivými body, které s mění (u sloupců souřadnice x, u řádků souřadnice y)
    # Vytvoření sloupců
    offset = 0
    x_1 = 1920 // 2 - 150
    y_1 = 1080 // 2 - 300
    x_2 = 1920 // 2 - 50
    y_2 = 1080 // 2 + 300

    for i in range(3):
        window.create_rectangle(x_1 + offset, y_1, x_2 + offset, y_2)
        offset += 100

    # Vytvoření řádků
    offset = 0
    x_1 = 1920 // 2 - 150
    y_1 = 1080 // 2 - 300
    x_2 = 1920 // 2 + 150
    y_2 = 1080 // 2 - 270

    for i in range(20):
        window.create_rectangle(x_1, y_1 + offset, x_2, y_2 + offset)
        offset += 30

    window.pack()
    window.mainloop()


def c():
    """
    Nakreslete Sluníčko (mnoho paprsků vycházejících z jednoho bodu všemi směry pomocí cyklu a pak je překryje kolečko.)
    """
    # Vytvoření paprsků
    radius = 200
    num_of_rays = 60
    offset = math.radians(360 / num_of_rays)  # Konstantní úhle, který odděluje dva vedlejší paprky
    phi = 0  # Úhel, o který se otočí každý paprsek
    x_1 = 1920 // 2
    y_1 = 1080 // 2

    for i in range(num_of_rays):
        x_2 = 1920 // 2 + (math.cos(phi) * radius)
        y_2 = 1080 // 2 + (math.sin(phi) * radius)
        window.create_line(x_1, y_1, x_2, y_2)
        phi += offset

    # Vytvoření kolečka
    x_1 = 1920 // 2 - 100
    y_1 = 1080 // 2 - 100
    x_2 = 1920 // 2 + 100
    y_2 = 1080 // 2 + 100
    window.create_oval(x_1, y_1, x_2, y_2, fill="yellow")

    window.pack()
    window.mainloop()


def e():
    """
    Nakreslete menší čtverečky, které vytvoří pravidelný vzor (tabulku), každý čtvereček
    bude mít náhodně jinou barvu výplně.
    """
    offset_1 = 0
    offset_2 = 50
    x_1 = 1920 // 2 - 150
    y_1 = 1080 // 2 - 150
    x_2 = 1920 // 2 - 150 + 50
    y_2 = 1080 // 2 - 150 + 50
    colors = ["red", "green", "yellow", "blue", "orange", "black"]

    for j in range(6):
        for i in range(6):
            window.create_rectangle(x_1 + offset_1, y_1, x_2 + offset_1, y_2, fill=random.choice(colors))
            offset_1 += 50

        offset_1 = 0
        x_1 = 1920 // 2 - 150
        y_1 = 1080 // 2 - 150 + offset_2
        x_2 = 1920 // 2 - 150 + 50
        y_2 = 1080 // 2 - 150 + 50 + offset_2
        offset_2 += 50

    window.pack()
    window.mainloop()
