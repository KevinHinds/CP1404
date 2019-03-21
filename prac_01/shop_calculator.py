total_cost = 0
number_of_items = int(input("Please enter of items:"))
for i in range(number_of_items):
    cost_of_item = float(input("Please enter cost of item: "))
    total_cost = total_cost + cost_of_item
if total_cost > 100:
    total_cost = total_cost * 0.9
print("Total price for ", number_of_items, "items is {:.2f}".format(total_cost))
