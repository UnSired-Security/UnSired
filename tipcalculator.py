print("Welcomee to our Restaurant...  ")
print("How much is your total ?   ")
purchase_price = float(input("$   "))
print("What kind of payment would you be making ?   ")
print("A> Cash ")
print("B> Bank ")
payment_choice = str(input(">  ")).lower()
if payment_choice == "A " or payment_choice == "cash":
    cash = int(input("How much cash are you paying ?   "))
    tip = 0.03 * purchase_price
    print(f"We will be charging you 3 percent  of what you bought as Tip which is {tip}")
    total_cost = tip + purchase_price
    response = str(input("Are you making (A) Joint or (B) Single payment ?   ")).lower()
    if response == "A" or "Joint" or "Joint Payment ":
        tip = 0.03 * purchase_price
        print(f"We will be charging you 3 percent  of what you bought as Tip which is {tip}")
        total_cost = tip + purchase_price
        print(F"Your Total cost is {total_cost}")
        balance = cash - total_cost
    elif response == "B" or "single" or "Single payment":
        print("How many of you are paying ? ")
        nop = int(input( ))
        payment_choice = total_cost / nop
        print(f"YOU all are to pay{payment_choice } each ")
        balance = cash - total_cost
        if balance == 0:
             print("you have no ballancee")
else: payment_choice == "B" or payment_choice == "Bank"
print("Please make your Bank or EPayment to our Bank Details ")
print("Thanks for shopping with us ")
contin = str(input(" Would you like to close this bot ? YEs OR NO ")).lower()
if contin == "yes":
    print("Goodbye🙌")
else: contin == "NO"
print("Please contact the help desk to get more services BYE 😊")

