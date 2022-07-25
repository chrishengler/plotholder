from io import BytesIO

from matplotlib import pyplot as plt
from PIL import Image


def bar_chart(x: list[int], y: list[int | float], x_title: str = None, y_title: str = None) -> Image:
    plt.bar(x, y, width=1)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    buf = BytesIO()
    plt.savefig(buf)
    plt.clf()
    buf.seek(0)
    return Image.open(buf).convert("RGB")

def pie_chart(amounts: list[float], labels: list[str] = None, title: str = None) -> Image:
    segments, text = plt.pie(amounts)
    plt.legend(segments, labels)
    plt.title(title)
    buf = BytesIO()
    plt.savefig(buf)
    plt.clf()
    buf.seek(0)
    return Image.open(buf).convert("RGB")
