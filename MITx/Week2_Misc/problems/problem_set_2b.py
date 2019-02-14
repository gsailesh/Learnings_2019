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
balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0


def calculate_unpaid_balance(payment, prev_balance):
    return prev_balance - payment

def calculate_new_balance(unpaid_balance, interest_rate):
    return round(unpaid_balance * (1 + interest_rate),2)


def calculate_fixed_monthly_payment(outstanding_amount, tenure_in_months, monthly_interest_rate, base_amount=10):
    # return monthly_min_payment_rate * prev_balance
    lowest_payment_amount = base_amount
    current_outstanding_amount = outstanding_amount
    new_outstanding_amount = outstanding_amount

    for _ in range(tenure_in_months):
        current_outstanding_amount = calculate_unpaid_balance(lowest_payment_amount, new_outstanding_amount)
        new_outstanding_amount = calculate_new_balance(current_outstanding_amount, monthly_interest_rate)

    if new_outstanding_amount <= 0:
        return lowest_payment_amount
    else:
        lowest_payment_amount += 10
        return calculate_fixed_monthly_payment(outstanding_amount, tenure_in_months, monthly_interest_rate, lowest_payment_amount)



emi = calculate_fixed_monthly_payment(balance, 12, monthlyInterestRate, 10)
print("Lowest Payment: {0}".format(emi))