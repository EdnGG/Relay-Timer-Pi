from gpiozero import Button
button = Button(27)

button.wait_for_press()
print("Buttons was pressed")

