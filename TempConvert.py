#TempConvert.py
#Name: Sara Salha
#Date: 2/5/2025
#Assignment: TempConvert


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("Enter a Fahrenheit temperature: ")
  tempF = float(tempF)
  tempC = (tempF - 32) * 5/9
  tempC = round(tempC, 2) #rounds to two decimal places
  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
