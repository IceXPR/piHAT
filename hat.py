from sense_hat import SenseHat
import XboxController

sense = SenseHat()

sense.set_rotation(180)
# sense.show_message("Hello")

y = 0
x = 0
back_colour = (0,0,0)

def buttonPress(controlId, value): 
  global y
  global x
  global back_colour
  if controlId == 17:
    if value == (0, -1):
      y = y + 1
    if value == (1, 0):
      x = x + 1
    if value == (0, 1):
      y = y - 1
    if value == (-1, 0):
      x = x - 1
  if controlId == 9:
    exit()

  if x == 8:
    x = 0
  if y == 8:
    y = 0
  if x == -1:
    x = 7
  if y == -1:
    y = 7

  red = (255, 0, 0)
  blue = (0, 0, 255)
  green = (0, 255, 0)

  sense.clear(back_colour)
  sense.set_pixel(x, y, 255,255,255)


  if controlId == 6:
    back_colour = green
  if controlId == 7:
    back_colour = red
  if controlId == 8:
    back_colour = blue


xboxCont = XboxController.XboxController(controllerCallBack = buttonPress)
xboxCont.start()

# sense.set_pixel(0,0,255,0,0)
