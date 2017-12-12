# Day_02_06_matplotlib_balance.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, colors, rc
import xlrd
from matplotlib.ticker import FuncFormatter
import pandas as pd

# 한글 사용되는 font로 변경
path = 'C:\\Windows\Fonts\malgun.ttf'
font_name = font_manager.FontProperties(fname=path).get_name()
print(font_name)
rc('font', family=font_name)

def get_data():
    wb = xlrd.open_workbook('Data/국가별수출입 실적_201711305.xls')
    print(wb)

    sheets = wb.sheets()
    print(sheets)

    sheet = sheets[0]
    print(sheet.nrows)

    # 제목 등의 6개 행 skip.

    result = []
    for row in range(6, sheet.nrows):
        #print(sheet.row_values(row))

        values = sheet.row_values(row)
        # 이름, 수출액, 수입액, 무역 수지
        country = values[1]
        outcome = int(values[3].replace(',',''))
        income = int(values[5].replace(',',''))
        balance = int(values[6].replace(',',''))

        result.append([country, outcome, income, balance])

    #print(*result, sep='\n')
    return result

# 무역수지 항목으로 정렬하고 싶다면,
result = get_data()

# print(*result[:10], sep='\n')

a = [21, 53, 12]
# print(sorted(a))
# print(sorted(a, key=lambda n: n%10))        # index 정렬 후, 위치에 맞게 재정렬

result.sort(key=lambda t: t[-1], reverse = True)
df1 = pd.DataFrame(result[:10], columns=['country', 'outcome', 'income', 'balance'])
df1.index = df1['country']

result.sort(key=lambda t: t[-1])
df2 = pd.DataFrame(result[:10], columns=['country', 'outcome', 'income', 'balance'])
df2.index = df2['country']

df3 = df1 + df2
print(df3)

# # 문제
# # 흑자 상위 10개국 막대 그래프
df1.plot(kind='bar')
plt.subplots_adjust(bottom=0.2, top=0.9)
#
# # 적자 상위 10개국 막대 그래프
plt.subplots_adjust(bottom=0.2, top=0.9)
df2.plot(kind='bar')
#
# # 흑자/적자 상위 10개국 막대 그래프
plt.show()

def draw_together(black_names, black_balances, red_names, red_balances) :
    formatter = FuncFormatter(lambda y, pos : int(y//1000))
    _, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)

    names = black_names + red_names[::-1]
    balances = black_balances + red_balances[::-1]

    index = np.arange(len(names))

    plt.bar(index, balances, color=['black'] * 10 + ['red'] * 10)
    plt.xticks(index, names, rotation='vertical')
    plt.subplots_adjust(bottom=0.2, top=0.9)
    plt.show()

def draw_balances(names, balances) :
    formatter = FuncFormatter(lambda y, pos : int(y//1000))
    _, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)

    index = np.arange(len(names))

    plt.bar(index, balances, color=colors.TABLEAU_COLORS)
    plt.xticks(index, names, rotation='vertical')
    plt.subplots_adjust(bottom=0.2, top=0.9)
    plt.show()

