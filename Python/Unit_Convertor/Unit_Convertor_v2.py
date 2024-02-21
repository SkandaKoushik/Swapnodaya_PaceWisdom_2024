import tkinter as tk
from tkinter import ttk


def convert(event):
    text_conv.delete(0, tk.END)
    
    type = combo_type.get()
    conv = combo_conv.get()
    
    try:
        value = int(text_value.get())
    except:
        value = 0
    
    
    if type == "Length":       
        if conv == "Centimeter to Meter":
            conv_val = value / 100
            text_conv.insert(0, conv_val)
        elif conv == "Meter to Centimeter": 
            conv_val = value * 100
            text_conv.insert(0, conv_val)
        elif conv == "Centimeter to INCH":
            conv_val = value / 2.54
            text_conv.insert(0, conv_val)
        elif conv == "INCH to Centimeter":
            conv_val = value * 2.54
            text_conv.insert(0, conv_val)
        elif conv == "Centimeter to KiloMetre": 
            conv_val = value / 100000
            text_conv.insert(0, conv_val)
        elif conv == "KiloMetre to Centimeter":
            conv_val = value * 100000
            text_conv.insert(0, conv_val)
        elif conv == "Centimeter to FOOT": 
            conv_val = value / 30.48
            text_conv.insert(0, conv_val)
        elif conv == "FOOT to Centimeter":
            conv_val = value * 30.48
            text_conv.insert(0, conv_val)
        elif conv == "Kilometre to Mile":
            conv_val = value /  1.609
            text_conv.insert(0, conv_val)
        elif conv == "Mile to Kilometre":
            conv_val = value *  1.609
            text_conv.insert(0, conv_val)            
        elif conv == "Feet to inches":
            conv_val = value * 12
            text_conv.insert(0, conv_val)
    
    
    elif type == "Mass":
        if conv == "Gram to Kilogram": 
            conv_val = value / 1000
            text_conv.insert(0, conv_val)
        elif conv == "Kilogram to Gram":
            conv_val = value * 1000
            text_conv.insert(0, conv_val)
        elif conv == "Kilogram to Tonne":
            conv_val = value / 1000
            text_conv.insert(0, conv_val)
        elif conv == "Tonne to Kilogram":
            conv_val = value * 1000
            text_conv.insert(0, conv_val)
        elif conv == "Milligram to Kilogram": 
            conv_val = value / 1000000
            text_conv.insert(0, conv_val)
        elif conv == "Kilogram to Milligram":
            conv_val = value * 1000000
            text_conv.insert(0, conv_val)
        elif conv == "Milligram to Gram":
            conv_val = value / 1000
            text_conv.insert(0, conv_val)
        elif conv == "Gram to Milligram":
            conv_val = value * 1000
            text_conv.insert(0, conv_val)
        elif conv == "kilogram to pound":
            conv_val = value * 2.20462
            text_conv.insert(0, conv_val)
        elif conv == "pound to Kilogram": 
            conv_val = value / 2.20462
            text_conv.insert(0, conv_val)
        elif conv == "Micrograms to gram":
            conv_val = value / 1e+6
            text_conv.insert(0, conv_val)
        elif conv == "Micrograms to Kg":
            conv_val = value / 1e+9
            text_conv.insert(0, conv_val)
    
      
    elif type == "Temperature":
        if conv == "Celsius to Fahrenheit":
            conv_val = (value * 9/5) + 32
            text_conv.insert(0, conv_val)
        elif conv == "Celsius to Kelvin":
            conv_val = value + 273.15
            text_conv.insert(0, conv_val)
        elif conv == "Fahrenheit to Celsius":
            conv_val = (value - 32) * 5/9
            text_conv.insert(0, conv_val)
        elif conv == "Fahrenheit to Kelvin":
            conv_val = (value - 32) * 5/9 + 273.15
            text_conv.insert(0, conv_val)
        elif conv == "Kelvin to Celsius":
            conv_val = value - 273.15
            text_conv.insert(0, conv_val)
        elif conv == "Kelvin to Fahrenheit":
            conv_val = (value - 273.15) * 95 + 32
            text_conv.insert(0, conv_val)
    
    
    elif type == "Time":
        if conv == "Second to Minute":
            conv_val = value / 60
            text_conv.insert(0, conv_val)
        elif conv == "Minute to Second":
            conv_val = value * 60
            text_conv.insert(0, conv_val)
        elif conv == "Second to Hour":
            conv_val = value / 3600
            text_conv.insert(0, conv_val)
        elif conv == "Minute to Hour":
            conv_val = value / 60
            text_conv.insert(0, conv_val)
        elif conv == "Hour to Minute":
            conv_val = value * 60
            text_conv.insert(0, conv_val)
        elif conv == "Day to Hour":
            conv_val = value * 24
            text_conv.insert(0, conv_val)
        elif conv == "Hour to Day":
            conv_val = value / 24
            text_conv.insert(0, conv_val)
    
        
    elif type == "Spead":
        if conv == "Mile/hour to Km/hour":
            conv_val = value * 1.609
            text_conv.insert(0, conv_val)
        elif conv == "Km/hour to Mile/hour":
            conv_val = value / 1.609
            text_conv.insert(0, conv_val)
        elif conv == "Mile/hour to Meter/Sec":
            conv_val = value / 2.237
            text_conv.insert(0, conv_val)
        elif conv == "Meter/Sec to Mile/hour":
            conv_val = value * 2.237
            text_conv.insert(0, conv_val)
        elif conv == "Km/hour to Meter/Sec":
            conv_val = value / 3.6
            text_conv.insert(0, conv_val)
        elif conv == "Meter/Sec to Km/hour":
            conv_val = value * 3.6
            text_conv.insert(0, conv_val)
    
            
    elif type == "Energy":
        if conv == "Joule to Kilojoule":
            conv_val = value / 1000
            text_conv.insert(0, conv_val)
        elif conv == "Kilojoule to Joule":
            conv_val = value * 1000
            text_conv.insert(0, conv_val)
        elif conv == "Joule to Kilocalorie":
            conv_val = value / 4184
            text_conv.insert(0, conv_val)
        elif conv == "Kilocalorie to Joule":
            conv_val = value * 4184
            text_conv.insert(0, conv_val)
        elif conv == "Kilojoule to Kilocalorie":
            conv_val = value / 4.184
            text_conv.insert(0, conv_val)
        elif conv == "Kilocalorie to Kilojoule":
            conv_val = value * 4.184
            text_conv.insert(0, conv_val)
    
            
    elif type == "Pressure":
        if conv == "Bar to Pascal":
            conv_val = value * 100000
            text_conv.insert(0, conv_val)
        elif conv == "Bar to Std atmosphere":
            conv_val = value / 1.013
            text_conv.insert(0, conv_val)
        elif conv == "Pascal to Bar":
            conv_val = value / 1.013
            text_conv.insert(0, conv_val)
        elif conv == "Pascal to Std atmosphere":
            conv_val = value / 101300
            text_conv.insert(0, conv_val)
        elif conv == "Std atmosphere to Pascal":
            conv_val = value * 101300
            text_conv.insert(0, conv_val)
        elif conv == "Std atmosphere to Bar":
            conv_val = value * 1.013
            text_conv.insert(0, conv_val)


    elif type == "Area":
        if conv == "Sqft to Sqmtrs":
            conv_val = value / 10.764
            text_conv.insert(0, conv_val)
        elif conv == "Sqmtrs to Sqft":
            conv_val = value * 10.764
            text_conv.insert(0, conv_val)
        elif conv == "Sqft to Hectre":
            conv_val = value / 107600
            text_conv.insert(0, conv_val)
        elif conv == "Hectre to Sqft":
            conv_val = value * 107600
            text_conv.insert(0, conv_val)
        elif conv == "Sqft to Acres":
            conv_val = value / 43560
            text_conv.insert(0, conv_val)
        elif conv == "Acres to Sqft":
            conv_val = value * 43560
            text_conv.insert(0, conv_val)
            

    
