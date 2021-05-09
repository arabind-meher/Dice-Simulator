from os import listdir
from os.path import join

import time
import random
import tkinter as tk
from PIL import Image, ImageTk


class Dice:
    def __init__(self):
        self.dice = list(join('images/dice/112x112', image) for image in listdir('images/dice/112x112'))

        self.dices = {
            'images/dice/112x112/1.png': 1,
            'images/dice/112x112/2.png': 2,
            'images/dice/112x112/3.png': 3,
            'images/dice/112x112/4.png': 4,
            'images/dice/112x112/5.png': 5,
            'images/dice/112x112/6.png': 6
        }

        self.graphics()

    def graphics(self):
        window = tk.Tk()

        window.title('Dice Roll Simulator')
        window.geometry('400x300')
        window.resizable(0, 0)

        heading = tk.Label(
            window,
            text='Dice Roll Simulator',
            font=('hack', 15, 'bold')
        )

        cube_image = ImageTk.PhotoImage(Image.open('images/cube/112x112/cubes.png'))

        dice_image_label = tk.Label(
            window,
            image=cube_image
        )

        dice_number_label = tk.Label(
            window,
            text='Roll The Dice',
            font=('hack', 12, 'bold')
        )

        def roll_button_clicked():
            time.sleep(0.5)

            new_dice_face = random.choice(self.dice)
            new_dice_image = ImageTk.PhotoImage(Image.open(new_dice_face))
            new_dice_number = self.dices[new_dice_face]

            dice_image_label.configure(image=new_dice_image)
            dice_image_label.image = new_dice_image

            dice_number_label.configure(text='Dice : ' + str(new_dice_number))
            dice_number_label.text = 'Dice : ' + str(new_dice_number)

            time.sleep(0.2)

        roll_button = tk.Button(
            window,
            text='Roll Dice',
            fg='#111111',
            bg='#cccccc',
            font=('hack', 10, 'bold'),
            command=roll_button_clicked
        )

        heading.pack(fill=tk.X, pady=5)
        dice_image_label.pack(pady=(35, 10))
        dice_number_label.pack(fill=tk.X)
        roll_button.pack(pady=(35, 0))

        window.mainloop()


if __name__ == "__main__":
    Dice()
