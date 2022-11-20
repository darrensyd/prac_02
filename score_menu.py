def determine_status(score):

    if 100 > score >= 90:
        print("Excellent")
    elif 90 > score >= 50:
        print("Passable")
    elif -1 < score < 50:
        print("Bad")
    else:
        print("Invalid score")


def main():
    print("(G)et a valid score ")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    choice = input(">>> ")
    score = None
    status = None
    while choice != 'Q':
        if choice == 'G':
            score = float(input("Enter your score: "))

            while status == "Invalid score":
                print("Invalid score")
                score = float(input("Enter your score: "))
                status = etermine_status(score)

        elif choice == 'P':
            if score is None:
                print("Enter G to complete your score: ")
            else:
                print(status)

        elif choice == 'S':
            if score is None:
                print("Enter G to complete your score: ")
            else:
                print('*' * int(score))
        else:
            print("Invalid enter!")


        choice = input(">>> ")


    print("Have a good day!")


main()





