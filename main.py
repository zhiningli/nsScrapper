import src.api as api

XR = api.get_exchange_rate()
prices_info = api.get_prices_multiple_regions("Zelda")

converted_prices_info = api.convert_prices_to_USD(prices_info, XR)
# Print table header
header_titles = ['Game Title', 'Region', 'Game ID', 'Original Price', 'USD Price']
header = "|".join(title.center(50) for title in header_titles)
print(header)
print("-" * len(header))  # Print a line to separate header from rows

# Print each row of the table
for price_info in converted_prices_info:
    # Ensure price_info has enough elements
    if len(price_info) >= 5:
        # Access each element of price_info by its index
        row = "|".join(str(price_info[index]).center(50) for index in range(5))
        print(row)
        print("\n")  # Additional newline for spacing; remove if not needed
    else:
        print("Incomplete price information")
