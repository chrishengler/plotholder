from plotholder.src.text_gen import produce_title


def test_title():
    title = produce_title("test")
    assert title == "number of hexagons"
