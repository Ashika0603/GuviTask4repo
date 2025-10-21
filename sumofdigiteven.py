
my_list = [12, 23, 34, 45, 56, 101, 123, 456]
result_list  = []
for number in my_list:
    sum = 0
    for digi_char in str(number):
        sum += int(digi_char)
    if sum % 2 == 0:
        result_list.append(sum)

print("Numbers with even Sum of digits:", result_list)

