toppings = ["pepperoni", "pineapple",
"cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2,6,1,3,2,7,2]
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)
print("We sell {} different kinds of pizza!".format(num_pizzas))
pizza_and_prices = []
for i in range(len(toppings)):
  pizza_and_prices.append([prices[i], toppings[i]])
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop()
peppers = [2.5, "peppers"]
for i in range(len(pizza_and_prices)):
  if  pizza_and_prices[i][0] >= peppers[0]:
     pizza_and_prices.insert(i, peppers)
     break
print(pizza_and_prices)
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
