import tkinter


from pogoda import get_locatrion_id, get_location_weather, weather_report

def pobierz_pogoda():
    location_name = pole.get()
    location_id = get_locatrion_id(location_name)
    weather = get_location_weather(location_id)
    report = weather_report(weather)
    wynik.configure(text=report)

root = tkinter.Tk()

label = tkinter.Label(master=root, text="Podaj miasto: ")
label.grid(row=1, column=1)

pole = tkinter.Entry(master=root)
pole.grid(row=1, column=2)

button = tkinter.Button(master=root, text="Pokaz pogode:", command=pobierz_pogoda)
button.grid(row=2, column=1)

wynik = tkinter.Label(master=root, text="")
wynik.grid(row=2, column=2)

root.mainloop()
