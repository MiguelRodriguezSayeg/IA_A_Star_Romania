from tkinter import ttk,Label, Tk, Frame
from PIL import Image, ImageDraw, ImageTk

class MainApplication(object):
	def __init__(self, tkinter_root, agent,*args, **kwargs):
		self.agent=agent
		#Root
		self.tkinter_root = tkinter_root
		tkinter_root.geometry("%dx%d+0+0" % self.tkinter_root.maxsize())
		self.frame = Frame(self.tkinter_root)
		#Presentation label
		self.presentation_label = Label(self.tkinter_root, text="How to get to Bucharest?")
		self.presentation_label.config(width=180)
		self.presentation_label.config(font=("Courier", 40,"bold"))
		self.presentation_label.pack()
		#Choose origin
		self.choose_origin = Label(self.tkinter_root, text="Where are you located?")
		self.choose_origin.pack(anchor="w")
		#Combobox
		self.combo_cities = ttk.Combobox(state="readonly")
		self.combo_cities.bind("<<ComboboxSelected>>", self.on_select)
		self.combo_cities["values"]=[key for key in self.agent.map.get_cities().keys() if key != 'Bucharest' ]
		self.combo_cities.pack(anchor="w")
		#Image panel
		self.image = Image.open("Map.png")
		self.img = ImageTk.PhotoImage(self.image)
		self.panel = Label(self.tkinter_root)
		self.panel.configure(image=self.img)
		self.panel.pack(side = "bottom", fill = "both", expand = "yes")

	def on_select(self,event=None):
		route_cities=[str(x) for x in self.agent.solve(self.combo_cities.get(), self.agent.map.get_cities())]
		route_coords=[self.agent.map.get_city_coords(el) for el in route_cities]
		im = Image.open("Map.png")
		d = ImageDraw.Draw(im)
		line_color = (0, 0, 255)
		d.line(route_coords, fill=line_color, width=6)
		img = ImageTk.PhotoImage(im)
		self.panel.configure(image=img)
		self.panel.image(img)



