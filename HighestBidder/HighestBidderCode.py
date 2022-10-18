from replit import clear
from art import logo

dictionary = {}
biddictionary = []

print(logo)
print("Welcome to the Secret Auction!\nThis is an easy way to decide who wins by bidding a number!")
name = input("What is your name? ")
bid = input("How much would you like to bid? ")
morepeople = input("Is anyone else bidding? Type yes or no. ")
dictionary = {name: bid}
biddictionary.append(bid) 

while morepeople == "yes":
    clear()
    print(logo)
    print("Welcome to the Secret Auction!\nThis is an easy way to decide who wins by bidding a number!")
    name = input("What is your name? ")
    bid = {input("How much would you like to bid? ")}
    morepeople = input("Is anyone else bidding? Type yes or no. ")
    dictionary.update({name: bid})
    biddictionary.append(bid)  
else:
    clear() 
    #print(biddictionary)
    maxnum = max(biddictionary)
    print("The person who won the bid is: " + dictionary[maxnum] + " with $" + maxnum)