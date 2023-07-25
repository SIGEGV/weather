from tkinter import *
from tkinter import ttk
import requests


def get_data():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=c24bcde400d3edcbdc514e2fa8001cb0").json()
    temperature1.config(text=str(round(data['main']['temp'] - 273.5, 2)))
    wth1.config(text=data['weather'][0]['description'])


root = Tk()
root.geometry("500x500")
root.title("weather_fetcher")
# root.config(bg="light blue")
label = Label(root, text="Weather APP", font=('Arial', 18, "bold"))
label.pack(padx=20, pady=20)
city_name = StringVar()

list = ["Andhra Pradesh", "Arunachal Pradesh",
         "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
         "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka",
         "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
         "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
         "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
         "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
         "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu",
         "Lakshadweep", "National Capital Territory of Delhi",
         "Puducherry"]

com = ttk.Combobox(root, values=list, font=('Arial', 18), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

# weather
wth = Label(root, text="Weather Climate", font=('Arial', 18, "bold"))
wth.place(x=25, y=260, height=50, width=210)
# weather -> value
wth1=Label(root,text="",font=('Arial',18,"bold"))
wth1.place(x=250,y=260,height=50,width=210)

temperature = Label(root, text="Temperature", font=('Arial', 18, "bold"))
temperature.place(x=20, y=310, height=50, width=210)
# temperature -> value

temperature1 = Label(root, text="", font=('Arial', 18, "bold"))
temperature1.place(x=250, y=310, height=50, width=210)

# button


button = Button(root, text="Search", font=('Arial', 18), command=get_data)
button.place(x=200, y=190, height=50, width=100)
root.mainloop()
