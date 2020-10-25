# Lowest Common Factor
def lcm():
    # Print info/instructions
    print("Enter 3 integers to find the LCM")

    # Input 3 numbers
    x = int(input("1st integer: "))
    y = int(input("2nd integer: "))
    z = int(input("3rd integer: "))

    # Determine greatest number
    if x > y and x > z:
        greatest = x
    elif y > x and y > z:
        greatest = y
    else:
        greatest = z

    # Determine LCM
    while(True):
        if (greatest%x == 0) and (greatest%y == 0) and (greatest%z == 0):
            return ("The LCM is: " + str(greatest) + " \n")
            break
        else:
            greatest += 1

# Greatest Common Factor
def gcf():
    # Print info/instructions
    print("Enter 3 integers to find the GCF")

    # Input 3 numbers
    x = int(input("1st integer: "))
    y = int(input("2nd integer: "))
    z = int(input("3rd integer: "))

    # Determine smallest number
    if x < y and x < z:
        smallest = x
    elif y < z and y < x:
        smallest = y
    else:
        smallest = z

    # Determine GCF
    for i in range(1, smallest+1):
        if (x%i == 0) and (y%i == 0) and (z%i == 0):
            gcf = i
    return ("The GCF is: " + str(gcf) + " \n")

# Run calculator
def run():
    user_input = int(input("Welcome! Enter one of the following digits: \n1) LCM \n2) GCF\n"))
    if user_input == 1:
        print(lcm())
    else:
        print(gcf())
    run_again = int(input("Would you like to calculate again? Enter one of the following digits: \n1) Yes \n2) No\n"))
    if run_again == 1:
        run()

run()






