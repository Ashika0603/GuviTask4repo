def FitsrAndlastLetter(value):

    words = value.split()
    for i in words:
        if len(i) == 1:
            print(i[0], end='')
        else:
            print(i[0] + i[-1], end='')

value = input("Enter the value: ")
FitsrAndlastLetter(value)
