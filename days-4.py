# # days--4 HEAD/TAILS exercise
#
# import random
#
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")
#
# ##Banker Roulette  exercise
#
#
# import random
#
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
#
# #Get the total number of items in list.
# num_items = len(names)
# #Generate random numbers between 0 and the last index.
# random_choice = random.randint(0, num_items - 1)
# #Pick out random person from list of names using the random number.
# person_who_will_pay = names[random_choice]
#
# print(person_who_will_pay + " is going to buy the meal today!")
#
#
#
# ##-Treasure map
#
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
#
# horizontal = int(position[0])
# vertical = int(position[1])
#
# selected_row = map[vertical -1]
# selected_row[horizontal -1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")

