from main import main

def test_index():
    assert main.index() == "De laatste opdracht"

def test_kasper():
    assert main.kasper() == "Lekker gewandeld"