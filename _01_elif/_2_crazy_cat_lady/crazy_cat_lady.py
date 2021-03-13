from tkinter import simpledialog, messagebox, Tk
import webbrowser


def play_video(url):
    webbrowser.open(url)


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    s = simpledialog.askinteger("","how many cats do you have?")
    if s > 3:
        messagebox.showinfo("you are a CRAZY cat person")
    elif s == 1:
        play_video("https://www.youtube.com/watch?v=tpiyEe_CqB4")
    elif s == 2:
        play_video("https://www.youtube.com/watch?v=tpiyEe_CqB4")
    elif s == 0:
        play_video("https://www.youtube.com/watch?v=tpiyEe_CqB4")
    # TODO 1) Make a new window variable, window = Tk()
    #      2) Hide the window using the window's .withdraw() method
    #      3) Ask the user how many cats they have
    #      4) If they have 3 or more cats, tell them they are a crazy cat lady
    #      5) If they have less than 3 cats AND more than 0 cats, call the method below to show them a cat video
    #      6) If they have 0 cats, show them a video of A Frog Sitting on a Bench Like a Human

    pass
