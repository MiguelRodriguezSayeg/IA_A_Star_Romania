from tkinter import ttk,Label, Tk
from dictionary import load_cities
from agent import solve
from PIL import Image, ImageDraw, ImageTk
from coords import get_city_coords


cities=load_cities()

def on_select(event=None):
	route_cities=[str(x) for x in solve(combo_cities.get(), cities)]
	route_coords=[get_city_coords(el) for el in route_cities]
	im = Image.open("Map.png")
	d = ImageDraw.Draw(im)
	line_color = (0, 0, 255)
	d.line(route_coords, fill=line_color, width=6)
	img = ImageTk.PhotoImage(im)
	panel.configure(image=img)
	panel.image(img)


tkinter_root = Tk()
tkinter_root.geometry("%dx%d+0+0" % tkinter_root.maxsize())

presentation_label = Label(tkinter_root, text="How to get to Bucharest?")
presentation_label.config(width=180)
presentation_label.config(font=("Courier", 40,"bold"))
presentation_label.pack()


choose_origin = Label(tkinter_root, text="Where are you located?")
choose_origin.pack(anchor="w")

combo_cities = ttk.Combobox(state="readonly")
combo_cities.bind("<<ComboboxSelected>>", on_select)
combo_cities["values"]=[key for key in cities.keys() if key != 'Bucharest' ]
combo_cities.pack(anchor="w")


image = Image.open("Map.png")
img = ImageTk.PhotoImage(image)
panel = Label(tkinter_root, image = img)
panel = Label(tkinter_root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
#image = PhotoImage(file="Map.png")
#Label(tkinter_root, image=image).pack()


tkinter_root.mainloop()