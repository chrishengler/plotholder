from plotholder.src.text_gen import title_nouns_per_capita, title_nouns_per_year


def test_title():
    per_year = title_nouns_per_year("test")
    assert per_year == "number of hexagons"
    per_capita = title_nouns_per_capita("test")
    assert per_capita == "hexagons per capita"
