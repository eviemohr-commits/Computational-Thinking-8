winter_points = 0
summer_points = 0

answer = input("Would you rather A be in cold weather or B be in warm weather? ")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1

answer = input("Would you spend your day at A the snow or B at the beach? ")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1

answer = input("Would you rather be A in lots of layers and cold or B in a t-shirt and very warm? ")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1

answer = input("Do you like A skiing or B jet skiing? ")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1

answer = input("Do you think you’re happier in the A summer or B winter? ")
if answer == "A":
    summer_points += 1   # summer answer should add to summer, not winter
elif answer == "B":
    winter_points += 1

# last question
summer = int(input("Enter a number for summer: "))
answer = input("Do you prefer to be A tan or B pale? ")
if answer == "A" and summer > 2:
    winter_points += 1
elif answer == "B":
    summer_points += 1

# final result
if summer_points > winter_points:
    print("You are a summer person")
elif winter_points > summer_points:
    print("You are a winter person")
else:
    print("It's a tie!")

