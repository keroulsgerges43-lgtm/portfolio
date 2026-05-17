# Problem 4 - Restaurant Bill with Tax and Tip



food_cost = float(input("Enter the cost of the food: "))



drink_cost = float(input("Enter the cost of the drink: "))



subtotal = food_cost + drink_cost



tax = subtotal * 0.062



total_after_tax = subtotal + tax



tip = total_after_tax * 0.20



final_total = total_after_tax + tip



print("Subtotal:", subtotal)



print("Total after tax:", total_after_tax)



print("Final total with tip:", final_total)