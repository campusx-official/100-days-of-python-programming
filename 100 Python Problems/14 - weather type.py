# Write a program that will determine whether the value of temperature and humidity is provided by the user.

# | TEMPERATURE(C) | HUMIDITY(%) |     WEATHER    |
# |----------------|-------------|----------------|
# |      >= 30     |    >= 90    | Hot and Humid  |
# |      >= 30     |    <  90    |      Hot       |
# |      <  30     |    >= 90    | Cold and Humid |
# |      <  30     |    <  90    |      Cold      |

temp = int(input("Enter temperature in Celsius: "))
humid = int(input("Enter humidity percentage: "))

if temp >= 30 and humid >= 90:
    print("Hot and Humid")
elif temp >= 30 and humid < 90:
    print("Hot")
elif temp < 30 and humid >= 90:
    print("Cold and Humid")
else:
    print("Cold")