'''2. The Restaurant Bill Splitter

The Goal: 
Calculate how much each person owes, including a tax and a custom tip percentage.

Concepts:  functions ,  default values ,  list .

The Problem: 
Write a function  split_bill(items_prices, people, tax=0.05, tip=0.10) . 
items_prices  will be a List of decimals (floats).

Input: A list like  [25.0, 15.0, 10.0]  and an integer for  people .

Output: A single float (the amount per person).

Hint:
Expected Flow: Calculate  sum()  of the list Add tax and tip amounts Divide the grand total by people return the result.'''



def split_bill(items_prices, people, tax=0.05, tip=0.10):

    total =0;
    for i in items_prices:
        total += i;
    print(total);
    print(total*tax/100);

    total_bill = (((total*tax)* tip)/people);

    return total_bill;


 

    





print("Amount per person to be paid is: ", split_bill([25.0, 15.0, 10.0], 3));
