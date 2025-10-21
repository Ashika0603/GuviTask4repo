import operator
my_dict = {'Ravi': 45, 'Vidhya': 76, 'Yamini': 3}
sorted_items_asc = sorted(my_dict.items(), key=operator.itemgetter(1))
sorted_dict_asc = dict(sorted_items_asc)
print("Sorted :", sorted_dict_asc)

mykeys = list(my_dict.keys())
mykeys.sort()
result ={i: my_dict[i] for i in mykeys}
print("sorted :", result)