#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Game board 
# Choose Player 1 or 2 
# Player Chooses where to place X and O
# Display new output 
# Check winner 
# Ask user if they want to keep playing 


# In[2]:


from IPython.display import clear_output


# In[3]:


def printboard(boardlist) : 
    clear_output()
    print (boardlist[0] + " | " + boardlist[1] + " | " + boardlist[2])
    print ("- - - - -")
    print (boardlist[3] + " | " + boardlist[4] + " | " + boardlist[5])
    print ("- - - - -")
    print (boardlist[6] + " | " + boardlist[7] + " | " + boardlist[8])


# In[4]:


def player_input():
    desired_range =[str(num) for num in range (1,10)] 
    while True :
        playerinput = input("Please input a number from 1-9: ") 
        if playerinput in desired_range and playerinput.isdigit(): 
            accepted_input = int(playerinput)
            return accepted_input
        else : 
            print ("\nError: Invalid Range")


# In[5]:


def checkwin(currentgame,mark) : 
    if mark == currentgame[0] and mark == currentgame[1] and mark == currentgame[2] or mark == currentgame[3] and mark == currentgame[4] and mark == currentgame[5] or mark == currentgame[6] and mark == currentgame[7] and mark == currentgame[8] or mark == currentgame[0] and mark == currentgame[3] and mark == currentgame[6] or mark == currentgame[1] and mark == currentgame[4] and mark == currentgame[7] or mark == currentgame[2] and mark == currentgame[5] and mark == currentgame[8] or mark == currentgame[0] and mark == currentgame[4] and mark == currentgame[8] or mark == currentgame[2] and mark == currentgame[4] and mark == currentgame[6] :
        winner = True 
    else :
        winner = False 
    return winner     


# In[6]:


def checkdraw(currentgame) : 
    if (currentgame[0] == "X" or currentgame[0] == "O") and (currentgame[1] == "X" or currentgame[1] == "O") and (currentgame[2] == "X" or currentgame[2] == "O") and (currentgame[3] == "X" or currentgame[3] == "O") and (currentgame[4] == "X" or currentgame[4] == "O") and (currentgame[5] == "X" or currentgame[5] == "O") and (currentgame[6] == "X" or currentgame[6] == "O") and (currentgame[7] == "X" or  currentgame[7] == "O") and (currentgame[8] == "X" or currentgame[8] == "O"):
        draw = True 
    else :
        draw = False 
    return draw   


# In[7]:


def players() : 
    player1 = input("Please input the name of player1: ")
    player2 = input("Please input the name of player2: ")
    players= (player1,player2)
    return players


# In[8]:


def stop_playing () : 
    while True : 
    #Ask player if they would like to continue playing or stop playing 
        player_input = input("Would you like to continue playing? 'Y' or 'N': ")
    #If player wants to continue playing return false 
        if player_input.upper() == 'Y' : 
            return False 
    #If player wants to stop playing return true  
        elif player_input.upper() == 'N' : 
            return True 
        else :  
            print("ERROR: Invalid input\nPlease select either 'Y' or 'N'")
    


# In[9]:


#Take the current boardlist, letter and the index the player wants to replace and return the new board list 
def replacement (boardlist, letter) :
    while True :
        index = player_input()
        if boardlist[index-1] == " " :
            boardlist[index-1] = letter
            return boardlist
        else : 
            print("\nBox already taken, please choose another box")


# In[10]:


#TIC TAC TOE Game 

#Display Welcome to the game 
#Flush = True makes sure that the statement is printed out first 
print ("Welcome to the Tic Tac Toe Game\n",flush = True)

#Assign names for player 1 and 2 
player1,player2 = players()


#Print out the empty board
boardlist = [" "," "," "," "," "," "," "," "," "," "]
printboard(boardlist)
letter = "X"
#Game starts 
while True :
    #Player inputs a placement point 
    #The new board starts printing 
    newboardlist = replacement(boardlist, letter)
    printboard(newboardlist)
    winner = checkwin(newboardlist,letter) 
    draw = checkdraw(newboardlist)
    if winner == True : 
        if letter == "X" : 
            print (f"{player1} has won")
        else :
            print (f"{player2} has won")
        break
    elif draw == True : 
        print("Game is a draw")
        break
    else :
        stop_game = stop_playing ()
        if stop_game == True : 
            print("Thank you for playing")
            break 
        else :    
        #Continue the game
            if letter == "X" : 
                letter = "O"
            else : 
                letter = "X"
        continue 


# 
