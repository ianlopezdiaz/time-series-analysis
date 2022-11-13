import numpy as np
import pandas as pd
from tvDatafeed import TvDatafeed,Interval

import datetime
from dateutil.relativedelta import relativedelta
from calendar import monthrange
import re

def date_from_string(string):
    if type(string) == str:
        if string.lower() == 'today':
            date = pd.to_datetime('today')
            return pd.to_datetime(datetime.date(year=date.year, month=date.month, day=date.day))
        elif '-' in string or '/' in string:
            date = re.split('[-/]', string)
            month = int(date[1])
            if len(date[0])==4:
                year = int(date[0])
                day = int(date[2])
            else:
                year = int(date[2])
                day = int(date[0])
            return pd.to_datetime(datetime.date(year=year, month=month, day=day))
        else:
            raise ValueError('string should be a date in one of the following formats: yyyy-mm-dd, yyyy/mm/dd, dd/mm/yyyy or dd-mm-yyyy')
    elif type(string) in (datetime.datetime, datetime.date, pd._libs.tslibs.timestamps.Timestamp):
        return pd.to_datetime(datetime.date(year=string.year, month=string.month, day=string.day))
    else:
        raise TypeError('string should be type str, datetime.date, datetime.datetime or pandas._libs.tslibs.timestamps.Timestamp')

def tradingview_get_hist(**kwargs):
    ticker = kwargs.get('ticker')
    exchange = kwargs.get('exchange')
    verbose = kwargs.get('verbose', False)
    tv=TvDatafeed()
    if verbose:
        print(f'Downloading {ticker} from TradingView:{exchange}...')
    return tv.get_hist(symbol=ticker, exchange=exchange, interval=Interval.in_daily, n_bars=5000)


url_bacen = {}
#12 	CDI 	% a.d. 	D 	06/03/1986 	25/08/2020 	Cetip 	N 	Visualizar metadados
url_bacen['CDI'] = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json'
#7478 	IPCA - 15 	Var. % mensal 	M 	31/05/2000 	ago/2020 	IBGE 	N 	Visualizar metadados
url_bacen['IPCA'] = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.7478/dados?formato=json'
#189 	Índice geral de preços do mercado (IGP-M) 	Var. % mensal 	M 	30/06/1989 	jul/2020 	FGV 	N 	Visualizar metadados
url_bacen['IGPM'] = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.189/dados?formato=json'
#192 	Índice nacional de custo da construção (INCC) 	Var. % mensal 	M 	29/02/1944 	jul/2020 	FGV 	N 	Visualizar metadados
url_bacen['INCC'] = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.192/dados?formato=json'
#225 	Índice de preços ao produtor amplo (IPA) 	Var. % mensal 	M 	29/02/1944 	jul/2020 	FGV 	N 	Visualizar metadados
url_bacen['IPA'] = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.225/dados?formato=json'


for k,v in url_bacen.items():
    df = pd.read_json(v)
    df['data'] = [date_from_string(d) for d in df['data']]
    df.to_csv(f'bacen/{k}.csv')


stock = {}
stock['IBOV'] = {'ticker':'IBOV', 'exchange':'INDEX', 'verbose':True}
stock['USDBRL'] = {'ticker':'USDBRL', 'exchange':'VANTAGE', 'verbose':True}
stock['BTCUSD'] = {'ticker':'BTCUSD', 'exchange':'INDEX', 'verbose':True}
stock['VT'] = {'ticker':'VT', 'exchange':'AMEX', 'verbose':True}
stock['VTI'] = {'ticker':'VTI', 'exchange':'AMEX', 'verbose':True}
stock['VXUS'] = {'ticker':'VXUS', 'exchange':'NASDAQ', 'verbose':True}

for k,v in stock.items():
    df = tradingview_get_hist(**v)
    df.to_csv(f'stocks/{k}.csv')

