import imageio
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker

from finance_programming3.finance_programming import *

# font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
# rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

raw_data1 = pd.read_excel('(2)_stock1.xlsx')
raw_data2 = pd.read_excel('(2)_stock2.xlsx')
raw_data3 = pd.read_excel('(2)_industry_index.xlsx')

df1 = refine_data(raw_data1)
df2 = refine_data(raw_data2)
df3 = refine_data(raw_data3)

"""
## 컬럼 분리 [짝수열: 주가, 홀수열: 수익률]
"""
stock_prices = df1.iloc[:, [i for i in range(0, len(df1.columns), 2)]].astype('float64')
log_returns = df1.iloc[:, [i for i in range(1, len(df1.columns), 2)]].astype('float64')

log_returns2 = df2.iloc[:, [i for i in range(1, len(df2.columns), 2)]].astype('float64')
log_returns3 = df3.iloc[:, [i for i in range(1, len(df3.columns), 2)]].astype('float64')

"""
## 함수들 모임
"""
# def rolling_window(arg1, arg2, dataframe_log_returns, window_size):
# def corr_matrix_date_to_date(dataframe_log_returns, start_date, end_date=None):
# def corr_matrix_window(dataframe_log_returns, start_date, shift_period):
# def rank_corr_from_all_stocks(dataframe_cov_matrix):
# def rank_corr_from_one_stock(dataframe_cov_matrix, arg1):
# def real_return_of_portfolio(dataframe_stock_prices, start_date, shift_period, stock1, stock2, portfolio_weight):

# 산업군별
corr_matrix_industry = corr_matrix_date_to_date(log_returns3, 20170102)
# 개별 종목별
corr_matrix_stocks = corr_matrix_date_to_date(log_returns, 20170102)
# 천안함
corr_matrix_result1 = corr_matrix_date_to_date(log_returns, 20100226, 20100326)
# # 연평도
corr_matrix_result2 = corr_matrix_date_to_date(log_returns, 20101023, 20101123)
# # 3차 핵실험
corr_matrix_result3 = corr_matrix_date_to_date(log_returns, 20130112, 20130212)
# # 4차 핵실험
corr_matrix_result4 = corr_matrix_date_to_date(log_returns, 20151206, 20160106)
# # 5차 핵실험
corr_matrix_result5 = corr_matrix_date_to_date(log_returns, 20160809, 20160909)
# # 6차 핵실험
corr_matrix_result6 = corr_matrix_date_to_date(log_returns, 20170803, 20170903)
# print(corr_matrix_result)

# rank = rank_corr_from_all_stocks(corr_matrix_industry)
# rank = rank_corr_from_all_stocks(corr_matrix_stocks)
# print(rank)
# print(rank[:10])
# print(rank[-10:])

# 천안함
# rank = rank_corr_from_one_stock(corr_matrix_result1, '한화테크윈')
# 연평도
# rank = rank_corr_from_one_stock(corr_matrix_result2, '한화테크윈')
# 3차 핵실험
# rank = rank_corr_from_one_stock(corr_matrix_result3, '한화테크윈')
# 4차 핵실험
# rank = rank_corr_from_one_stock(corr_matrix_result4, '한화테크윈')
# 5차 핵실험
# rank = rank_corr_from_one_stock(corr_matrix_result5, '한화테크윈')
# 6차 핵실험
rank = rank_corr_from_one_stock(corr_matrix_result6, '한화테크윈')
print(rank)

