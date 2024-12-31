# Raumzeit-Pythagoras

Dieses Projekt demonstriert den Satz des Pythagoras in der Raumzeit. Es berechnet die Hypotenuse eines rechtwinkligen Dreiecks basierend auf zwei Raumdimensionen und visualisiert das Ergebnis in einem 3D-Plot.

## Inhalt

- [Installation](#installation)
- [Verwendung](#verwendung)
- [Funktionen](#funktionen)
- [Beispiel](#beispiel)
- [Lizenz](#lizenz)

## Installation

Um dieses Projekt auszuführen, benötigen Sie Python sowie die Bibliotheken `numpy` und `matplotlib`. Sie können diese Bibliotheken mit `pip` installieren:

```bash
pip install numpy matplotlib
```

## Verwendung

1. Klonen Sie das Repository oder laden Sie die Datei `raumzeit_pythagoras.py` herunter.
2. Führen Sie das Skript aus:

```bash
python raumzeit_pythagoras.py
```
![image](https://github.com/user-attachments/assets/e8f06373-5209-4cfa-9283-97ad3f0ef430)

## Funktionen

### `berechne_ct(x: float, y: float) -> float`

Berechnet die Hypotenuse `ct` basierend auf der Pythagoras-Beziehung: \( ct^2 = x^2 + y^2 \).

- **Parameter:**
  - `x`: Raumdimension 1 (Kathete a im Pythagoras-Satz).
  - `y`: Raumdimension 2 (Kathete b im Pythagoras-Satz).
- **Rückgabe:**
  - Berechneter Wert für `ct` (Hypotenuse c im Pythagoras-Satz).

### `pythagoras_in_universum(ct: float, x: float, y: float) -> bool`

Prüft, ob die Hypotenuse `ct` im Verhältnis zu den beiden Raumdimensionen `x` und `y` dem Satz des Pythagoras entspricht.

- **Parameter:**
  - `ct`: Zeitkomponente multipliziert mit Lichtgeschwindigkeit (Hypotenuse).
  - `x`: Raumdimension 1 (Kathete a).
  - `y`: Raumdimension 2 (Kathete b).
- **Rückgabe:**
  - Wahrheitswert, ob der Satz des Pythagoras erfüllt ist.

### `plot_light_cone(ct: float, x: float, y: float)`

Visualisiert das Raumzeit-Dreieck in einem 3D-Plot.

- **Parameter:**
  - `ct`: Zeitkomponente multipliziert mit Lichtgeschwindigkeit (Hypotenuse).
  - `x`: Raumdimension 1 (Kathete a).
  - `y`: Raumdimension 2 (Kathete b).

## Beispiel

Im folgenden Beispiel werden die Raumdimensionen `x` und `y` auf 3 bzw. 4 Meter gesetzt. Die Hypotenuse `ct` wird berechnet und der Satz des Pythagoras wird überprüft. Anschließend wird das Raumzeit-Dreieck visualisiert.

```python
# Physikalische Konstanten und Werte
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
```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der Datei [LICENSE](LICENSE).
