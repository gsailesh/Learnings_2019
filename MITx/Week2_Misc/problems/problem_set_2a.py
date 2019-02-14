'''
Problem set 2
-------------

Say you've made a $5,000 purchase on a credit card with an 18% annual interest rate and a 2% minimum monthly payment rate. 
If you only pay the minimum monthly amount for a year, how much is the remaining balance?

b_i: balance at month i
p_i: payment at month i
ub_i: unpaid balance at month i
r: annual rate of interest

ub_i = b_i - p_i

b_2 = ub_1 + (r/12.0 * ub_1)

---------------------------------

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 


'''
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12.0


def calculate_min_monthly_payment(prev_balance, monthly_min_payment_rate):
    return monthly_min_payment_rate * prev_balance

def calculate_unpaid_balance(payment, prev_balance):
    return prev_balance - payment

def calculate_new_balance(unpaid_balance, interest_rate):
    return round(unpaid_balance * (1 + interest_rate),2)

remaining_balance = int(balance)

for month in range(12):
    payment = calculate_min_monthly_payment(balance, monthlyPaymentRate)
    remaining_balance = calculate_unpaid_balance(payment, balance)
    balance = calculate_new_balance(remaining_balance, monthlyInterestRate)

    # print("Month {0} Remaining balance: {1}".format(month+1, balance))
print("Remaining balance: {0}".format(balance))