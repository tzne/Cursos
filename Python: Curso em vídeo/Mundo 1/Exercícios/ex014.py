# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

celsius = float(input("Insira a temperatura, em Celsius: "))
fahrenheit = celsius * 9/5 + 32
print("{:.1f}°C é equivalente a {:.1f}°F".format(celsius, fahrenheit))
