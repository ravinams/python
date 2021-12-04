#!/usr/bin/env python

"""cachier.py: Program to purchase items and dispay items and price"""

__author__      = "Abdul"
__copyright__   = "Copyright 2021, Abdul"


#Login details for the cachier
userid="cachier"
password="hardtoguess"

#initiliaze the counter variables   
num_of_customers=0 #number of customers
total_items_purchased=0 #total number of items purchased
total_value_of_purchases=0 #total value of all purchases

"""
while(True):
    #prompt the user for login
    user_id=input("Enter your user id: ")
    if(user_id==userid):
        password=input("Enter your password: ")
        if(password==password):
            print("Login successful")
            break
        else:
            print("Incorrect password")
    else:
        print("Incorrect user id") """

while(True):
    print("\n-------")
    print(" Menu ")
    print("-------\n")
    print("1- View Details")
    print("2- Purchase")
    print("3- Logout")
    option = int(input("\nSelect an option (number) : "))
    if(option ==1):
        # print("Userid : ",userid)
        print("Number of customers : ",num_of_customers)
        print("Total items purchased : ",total_items_purchased)
        print("Total value of purchases : ",total_value_of_purchases)
    elif(option ==2):
        print("Purchase")
        items = int(input("How many items are you buying :"))
        item_prices=[]
        item_num = 0
        for item in range(items):
            item_num = item_num + 1
            item_prices.append(float(input("Enter the price of "+str(item_num)+" item :")))

        total_price = sum(item_prices)
        total_cost = total_price + total_price * 0.13 #13% tax
        print("Total cost (with 13% HST): ",total_cost)
       
        while(True):          
            cash_recieved = float(input("\nEnter the cash recieved :"))  
            cash_chnage = cash_recieved - total_cost
            if(cash_chnage < 0):
                print("Insufficient cash recieved")
            else:
                print("Cash change : ",cash_chnage)
                break
        
        total_value_of_purchases = total_value_of_purchases + total_cost
        total_items_purchased = total_items_purchased + items
        num_of_customers = num_of_customers + 1

    elif(option ==3):
        print("Logout")
        break
    else:
        print("Invalid option")

    