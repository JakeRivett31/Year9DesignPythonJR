if timeneededlabel[len(timeneededlabel) - 1] < 20:
    eventcanvas.config(fg="green")

  elif timeneededlabel[len(timeneededlabel) - 1] < 40 or timeneededlabel[len(timeneededlabel) - 1] >= 21:
    eventcanvas.config(fg="yellow")

  else:
    eventcanvas.config(fg="red")
