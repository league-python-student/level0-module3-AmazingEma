from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
w = Tk()
w.withdraw()
one = simpledialog.askstring("", "What is full of holes but still holds water?")

if one == "A Sponge":
    two = simpledialog.askstring("","I shave everyday but my beard stays the same. What am I?")
    if two == "A Barber":
        messagebox.showinfo("You are a riddle superstar")
    else:
        messagebox.showinfo("you are pretty good at riddles")

else:
    three = simpledialog.askstring("","there is a one story house where everything is yellow what color are the stairs?")
    if three == "There are no stairs":
        messagebox.showinfo("you are ok at riddles")
    else:
        messagebox.showinfo("you should work on your cognitive thinking skills")


