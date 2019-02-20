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
balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12.0
monthlyPaymentLowerBound = balance/12
monthlyPaymentUpperBound = (balance*(1+monthlyInterestRate)**12)/12.0
tol = 0.2

def calculate_unpaid_balance(payment, prev_balance):
    return prev_balance - payment

def calculate_new_balance(unpaid_balance, interest_rate):
    return round(unpaid_balance * (1 + interest_rate),2)


def calculate_fixed_monthly_payment(outstanding_amount, tenure_in_months, monthly_interest_rate, ub, lb, tol):
    
    lowest_payment_amount = (lb + ub)/2
    current_outstanding_amount = outstanding_amount
    new_outstanding_amount = outstanding_amount

    for _ in range(tenure_in_months):
        current_outstanding_amount = calculate_unpaid_balance(lowest_payment_amount, new_outstanding_amount)
        new_outstanding_amount = calculate_new_balance(current_outstanding_amount, monthly_interest_rate)
        
    if abs(new_outstanding_amount) <= tol:
        return lowest_payment_amount
    elif new_outstanding_amount < -tol:
        ub = lowest_payment_amount
        return calculate_fixed_monthly_payment(outstanding_amount, tenure_in_months, monthly_interest_rate, ub, lb, tol)
    elif new_outstanding_amount > tol:
        lb = lowest_payment_amount
        return calculate_fixed_monthly_payment(outstanding_amount, tenure_in_months, monthly_interest_rate, ub, lb, tol)




emi = calculate_fixed_monthly_payment(balance, 12, monthlyInterestRate, monthlyPaymentUpperBound, monthlyPaymentLowerBound, tol)
print("Lowest Payment: {0}".format(round(emi,2)))