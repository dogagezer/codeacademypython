hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = sum(prices)
def average_price_for(plist):
  print("The average haircut price: {}".format((sum(plist) / len(hairstyles))))
average_price_for(prices)
new_prices = [price - 5 for price in prices]
print(new_prices)
average_price_for(new_prices)
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
print("Total revenue:{}".format(total_revenue))
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
