import random
import quiz_game1_capital_cities

print("Welcome to the African Quiz game! You will be asked 5 questions. The player with the most correct answers will win. Let's begin!")
number_of_players = ["1", "2"]
starting_player = random.choice(number_of_players)

print(f"Player {starting_player} starts.")

starting_player_score = 0
player_two_score = 0

#QUESTION ONE
country = quiz_game1_capital_cities.selected_country
city = quiz_game1_capital_cities.selected_capital_city

user_answer = input(f"What is the capital of {country}?\n")

question_one_country = str(country)
question_one_answer = str(city)

question_one_user_answer = str(user_answer)

if question_one_user_answer == question_one_answer:
    print("Correct!")
    starting_player_score += 1
    print(f"Player {starting_player} score = {starting_player_score}/5 .")
    print(f"Other player score = {player_two_score}/5.")
else:
    print("Incorrect.")
    starting_player_score +=0
    print(f"Player {starting_player} score = {starting_player_score}/5 .")
    print(f"Other player score = {player_two_score}/5.")

#QUESTION TWO
question_two_user_answer = input("Ashanti is a tribe found in which African country?\n")

if question_two_user_answer == "ghana":
    print("Correct!")
    player_two_score += 1
    print(f"Player {starting_player} score =  {starting_player_score}/5 .")
    print(f"Other player score ={player_two_score}/5.")
else:
    print("Incorrect.")
    starting_player_score +=0
    print(f"Player {starting_player} score =  {starting_player_score}/5 .")
    print(f"Other player score = {player_two_score}/5.")

#QUESTION THREE
question_three_user_answer = input("Who is the president of South Africa? Give one name only.\n")

if question_three_user_answer == "cyril" or question_three_user_answer == "ramaphosa":
    print("Correct!")
    starting_player_score += 1
    print(f"Player {starting_player} score =  {starting_player_score}/5 .")
    print(f"Other player score = {player_two_score}/5.")
else:
    print("Incorrect.")
    starting_player_score +=0
    print(f"Player {starting_player} score =  {starting_player_score}/5 .")
    print(f"Other player score = {player_two_score}/5.")

#QUESTION FOUR
question_four_user_answer = input("Which colour is not found on the Kenyan flag? Red, Yellow or Green.\n")


if question_four_user_answer == "yellow":
    print("Correct!")
    player_two_score += 1
    print(f"Player {starting_player} score =  {starting_player_score}/5 .")
    print(f"Other player score = {player_two_score}/5.")
else:
    print("Incorrect.")
    starting_player_score +=0
    print(f"Player {starting_player} score =  {starting_player_score}/5 .")
    print(f"Other player score = {player_two_score}/5.")

#QUESTION FIVE
question_five_user_answer = input("Which African country is not landlocked? Mali, Burundi or Somalia.\n")

if question_five_user_answer == "somalia":
    print("Correct!")
    starting_player_score += 1
    print(f"Player {starting_player} score =  {starting_player_score}/5 .")
    print(f"Other player score ={player_two_score}/5.")
else:
    print("Incorrect.")
    player_two_score +=0
    print(f"Player {starting_player} score =  {starting_player_score}/5 .")
    print(f"Other player score = {player_two_score}/5.")

if starting_player_score > player_two_score:
    print(f"Player {starting_player} wins!")
elif starting_player_score == player_two_score:
    print("It's a tie!")
else:
    print(f"{starting_player} loses, other player wins!")