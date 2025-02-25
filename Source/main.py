
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from signup import open_signup_window


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TestTrust\Tkinter-Designer-master\Source\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1251x650")
window.configure(bg = "#F5F1EB")


canvas = Canvas(
    window,
    bg = "#F5F1EB",
    height = 650,
    width = 1251,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1251.0,
    84.0,
    fill="#D9D9D9",
    outline="black")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_signup_window(window),
    relief="flat"
)
button_1.place(
    x=942.0,
    y=32.0,
    width=92.0,
    height=32.0
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
    x=821.0,
    y=32.0,
    width=106.0,
    height=28.0
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
    x=700.0,
    y=34.0,
    width=106.0,
    height=28.0
)

canvas.create_text(
    94.0,
    130.0,
    anchor="nw",
    text="Welcome to the \nTestTrust Community ",
    fill="#EB5E28",
    font=("Anton Regular", 64 * -1)
)

canvas.create_text(
    98.0,
    335.0,
    anchor="nw",
    text="The place to get support, create assignments, correct answers ,Add students and assign exams.\n Monitor live exams in real-time, and contribute to the open source learning platform,TestTrust LMS.",
    fill="#A78C8C",
    font=("AnticDidone Regular", 14 * -1)
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
    x=270.0,
    y=517.0,
    width=254.0327911376953,
    height=39.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    999.0,
    382.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    89.0,
    41.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
