from PIL import Image, ImageChops

from plotholder.src.plot_gen import bar_chart


def test_bar():
    x = [0, 3, 4, 7]
    y = [3, 1, 0, 8]
    img = bar_chart(x, y)
    target = Image.open("resources/bar_chart.png")
    assert ImageChops.difference(img, target).getbbox() is None
