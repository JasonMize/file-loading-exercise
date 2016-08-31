import json

massive_dictionary = json.loads(open('store_data.json').read())

most_expensive = 0
least_expensive = 1000
total_revenue = 0
total_sold = 0
total_price = 0
total_cost_to_make = 0
total_profit = 0
sellers = []
best_sellers = []

for dictionary in massive_dictionary:
	if dictionary["price"] > most_expensive:
		most_expensive = dictionary["price"]

	else: 
		least_expensive = dictionary["price"]
	
	total_sold = total_sold + (dictionary["sold"])
	total_price = total_price + (dictionary["price"])
	total_revenue = total_sold * total_price
	
	total_cost_to_make = total_cost_to_make + (dictionary["cost_to_make"])
	
	total_profit = total_revenue - total_cost_to_make
	
	seller_dict = {
		"name" : dictionary["name"],
		"sold" : dictionary["sold"]
	}
	sellers.append(seller_dict)


sellersX = sorted(sellers, key = lambda k: k['sold'])
best_sellers = sellersX[-1: -11: -1]

print ("Most Expensive Item: ${:,.2f}".format(most_expensive))
print ("Least Expensive Item: ${:,.2f}".format(least_expensive))
print ("Total Revenue: ${:,.2f}".format(total_revenue))
print ("Total Profit: ${:,.2f}".format(total_profit))

for key in best_sellers:
  	print("10 Best Sellers: {}: {}".format(key["name"], key["sold"]))

for key in massive_dictionary:
	print("Department: {}, \n\tNumber Sold: {}".format(key["department"], key["sold"]))
