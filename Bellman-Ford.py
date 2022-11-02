import graphlib
import sys


# Datenklasse einer Kante
class Kante:

    def __init__(self, start, ende, gewicht) -> None:
        self.Gewicht = gewicht
        self.Start = start
        self.Ende = ende


# Datenklasse eines Knotens
class Knoten:
    def __init__(self, name) -> None:
        self.name = name


# Graph Klasse
class Graph:

    def __init__(self) -> None:
        self.knoten = []
        self.kanten = []

    # Fügt einen neuen Knoten hinzu
    def addKnoten(self, knoten: Knoten):
        self.knoten.append(knoten)

    # Fügt eine neue Kante zwischen zwei Knoten hinzu
    def addKante(self, start: Knoten, ziel: Knoten, gewicht):
        if start not in self.knoten or ziel not in self.knoten:
            print("Knoten konnte nicht gefunden werden!")
            sys.exit()
        kante = Kante(start, ziel, gewicht)
        self.kanten.append(kante)


# Ausführung des Algorithmus
def algorythm(graph: Graph, startKnoten: Knoten):
    if startKnoten not in graph.knoten:
        print("Startknoten existiert nicht!")
        sys.exit()
    knotenZahl = len(graph.knoten)
    distanzen = {}
    vorgaenger = {}

    # setzen der Distanzen aller Knoten auf Unendlich ("u")
    for knoten in graph.knoten:
        distanzen[knoten] = "u"

    # manuelles hinzufügen des Startknotens
    distanzen[startKnoten] = 0
    vorgaenger[startKnoten] = startKnoten

    # ausführen des Algorithmus auf alle Knoten
    for i in range(knotenZahl):
        for kante in graph.kanten:
            neuesGewicht = distanzen[kante.Start] + kante.Gewicht
            altesGewicht = distanzen[kante.Ende]
            # kontrolle, ob der Knoten schon seine Kosten verändert hat bzw. der neue Wert kleiner ist
            if isinstance(altesGewicht, str) or neuesGewicht < altesGewicht:
                distanzen[kante.Ende] = neuesGewicht
                vorgaenger[kante.Ende] = kante.Start

    # Kontrolle, ob ein negativer Zyklus vorliegt
    for kante in graph.kanten:
        neuesGewicht = distanzen[kante.Start] + kante.Gewicht
        altesGewicht = distanzen[kante.Ende]
        if neuesGewicht < altesGewicht:
            print("Es gibt einen negativen Zyklus...")
            return

    # Ausgeben aller Kosten der Knoten und ihrer Vorgänger
    for knoten in graph.knoten:
        print(f"Knoten {knoten.name}: {distanzen[knoten]} über {vorgaenger[knoten].name}")


# Test für einen negativen Zyklus
def negativerZyklus():
    graph = Graph()
    knotenA = Knoten("A")
    knotenB = Knoten("B")
    knotenC = Knoten("C")
    knotenD = Knoten("D")
    knotenE = Knoten("E")
    knotenF = Knoten("F")
    graph.addKnoten(knotenA)
    graph.addKnoten(knotenB)
    graph.addKnoten(knotenC)
    graph.addKnoten(knotenD)
    graph.addKnoten(knotenE)
    graph.addKnoten(knotenF)

    graph.addKante(knotenA, knotenB, 50)
    graph.addKante(knotenB, knotenC, -10)
    graph.addKante(knotenC, knotenD, -5)
    graph.addKante(knotenD, knotenE, -1)
    graph.addKante(knotenE, knotenB, -1)
    graph.addKante(knotenD, knotenF, 5)

    return graph, knotenA


# Test für einen "normalen" Graphen
def normalerGraph():
    graph = Graph()
    knotenA = Knoten("A")
    knotenB = Knoten("B")
    knotenC = Knoten("C")
    graph.addKnoten(knotenA)
    graph.addKnoten(knotenB)
    graph.addKnoten(knotenC)

    graph.addKante(knotenA, knotenB, 3)
    graph.addKante(knotenA, knotenC, 11)
    graph.addKante(knotenC, knotenB, -9)

    return graph, knotenA


if __name__ == "__main__":
    print("Negativer Zyklus Graph")
    negGraph = negativerZyklus()
    algorythm(negGraph[0], negGraph[1])
    print("------------------------------")
    print("Normaler Graph")
    normGraph = normalerGraph()
    algorythm(normGraph[0], normGraph[1])
    print("------------------------------")
