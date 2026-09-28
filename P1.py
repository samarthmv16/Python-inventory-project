tools = ["Spanner", "Hammer", "Screwdriver", "Wrench"]
stock = [5, 2, 7, 3]

while True:
    print("\nHELLO")
    print("WORKSHOP INVENTORY")
    print("1. View Inventory ," , "2. Add Stock ," , "3. Remove Stock ," , "4. Check Stock")
    option = int(input("Choose your option "))

    if option==1:
        for i in range(len(tools)):
            print(tools[i],stock[i],sep=": ")

    elif option==2:
        add_tool = input("What tool? ")
        add_tool = add_tool.title().strip()
        while True:
            n1 = int(input("How many? "))
            if n1>=0:
                break
        match add_tool:
            case "Spanner":
                stock[0] += n1
            case "Hammer":
                stock[1] += n1
            case "Screwdriver":
                stock[2] += n1
            case "Wrench":
                stock[3] += n1

    elif option==3:
        sub_tool = input("What tool? ")
        sub_tool = sub_tool.title().strip()
        while True:
            n2 = int(input("How many? "))
            if n2 >=0:
                break
        match sub_tool:
            case "Spanner":
                if stock[0] < n2:
                    print("Not enough stocks")
                else:
                    stock[0] -= n2
            case "Hammer":
                if stock[1] < n2:
                    print("Not enough stocks")
                else:
                    stock[1] -= n2
            case "Screwdriver":
                if stock[2] < n2:
                    print("Not enough stocks")
                else:
                    stock[2] -= n2
            case "Wrench":
                if stock[3] < n2:
                    print("Not enough stocks")
                else:
                    stock[3] -= n2

    elif option==4:
        check_tool = input("What tool? ")
        check_tool = check_tool.title().strip()
        match check_tool:
            case "Spanner":
                print("Spanner has" , stock[0] ," units")
            case "Hammer":
                print("Hammer has" , stock[1] ," units")
            case "Screwdriver":
                print("Screwdriver has" , stock[2] ," units")
            case "Wrench":
                print("Wrench has" , stock[3] ," units")

    else:
        print("Invalid Option")

    cont = input("Want to continue? Yes or No ")
    cont = cont.title().strip()
    if cont == "No":
        break