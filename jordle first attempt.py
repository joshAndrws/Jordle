word_list_wrong = ['troot','union','barbaque','desise','gulubal','pinisulas','upstait','kuntuky','greatfull','Quite ']
word_list_right = ['trout','onion','barbeque','disease','gullible','peninsulas','upstate','kentucky','grateful','Quiet']
user_list_rightmaybey = []
userinput = ''
userscore = 0
storeright = []
print("WELCOME TO JODLEEEEEEEEEE!!!!!!!!!!!!!!!!!!!!!")

print("today you will attempt to spell 10 words and see if you know how to spell htem corectly")
print("the twist is that of course all the wrods were spelled by the one the only jooshhhhhhhhhh")
print("best of luck and may the best man win")

for i in range(len(word_list_right)):
    userinput = ''
    print(f"the {i+1}'st word to spell is: {word_list_right[i]}")
    userinput = input()
    user_list_rightmaybey.append(userinput)

for i in range(len(word_list_right)):
    if word_list_wrong[i] == user_list_rightmaybey[i]:
        userscore = userscore + 1
        storeright.append(user_list_rightmaybey[i])

print(f"Congrats on completing the game your score was: {userscore}!")
print(f"you spelled the words: {storeright} ,Corect!")

input("\nPress Enter to exit...")
    
    

    
    
