def voltage():
    i = float(input("Enter current(A): "))
    r = float(input("Enter resistance(Ω): "))
    v = i * r
    print("Answer:",v,"volts")
def current():
    v = float(input("Enter voltage(V): "))
    r = float(input("Enter resistance(Ω): "))
    i = v / r
    print("Answer:",i,"amps")
def resistance():
    v = float(input("Enter voltage(V): "))
    i = float(input("Enter current(A): "))
    r = v / i
    print("Answer:",r,"ohms")
def wattage():
    v = float(input("Enter voltage(V): "))
    i = float(input("Enter current(A): "))
    p = v * i
    print("Answer:",p,"watts")
def helpme():
    print('*'*40)
    print("This is a program to calculate voltage, current,")
    print("and resistance, using Ohm's Law.")
    print("Input is somewhat flexible; (eg.'v','volts','voltage')")
    print("*Use standard units.")
    print('*'*40)          
    
while 1==1:
    ask = input("What would you like to solve for?(or, type 'helpme')")
    if ask == "v" or ask == "voltage" or ask == "volts":
        voltage()
    elif ask == "i" or ask == "amps" or ask == "current" or ask == "amperage":
        current()
    elif ask == "r" or ask == "ohms" or ask == "resistance":
        resistance()
    elif ask == "w" or ask == "watts" or ask == "wattage" or ask == "power":
        wattage()
    elif ask == "helpme":
        helpme()
    elif ask == "quit":
        break
    

