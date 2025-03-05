
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TestTrust\Tkinter-Designer-master\Source\assets\frame6")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    22.0,
    0.0,
    1494.0,
    89.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    685.0,
    10.0,
    755.6033325195312,
    69.28482437133789,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=10.571428298950195,
    y=22.0,
    width=279.20635986328125,
    height=47.0
)

canvas.create_rectangle(
    1336.5333251953125,
    18.0,
    1395.8222160339355,
    69.0,
    fill="#000000",
    outline="")

canvas.create_text(
    486.0,
    107.0,
    anchor="nw",
    text="Hey Again ! Time For A New Exam",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 30 * -1)
)

canvas.create_text(
    343.0,
    505.0,
    anchor="nw",
    text="Exam Date\n",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 30 * -1)
)

canvas.create_text(
    367.0,
    341.0,
    anchor="nw",
    text="Subject",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 30 * -1)
)

canvas.create_text(
    308.0,
    423.0,
    anchor="nw",
    text="No. Of Students",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 30 * -1)
)

canvas.create_text(
    333.0,
    189.0,
    anchor="nw",
    text="Department",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 30 * -1)
)

canvas.create_text(
    350.0,
    587.0,
    anchor="nw",
    text="Duration",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 30 * -1)
)

canvas.create_text(
    379.0,
    669.0,
    anchor="nw",
    text="Mark",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 30 * -1)
)

canvas.create_text(
    261.0,
    751.0,
    anchor="nw",
    text="No. Of Exam Questions",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 30 * -1)
)

canvas.create_text(
    385.0,
    259.0,
    anchor="nw",
    text="Year",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 30 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    887.0,
    209.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=651.0,
    y=184.0,
    width=472.0,
    height=48.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    887.0,
    537.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=651.0,
    y=512.0,
    width=472.0,
    height=48.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    887.0,
    619.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=651.0,
    y=594.0,
    width=472.0,
    height=48.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    887.0,
    701.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=651.0,
    y=676.0,
    width=472.0,
    height=48.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    887.0,
    782.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=651.0,
    y=757.0,
    width=472.0,
    height=48.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    887.0,
    455.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=651.0,
    y=430.0,
    width=472.0,
    height=48.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    887.0,
    291.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=651.0,
    y=266.0,
    width=472.0,
    height=48.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    887.0,
    373.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=651.0,
    y=348.0,
    width=472.0,
    height=48.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=552.0,
    y=923.0,
    width=335.0,
    height=62.1171875
)

canvas.create_rectangle(
    1216.0,
    737.0,
    1440.0,
    1132.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    1144.0,
    89.0,
    1450.0,
    252.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    132.0,
    851.0,
    487.0,
    1040.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    137.0,
    88.0,
    492.0,
    277.0,
    fill="#FFFFFF",
    outline="")
window.resizable(False, False)
window.mainloop()
