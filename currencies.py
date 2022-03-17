# Data and functions related to the currencies supported by CurrEx

# Supported currencies (Code, Name)
currencies = [
	['EUR', 'Euro Member Countries'],
	['IDR', 'Indonesia Rupiah'],
	['BGN', 'Bulgaria Lev'],
	['ILS', 'Israel Shekel'],
	['GBP', 'United Kingdom Pound'],
	['DKK', 'Denmark Krone'],
	['CAD', 'Canada Dollar'],
	['JPY', 'Japan Yen'],
	['HUF', 'Hungary Forint'],
	['RON', 'Romania New Leu'],
	['MYR', 'Malaysia Ringgit'],
	['SEK', 'Sweden Krona'],
	['SGD', 'Singapore Dollar'],
	['HKD', 'Hong Kong Dollar'],
	['AUD', 'Australia Dollar'],
	['CHF', 'Switzerland Franc'],
	['KRW', 'Korea (South) Won'],
	['CNY', 'China Yuan Renminbi'],
	['TRY', 'Turkey Lira'],
	['HRK', 'Croatia Kuna'],
	['NZD', 'New Zealand Dollar'],
	['THB', 'Thailand Baht'],
	['USD', 'United States Dollar'],
	['NOK', 'Norway Krone'],
	['RUB', 'Russia Ruble'],
	['INR', 'India Rupee'],
	['MXN', 'Mexico Peso'],
	['CZK', 'Czech Republic Koruna'],
	['BRL', 'Brazil Real'],
	['PLN', 'Poland Zloty'],
	['PHP', 'Philippines Peso'],
	['ZAR', 'South Africa Rand']
];

# Prints the list of supported currencies
def printCurrencies():
	for rows in currencies:
		print("%s (%s)" %(rows[1], rows[0]));