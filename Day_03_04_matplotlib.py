# Day_03_04_matplotlib.py
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def random_walker01():
    np.random.seed(1)

    walks, heights, pos = [], [], 0
    for _ in range(100):
        state = np.random.randint(3) - 1
        # print(state)
        pos += state

        walks.append(state)
        heights.append(pos)

    plt.plot(walks, 'ro')
    plt.plot(heights)
    plt.show()

def random_walker02():
    # 문제
    # 반복문 없이 위와 같은 그래프를 그려보세요. (np.cumsum)
    walks = np.random.randint(-1, 2, 100)
    heights = walks.cumsum()

    plt.plot(walks, 'ro')
    plt.plot(heights)
    plt.show()

def ggplot_style():
    print(plt.style.available) # ['bmh', 'classic', 'dark_background', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn', '_classic_test']
    print(len(plt.style.available))

    x = np.linspace(0, 10)
    print(len(x))

    with plt.style.context('ggplot'):
        plt.plot(x, np.sin(x) + 0.5 * x + np.random.randn(50))
        plt.plot(x, np.sin(x) + 1.0 * x + np.random.randn(50))
        plt.plot(x, np.sin(x) + 2.0 * x + np.random.randn(50))

    plt.show()

def all_in_one():
    x = np.linspace(0, 10)
    n = np.random.randn(50)

    y1 = np.sin(x) + 0.5 * x + n
    y2 = np.sin(x) + 1.0 * x + n
    y3 = np.sin(x) + 2.5 * x + n

    for i, style in enumerate(plt.style.available):
        plt.figure(i+1)
        with plt.style.context(style):
            plt.plot(x, y1)
            plt.plot(x, y2)
            plt.plot(x, y3)
            plt.title(style)

    plt.show()

# 문제
# 아래 그래프를 하나의 피겨에 모두 그려 주세요.
def all_in_one02():
    x = np.linspace(0, 10)
    n = np.random.randn(50)

    y1 = np.sin(x) + 0.5 * x + n
    y2 = np.sin(x) + 1.0 * x + n
    y3 = np.sin(x) + 2.5 * x + n

    plt.figure(figsize=(20,15))
    for i, style in enumerate(plt.style.available):
        with plt.style.context(style):
            plt.subplot(5, 5, i + 1)
            plt.plot(x, y1)
            plt.plot(x, y2)
            plt.plot(x, y3)
            plt.title(style)

    plt.tight_layout()
    plt.savefig('Data/style.png')
    plt.show()

def wc():
    f = open('Data/i_have_a_dream.txt', 'r', encoding='utf-8')
    text = f.read()
    f.close()

    plt.figure(1)
    wc1 = WordCloud().generate(text)
    plt.imshow(wc1, interpolation='bilinear')
    plt.axis('off')

    plt.figure(2)
    wc2 = WordCloud(max_font_size=40).generate(text)
    plt.imshow(wc2, interpolation='bilinear')
    plt.axis('off')

    plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# Fixing random state for reproducibility
np.random.seed(19680801)

n = 100000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xmin = x.min()
xmax = x.max()
ymin = y.min()
ymax = y.max()

fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(7, 4))
fig.subplots_adjust(hspace=0.5, left=0.07, right=0.93)
ax = axs[0]
hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.axis([xmin, xmax, ymin, ymax])
ax.set_title("Hexagon binning")
cb = fig.colorbar(hb, ax=ax)
cb.set_label('counts')

ax = axs[1]
hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
ax.axis([xmin, xmax, ymin, ymax])
ax.set_title("With a log color scale")
cb = fig.colorbar(hb, ax=ax)
cb.set_label('log10(N)')

plt.show()