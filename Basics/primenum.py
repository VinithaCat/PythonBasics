while True:
    num = int(input("Enter number : "))
    for i in range(2, num):
        if(num%i == 0):
            print(f"{num} is not a prime")
            break
    else:
        print(f"{num} is a prime")
    decision = input("Do you want to enter other number ?(Yes/No) : ")
    if(decision == "Yes"):
        continue
    else:
        break