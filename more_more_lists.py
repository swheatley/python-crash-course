#3.8 Seeing the World
# Five places I would like to visit:
places_to_visit = ['National Parks', 'Sweden', 'Holland', 'Hawaii', 'Moon']

original_order =  places_to_visit
print("Original order: ")
print(original_order)

alphabetically = sorted(original_order)
print("Sorted alphabetically: ")
print(alphabetically)

print("Still in original order:")
print(original_order)

reverse_alphabetical = sorted(alphabetically, reverse=True)
print("Reverse alphabetical:")
print(reverse_alphabetical)

print("Still the same old list:")
print(original_order)

original_order.reverse()
print("Reversed: ")
print(original_order)

original_order.sort()
print("Sort: ")
print(original_order)

original_order.sort()
print("Sort again: ")
print(original_order)
#
#
#3.9 Dinner Guests
dinner_guests = ['Abraham Lincoln', 'Lebron James', 'Joseph Smith', 'Amy Winehouse']
print("Dinner Guests: ")
print(len(dinner_guests))
#
#
#3.10 Every Function
halloween_candy = ['candy corn', 'butterfingers', 'pumpkin seeds', 'smarties', 'snickers', 'skittles','carmel apple suckers']
print("Length of candy list: ")
print(len(halloween_candy))
print('++++++++++++++++++++')

print("Last listed candy: ")
last_candy = halloween_candy[-1]
print(last_candy)
print('++++++++++++++++++++')

print("Third candy listed is: ")
candy = halloween_candy[2].title()
print(candy)
print('++++++++++++++++++')

print('Bain of all Halloween candy is: ')
print(halloween_candy[0].upper())
print('++++++++++++++++++')

candy_message = "My favorite Halloween candy is " + halloween_candy[0].lower() + "." 
print(candy_message)
print('++++++++++++++++')

halloween_candy.append('Boo Berry Cereal')
print("Added :")
print(halloween_candy[-1])  
