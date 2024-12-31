import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def berechne_ct(x: float, y: float) -> float:
    """
    Berechnet ct basierend auf der Pythagoras-Beziehung: ct² = x² + y².

    Diese Funktion nutzt die Quadratwurzel, um die Hypotenuse (ct) eines rechtwinkligen Dreiecks
    in der Raumzeit zu berechnen. Die Werte für x und y repräsentieren die beiden Raumdimensionen.

    :param x: Raumdimension 1 (Kathete a im Pythagoras-Satz).
    :param y: Raumdimension 2 (Kathete b im Pythagoras-Satz).
    :return: Berechneter Wert für ct (Hypotenuse c im Pythagoras-Satz).
    """
    return np.sqrt(x**2 + y**2)

def pythagoras_in_universum(ct: float, x: float, y: float) -> bool:
    """
    Demonstriert den Satz des Pythagoras in der Raumzeit.

    Diese Funktion prüft, ob die Hypotenuse (ct) im Verhältnis zu den beiden
    Raumdimensionen (x und y) dem Satz des Pythagoras entspricht. Die Hypotenuse
    wird im Quadrat mit der Summe der Quadrate der Katheten verglichen.

    :param ct: Zeitkomponente multipliziert mit Lichtgeschwindigkeit (Hypotenuse).
    :param x: Raumdimension 1 (Kathete a).
    :param y: Raumdimension 2 (Kathete b).
    :return: Wahrheitswert, ob der Satz des Pythagoras erfüllt ist.
    """
    # Berechnung der Quadrate von Hypotenuse und Katheten
    hypotenuse_squared = ct**2
    sides_squared = x**2 + y**2

    # Vergleich der Werte mit numerischer Toleranz
    return np.isclose(hypotenuse_squared, sides_squared)

def plot_light_cone(ct: float, x: float, y: float):
    """
    Visualisiert das Raumzeit-Dreieck.

    Diese Funktion erstellt einen 3D-Plot, der die beiden Raumdimensionen (x, y)
    und die Hypotenuse (ct) darstellt. Die Linien und Punkte visualisieren das
    rechtwinklige Dreieck in der Raumzeit.

    :param ct: Zeitkomponente multipliziert mit Lichtgeschwindigkeit (Hypotenuse).
    :param x: Raumdimension 1 (Kathete a).
    :param y: Raumdimension 2 (Kathete b).
    """
    # Erstellen einer neuen Figur für den 3D-Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Punkte für das Raumzeit-Dreieck
    ax.scatter([0, x, 0], [0, 0, y], [0, ct, ct], c='r', label='Photon Pfad')

    # Linien, die das Dreieck verbinden
    ax.plot([0, x], [0, 0], [0, ct], 'b-', label='Hypotenuse (ct)')
    ax.plot([0, 0], [0, y], [0, ct], 'g-', label='Raumdimension Y')
    ax.plot([x, 0], [0, y], [ct, ct], 'k--', label='Raumdimension X')

    # Achsentitel hinzufügen
    ax.set_xlabel('X (Raumdimension in Metern)')
    ax.set_ylabel('Y (Raumdimension in Metern)')
    ax.set_zlabel('ct (Raumzeit in Metern)')

    # Titel und Legende
    ax.legend()
    plt.title("Beweis des Satzes des Pythagoras in der Raumzeit")
    plt.show()

# Physikalische Konstanten und Werte
# Raumdimensionen (x und y) repräsentieren die Katheten eines rechtwinkligen Dreiecks
x = 3       # Raumdimension 1 (in Metern, entspricht Kathete a)
y = 4       # Raumdimension 2 (in Metern, entspricht Kathete b)

# Berechnung der Hypotenuse ct basierend auf x und y
ct = berechne_ct(x, y)  # Dynamisch berechnete Hypotenuse (c)

# Überprüfung des Satzes des Pythagoras
ergebnis = pythagoras_in_universum(ct, x, y)

# Ausgabe der Ergebnisse
print("Beweis des Satzes des Pythagoras in der Raumzeit:")
print(f"Länge der Hypotenuse (ct): {ct:.2f}")
print(f"Summe der Quadrate der Katheten (x² + y²): {x**2 + y**2:.2f}")
print(f"Erfüllt der Satz des Pythagoras? {'Ja' if ergebnis else 'Nein'}")

# Visualisierung des Raumzeit-Dreiecks
plot_light_cone(ct, x, y)
