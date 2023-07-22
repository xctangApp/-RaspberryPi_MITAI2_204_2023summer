from gpiozero import Button
btn = Button(17)

def hello():
    print('Hello')

btn.when_pressed = hello
