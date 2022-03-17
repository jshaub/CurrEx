# Main runtime environment for CurrEx application
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from currencies import *

# Get references to exchanges rates and currency symbols
currencyRates = CurrencyRates();
currencyCodes = CurrencyCodes();

print("Welcome to CurrEx, the currency exchange program!");
print("Please select the base currency from the following list:");
printCurrencies();

baseCurrency = input("Enter base currency code (ex. USD): ");
exchangeCurrency = input("Enter the exchange currency code: ");
currencyAmount = float(input("Enter currency amount: "));

print("%.2f %s (%s) is %.2f %s (%s)" %(currencyAmount, baseCurrency, currencyCodes.get_symbol(baseCurrency),
	currencyRates.convert(baseCurrency, exchangeCurrency, currencyAmount), exchangeCurrency, currencyCodes.get_symbol(exchangeCurrency)));