#============== Window ================

root = tk.Tk()
root.title('Unit Convertion')

window_width = 500
window_height = 250
root.geometry(f"{window_width}x{window_height}")


frame = ttk.Frame(root, padding='20')
frame.grid(row=0, column=0)


label_type = tk.Label(
    frame, 
    text = 'Unit Type: ', 
    padx=10, 
    pady=10,
    font=(12)
)
label_type.grid(row=0, column=0, columnspan=2)


label_conv = tk.Label(
    frame, 
    text = 'Convertion: ', 
    padx=10, 
    pady=10,
    font=(12)
)
label_conv.grid(row=1, column=0, columnspan=2)


label_to = tk.Label(
    frame, 
    text = 'TO', 
    padx=10, 
    pady=2,
    font=6
)
label_to.grid(row=3, column=1)

list_type = [
    "Length",
    "Mass",
    "Temperature",
    "Time",
    "Spead",
    "Energy",
    "Pressure",
    "Area"
]

combo_type = ttk.Combobox(
    frame, 
    values=list_type, 
    width=30
)
combo_type.grid(row=0, column=2)
combo_type.set('Length')


list_conv = {
    "Length": ["Centimeter to Meter", "Meter to Centimeter", "Centimeter to INCH", "INCH to Centimeter",
            "Centimeter to KiloMetre", "KiloMetre to Centimeter", "Centimeter to FOOT", "FOOT to Centimeter",
            "Kilometre to Mile", "Mile to Kilometre", "Feet to inches"],
    
    "Mass": ["Gram to Kilogram", "Kilogram to Gram", "Kilogram to Tonne", "Tonne to Kilogram",
            "Milligram to Kilogram", "Kilogram to Milligram", "Milligram to Gram", "Gram to Milligram", 
            "kilogram to pound", "pound to Kilogram", "Micrograms to gram", "Micrograms to Kg" ],
    
    "Temperature": ["Celsius to Fahrenheit", "Celsius to Kelvin", "Fahrenheit to Celsius",
                    "Fahrenheit to Kelvin", "Kelvin to Celsius", "Kelvin to Fahrenheit"],
    
    "Time": ["Second to Minute", "Minute to Second", "Second to Hour", 
             "Minute to Hour", "Hour to Minute", "Day to Hour", "Hour to Day"],
    
    "Spead": ["Mile/hour to Km/hour", "Km/hour to Mile/hour", "Mile/hour to Meter/Sec", 
              "Meter/Sec to Mile/hour", "Km/hour to Meter/Sec", "Meter/Sec to Km/hour"],
    
    "Energy": ["Joule to Kilojoule", "Kilojoule to Joule", "Joule to Kilocalorie", "Kilocalorie to Joule",
               "Kilojoule to Kilocalorie", "Kilocalorie to Kilojoule"],
    
    "Pressure": ["Bar to Pascal", "Bar to Std atmosphere", "Pascal to Bar", "Pascal to Std atmosphere",
                "Std atmosphere to Pascal", "Std atmosphere to Bar"],
    
    "Area": ["Sqft to Sqmtrs", "Sqmtrs to Sqft", "Sqft to Hectre", "Hectre to Sqft", 
             "Sqft to Acres", "Acres to Sqft"]
}


label_value = tk.Label(
    frame, 
    text = list_conv.get("Length")[0],
    padx=0,
    pady=20,
    font=(12)
)
label_value.grid(row=2, columnspan=3, column=0)


combo_conv = ttk.Combobox(
    frame,
    width=30,
    values=list_conv.get("Length")
)
combo_conv.grid(row=1, column=2)
combo_conv.set(list_conv.get("Length")[0])


def update_conv(event):
    type = combo_type.get()
    combo_conv['values'] = list_conv.get(type)
    combo_conv.set(list_conv.get(type)[0])
    conv = combo_conv.get()
    label_value.config(text=conv)
        
combo_type.bind("<<ComboboxSelected>>", update_conv)


def update_value(event):
    conv = combo_conv.get()
    label_value.config(text=conv)

combo_conv.bind("<<ComboboxSelected>>", update_value)

text_value = ttk.Entry(frame, width=20, font=12)
text_value.grid(row=3, column=0, padx=10, pady=10)
text_value.insert(0, '0')

text_conv = ttk.Entry(frame, width=20, font=12)
text_conv.grid(row=3, column=2, padx=10, pady=10)
text_conv.insert(0, '0')

text_value.bind("<KeyRelease>", convert)

root.mainloop()

