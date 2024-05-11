winning_num=45
print("your number of guesses is 5 so please play attentively")
def game():
    i=5
    while (i):
        input_num= int(input("guess number between 1 to 100: "))
        if (winning_num>input_num):
            print("your input number is too low,please input high number")
            i=i-1
            print("try again",i,"no of guesses left")
        elif(winning_num<input_num):
            print("your input number is too high,please inpuit low number")
            i = i-1
            print("try again",i,"no of guesses left")
        else:
            i=i-1
            print("you win ! , congratulation","win in",i,"no of guesses",winning_num)
            break
    if i>5:
        print("game over")
game()
print("Do you want to play again game type [y/n]: ")
ans = input("type: ")
if ans == "y":
    game()
else:
    print("thanks for playing this game")
