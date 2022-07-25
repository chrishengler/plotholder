from os import path

from PIL import Image, ImageChops

from plotholder.src.plot_gen import bar_chart, pie_chart


def relative_path_to_full_path(rel_path: str) -> str:
    current_dir = path.dirname(path.realpath(__file__))
    return path.join(current_dir, rel_path)


def test_bar():
    x = [0, 3, 4, 7]
    y = [3, 1, 0, 8]
    img = bar_chart(x, y, "x-axis", "y-axis")
    target = Image.open(relative_path_to_full_path("resources/bar_chart.png"))
    # img.save('./resources/bar_chart.png')
    assert ImageChops.difference(img, target).getbbox() is None


def test_pie_with_autopct():
    amounts = [1, 2, 4, 8]
    labels = ["this", "is", "a", "pie"]
    img = pie_chart(amounts, labels, title="pie chart title")
    target = Image.open(relative_path_to_full_path("resources/pie_chart.png"))
    # img.save('./resources/pie_chart.png')
    assert ImageChops.difference(img, target).getbbox() is None
