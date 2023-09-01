from Xlib import display

while True:
    data = display.Display().screen().root.query_pointer()._data
    print(data["root_x"], data["root_y"])

