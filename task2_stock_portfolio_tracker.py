# Stock Portfolio Tracker

# Dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 145
}

total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")

# Number of stocks user wants to enter
num_stocks = int(input("How many stocks do you want to add? "))

# Loop for stock input
for i in range(num_stocks):

    stock_name = input("\nEnter stock symbol: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity

        total_investment += investment

        print(f"✅ {stock_name} added successfully.")
        print(f"Investment in {stock_name}: ${investment}")

    else:
        print("❌ Stock not found in database.")

# Final output
print("\n📊 Total Investment Value: $", total_investment)

# Optional: Save result in a text file
save = input("\nDo you want to save the result in a file? (yes/no): ").lower()

if save == "yes":

    file = open("portfolio.txt", "w")

    file.write(f"Total Investment Value: ${total_investment}")

    file.close()

    print("✅ Result saved in portfolio.txt")

else:
    print("👍 Result not saved.")
