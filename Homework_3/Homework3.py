value_1 = 10
new_value_1 = value_1 // 2 if value_1 < 100 else - value_1
print(new_value_1)

#####################################################

value_2 = 10
new_value_2 = 1 if value_2 < 100 else 0
print(new_value_2)

#####################################################

value_3 = 100
new_value_3 = True if value_3 < 100 else False
print(new_value_3)

#####################################################

my_str_1 = "0123456789"
print(my_str_1[::2])

#####################################################

my_str_2 = "0123456789"
print(my_str_2[1::2])

#####################################################

my_str_3 = "str"
if len(my_str_3) < 5:
    print(my_str_3 * 2)
else:
    print(my_str_3)

#####################################################

my_str_4 = "str"
if len(my_str_4) < 5:
    print(f"{my_str_4}{my_str_4[::-1]}")
else:
    print(my_str_4)
