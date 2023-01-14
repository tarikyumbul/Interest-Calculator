print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("/\/\/\ <-- Welcome to the Interest Calculator --> /\/\/\ ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print()

name = input("Please Enter Your Full Name: ") #"Full Name" because I thought this program is kind of a serious one, used by e.g. banks.

print()

print("Welcome " + name + "!")
print()
print("This program is designed to calculate Interest. By giving 3 values \nsuch as time -in terms of months, "
      "years and iteration-, amount of \nmoney and interest rate, you can easily calculate how much extra you "
      "\nare going to pay or get paid.") #Learned the command "\n" from a mobile code learning app named SoloLearn and also saw in practice session.
print()
print("To start, please enter your values below.")
print()
print()

rate = float(input("Annual Interest Rate: ")) #What Percent The Amount of Money/Loan is Going to Increase Anually / A float or an integer can be entered.
money = float(input("Amount of Money: ")) #Money/Loan Amount at the Beginning / A float or an integer can be entered.
year = int(input("Loan Term in Full Years: ")) #Number of Full Years in the Total Duration / I assume the user will enter an integer. In order to be sure, I say "Full Years"
month = int(input("Loan Term in Full Months (Without Years Above): ")) #Number of Months Left from Duration After Years are Substracted / I assume the user will enter an integer.
iteration = int(input("Iteration in Terms of Months: ")) #How Many Months There Will Be Between Each Entry's Values Such As Time, and Total and Monthly Payments / I assume the user will enter an integer.

#A little aesthetic
print()
print()
print("<———————————————————— Calculating —————————————————————>")
print()
print()
import time #I admit I have found this command on the internet but it is not a key factor, so.
time.sleep(3)


def print_full_report(loan_amount, int_rate, max_year, max_month, iteration):

    print("Interest Report for " + name)
    print()
    print("————————————————————————————")

    total_month = (max_year * 12 + max_month)

    for entry_loop in range(iteration, total_month + 1, iteration): #The Loop for Printing Different Entries According to Time. "total_month + 1" because we want the last month included.

        def print_entry(loan_amount, int_rate, month): #The Function to Print a Single Entry

                def print_duration(month): #Function to Print Different Timeframes According to Total Number of Months and Iteration
                    year1 = int(month / 12) #Number of Full Years in the Value Given By The Loop
                    month1 = int(month % 12) #Number of Full Months in the Value Given By The Loop, Years Excluded / I do not see the operator "%" in our lecture slides; so, I wanted to tell where I have found it. From the book, Page 41 / 5.1 Modulus Operator
                    print("Year: " + str(int(year1)) + " Month: " + str(month1))

                print_duration(month)


                def print_money(money):
                    print("Total Payment: " + str(int((money + (money / 100) * (int_rate / 12) * entry_loop) * 10) / 10) + "$") #To remove the decimals except for the one coming just after the dot, I multiply the value with 10, then convert it to an integer and then divide it by 10.
                    print("Monthly Payment: " + str(int((money + (money / 100) * (int_rate / 12) * entry_loop) / entry_loop * 10) / 10) + "$") #Same method used above.

                print_money(loan_amount)


                print("————————————————————————————")

        print_entry(loan_amount, int_rate, entry_loop)

print_full_report(money, rate, year, month, iteration)

#This program/code was made/written by Hasan Tarık Yumbul
#Student Identity Number: 219171247
