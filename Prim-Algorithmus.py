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



def prim_algorithmus(graph: Graph, startKnoten: Knoten):
    if startKnoten not in graph.knoten:
        exit
    knoten = [startKnoten]
    kanten = []
    
    while len(graph.knoten) != len(knoten):
        kuerzesteKante = None
        for knot in knoten:
            for kante in graph.kanten:
                if kante.Start == knot and kante.Ende not in knoten:
                    if kuerzesteKante is None or kuerzesteKante.Gewicht > kante.Gewicht:
                        kuerzesteKante = kante
        if kuerzesteKante is None:
            print("Der Graph ist kein vollständiger Graph")
            break
        else:
            knoten.append(kuerzesteKante.Ende)
            kanten.append(kuerzesteKante)
    
    for kante in kanten:
        print(kante.Start, " -> ", kante.Ende)

graph = Graph()
graph.addKnoten("A")
graph.addKnoten("B")
graph.addKnoten("C")
graph.addKnoten("D")
graph.addKnoten("E")
graph.addKnoten("F")
graph.addKnoten("G")

#AD
graph.addKante("A", "D", 5)
graph.addKante("D", "A", 5)
#AB
graph.addKante("A", "B", 7)
graph.addKante("B", "A", 7)
#BC
graph.addKante("B", "C", 8)
graph.addKante("C", "B", 8)
#DB
graph.addKante("D", "B", 9)
graph.addKante("B", "D", 9)
#DF
graph.addKante("D", "F", 6)
graph.addKante("F", "D", 6)
#DE
graph.addKante("D", "E", 15)
graph.addKante("E", "D", 15)
#FE
graph.addKante("E", "F", 8)
graph.addKante("F", "E", 8)
#FG
graph.addKante("G", "F", 11)
graph.addKante("F", "G", 11)
#GE
graph.addKante("G", "E", 9)
graph.addKante("E", "G", 9)
#BE
graph.addKante("B", "E", 7)
graph.addKante("E", "B", 7)
#CE
graph.addKante("C", "E", 5)
graph.addKante("E", "C", 5)

prim_algorithmus(graph, "A")









