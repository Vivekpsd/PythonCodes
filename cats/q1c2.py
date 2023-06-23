def swap_dictionary_elements(dictionary, key1, key2):
    temp = dictionary[key1]
    dictionary[key1] = dictionary[key2]
    dictionary[key2] = temp

# Creating the country-capital dictionary
country_capital = {
    "India": "New Delhi",
    "United States": "Washington, D.C.",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Australia": "Canberra"
}

# Displaying the original dictionary
print("Original Dictionary:")
for country, capital in country_capital.items():
    print(country, "->", capital)

# Swapping elements based on key values
key_to_swap1 = "India"
key_to_swap2 = "France"
swap_dictionary_elements(country_capital, key_to_swap1, key_to_swap2)

# Displaying the modified dictionary
print("\nModified Dictionary:")
for country, capital in country_capital.items():
    print(country, "->", capital)
