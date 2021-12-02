import app

def test_index():
    assert app.index() == "De laatste opdracht"

def test_kasper():
    assert app.kasper() == "Lekker gewandeld"