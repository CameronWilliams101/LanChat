# pip install tk
import tkinter as tk
import clientAndServer
import threading


# Global Vars
txtBox = None
msg = None

def write():
    # threading.Thread(target=clientAndServer.client).start()
    clientAndServer.client(msg.get())

def start():
    clientAndServer.start(txtBox)

def Print(text):
    global txtBox
    currLine = txtBox.index("end")

    txtBox.insert(tk.END, "\n>" + str(text))
    txtBox.tag_add("start", currLine, currLine[:-1] + "1")
    txtBox.tag_config("start", foreground="red")


# Driver
def main():
    # Main Window--------
    window = tk.Tk()
    window.title('LAN Chat')
    window.geometry("800x500")

    # Message entry and button
    global msg
    msg = tk.Entry(window)
    msg.pack()
    button1 = tk.Button(window, text='Write', width=25, command=lambda: write())
    button1.pack()

    # Full Terminal mimic
    global txtBox
    txtBox = tk.Text(window, height=20, width=50)
    txtBox.pack()
    txtBox.insert(tk.END, '--------------Welcome to LAN Chat--------------')
    txtBox.tag_add("intro", "1.0", "1.47")
    txtBox.tag_config("intro", background="black", foreground="green")

    # Start lanChat client and server button
    button2 = tk.Button(window, text='Start', width=25, command=lambda: start())
    button2.pack()

    # Begin indefinite loop to run the window---------
    window.mainloop()


# Run main
if __name__ == "__main__":
    main()