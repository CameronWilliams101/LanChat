# pip install tk
import tkinter as tk
import clientAndServer
import threading


# Global Vars
txtBox = None
msg = None
targetIP = None

def send():
    # threading.Thread(target=clientAndServer.client).start()
    clientAndServer.connAndSend(targetIP.get(), msg.get())
    

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
    button1 = tk.Button(window, text='Send', width=25, command=lambda: send())
    button1.pack()

    # Full Terminal mimic
    global txtBox
    txtBox = tk.Text(window, height=20, width=50)
    txtBox.pack()
    txtBox.insert(tk.END, '--------------Welcome to LAN Chat--------------')

    # Entry for targetIP
    global targetIP
    targetIPLable = tk.Label(window, text = "TargetIP").pack()  
    targetIP = tk.Entry(window)
    targetIP.pack()

    # Start LanChat server
    clientAndServer.start(txtBox)

    # Begin indefinite loop to run the window---------
    window.mainloop()


# Run main
if __name__ == "__main__":
    main()