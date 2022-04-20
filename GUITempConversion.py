import tkinter as tk

class TempConv:
    def __init__(self): # All GUI elements can be found in the constructor
        self.root = tk.Tk()
        self.root.geometry("809x500")
        self.root.resizable(0,0)
        self.root.title("Temperature conversion GUI - LEK OOP")
        self.root.configure(background="grey75")

        self.left_frame = tk.Frame(self.root,bg="grey75") #input frame
        self.value= tk.DoubleVar() # Wanted to allow conversion of non-integer
        self.value.set(0.00) #      temperature values
        self.textfield = tk.Entry(self.left_frame, textvariable=self.value,
            width=25,
            font=("courier 10 pitch",16),
            bg="lemon chiffon", # “An entry field for putting in a value” constructed
            fg="grey35", justify="center", highlightthickness=2,highlightbackground="black")
        self.var1= tk.StringVar()
        self.var1.set("Celcius")
        self.menu = tk.OptionMenu(
            self.left_frame,
            self.var1,
            "Celcius", #”Options menu” constructed
            "Kelvin",
            "Farenheit")
        self.label2 = tk.Message(self.left_frame,width=250, text="Please select a temperature unit from the menu to convert what you wrote in the entry field.\n\nYour conversion output will be displayed to 2 decimal places after the unit, at most.",font=("courier 10 pitch",12),bg="grey85", highlightthickness=2,highlightbackground="black", pady=25)
        self.label2.grid(row=1)
        self.space = tk.Label(self.left_frame, height=3,bg="grey75")
        self.menu.grid(row=5) # Packing of options menu
        self.textfield.grid(row=3) # Packing of user entry field
        self.space2 = tk.Label(self.left_frame, height=1,bg="grey75")
        self.space5 = tk.Label(self.left_frame, height=1,bg="grey75")
        self.space5.grid(row=4)
        self.space.grid(row=0)
        self.space2.grid(row=2)


        self.right_frame = tk.Frame(self.root,bg="grey75") # conversion and output frame
        self.label1 = tk.Message(self.right_frame,text="Please supply something to convert using the entry field and menu \n(both left)",
            font=("courier 10 pitch",15),# Tk message used to construct the
            fg="dim gray",              # results display because of flexibility
            bg="grey85", highlightthickness=1,highlightbackground="black")
        self.label1.grid(row=0)
        self.space3 =tk.Label(self.right_frame, height=1,bg="grey75")
        self.space3.grid(row=1)
        self.button1 = tk.Button(self.right_frame, text="Convert!", command=self.ConvTemp,font=("courier 10 pitch",15,"bold"),bg="light goldenrod",fg="grey12", highlightthickness=1,highlightbackground="black")
        self.button1.grid(row=2) # "A button that starts the conversion" (constructed and packed)
        self.space4 = tk.Label(self.root, width=2,bg="grey75")
        self.space4.grid(column=0,row=0)
        self.space6 = tk.Label(self.root, width=4,bg="grey75")
        self.space6.grid(column=2,row=0)
        self.left_frame.grid(column=1,row=0) # Input frame
        self.right_frame.grid(column=3,row=0) # Conversion and output frame
        self.root.mainloop()

    def ConvTemp(self): # Handles each value entered based on temperature unit
        #first part rejects non-number inputs
        while True:
            try:
                type(self.value.get()) == type(0.00)
                break
            except tk.TclError:
                self.value.set(0.00)
                self.label1.config(text=f"That is not a number. What am I supposed to do with this? Please try something else.",font=("courier 10 pitch",19))
                return
            except UnboundLocalError:
                self.value.set(0.00)
                self.label1.config(text=f"That is not a number. What am I supposed to do with this? Please try something else.",font=("courier 10 pitch",19))
                return
            except:
                pass
        # now the VarType is checked, we can start manipulating the number
        temp = self.value.get() # And prints into message the value of that temp
        tempnum = float(temp)
        tempunit = self.var1.get()
        # Handles the conversions based on the unit selected in menu
        if tempunit == "Celcius":
            Kel = round(tempnum + 273.15,2)
            Far = round(((9*tempnum)/5)+32,2)
            # In all nested "if" statements, Kelvin value is >0 is checked.
            # The user should not be able to input lower values than absolute
            # zero. (thanks Fabian for this idea)
            if Kel >= 0:
                self.label1.config(text=f"Converted temperature values ({tempnum} {tempunit}):\n\n{Kel} Kelvin\n{Far} Farenheit",font=("courier 10 pitch",19))
            else:
                self.label1.config(text=f"{temp}C is not a valid input. Please try something else.",font=("courier 10 pitch",19))
        elif tempunit == "Kelvin":
            Cel = round(tempnum - 273.15,2)
            Far = round((((tempnum - 273.15)*9)/5)+32,2)
            if tempnum >= 0:
                self.label1.config(text=f"Converted temperature values ({tempnum} {tempunit}):\n\n{Cel} Celsius\n{Far} Farenheit",font=("courier 10 pitch",19))
            else:
                self.label1.config(text=f"{temp}K is not a valid input! Please try something else.",font=("courier 10 pitch",19))
        elif tempunit == "Farenheit":
            Cel = round((tempnum - 32)*(5/9), 2)
            Kel = round(((tempnum - 32)*(5/9))+273.15,2)
            if Kel >= 0:
                self.label1.config(text=f"Converted temperature values ({tempnum} {tempunit}):\n\n{Cel} Celcius\n{Kel} Kelvin",font=("courier 10 pitch",19))
            else:
                self.label1.config(text=f"{temp}F is not a valid input. Please try something else.",font=("courier 10 pitch",19))
        # This bit really shouldn't happen
        else:
            self.label1.config(text="Please select a temperature unit")




TempConv() # Class with widget in constructor is called
