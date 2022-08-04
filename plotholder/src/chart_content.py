from dataclasses import dataclass
from typing import Tuple


@dataclass
class ChartContent:
    title: str


@dataclass
class ChartContentBar:
    x_label: str
    y_label: str
    values: list[Tuple[int | float | str, int | float]]


@dataclass
class ChartContentPie:
    values: list[Tuple[str, float]]


@dataclass
class ChartContentScatter:
    x_label: str
    y_label: str
    values: list[Tuple[int | float, int | float]]
