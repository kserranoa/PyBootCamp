#Bob, Ann, Jane and Ashwin want to order pizza - they know they will each eat
#4 slices of pizza. The local pizza shop sells pizzas of only 6 slices
#What is the minimum number of pizzas needed - Use floor division
def pizzaCounter():
    slicesinPizza = 6
    sliceperP = 4
    total_clients = 4
    total_slices = 4*4
    total_pizzas = round(total_slices / slicesinPizza)
    invoice = print(">>> Total pizzas: " , total_pizzas)
    return invoice
