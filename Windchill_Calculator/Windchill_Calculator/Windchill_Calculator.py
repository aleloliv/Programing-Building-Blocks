#added a function to validate the scale input from the user, added a while loop to continue the code as long as the user wants to, added a graph library to show a graph of the wind chill

import matplotlib.pyplot as plt


def wind_chill_calculator(temperature, speed):
    wind_chill = 35.74+0.6215 * temperature - 35.75 * (speed ** 0.16) + 0.4275 * temperature * (speed ** 0.16)
    return wind_chill

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip().lower() in ['c', 'f']:
            return user_input.strip().lower()
        print("Please enter 'C' for Celsius or 'F' for Fahrenheit.")

while True:
    temperature = float(input("What is the temperature? "))
    scale = get_user_input("Celsius or Fahrenheit? C/F: ")

    wind_chills = []

    winds = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

    if scale.lower() == "c":
        temperature = celsius_to_fahrenheit(temperature)

    for wind in winds:
        wind_chill = wind_chill_calculator(temperature, wind)
        wind_chills.append(wind_chill)
        print(f"At temperature {temperature}F, and wind speed {wind} mph, the windchill is: {wind_chill:.2f}F")
    
    # Create a line chart
    plt.plot(winds, wind_chills)

    # Add labels and title
    plt.xlabel('Temperature (F)')
    plt.ylabel('Wind Speed (mph)')
    plt.title('Wind Chill')

    # Display the chart
    plt.show()


    choice = input("Do you wish to continue? YES / NO ").lower()

    while choice not in ['yes', 'no']:
        print("Please select YES or NO.")
        choice = input("Do you wish to continue? YES / NO ").lower()

    if choice == "no":
        break