# 천안함
# print(real_return_of_portfolio(stock_prices, 20100326, 10, '한화테크윈', '한국토지신탁', 0.5))
# print(real_return_of_portfolio(stock_prices, 20100326, 10, '한화테크윈', '아모레퍼시픽', 0.5))
# 연평도
# print(real_return_of_portfolio(stock_prices, 20101123, 10, '한화테크윈', 'SK머티리얼즈', 0.5))
# print(real_return_of_portfolio(stock_prices, 20101123, 10, '한화테크윈', '아모레퍼시픽', 0.5))
# 3차 핵실험
# print(real_return_of_portfolio(stock_prices, 20130212, 10, '한화테크윈', 'KT&G', 0.5))
# print(real_return_of_portfolio(stock_prices, 20130212, 10, '한화테크윈', '아모레퍼시픽', 0.5))
# 4차 핵실험
# print(real_return_of_portfolio(stock_prices, 20160106, 10, '한화테크윈', 'SK텔레콤', 0.5))
# print(real_return_of_portfolio(stock_prices, 20160106, 10, '한화테크윈', '아모레퍼시픽', 0.5))
# 5차 핵실험
# print(real_return_of_portfolio(stock_prices, 20160909, 10, '한화테크윈', '한국전력', 0.5))
# print(real_return_of_portfolio(stock_prices, 20160909, 10, '한화테크윈', '아모레퍼시픽', 0.5))
# 6차 핵실험
print(real_return_of_portfolio(stock_prices, 20170903, 10, '한화테크윈', '서울반도체', 0.5))
print(real_return_of_portfolio(stock_prices, 20170903, 10, '한화테크윈', '아모레퍼시픽', 0.5))




"""
## Generating Heatmap GIF
"""
# writer = imageio.get_writer('C:/Users/daham/Desktop/gif/heatmap.gif')
# for i in range(50):
#     if i < 30:
#         start_date = int(20170102 + i)
#     else:
#         i = i - 30
#         start_date = int(20170201 + i)
#     corr_matrix_result = corr_matrix_window(log_returns2, start_date, 30)
#     fig = plt.figure(figsize=(16, 8))
#     plt.imshow(corr_matrix_result, cmap='Oranges', interpolation='none', vmin=1, vmax=-1)
#     plt.colorbar()
#     plt.xticks(range(len(corr_matrix_result)), corr_matrix_result.columns, rotation=90)
#     plt.yticks(range(len(corr_matrix_result)), corr_matrix_result.columns)
#     fig.savefig('C:/Users/daham/Desktop/gif/corr_matrix_{}.png'.format(start_date), dpi=fig.dpi)
#     plt.close()
#     image = imageio.imread('C:/Users/daham/Desktop/gif/corr_matrix_{}.png'.format(start_date))
#     writer.append_data(image)
#     print(i)
"""
## Heatmap of Correlations
"""

# plt.figure(figsize=(16, 8))
# plt.imshow(corr_matrix_stocks, cmap='Oranges', interpolation='none')
# plt.colorbar()
# plt.xticks(range(len(corr_matrix_stocks)), corr_matrix_stocks.columns, rotation=90)
# plt.yticks(range(len(corr_matrix_stocks)), corr_matrix_stocks.columns)
# plt.show()

"""
## Generating Rolling Window GIF
"""
# writer = imageio.get_writer('C:/Users/daham/Desktop/gif/rolling.gif')
# for i in range(100):
#     start_date = int(20170102 + i)
#     rolling = rolling_window('NAVER', '현대차', log_returns2, 30)
#     fig = plt.figure(figsize=(16, 8))
#     plt.plot(rolling[49:49 + i], color='r')
#     plt.axis(ymin=-1, ymax=1)
#     plt.axhline(linestyle='--', color='k', linewidth=1)
#     fig.savefig('C:/Users/daham/Desktop/gif/rolling_{}.png'.format(start_date), dpi=fig.dpi)
#     plt.close()
#     image = imageio.imread('C:/Users/daham/Desktop/gif/rolling_{}.png'.format(start_date))
#     writer.append_data(image)
#     print(i)

"""
10. matplotlib (1)
raw_data = pd.read_excel('(2)_industry_index.xlsx') 일 때,
산업군별 Correlation 하위 5개
"""

# def setup_plot(ax):
#     ax.grid(which='both')
#     ax.grid(which='major', alpha=0.1, linestyle='-')
#     ax.axhline(linestyle='--', color='k', linewidth=1)
#     ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
#     ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#
#
# window_size = 50
#
# fig = plt.figure(figsize=(10, 10))
# font = FontProperties()
# font.set_weight('bold')
# font.set_size('x-large')
# fig.suptitle('산업군별 Correlation 하위 5개 (Window {})'.format(window_size), fontproperties=font)

