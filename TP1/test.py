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
    
    # Test avec des valeurs positives et des exposants négatifs
    assert f.puissance(5, -2) == 1/25
    assert f.puissance(2, -4) == 1/16
    
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

