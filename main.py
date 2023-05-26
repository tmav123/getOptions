import robin_stocks.robinhood as robin
import config
import json
import pandas as pd


def main():
    login = robin.login(config.username, config.password)

    t_list=['SPY', 'AAPL', 'NVDA', 'MSFT', 'GOOGL']


    for ticker in t_list:
        z = {'yes': '08461'}
        json_obj = json.dumps(z, indent=4)

        with open(ticker+'_'+'call'+".json", "w") as outfile:
            outfile.write(json_obj)

        with open(ticker+'_'+'put'+".json", "w") as outfile:
            outfile.write(json_obj)

        get_ladder_data(ticker)



def write_to_json(data, ticker, type):
    j  = json.dumps(data,indent=4)
    with open(ticker+'_'+type+'.json', 'a') as f:
        f.write(j)
        f.write('\n')

def get_ladder_data(ticker):
    x = robin.get_chains(ticker)
    for date in x['expiration_dates']:
        data = robin.find_options_by_expiration(ticker, date, optionType='call')
        write_to_json(data, ticker, 'call')

    for date in x['expiration_dates']:
        data = robin.find_options_by_expiration(ticker, date, optionType='put')
        write_to_json(data, ticker, 'put')

if __name__ == "__main__":
    main()
