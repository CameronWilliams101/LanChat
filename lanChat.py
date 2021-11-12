import echoclient
import echoserver

def main():
    while True:
        print("--------------------LAN Chat--------------------------") 
        print("Be a Client \'1\'")
        print("Be a Server \'2\'")
        print("Exit: Terminate program \'0\'")

        operation = input("\nEnter the option you wish:")

        #Parse input
        try:
            operation = int(operation)
        except:
            print("Invalid input, try again...")
            continue

        # Operation choice
        if operation < 0 or operation > 2:
            print("Invalid option, try again...")
            continue        
        if operation == 0:
            print("Goodbye...")
            break
        elif operation == 1:
            host = input("\nEnter ip-address of host you wish to connect to: ")
            echoclient.start(host)
        elif operation == 2:
            echoserver.start(80)

# Run main
if __name__ == "__main__":
    main()