# ax1 = fig.add_subplot(612)
# ax2 = fig.add_subplot(613)
# ax3 = fig.add_subplot(614)
# ax4 = fig.add_subplot(615)
# ax5 = fig.add_subplot(616)
#
# ax1.set_title('음식료 및 담배 & 하드웨어')
# ax2.set_title('생활용품 & 하드웨어')
# ax3.set_title('자동차 및 부품 & 하드웨어')
# ax4.set_title('소비자 서비스 & 하드웨어')
# ax5.set_title('소비자 서비스 & 반도체')

# ax1_plot = rolling_window('음식료 및 담배', '하드웨어', window_size)[window_size:]
# ax2_plot = rolling_window('생활용품', '하드웨어', window_size)[window_size:]
# ax3_plot = rolling_window('자동차 및 부품', '하드웨어', window_size)[window_size:]
# ax4_plot = rolling_window('소비자 서비스', '하드웨어', window_size)[window_size:]
# ax5_plot = rolling_window('소비자 서비스', '반도체', window_size)[window_size:]

# ax1.plot(ax1_plot, color='r')
# ax2.plot(ax2_plot, color='k')
# ax3.plot(ax3_plot, color='g')
# ax4.plot(ax4_plot, color='b')
# ax5.plot(ax5_plot, color='c')
#
# ax1.axis(xmin=min(ax1_plot.index), xmax=max(ax1_plot.index), ymin=-1, ymax=1)
# ax2.axis(xmin=min(ax2_plot.index), xmax=max(ax2_plot.index), ymin=-1, ymax=1)
# ax3.axis(xmin=min(ax3_plot.index), xmax=max(ax3_plot.index), ymin=-1, ymax=1)
# ax4.axis(xmin=min(ax4_plot.index), xmax=max(ax4_plot.index), ymin=-1, ymax=1)
# ax5.axis(xmin=min(ax5_plot.index), xmax=max(ax5_plot.index), ymin=-1, ymax=1)
#
# setup_plot(ax1)
# setup_plot(ax2)
# setup_plot(ax3)
# setup_plot(ax4)
# setup_plot(ax5)
#
#
# plt.tight_layout()
# plt.subplots_adjust(left=0.1)
# plt.show()

"""
11. matplotlib (2)
raw_data = pd.read_excel('(2)_industry_index.xlsx') 일 때,
Window Size 별 "음식료 및 담배" & "하드웨어" Correlation 변화
"""

# def setup_plot(ax):
#     # ax.grid(True)
#     ax.grid(which='both')
#     ax.grid(which='major', alpha=0.1, linestyle='-')
#     ax.axhline(linestyle='--', color='k', linewidth=1)
#     ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
#     ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#
#
# window_size1 = 20
# window_size2 = 40
# window_size3 = 60
#
# fig = plt.figure(figsize=(10, 10))
# font = FontProperties()
# font.set_weight('bold')
# font.set_size('x-large')
# fig.suptitle('Window Size 별 "음식료 및 담배" & "하드웨어" Correlation 변화', fontproperties=font)
#
# ax1 = fig.add_subplot(412)
# ax2 = fig.add_subplot(413)
# ax3 = fig.add_subplot(414)
#
# ax1.set_title('Window Size: {}'.format(window_size1))
# ax2.set_title('Window Size: {}'.format(window_size2))
# ax3.set_title('Window Size: {}'.format(window_size3))
#
# ax1_plot = rolling_window('음식료 및 담배', '하드웨어', window_size1)[window_size1:]
# ax2_plot = rolling_window('음식료 및 담배', '하드웨어', window_size2)[window_size2:]
# ax3_plot = rolling_window('음식료 및 담배', '하드웨어', window_size3)[window_size3:]
#
# ax1.plot(ax1_plot, color='r')
# ax2.plot(ax2_plot, color='k')
# ax3.plot(ax3_plot, color='g')
#
# ax1.axis(xmin=min(ax3_plot.index), xmax=max(ax3_plot.index), ymin=-1, ymax=1)
# ax2.axis(xmin=min(ax3_plot.index), xmax=max(ax3_plot.index), ymin=-1, ymax=1)
# ax3.axis(xmin=min(ax3_plot.index), xmax=max(ax3_plot.index), ymin=-1, ymax=1)
#
# setup_plot(ax1)
# setup_plot(ax2)
# setup_plot(ax3)
#
# plt.tight_layout()
# plt.subplots_adjust(left=0.1)
# plt.show()

