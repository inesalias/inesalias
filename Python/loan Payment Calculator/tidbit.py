
# Ask the user for the purchase price
purchase_price = float(input("Enter the purchase price: "))

# Calculate the down payment (10% of purchase price)
down_payment = purchase_price * 0.10

# Print the down payment
print(f"Down Payment (10%): ${down_payment:.2f}")

# The starting balance is the purchase price minus the down payment
initial_balance = purchase_price - down_payment

# Print the initial balance
print(f"Initial Balance: ${initial_balance:.2f}")   

# Monthly payment is 5% of the purchase price
monthly_payment = initial_balance * 0.05

# Print the monthly payment
print(f"Monthly Payment (5% of purchase price): ${monthly_payment:.2f}")

# Print table headers
print("\nMonth\tBalance\t\tInterest\tPrincipal\tPayment\tRemaining Balance")

# Start with month 1 and the initial balance
month = 1
balance = initial_balance

# Loop until the balance is paid off
while balance > 0:
    # Monthly interest (balance * annual rate / 12)
    interest = balance * 0.12 / 12

    # Principal is the part of the payment that goes toward reducing the balance
    principal = monthly_payment

    # If the principal is more than the balance (final payment), adjust it
    if principal > balance:
        principal = balance
        payment = principal + interest
    else:
        payment = monthly_payment + interest

    # Calculate remaining balance
    remaining_balance = balance - principal

    # Print row for this month
    print(month, "\t",
          round(balance, 2), "\t",
          round(interest, 2), "\t\t",
          round(principal, 2), "\t",
          round(payment, 2), "\t",
          round(remaining_balance, 2))

    # Move to the next month
    balance = remaining_balance
    month += 1
