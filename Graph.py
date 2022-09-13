class Graph:
  def __init__(self, knoten = [], kanten=[]):
    self.knoten = knoten
    self.kanten = kanten
  
  def getAlleKnoten(self) -> list:
    return self.knoten
  
  def existiertKnoten(self, nameKnoten:str) -> bool:
    return nameKnoten in self.knoten
  
  def addKnoten(self, nameKnoten:str):
    self.knoten.append(nameKnoten)
  
  def delKnoten(self, nameKnoten:str):
    self.knoten.remove(nameKnoten)
  
  def existiertKante(self, nameStartKnoten:str, nameZielKnoten:str):
    return [nameStartKnoten, nameZielKnoten] in self.kanten
  
  def addKante(self, nameStartKnoten:str, nameZielKnoten:str):
    self.kanten.append([nameStartKnoten, nameZielKnoten])
  
  def delKante(self, nameStartKnoten:str, nameZielKnoten:str):
    self.kanten.remove([nameStartKnoten, nameZielKnoten])
  
  def getAlleNachbarn(self, nameKnoten) -> list:
    nachbarn = []
    for kante in self.kanten:
      if kante[0] == nameKnoten:
        nachbarn.append(kante[1])
    return nachbarn

def mooreAlgorythm(nameStartKnoten, graph: Graph):
  if graph.existiertKnoten(nameStartKnoten):
    ergebnis = {nameStartKnoten:0}
    toCheck = [nameStartKnoten]
    while len(toCheck) != 0:
      knotenName = toCheck.pop(0)
      print(knotenName, graph.getAlleNachbarn(knotenName))
      for nachbar in graph.getAlleNachbarn(knotenName):
        if not nachbar in ergebnis.keys():
          toCheck.append(nachbar)
          ergebnis[nachbar] = ergebnis[knotenName] + 1
    return ergebnis

  
  

# graph = Graph()
# graph.addKnoten("A")
# graph.addKnoten("B")
# graph.addKnoten("C")
# graph.addKnoten("D")

# graph.addKante("A", "B")
# graph.addKante("B", "B")
# graph.addKante("B", "C")
# graph.addKante("B", "D")
# graph.addKante("C", "A")
# graph.addKante("C", "B")

# print("Nachbarn", graph.getAlleNachbarn("B"))
# print("Moore", mooreAlgorythm("A", graph))

graph1 = Graph()
graph1.addKnoten("A")
graph1.addKnoten("B")
graph1.addKnoten("C")
graph1.addKnoten("D")
graph1.addKnoten("E")
graph1.addKnoten("F")
graph1.addKnoten("G")
graph1.addKnoten("H")

graph1.addKante("A", "C")
graph1.addKante("A", "E")
graph1.addKante("A", "G")

graph1.addKante("B", "C")
graph1.addKante("B", "D")

graph1.addKante("C", "D")
graph1.addKante("C", "E")
graph1.addKante("C", "A")

graph1.addKante("D", "B")
graph1.addKante("D", "E")

graph1.addKante("E", "D")
graph1.addKante("E", "G")

graph1.addKante("F", "D")
graph1.addKante("F", "H")

graph1.addKante("G", "D")

graph1.addKante("H", "G")
graph1.addKante("H", "F")

print("Moore", mooreAlgorythm("A", graph1))