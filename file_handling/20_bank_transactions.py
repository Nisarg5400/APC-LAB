with open("transactions.txt", "w") as f:
    f.write("deposit,5000\n")
    f.write("withdraw,2000\n")
    f.write("deposit,3000\n")
    f.write("withdraw,1000\n")

total_deposit = 0
total_withdraw = 0
largest = 0

with open("transactions.txt", "r") as f:
    for line in f:
        t_type, amount = line.strip().split(",")
        amount = float(amount)
        if t_type == "deposit":
            total_deposit += amount
        else:
            total_withdraw += amount
        if amount > largest:
            largest = amount

balance = total_deposit - total_withdraw

print("Total deposits:", total_deposit)
print("Total withdrawals:", total_withdraw)
print("Final balance:", balance)
print("Largest transaction:", largest)
