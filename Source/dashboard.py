
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TestTrust\Tkinter-Designer-master\Source\assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1270x650")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 650,
    width = 1270,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    650.0,
    fill="#F5F1EB",
    outline="")

canvas.create_rectangle(
    0.0,
    74.0,
    219.25189208984375,
    660.0,
    fill="#D9D9D9",
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
    x=13.0,
    y=270.0,
    width=191.0,
    height=30.17543601989746
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
    x=10.0,
    y=175.0,
    width=175.0,
    height=29.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=16.0,
    y=225.0,
    width=167.0,
    height=24.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=3.0,
    y=321.0,
    width=216.0,
    height=27.28788185119629
)

canvas.create_text(
    55.0,
    92.0,
    anchor="nw",
    text="Dashboard",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 20 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    1288.0,
    89.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    844.0,
    25.0,
    anchor="nw",
    text="welcome back shahd!",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 30 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    609.0,
    45.0,
    image=image_image_1
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=10.0,
    y=20.0,
    width=226.0,
    height=49.0
)

canvas.create_rectangle(
    219.0,
    89.0,
    1270.0,
    136.0,
    fill="#000000",
    outline="")

canvas.create_text(
    257.9615478515625,
    92.0,
    anchor="nw",
    text="Exam status",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 24 * -1)
)

canvas.create_rectangle(
    219.0,
    362.0,
    1270.0,
    412.0,
    fill="#000000",
    outline="")

canvas.create_text(
    257.0750427246094,
    368.0,
    anchor="nw",
    text="Upcoming Exams",
    fill="#EB5E28",
    font=("AbrilFatface Regular", 24 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    103.0,
    538.0,
    image=image_image_2
)

canvas.create_text(
    217.0,
    154.0,
    anchor="nw",
    text="                    IT          4TH          1:30:00          CCNAIV          30/30            A201                                                                                            ",
    fill="#000000",
    font=("AbrilFatface Regular", 20 * -1)
)

canvas.create_text(
    216.0,
    431.0,
    anchor="nw",
    text="                    IT          4TH          1:30:00          IOT Security           A201           25/3/2025                                                                                 ",
    fill="#000000",
    font=("AbrilFatface Regular", 20 * -1)
)

canvas.create_rectangle(
    235.99999737731832,
    139.99999934306288,
    1211.0,
    200.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    234.99999737731832,
    415.9999993430629,
    1210.0,
    476.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1233.0,
    136.0,
    1262.0,
    361.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1233.0,
    416.0,
    1262.0,
    641.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
