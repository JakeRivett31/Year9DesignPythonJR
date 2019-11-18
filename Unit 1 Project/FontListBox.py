variable = IntVar(root)
variable.set("30") # default value

FontListBox = OptionMenu(root, variable, "Font Sizes", "11", "12", "etc")
FontListBox.config(fg="#243c6a", width=5, font =("Franklin Gothic", "15"))
FontListBox.grid(row=1, column=0)