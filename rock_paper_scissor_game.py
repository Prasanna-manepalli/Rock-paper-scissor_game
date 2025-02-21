import random
score=0
game_over=False
while not game_over:
    user_choice=input("enter your choice:0 for Rock✊,1 for paper✋,2 for scissor✌️ and press 'x' for exit:")
    if user_choice.lower()=='x':
        print(f"Your initial score is {score}")
        break #exit the loop
    if user_choice.isdigit():
        user_choice=int(user_choice)
    if user_choice not in[0,1,2]:
        print("Invalid choice! Please enter 0,1,0r 2.")
        continue
    choices=["✊","✋","✌️"]
    print(f"You choose:{choices[user_choice]}")
    computer_choice=random.randint(0,2)
    print(f"computer choose:{choices[computer_choice]}")
    if user_choice==computer_choice:
        print("it's a draw!")
    elif(user_choice==0 and computer_choice==2) or\
        (user_choice==1 and computer_choice==0) or\
        (user_choice==2 and computer_choice==1):
            score+=1
            print(f"You win! Your score:{score}")
    else:
        print(f"You lose!Your score:{score}")
        
        