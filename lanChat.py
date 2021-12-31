import tkinter as tk
import clientAndServer
import os


# Global Vars
txtBox = None
msg = None
targetIP = None
txtBoxTagCount = 0

def send(event = None):
    clientAndServer.connAndSend(targetIP.get(), msg.get())
    msg.delete(0, 'end')
    

def Print(text, colour = "red"):
    global txtBox
    global txtBoxTagCount
    currLine = txtBox.index("end")

    txtBox.insert(tk.END, "\n>" + str(text))
    txtBox.tag_add("tag" + str(txtBoxTagCount), currLine, currLine[:-1] + "1")
    txtBox.tag_config("tag" + str(txtBoxTagCount), foreground=colour)
    txtBoxTagCount += 1

    # scroll to end of box
    txtBox.see('end')


# Driver
def main():
    # Main Window--------
    window = tk.Tk()
    window.title('LAN Chat')
    window.geometry("800x500")
    window.bind('<Return>', send)

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

    # My IP
    myIPPannel = tk.PanedWindow()
    myIPPannel.pack()
    myIPLable = tk.Label(window, text = "MyIP:")
    myIP = tk.Text(window, height=1, width=15)
    myIPPannel.add(myIPLable)
    myIPPannel.add(myIP)
    myIP.insert(tk.END, str(clientAndServer.getMyIP()))
    myIP.config(state=tk.DISABLED)

    # Begin indefinite loop to run the window---------
    window.mainloop()

    # Ends all threads when window is closed
    os._exit(0)


# Run main
if __name__ == "__main__":
    main()