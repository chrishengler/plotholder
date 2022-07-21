import os

from PIL import Image, ImageChops

from plotholder.src.plot_gen import bar_chart


def relative_path_to_full_path(rel_path: str) -> str:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, rel_path)


def test_bar():
    x = [0, 3, 4, 7]
    y = [3, 1, 0, 8]
    img = bar_chart(x, y)
    target = Image.open(relative_path_to_full_path("resources/bar_chart.png"))
    assert ImageChops.difference(img, target).getbbox() is None
