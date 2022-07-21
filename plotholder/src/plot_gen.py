from io import BytesIO

from matplotlib import pyplot as plt
from PIL import Image


def bar_chart(x: list[int], y: list[int | float]):
    plt.bar(x, y, width=1)
    buf = BytesIO()
    plt.savefig(buf)
    buf.seek(0)
    return Image.open(buf).convert("RGB")
