

print("Written by EMİN AYYILDIZ")
print("""    Please enter your choice. 
    Your choice determines which field you will convert units to. these fields are as follows for this program. 
    length, mass, temperature, time \n       \n""")
while True:

    choice = input("Please enter your choice :")
    if choice == "length" or choice == "uzunluk":
      value = float(input('Enter a value (km, m, cm, mm, yd): '))
      from_unit = input('Enter the unit to convert from (km, m, cm, mm, yd): ')
      to_unit = input('Enter the unit to convert to (km, m, cm, mm, yd): ')
  #length ynits converter
      if from_unit == "m" or value == "metre":
        if to_unit == "cm":
          new_value = (value)*(100)
        elif to_unit == "mm":
          new_value = (value)*(1000)
        elif to_unit == 'km':
          new_value = (value)*0.001
        elif to_unit == "yd":
          new_value = value*(1.09)
      elif from_unit == "cm":
        if to_unit == "m" or to_unit == "metre":
          new_value = value*0.01
        elif to_unit == "mm":
          new_value = value*10
        elif to_unit == "km":
          new_value = 0.000001
        elif to_unit =="yd":
          new_value = value*0.010936133
      elif from_unit == "mm":
        if to_unit == "cm":
          new_value = (value)*(10)
        elif to_unit == "m":
          new_value = (value)*(0.001)
        elif to_unit == 'km':
          new_value = (value)*(0.000001)
        elif to_unit == "yd":
          new_value = value*(0.0010936133)
      elif from_unit == "km":
        if to_unit == "m":
          new_value = (value)*(1000)
        elif to_unit == "cm":
          new_value = (value)*(100000)
        elif to_unit == 'mm':
          new_value = (value)*(1000000)
        elif to_unit == "yd":
          new_value = value*(1093.6133)
      elif from_unit == "yd":
        if to_unit == "m" or to_unit == "metre":
          new_value = value* (0.9144)
        elif to_unit == "cm":
          new_value = value*(91.44)
        elif to_unit == "km":
          new_value = value*(0.0009144)
        elif to_unit == "mm":
          new_value = value*(914.4)
    
     #temperature units converter
    elif choice  ==  "temperature" or choice == "sıcaklık":
      value = float(input('Enter a value (C, K, F): '))
      from_unit = input('Enter the unit to convert from (C, K, F): ')
      to_unit = input('Enter the unit to convert to (C, K, F): ')
      if from_unit == "C":
        if to_unit == "K" or to_unit == "kelvin":
          new_value = value+273.15
        elif to_unit == "F" or from_unit == "Fahrenheit":
          new_value = (value*(1.8))+32
        
      elif from_unit == 'K' or from_unit == "kelvin":
        if to_unit == "C":
          new_value = (value)-(273.15)
        elif to_unit == "F":
          new_value = (value*(9/5))-459.67
      elif from_unit == "F" or from_unit == "Fahrenheit":
        if to_unit == "C":
          new_value = ((value)-32)/1.8
        elif to_unit == "K" or to_unit == "kelvin":
          new_value = (value + 459.67)*(5/9)
      #mass units converter
    elif choice == "mass" or choice == "kütle":
      value = float(input('Enter a value (T, kg, g, mg): '))
      from_unit = input('Enter the unit to convert from (T, kg, g, mg): ')
      to_unit = input('Enter the unit to convert to (T, kg, g, mg): ')
      if from_unit == "T" or from_unit == "ton":
        if to_unit == "kg":
          new_value = value*1000
        elif to_unit == "g":
          new_value = value*1000000
        elif to_unit == "mg":
          new_value = value*1000000000
      elif from_unit == "kg":
        if to_unit == "T" or to_unit == "ton":
          new_value = value* 0.001
        elif to_unit == "g":
          new_value = value* 1000
        elif to_unit == "mg":
          new_value = value*1000000
      elif from_unit == "g":
        if to_unit == "T" or to_unit == "ton":
          new_value = value*0.000001
        elif to_unit == "kg":
          new_value = value*0.001
        elif to_unit == "mg":
          new_value = value*1000
      elif from_unit == "mg":
        if to_unit == "T" or to_unit == "ton":
          new_value = value*0.000000001
        elif to_unit == "kg":
          new_value = value*0.000001
        elif to_unit == "g":
          new_value = value*0.001
     
#time unit converter
    elif choice == "time" or choice == "zaman":
      value = float(input('Enter a value (s, min, ms): '))
      from_unit = input('Enter the unit to convert from (s, min, ms): ')
      to_unit = input('Enter the unit to convert to (s, min, ms): ')
      if from_unit == "s" or from_unit == "saniye":
        if to_unit == "min" or to_unit == "dakika":
          new_value = value * 0.0166666667
        elif to_unit == "ms":
          new_value = value*1000
      elif from_unit == "min" or from_unit == "dakika":
        if to_unit == "s" or to_unit == "saniye":
          new_value = value* 60
        elif to_unit == "ms":
          new_value = value*60000
      elif from_unit == "ms":
        if to_unit == "min" or to_unit == "dakika":
          new_value = value * (167/10000000)
        elif to_unit == "s":
          new_value = value*0.01

      
    print(f'{value} {from_unit} is equal to {new_value} {to_unit}')
  
    order = input("Press Q to exit or Enter to continue")
    if order == "q" or order == "Q":
      print("BYE BYE :))")
      break
    else:
      continue
