from tkinter import *
import Drawning



root = Tk() # Корневой объект - окно
root.title("Auto Epur maker")
root.geometry("1400x1200")

try:
    icon = PhotoImage(file = "2914917.png")
    root.iconphoto(False, icon)
except (TclError):
    pass

SCALE = IntVar(value=40)
points = []



# Scale
frame_optns = Frame(root)
frame_optns.pack(anchor="ne", padx=SCALE.get(), pady=SCALE.get()/5)
scale_label = Label(frame_optns, text="Scale of grid")
scale_label.pack(side="bottom")
grid_scale = Scale(frame_optns, orient=HORIZONTAL, length=300, from_=10.0, to=50.0, variable=SCALE, command=Drawning.resize_canvas)
grid_scale.pack()



# Clear and Enter buttons 
frame_btns = Frame(root)
frame_btns.pack(anchor="se", side="bottom", padx=SCALE.get(), pady=SCALE.get()/5)
Clear_btn  = Button(frame_btns, text="Clear", command=Drawning.clear_spots)
Clear_btn.pack(side="left")
Enter_btn = Button(frame_btns, text="Enter", command=Drawning.take_cords)
Enter_btn.pack(side="left")



# Z cords field
frame_z = Frame(root)
frame_z.pack(anchor="se", side="bottom", padx=SCALE.get(), pady=SCALE.get()/5)
z_label = Label(frame_z, text="Z = ")
z_label.pack(side="left")
cords_taker_z = Entry(frame_z)
cords_taker_z.pack(side="left")

# Y cords field
frame_y = Frame(root)
frame_y.pack(anchor="se", side="bottom", padx=SCALE.get(), pady=SCALE.get()/5)
y_label = Label(frame_y, text="Y = ")
y_label.pack(side="left")
cords_taker_y = Entry(frame_y)
cords_taker_y.pack(side="left")

# X cords field
frame_x = Frame(root)
frame_x.pack(anchor="se", side="bottom", padx=SCALE.get(), pady=SCALE.get()/5)
x_title = Label(frame_x, text="X = ")
x_title.pack(side="left")
cords_taker_x = Entry(frame_x)
cords_taker_x.pack(side="left")

# Spot name field
frame_spot_name = Frame(root)
frame_spot_name.pack(anchor="se", side="bottom", padx=SCALE.get(), pady=SCALE.get()/5)
spot_name_title = Label(frame_spot_name, text="Имя точки: ")
spot_name_title.pack(side="left")
spot_name_taker = Entry(frame_spot_name)
spot_name_taker.pack(side="left")



# Graph
canvas = Canvas(bg="white", width=22*SCALE.get(), height=22*SCALE.get()) # Канвас...
canvas.pack(anchor="sw")

canvas.create_line(SCALE.get()+10*SCALE.get(), SCALE.get(), SCALE.get()+10*SCALE.get(), SCALE.get()+20*SCALE.get(), width=3.5) # Основные линии координат
canvas.create_line(SCALE.get(), SCALE.get()+10*SCALE.get(), SCALE.get()+20*SCALE.get(), SCALE.get()+10*SCALE.get(), width=3.5)
canvas.create_line(SCALE.get(), SCALE.get(), SCALE.get()+20*SCALE.get(), SCALE.get()+20*SCALE.get()) # Диагональ

for c in range (22): # сетка 
    canvas.create_line(c*SCALE.get(), SCALE.get(), c*SCALE.get(), 21*SCALE.get())
for r in range (22):
    canvas.create_line(SCALE.get(), r*SCALE.get(), 21*SCALE.get(), r*SCALE.get())