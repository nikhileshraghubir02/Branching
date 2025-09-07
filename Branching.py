rate_for_first_1000 = 7.633
rate_over_1000 = 9.259

kw_hours_used = int(input("Enter the number of KW hours used: "))

if kw_hours_used <= 1000:
    amount_of_cents = kw_hours_used * rate_for_first_1000
else:
    amount_of_cents = (rate_for_first_1000 * 1000) + ((kw_hours_used - 1000) * rate_over_1000)

total_amount_of_dollars = amount_of_cents / 100

print(f"Amount owed is ${total_amount_of_dollars:.2f}")