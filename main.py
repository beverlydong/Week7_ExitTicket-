# Today you will run on loops...but this time through dictionaries! (Last week, you ran loops through lists.)

# Here's a recap of what you did weeks ago with dictionaries:
"""" EXIT TICKET """
# Create your food table here via key:value pairs
# (input the food & prices from lines 73-76):
food_prices = {
 "Chicken" : 1.59 ,
        "Beef" : 1.99,
        "Cheese" : 1.00,
        "Milk" : 2.50
  }
print(food_prices)

# Here's a way to loop through all the key-value pairs in the food_prices dictionary using the items() methods
for food, prices in food_prices.items():
  print (f"\nFood: {food}")
  print (f"\nPrice: {prices}")

# Now, get ready to code!
  
# Make a new dictionary using these key:value pairs of average rent estimates for 1-bedroom in different Bay Area cities in July 2022 according to apartmentlist.com:
# Oakland: 1573
# San Jose: 2103
# Richmond: 1436
# Berkeley: 1715
# South San Francisco: 1809
# San Francisco: 2352
# Hayward: 1898
city_rent = {
"Oakland" : 1573,
  "San Jose" : 2103,
  "Richmond" : 1436,
  "Berkeley" : 1715,
  "South San Francisco" : 1809,
  "San Francisco" : 2352,
  "Hayward" : 1898
}
print(city_rent)

# Let's use a for loop that will print each key:value pair, similar to codes in lines 16-18.
for city, rent in city_rent.items():
  print (f"\nCity: {city}")
  print (f"\nRent: {rent}")

# Let's print another f-string that uses a for loop that prints all key:value pairs.
for city, rent in city_rent.items():
  print(f"The average rent in {city} last month was $ {rent}  .")

# You can also loop through all the keys in a dictionary using the keys() method:
for city in city_rent.keys():
  print(city.title())

# You can also use the keys() method to create a loop to see if a key is in the dictionary--in this case, if a the city of Alameda is in this dictionary:
if 'Alameda' not in city_rent.keys():
  print("We do not have info about Alameda.")

# How about looping through all the values in a dictionary? This can be done using the values() method:
print("These are the average rent in some Bay Area cities last month:")
for rent in city_rent.values():
  print(rent)

# Now in the next line, create your own dictionary of your top 3 favorite restaurants and how many times you have eaten or ordered take-out/drive-through from there in the past month. For example, if you ate at Addis Ethiopian Restaurant twice in the past month, then this key:value pair would be Addis:2. Think about your three favorite restaurants (there are no right or wrong answers--it's your favorite!!) & add them to restaurant_visit dictionary:
restaurant_visit = {
"Chipotle" : 1,
  "Chef Wok" : 1,
  "Well Season" : 2
  
}
print(restaurant_visit)

# In the next line, create a for loop that prints out an f-string that says "In the past month, I have eaten out {visit} times at {restaurant}." This is similar to the code  in lines 47-48.
for restaurant, visit in restaurant_visit.items():
  print(f"\nRestaurant: {restaurant}")
  print(f"\nVisit: {visit}")

for restaurants, vists in restaurant_visit.items():
  print(f"In the past month, I have eaten out {visit} times at {restaurant} .")


# Afterwards, create a for loop that prints out all the keys in your dictionary using the keys() method. This code is similar to lines 51-52.
for restaurants in restaurant_visit.keys():
  print(restaurant.title())


# Then, create a for loop that prints out all the values in your dictionary using the values() method. This code is similar to lines 60-61.
for visits in restaurant_visit.values():
  print(visit)


# Have you ever heard of nesting? It's when you store multiple dictionaries in a list or a list of items as a value in a dictionary or a dictionary within another dictionary. 
# Let's create a list of dictionaries of avatars--a fleet of avatars, in fact! Each avatar dictionary will include the primary element that avatar can bend naturally when they were born. If we're trying to create an Avatar game, we can also include how many points a player has to earn in order to access this particular avatar. Here are 4 dictionaries:
avatar_0 = {'element': 'water' , 'points': 11}
avatar_1 = {'element': 'air', 'points': 17}
avatar_2 = {'element': 'fire', 'points': 7}
avatar_3 = {'element': 'earth', 'points': 9}
# now we can create a list of these dictionaries:
avatars = [avatar_0, avatar_1, avatar_2, avatar_3]

# We can now run a loop through this list of dictionaries & print out each avatar:
for avatar in avatars:
  print(avatar)

# Now let's access the last 33 reincarnations of the avatar using the range() method. First make an empty list for storing avatars:
avatars = []

# now make 33 avatars:
for avatar_number in range(33):
  new_avatar = {'element': 'earth', 'points': 9, 'speed':     'slow'}
  avatars.append(new_avatar)

# Show the first 4 avatars created using a slice
for avatar in avatars[:5]:
  print(avatar)
print("...")

# Show how many avatars have been created with this code:
print(f"Total number of avatars: {len(avatars)}")












    
