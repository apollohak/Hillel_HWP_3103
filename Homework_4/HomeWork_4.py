my_list_1 = [20, 140, 80, 160, 50, 110]

for value_1 in my_list_1:
    if value_1 > 100:
        print(value_1)

###############################################

my_list_2 = [20, 140, 80, 160, 50, 110]
my_result_1 = []

for value_2 in my_list_2:
    if value_2 > 100:
        my_result_1.append(value_2)

print(my_result_1)

###############################################

my_list_3 = [20, 140, 80, 160, 50, 110]

if len(my_list_3) >= 2:
    my_list_3.append(my_list_3[-1] + my_list_3[-2])
else:
    my_list_3.append(0)

print(my_list_3)

###############################################

my_string_1 = '0123456789'
my_list_4 = []

for symb_1 in my_string_1:
    for symb_2 in my_string_1:
        my_list_4.append(int(symb_1 + symb_2))

print(my_list_4)
