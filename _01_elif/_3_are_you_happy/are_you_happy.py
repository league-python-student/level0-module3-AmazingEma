from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    W = Tk()
    W.withdraw()
    h = simpledialog.askstring("", "Are You Happy?")
    if h == "No":
        do = simpledialog.askstring("", "Do you want to be happy?")
    else:
        messagebox.showinfo("", "Keep doing whatever you're doing")
    if do == "Yes":
        messagebox.showinfo("",  "Change Something")
    else:
        messagebox.showinfo("",  "Keep doing whatever you're doing")

    pass
