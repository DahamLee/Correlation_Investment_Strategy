import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker

"""
## Rolling Window Function Between Two Assets
"""


def rolling_window(arg1, arg2, dataframe_log_returns, window_size):
    if arg1.upper() and arg2.upper() in dataframe_log_returns.columns:
        return dataframe_log_returns[arg1.upper()].rolling(window=window_size).corr(dataframe_log_returns[arg2.upper()])
    else:
        raise ValueError("please check arguments' name")


"""
## Correlation Matrix From Start date to End date

* end_date 미입력시 오늘날짜까지 산출
"""


def corr_matrix_date_to_date(dataframe_log_returns, start_date, end_date=None):
    if end_date == None:
        end = pd.to_datetime(pd.datetime.today().date())
    else:
        temp_end = str(end_date)
        end = pd.datetime(int(temp_end[:4]), int(temp_end[4:6]), int(temp_end[6:]))
    temp_start = str(start_date)
    start = pd.datetime(int(temp_start[:4]), int(temp_start[4:6]), int(temp_start[6:]))
    return dataframe_log_returns.loc[start:end].dropna(axis=1, how='any').corr()


"""
## Correlation Matrix From Start date during Window period

* find accessible date (within 2 days) because if I chose weekend there is no index
* starting from the input date until the number of rows is counted to shift_period
"""


def corr_matrix_window(dataframe_log_returns, start_date, shift_period):
    index_numbering = {dataframe_log_returns.index[i]: i for i in range(len(dataframe_log_returns))}
    temp_start = str(start_date)
    start = pd.datetime(int(temp_start[:4]), int(temp_start[4:6]), int(temp_start[6:]))
    accessible_start_date = dataframe_log_returns.loc[start:start + datetime.timedelta(4)].index[0]
    accessible_start_date_index = index_numbering[accessible_start_date]
    return dataframe_log_returns.iloc[accessible_start_date_index:accessible_start_date_index + shift_period].corr()


"""
## Rank of Correlations from All stocks
"""


def rank_corr_from_all_stocks(dataframe_cov_matrix):
    idx = []
    vals = []
    for ix, i in enumerate(dataframe_cov_matrix.columns.values):
        for j in dataframe_cov_matrix.columns.values[ix + 1:]:
            idx.append((i, j))
            vals.append(dataframe_cov_matrix[i][j])

    return pd.Series(data=vals, index=idx).sort_values(ascending=False)


"""
## Rank of Correlations comparing to specific stock
"""


def rank_corr_from_one_stock(dataframe_cov_matrix, arg1):
    idx = []
    vals = []
    for i in dataframe_cov_matrix.columns.values:
        idx.append(i)
        vals.append(dataframe_cov_matrix[arg1][i])
    return pd.Series(data=vals, index=idx).sort_values(ascending=False)[1:]


"""
## Real Return after specific period

* find accessible date (within 2 days) because if I chose weekend there is no index
* starting from the input date until the number of rows is counted to shift_period
"""


def real_return_of_portfolio(dataframe_stock_prices, start_date, shift_period, stock1, stock2, portfolio_weight):
    '''date handling'''
    index_numbering = {dataframe_stock_prices.index[i]: i for i in range(len(dataframe_stock_prices))}
    temp_start = str(start_date)
    start = pd.datetime(int(temp_start[:4]), int(temp_start[4:6]), int(temp_start[6:]))
    accessible_start_date = dataframe_stock_prices.loc[start:start + datetime.timedelta(2)].index[0]
    accessible_start_date_index = index_numbering[accessible_start_date]
    end_date = dataframe_stock_prices.iloc[accessible_start_date_index + shift_period].name
    new_dataframe = dataframe_stock_prices.iloc[accessible_start_date_index:accessible_start_date_index + shift_period]

    '''calculate 2 stocks' return'''
    stock1_return = (new_dataframe[stock1][-1] - new_dataframe[stock1][0]) / new_dataframe[stock1][0]
    stock2_return = (new_dataframe[stock2][-1] - new_dataframe[stock2][0]) / new_dataframe[stock2][0]

    '''2 stock portfolio return'''
    portfolio_return = portfolio_weight * stock1_return + (1 - portfolio_weight) * stock2_return
    return '{} 부터 {} 까지 "{}" 일 동안\n' \
           '{}의 수익률: {:04.2f} %\n' \
           '{}의 수익률: {:04.2f} %\n' \
           '포트폴리오의 수익률: {:04.2f} %'.format(accessible_start_date.date(), end_date.date(), shift_period,
                                           stock1, stock1_return * 100,
                                           stock2, stock2_return * 100,
                                           portfolio_return * 100)


"""
## 데이터가이드에서 받은 raw_data 가공
"""


def refine_data(raw_dataframe):
    df = raw_dataframe[8:]
    df.columns = df.iloc[0].str.upper()
    df = df.drop(['Symbol Name', 'Kind', 'Item', 'Item Name', 'Frequency'])
    return df
