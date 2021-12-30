# pip install tk
import tkinter as tk
import clientAndServer


# Global Vars
txtBox = None
msg = None
targetIP = None

def send():
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

    # Full Terminal mimic
    global txtBox
    txtBox = tk.Text(window, height=20, width=50)
    txtBox.pack()
    txtBox.insert(tk.END, '---------------Welcome to LAN Chat----------------')

    # Pannel 1
    pannel1 = tk.PanedWindow()
    pannel1.pack()

    # Target Pannel
    targetPannel = tk.PanedWindow()
    global targetIP
    targetIPLable = tk.Label(window, text = "TargetIP:") 
    targetIP = tk.Entry(window)
    targetPannel.add(targetIPLable)
    targetPannel.add(targetIP)
    pannel1.add(targetPannel)
    pannel1.add(tk.Label(window, text = "       Message:"))

    # Msg Pannel
    msgPannel = tk.PanedWindow()
    global msg
    msg = tk.Entry(window, width=50)
    msgPannel.add(msg)
    sendButton = tk.Button(window, text='Send', command=lambda: send())
    msgPannel.add(sendButton)
    pannel1.add(msgPannel)

    # Start LanChat server---------
    clientAndServer.start(txtBox)

    # Begin indefinite loop to run the window---------
    window.mainloop()


# Run main
if __name__ == "__main__":
    main()