# Main runtime environment for CurrEx application
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from currencies import CurrencyList

# Get references to exchanges rates and currency symbols
currencyRates = CurrencyRates();
currencyCodes = CurrencyCodes();
currList = CurrencyList();

validCode = False; # Boolean used to determine if entered currency code is valid

print("Welcome to CurrEx, the currency exchange program!");
print("Please select the base currency from the following list:");
currList.print();

# Get user input for base currency
baseCurrency = input("Enter base currency code (ex. USD): ");

while(not currList.checkCode(baseCurrency)):
	baseCurrency = input("Invalid code selected. Please enter a new code: ");

# Get user input for the target currenc
exchangeCurrency = input("Enter the exchange currency code: ");

while(not currList.checkCode(exchangeCurrency)):
	exchangeCurrency = input("Invalid code selected. Please enter a new code: ");

# Get user input for the amount of currency to convert
currencyAmount = float(input("Enter currency amount: "));

print("%.2f %s (%s) is %.2f %s (%s)" %(currencyAmount, baseCurrency, currencyCodes.get_symbol(baseCurrency),
	currencyRates.convert(baseCurrency, exchangeCurrency, currencyAmount), exchangeCurrency, currencyCodes.get_symbol(exchangeCurrency)));