#Victoria Larrazolo Lesson 4 Hands On

#Part 1
Luna= dict(animaltype="Cat", color="Black", nickname="Lunis", ownersname="Victoria Larrazolo" )
Paisley= dict(animaltype="dog", color="brown", nickname="paie", ownersname="Ben Larrazolo")
for key, value in Luna.items():
    print(key, ':', value)

for key, value in Paisley.items():
    print(key, ':', value)

#Part 2
SanFrancisco= dict(population="874,961", interestingfact= "San Francisco has three murals by Diego Rivera", localLanguage="English")
Guanajuato= dict(population="72 237", interestingfact="The narrow streets and alleys have given rise to a pastime called 'callejoneadas'. These are roving parties, traditionally held by the students of the University of Guanajuato with live musicians. Today, there are callejoneadas arranged for tourists as well.", localLanguage="Spanish")
SaltLake= dict(population="197,756", interestingfact="Downtown Salt Lake City is the world headquarters of the Mormon Church.", localLanguage="English")
print(SanFrancisco, Guanajuato, SaltLake)
england = dict(calpital="London", population="53.01 million", interestingfact="England is the most populated country in the United Kingdom.", localLanguage="English" )
france = dict(capital="Paris", population="66.9 million", interestingfact="France Is the Most-Visited Country in the World.", localLanguage="French")
belgium = dict(capital="Brussles", population="11.35 million", interestingfact="Belgium produces more than 220,000 tons of chocolate per annum", localLanguage="Dutch")
for key, value in SanFrancisco.items():
    print(key, ':', value)
for key, value in Guanajuato.items():
    print(key, ':', value)
for key, value in SaltLake.items(): 
    print(key, ':', value)
for key, value in england.items():
    print(key, ':', value)
for key, value in france.items(): 
    print(key, ':', value)
for key,value in belgium.items():
    print(key, ':', value)

#Part 3
pizza_order= dict(customerName= "Victoria", pizzaSize= "Small", crustType= "Gluten Free", toppings=" Artichoke, Onion, Pineapple, Smoked Ham")
print(pizza_order.get('customerName'))
print("Thank you for your order, " + pizza_order.get("customerName")), print("You have ordered a " + pizza_order.get("pizzaSize") + ' ' + pizza_order.get("crustType") + " pizza with the following toppings:" + pizza_order.get("toppings")) 
