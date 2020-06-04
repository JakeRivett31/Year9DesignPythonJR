import turtle 

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return


spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)
    
turtle.bind('<Motion>',motion)

    
turtle.done()