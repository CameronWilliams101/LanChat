import clientAndServer

def main():
    while True:
        print("--------------------LAN Chat--------------------------") 
        print("Be both Client and Server \'1\'")
        print("Exit: Terminate program \'0\'")

        operation = input("\nEnter the option you wish:")

        #Parse input
        try:
            operation = int(operation)
        except:
            print("Invalid input, try again...")
            continue

        # Operation choice       
        if operation == 0:
            print("Goodbye...")
            break
        elif operation == 1:
            clientAndServer.start()
            break
        else:
            print("Invalid option, try again...")
            continue 

# Run main
if __name__ == "__main__":
    main()