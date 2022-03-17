# Data and functions related to the currencies supported by CurrEx

class CurrencyList:

	# Dictionary of support currencies
	# Formatted as: (Code, Complete Name)
	currencies = {
		"EUR": "Euro Member Countries",
		"IDR": "Indonesia Rupiah",
		"BGN": "Bulgaria Lev",
		"ILS": "Israel Shekel",
		"GBP": "United Kingdom Pound",
		"DKK": "Denmark Krone",
		"CAD": "Canada Dollar",
		"JPY": "Japan Yen",
		"HUF": "Hungary Forint",
		"RON": "Romania New Leu",
		"MYR": "Malaysia Ringgit",
		"SEK": "Sweden Krona",
		"SGD": "Singapore Dollar",
		"HKD": "Hong Kong Dollar",
		"AUD": "Australia Dollar",
		"CHF": "Switzerland Franc",
		"KRW": "Korea (South) Won",
		"CNY": "China Yuan Renminbi",
		"TRY": "Turkey Lira",
		"HRK": "Croatia Kuna",
		"NZD": "New Zealand Dollar",
		"THB": "Thailand Baht",
		"USD": "United States Dollar",
		"NOK": "Norway Krone",
		"RUB": "Russia Ruble",
		"INR": "India Rupee",
		"MXN": "Mexico Peso",
		"CZK": "Czech Republic Koruna",
		"BRL": "Brazil Real",
		"PLN": "Poland Zloty",
		"PHP": "Philippines Peso",
		"ZAR": "South Africa Rand"
	}

	# Prints the list of supported currencies
	def print(self):
		for keys in self.currencies:
			print("%s (%s)" %(keys, self.currencies.get(keys)));

	# Return list of currencies
	def getCurrencies(self):
		return self.currencies;

	# Check if given code exists in the currencies dictionary
	# Returns true if it exists, and false otherwise
	def checkCode(self, code):
		if(self.currencies.get(code)):
			return True;
		else:
			return False;