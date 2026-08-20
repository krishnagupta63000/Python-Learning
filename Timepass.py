# sum = 0
# n = int(input("Enter Num: "))
# while (n!=1):
#     n = int(input("Enter Num: "))
#     if(n!=1):
#         sum+=n
#         print(sum)
#     else:
#         sum+=n
#         print(sum-1)

#mini calculator->
# n1 = int(input("Enter first num: "))
# opp = input("Enter Operator: ")
# n2 = int(input("Enter Second num: "))
# if(opp == "+"):
#     print("sum:", n1 + n2 )
# elif(opp == "-"):
#     print("diffrence: ", n1 - n2)
# elif(opp== "/"):
#     print("division: ", n1/n2)
# elif(opp == "*"):
#     print("Multiplication: ", n1*n2)
# else:
#     print("Invalid Operator")


import random
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
print("🎮 ROCK PAPER SCISSORS")
print("-----------------------")
while True:
    player = input("\nChoose rock, paper, scissors (or quit): ").lower()
    if player == "quit":
        break
    if player not in choices:
        print("❌ Invalid choice! Try again.")
        continue
    computer = random.choice(choices)
    print("You chose:", player)
    print("Computer chose:", computer)
    if player == computer:
        print("🤝 It's a draw!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("🎉 You win!")
        player_score += 1
    else:
        print("💀 Computer wins!")
        computer_score += 1
    print(f"Score → You: {player_score} | Computer: {computer_score}")
print("\n🏁 GAME OVER")
print(f"Final Score → You: {player_score} | Computer: {computer_score}")
print("Thanks for playing! 😎")