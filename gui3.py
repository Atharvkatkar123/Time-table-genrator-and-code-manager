from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import pandas as pd
from data import *
from subprocess import run
import webbrowser


# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\katka\Documents\tkinter design\Tkinter-Designer-master\build1\assets\frame3")

def open_gui2():
    run(["python", str(Path(r"C:\Users\katka\Documents\tkinter design\Tkinter-Designer-master\build1\gui2.py"))])

def open_url():
    url = "https://coek.dypgroup.edu.in/academics/syllabus/"  # Replace with your desired URL
    webbrowser.open(url)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("880x550")
window.configure(bg = "#2C4072")


canvas = Canvas(
    window,
    bg = "#2C4072",
    height = 550,
    width = 880,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    146.0,
    225.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    146.0,
    402.0,
    image=image_image_2
)


image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    439.0,
    225.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    439.0,
    402.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    734.0,
    225.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    734.0,
    402.0,
    image=image_image_6
)

canvas.create_text(
    19.0,
    199.0,
    anchor="nw",
    text="TOTAL HOURS",
    fill="#000000",
    font=("JuliusSansOne Regular", 11 * -1)
)

canvas.create_text(
    115.0,
    208.0,
    anchor="nw",
    text="23",
    fill="#000000",
    font=("Armata Regular", 36 * -1)
)

canvas.create_text(
    410.0,
    208.0,
    anchor="nw",
    text="3.6 ",
    fill="#000000",
    font=("Armata Regular", 36 * -1)
)

canvas.create_text(
    712.0,
    212.0,
    anchor="nw",
    text="7 ",
    fill="#000000",
    font=("Armata Regular", 36 * -1)
)

canvas.create_text(
    300.0,
    199.0,
    anchor="nw",
    text="SUBJECT HOURS",
    fill="#000000",
    font=("JuliusSansOne Regular", 11 * -1)
)

canvas.create_text(
    611.0,
    199.0,
    anchor="nw",
    text="FREE SLOTS ",
    fill="#000000",
    font=("JuliusSansOne Regular", 11 * -1)
)

canvas.create_rectangle(
    0.0,
    72.0,
    880.0,
    96.0,
    fill="#FFFFFF",
    outline="")

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    440.0,
    36.0,
    image=image_image_7
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui2,
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
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=329.0,
    y=111.0,
    width=211.63711547851562,
    height=34.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_url,
    relief="flat"
)
button_3.place(
    x=660.0,
    y=111.0,
    width=211.63711547851562,
    height=34.0
)

date = [ "2022-08-19",
        "2022-08-20",
        "2022-08-23",
        "2022-08-24",
        "2022-08-25",
        "2022-08-26",
        "2022-08-27"]

amount = [ 105.73,
        89.15,
        107.04,
        50.23,
        85.52,
        104.61,
        25.7
]

fig_1 = Figure(figsize=(2.5, 2.5), facecolor="#A2B7FF")
ax_1 = fig_1.add_subplot()
ax_1.set_facecolor("#A2B7FF")
ax_1.fill_between(x=date, y1=amount, alpha=0.7, color = "#FF7147")
ax_1.tick_params(labelsize=6, colors="Black")
fig_1.autofmt_xdate()
ax_1.plot(date, amount, color="#2C4072")
ax_1.grid(visible=True)
fig_1.suptitle("HOURS IN WEEK")

canvas = FigureCanvasTkAgg(figure=fig_1, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=20, y=280)


# Subplot for the pie chart
colors = ["#A2B7FF","#2C4072","#FF7147","#E2A08C"]

fig_2 = Figure(figsize=(2.5, 2.5), facecolor="#FFFFFF")
ax_2 = fig_2.add_subplot()  # 2 rows, 1 column, subplot 2
labels = ['TMA', 'TSF', 'DL', 'MOOC']  # Example labels for the pie chart
sizes = [15, 30, 45, 10]  # Example sizes for the pie chart
ax_2.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=270, colors= colors)
ax_2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
ax_2.set_title("SUBJECT HOURS")

canvas = FigureCanvasTkAgg(figure=fig_2, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=315, y=279)

#Bar chart
days = ["MON","TUE","WED","THU","FRT"]
Free_slots = [1,0,1,2,3]

fig_3 = Figure(figsize=(2.5, 2.5), facecolor="#E2A08C")
ax_3 = fig_3.add_subplot()
ax_3.set_facecolor("#E2A08C")
ax_3.tick_params(labelsize=6, colors="Black")
fig_3.autofmt_xdate()
ax_3.bar(days, Free_slots, color="#2C4072")
fig_3.suptitle("FREE SLOTS")

canvas = FigureCanvasTkAgg(figure=fig_3, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=608, y=280)


window.resizable(False, False)
window.mainloop()
