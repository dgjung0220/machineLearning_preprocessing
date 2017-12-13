# Day_03_01_colormap.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

def not_used01():
    x = np.random.rand(100)
    y = np.random.rand(100)
    t = np.arange(100)

    plt.scatter(x,  y, c=t)          # 산점도   # c - color 옵션, 내부적으로 사용되는 색상 colormap
    plt.show()

def not_used02():
    x = np.arange(100)
    y = x
    t = x

    plt.scatter(x, -y, c = t, cmap='viridis')                       # viridis, default colormap
    plt.scatter(x, -y, c = cm.viridis(0))                           # viridis 0번째 색상
    plt.scatter(x, -y, c = [cm.viridis(0), cm.viridis(255)])
    plt.show()

def not_used03():
    print(plt.colormaps())                      # # ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Vega10', 'Vega10_r', 'Vega20', 'Vega20_r', 'Vega20b', 'Vega20b_r', 'Vega20c', 'Vega20c_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spectral', 'spectral_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
    print(len(plt.colormaps()))                 # 168

    # 문제
    # 아무 colormap이나 하나 선택해서
    # 대각선이 교차하도록 정상과 거꾸로 colormap을 그려주세요.

    # 1번.
    # x = np.arange(-100,100)
    # y = x
    # t = x
    # plt.scatter(x, -y, c=t, cmap=plt.colormaps().pop(100))
    # plt.scatter(x, y, c=t, cmap=plt.colormaps().pop(99))

    # 2번
    x = np.arange(100)
    y = x
    t = x

    # 색깔 뒤집기
    plt.subplot(2, 1, 1)
    plt.scatter(x,y, c=t)           # viridis
    plt.subplot(2, 1, 2)
    plt.scatter(x,y, c=t[::-1])     # viridis_r
    plt.show()

def not_used04():
    values = np.random.rand(10, 10)
    print(values)
    print(values.shape)

    plt.imshow(values)      # image show
    plt.copper()            # colormap 변경, default viridis
    plt.show()

def not_used05():
    jet = cm.get_cmap('jet')    # <matplotlib.colors.LinearSegmentedColormap object at 0x000002D606451E80>
    print(jet(0))
    print(jet(127))
    print(jet(255))
    print(jet(2550))
    print('-' * 50)

    # 색상을 표현하는 다양한 방법
    print(jet([0, 255]))
    print(jet(range(0, 5, 2)))
    print(jet(np.linspace(0.3, 0.7, 5)))
    print('-' * 50)
    print(cm.jet(0))
    print(cm.copper(0))

# https://matplotlib.org/examples/color/colormaps_reference.html 색상표
def not_used06():
    """
    ==================
    Colormap reference
    ==================

    Reference for colormaps included with Matplotlib.

    This reference example shows all colormaps included with Matplotlib. Note that
    any colormap listed here can be reversed by appending "_r" (e.g., "pink_r").
    These colormaps are divided into the following categories:

    Sequential:
        These colormaps are approximately monochromatic colormaps varying smoothly
        between two color tones---usually from low saturation (e.g. white) to high
        saturation (e.g. a bright blue). Sequential colormaps are ideal for
        representing most scientific data since they show a clear progression from
        low-to-high values.

    Diverging:
        These colormaps have a median value (usually light in color) and vary
        smoothly to two different color tones at high and low values. Diverging
        colormaps are ideal when your data has a median value that is significant
        (e.g.  0, such that positive and negative values are represented by
        different colors of the colormap).

    Qualitative:
        These colormaps vary rapidly in color. Qualitative colormaps are useful for
        choosing a set of discrete colors. For example::

            color_list = plt.cm.Set3(np.linspace(0, 1, 12))

        gives a list of RGB colors that are good for plotting a series of lines on
        a dark background.

    Miscellaneous:
        Colormaps that don't fit into the categories above.

    """
    import numpy as np
    import matplotlib.pyplot as plt

    # Have colormaps separated into categories:
    # http://matplotlib.org/examples/color/colormaps_reference.html
    cmaps = [('Perceptually Uniform Sequential', [
        'viridis', 'plasma', 'inferno', 'magma']),
             ('Sequential', [
                 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
             ('Sequential (2)', [
                 'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
                 'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
                 'hot', 'afmhot', 'gist_heat', 'copper']),
             ('Diverging', [
                 'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
                 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
             ('Qualitative', [
                 'Pastel1', 'Pastel2', 'Paired', 'Accent',
                 'Dark2', 'Set1', 'Set2', 'Set3',
                 'tab10', 'tab20', 'tab20b', 'tab20c']),
             ('Miscellaneous', [
                 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
                 'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
                 'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'])]

    nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps)
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    def plot_color_gradients(cmap_category, cmap_list, nrows):
        fig, axes = plt.subplots(nrows=nrows)
        fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
        axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

        for ax, name in zip(axes, cmap_list):
            ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
            pos = list(ax.get_position().bounds)
            x_text = pos[0] - 0.01
            y_text = pos[1] + pos[3] / 2.
            fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

        # Turn off *all* ticks & spines, not just the ones with colormaps.
        for ax in axes:
            ax.set_axis_off()

    for cmap_category, cmap_list in cmaps:
        plot_color_gradients(cmap_category, cmap_list, nrows)

    plt.show()