"""
12. matplotlib (3)
raw_data = pd.read_excel('(2)_stock1.xlsx') 일 때,
종목별 Correlation 하위 5개
"""

# def setup_plot(ax):
#     ax.grid(which='both')
#     ax.grid(which='major', alpha=0.1, linestyle='-')
#     ax.axhline(linestyle='--', color='k', linewidth=1)
#     ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
#     ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#
#
# window_size = 50
#
# fig = plt.figure(figsize=(10, 10))
# font = FontProperties()
# font.set_weight('bold')
# font.set_size('x-large')
# fig.suptitle('산업군별 Correlation 하위 5개 (Window {})'.format(window_size), fontproperties=font)
#
# ax1 = fig.add_subplot(612)
# ax2 = fig.add_subplot(613)
# ax3 = fig.add_subplot(614)
# ax4 = fig.add_subplot(615)
# ax5 = fig.add_subplot(616)
#
# ax1.set_title('SK하이닉스 & LIG넥스원')
# ax2.set_title('현대글로비스 & 삼성전자')
# ax3.set_title('현대글로비스 & SK하이닉스')
# ax4.set_title('아모레퍼시픽 & 삼성전자')
# ax5.set_title('KT&G & 삼성전자')
#
# ax1_plot = rolling_window('SK하이닉스', 'LIG넥스원', window_size)[window_size:]
# ax2_plot = rolling_window('현대글로비스', '삼성전자', window_size)[window_size:]
# ax3_plot = rolling_window('현대글로비스', 'SK하이닉스', window_size)[window_size:]
# ax4_plot = rolling_window('아모레퍼시픽', '삼성전자', window_size)[window_size:]
# ax5_plot = rolling_window('KT&G', '삼성전자', window_size)[window_size:]
#
# ax1.plot(ax1_plot, color='r')
# ax2.plot(ax2_plot, color='k')
# ax3.plot(ax3_plot, color='g')
# ax4.plot(ax4_plot, color='b')
# ax5.plot(ax5_plot, color='c')
#
# ax1.axis(xmin=min(ax1_plot.index), xmax=max(ax1_plot.index), ymin=-1, ymax=1)
# ax2.axis(xmin=min(ax2_plot.index), xmax=max(ax2_plot.index), ymin=-1, ymax=1)
# ax3.axis(xmin=min(ax3_plot.index), xmax=max(ax3_plot.index), ymin=-1, ymax=1)
# ax4.axis(xmin=min(ax4_plot.index), xmax=max(ax4_plot.index), ymin=-1, ymax=1)
# ax5.axis(xmin=min(ax5_plot.index), xmax=max(ax5_plot.index), ymin=-1, ymax=1)
#
# setup_plot(ax1)
# setup_plot(ax2)
# setup_plot(ax3)
# setup_plot(ax4)
# setup_plot(ax5)
#
# plt.tight_layout()
# plt.subplots_adjust(left=0.1)
# plt.show()

