#3.4 Guest List
dinner_guests = ['Abraham Lincoln', 'Joseph Smith', 'Wayne Gretsky']
print(dinner_guests[0] + " you are invited to my dinner party")
print(dinner_guests[1] + " you are invited to my dinner party")
print(dinner_guests[2] + " you are invited to my dinner party")
#
#
#3.5 Changing Guest List
cant_make_it = dinner_guests.pop(1)
print(cant_make_it + " won't be able to make it to the dinner party")
dinner_guests.insert(1, 'Kayne West')
print(dinner_guests)
print(dinner_guests[0] + " you are invited to my dinner party")
print(dinner_guests[1] + " you are invited to my dinner party")
print(dinner_guests[2] + " you are invited to my dinner party")
#
#
#3.6 More Guests
print("I've found a bigger table so I can invite more guests! Woohoo!!!")
dinner_guests.insert(0,"Tilakum")
dinner_guests.insert(2, "Shamu")
dinner_guests.append("Lebron James")
print(dinner_guests)
print(dinner_guests[0] + " you are invited to my dinner party")
print(dinner_guests[1] + " you are invited to my dinner party")
print(dinner_guests[2] + " you are invited to my dinner party")
print(dinner_guests[3] + " you are invited to my dinner party")
print(dinner_guests[4] + " you are invited to my dinner party")
print(dinner_guests[5] + " you are invited to my dinner party")
#
#
#3.7 Shrinking Guest List
print("Something came up so now I can only invite two people to my dinner party")
removed_guest = dinner_guests.pop()
print("Sorry, " + removed_guest + " you are no longer invited to my party")
removed_guest = dinner_guests.pop()
print("Sorry, " + removed_guest + " you are no longer invited to my party")
removed_guest =  dinner_guests.pop()
print("Sorry, " + removed_guest + " you are no longer invited to my party")
removed_guest =  dinner_guests.pop()
print("Sorry, " + removed_guest + " you are no longer invited to my party")
print(dinner_guests)
print("Guess what??? " + dinner_guests[0] + " you are still invited to my party")
print("Guess what??? " + dinner_guests[1] + " you are still invited to my party")
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)

#
#
