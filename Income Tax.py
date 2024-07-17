def main():
    income = int(input("Enter your income: "))

    if income <= 9875:
        tax = 0.1 * income
        tax_value = "10%"
    elif income <= 40125:
        tax = 987.50 + 0.12 * (income - 9875)
        tax_value = "12%"
    elif income <= 85525:
        tax = 4617.50 + 0.22 * (income - 40125)
        tax_value = "22%"
    elif income <= 163300:
        tax = 14605.50 + 0.24 * (income - 85525)
        tax_value = "24%"
    elif income <= 207350:
        tax = 33271.50 + 0.32 * (income - 163300)
        tax_value = "32%"
    elif income <= 518400:
        tax = 47367.50 + 0.35 * (income - 207350)
        tax_value = "35%"
    else:
        tax = 156235 + 0.37 * (income - 518400)
        tax_value = "37%"

    print(f"Your tax is {tax} and your tax rate is {tax_value}")


if __name__ == "__main__":
    main()
