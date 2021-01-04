import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

"""
Crypto Currency Manager

"""

#API call
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
url_end = "?structure=array&convert=USD"
parameters = {
  'limit':"10",
  'convert':'USD'
}
#API key for successful call
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '$$KEY$$',
}

session = Session()
session.headers.update(headers)

#Execute if API call is successful 
try:
    #Get requested API
    response = session.get(url, params=parameters)

    print()
    print("MY PORTFOLIO")
    print()

    #Instantiate portfolio value as a float
    my_portfolio = 0.00

    #How recent the data is
    last_updated = 0

    #Adding in table labels
    table = PrettyTable(["Asset","Amount Owned","Price","1h","24h","7d","Last Updated"])
    portfolio_path = "$PATH_TO_PORTFOLIO_DATA"
    with open(portfolio_path,"r") as file:
        for line in file:
            symbol, amount = line.split()
            #API call for each piece of data to utilize in the prettytable
            symbol_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=" +symbol
        
            request = session.get(symbol_url)
            request_results = request.json()

            #print(json.dumps(request_results,sort_keys=True,indent=4))

            #Get all the data
            currency_data = request_results["data"][symbol]
            currency_name = currency_data["name"]
            currency_last_updated = currency_data["last_updated"]
            currency_symbol = currency_data["symbol"]
            quote = currency_data["quote"]["USD"]
            currency_1h_change = quote["percent_change_1h"]
            currency_24h_change = quote["percent_change_24h"]
            currency_7d_change = quote["percent_change_7d"]
            currency_price = quote["price"]

            #Color terminal data in the table based off positive or negative vals
            if currency_1h_change > 0:
                currency_1h_change = Back.GREEN + str(currency_1h_change) + "%" + Style.RESET_ALL
            else:
                currency_1h_change = Back.RED + str(currency_1h_change) + "%" + Style.RESET_ALL

            if currency_24h_change > 0:
                currency_24h_change = Back.GREEN + str(currency_24h_change) + "%" + Style.RESET_ALL
            else:
                currency_24h_change = Back.RED + str(currency_24h_change) + "%" + Style.RESET_ALL
            
            if currency_7d_change > 0:
                currency_7d_change = Back.GREEN + str(currency_7d_change) + "%" + Style.RESET_ALL
            else:
                currency_7d_change = Back.RED + str(currency_7d_change) + "%" + Style.RESET_ALL

            value_of_asset = float(currency_price) * float(amount)

            my_portfolio += value_of_asset

            value_str = "{:,}".format(round(value_of_asset,2))

            table.add_row([currency_name + " (" + currency_symbol + ")",
                        "$" + str(value_of_asset),
                        "$" +str(currency_price),
                        str(currency_1h_change)+" %",
                        str(currency_24h_change)+" %",
                        str(currency_7d_change)+" %",
                        str(currency_last_updated)])
    print(table)
    print()

    portfolio_val_str = "{:,}".format(round(my_portfolio,2))

    print("Total portfolio value is {} ${}{}".format(Back.GREEN,portfolio_val_str,Style.RESET_ALL))


#print error if API call is unsuccessful
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)