"""
13. matplotlib (4)
raw_data = pd.read_excel('(2)_stock1.xlsx') 일 때,
Window Size 별 "아모레퍼시픽" & "삼성전자" Correlation 변화
"""
#
#
# def setup_plot(ax):
#     ax.grid(which='both')
#     ax.grid(which='major', linestyle='-')
#     ax.axhline(linestyle='--', color='k', linewidth=1)
#     ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
#     ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#
#
# window_size1 = 20
# window_size2 = 40
# window_size3 = 60
#
# fig = plt.figure(figsize=(10, 10))
# font = FontProperties()
# font.set_weight('bold')
# font.set_size('x-large')
# fig.suptitle('아모레퍼시픽" & "삼성전자" Correlation 변화', fontproperties=font)
#
# ax1 = fig.add_subplot(412)
# ax2 = fig.add_subplot(413)
# ax3 = fig.add_subplot(414)
#
# ax1.set_title('Window Size: {}'.format(window_size1))
# ax2.set_title('Window Size: {}'.format(window_size2))
# ax3.set_title('Window Size: {}'.format(window_size3))
#
# ax1_plot = rolling_window('아모레퍼시픽', '삼성전자', window_size1)[window_size1:]
# ax2_plot = rolling_window('아모레퍼시픽', '삼성전자', window_size2)[window_size2:]
# ax3_plot = rolling_window('아모레퍼시픽', '삼성전자', window_size3)[window_size3:]
#
# ax1.plot(ax1_plot, color='r')
# ax2.plot(ax2_plot, color='k')
# ax3.plot(ax3_plot, color='g')
#
# ax1.axis(xmin=min(ax3_plot.index), xmax=max(ax3_plot.index), ymin=-1, ymax=1)
# ax2.axis(xmin=min(ax3_plot.index), xmax=max(ax3_plot.index), ymin=-1, ymax=1)
# ax3.axis(xmin=min(ax3_plot.index), xmax=max(ax3_plot.index), ymin=-1, ymax=1)
#
# setup_plot(ax1)
# setup_plot(ax2)
# setup_plot(ax3)
#
# plt.tight_layout()
# plt.subplots_adjust(left=0.1)
# plt.show()

"""
## Rolling Window 현대자동차 NAVER
"""

# rolling = rolling_window('NAVER', '현대차', log_returns2, 30)
# fig = plt.figure(figsize=(16, 8))
# plt.plot(rolling, color='r')
# plt.axis(ymin=-1, ymax=1)
# plt.axhline(linestyle='--', color='k', linewidth=1)
# plt.xlabel('date')
# plt.ylabel('rho')
# plt.suptitle('NAVER & 현대차 Correlation (Window: 30days)')
# plt.show()
# plt.close()

"""
## 주가 추이
"""
date = pd.datetime(2010,3,26)
# stock = stock_prices.loc[date:date + datetime.timedelta(10), ['한국토지신탁']]/stock_prices.loc[date, ['한국토지신탁']]
# benchmark = stock_prices.loc[date:date + datetime.timedelta(10), ['아모레퍼시픽']]/stock_prices.loc[date, ['아모레퍼시픽']]
# oponant = stock_prices.loc[date:date + datetime.timedelta(10), ['한화테크윈']]/stock_prices.loc[date, ['한화테크윈']]
# stock = log_returns.loc[date:date + datetime.timedelta(10), ['한국토지신탁']]
# benchmark = log_returns.loc[date:date + datetime.timedelta(10), ['아모레퍼시픽']]
# oponant = log_returns.loc[date:date + datetime.timedelta(10), ['한화테크윈']]
# fig = plt.figure(figsize=(16, 8))
# plt.plot(stock, color='b')
# plt.plot(benchmark, color='r')
# plt.plot(oponant, color='k')
# plt.grid(True)
# plt.axis(ymin=-1, ymax=1)
# plt.axhline(linestyle='--', color='k', linewidth=1)
# plt.xlabel('date')
# plt.ylabel('Nomarlized Stock Price')
# plt.suptitle('')
# plt.show()
# plt.close()
"""
14. Correlation Matrix extraction
"""

# writer = pd.ExcelWriter('C:/Users/daham/Desktop/example.xlsx', engine='xlsxwriter', datetime_format='yyyy-mm-dd')
# corr_matrix_result.to_excel(writer, encoding='utf-8')
# writer.save()
