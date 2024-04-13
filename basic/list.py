fruits = ['apple', 'peach', 'melon', 'grapes']

hetro_list = ['string', 1, 3.4, True, fruits]

fruits.append("banana")
print(fruits)

fruits.insert(3, "lemon")
print(fruits)

fruits.remove('peach')
print(fruits)

fruits.sort(reverse=True)
print(fruits)

print(len(fruits))
