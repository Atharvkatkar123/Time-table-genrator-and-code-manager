from pathlib import Path
from subprocess import run
from tkinter import Toplevel, Label, Button
import webbrowser
from tkinter import simpledialog


# from tkinter import *

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\katka\Documents\tkinter design\Tkinter-Designer-master\build1\assets\frame1")

def open_gui2():
    run(["python", str(Path(r"C:\Users\katka\Documents\tkinter design\Tkinter-Designer-master\build1\gui2.py"))])

def open_gui3():
    run(["python", str(Path(r"C:\Users\katka\Documents\tkinter design\Tkinter-Designer-master\build1\gui3.py"))])

def open_url():
    url = "https://coek.dypgroup.edu.in/academics/syllabus/"  # Replace with your desired URL
    webbrowser.open(url)

def open_gui4():
    run(["python", str(Path(r"C:\Users\katka\Documents\tkinter design\Tkinter-Designer-master\build1\Genetic Algo.py"))])

def check_password(entry_widget):
    # Replace 'your_password' with the actual password you want to use
    correct_password = "1234"
    
    entered_password = entry_widget.get()

    if entered_password == correct_password:
        open_gui2()
    else:
        print("Incorrect password")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("880x550")
window.configure(bg = "#2C4072")


window.pack_propagate(False)


canvas = Canvas(
    window,
    bg = "#2C4072",
    height = 550,
    width = 880,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.pack(fill="both", expand=True)


canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    255.00001003318835,
    337.1902781724493,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    72.0,
    880.0,
    96.0,
    fill="#FFFFFF",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    440.0,
    36.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=check_password,
    relief="flat"
)
button_1.place(
    x=8.0,
    y=110.0,
    width=211.63711547851562,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: check_password(entry_2),
    relief="flat"
)
button_2.place(
    x=90.0,
    y=428.0,
    width=304.0,
    height=56.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui4,
    relief="flat"
)
button_3.place(
    x=329.0,
    y=111.0,
    width=211.63711547851562,
    height=34.0
)

canvas.create_text(
    45.0,
    233.0,
    anchor="nw",
    text="Name",
    fill="#FFFFFF",
    font=("JuliusSansOne Regular", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    242.5,
    284.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font= 19
)
entry_1.place(
    x=45.0,
    y=268.0,
    width=395.0,
    height=31.0
)

canvas.create_text(
    45.0,
    315.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("JuliusSansOne Regular", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    242.5,
    364.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font= 19
)
entry_2.place(
    x=45.0,
    y=348.0,
    width=395.0,
    height=31.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    623.0,
    331.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    810.0,
    323.0,
    image=image_image_4
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_url,
    relief="flat"
)
button_4.place(
    x=660.0,
    y=111.0,
    width=211.63711547851562,
    height=34.0
)
window.resizable(True, True)
window.mainloop()
