import pytest
import fonctions as f

def test_1():
    assert f.puissance(2, 3) == 8
    assert f.puissance(2, 2) == 4

def test_2():
    # Test avec des valeurs négatives et des exposants négatifs
    assert f.puissance(-2, 2) == 4
    assert f.puissance(-2, -3) == -0.125
    
    # Test avec des valeurs négatives et des exposants positifs
    assert f.puissance(-3, 3) == -27
    assert f.puissance(-4, 5) == -1024
    
    # Cas limite : Exposant nul
    assert f.puissance(10, 0) == 1
    
    # Cas limite : Base nulle, exposant positif
    assert f.puissance(0, 5) == 0
    
    # Cas limite : Base nulle, exposant nul
    assert f.puissance(0, 0) == 1
    
    # Cas limite : Base négative, exposant pair
    assert f.puissance(-2, 4) == 16
    
    # Cas limite : Base négative, exposant impair
    assert f.puissance(-2, 3) == -8

def test_3():
    # Cas limite : Base nulle, exposant négatif (avec une exception)
    with pytest.raises(ValueError):
        f.puissance(0, -5)

def test_4():
    # Test avec des exposants négatifs pour des valeurs non nulles
    assert f.puissance(5, -2) == 0.04
    assert f.puissance(1, -10) == 1
    assert f.puissance(-2, -3) == -0.125

def test_5():
    # Test avec des exposants positifs pour des valeurs non nulles
    assert f.puissance(3, 5) == 243
    assert f.puissance(2, 6) == 64
    assert f.puissance(10, 3) == 1000

def test_6():
    # Test avec des exposants négatifs pour des valeurs négatives
    assert f.puissance(-3, -2) == 0.1111111111111111
    assert f.puissance(-1, -4) == 1
    assert f.puissance(-4, -3) == -0.015625

def test_7():
    # Test avec des exposants positifs pour des valeurs négatives
    assert f.puissance(-3, 4) == 81
    assert f.puissance(-2, 5) == -32
    assert f.puissance(-10, 3) == -1000
