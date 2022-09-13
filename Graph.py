class Graph:
  def __init__(self, knoten = [], kanten=[]):
    self.knoten = knoten
    self.kanten = kanten
  
  def getAlleKnoten(self) -> list:
    return self.knoten
  
  def existiertKnoten(self, nameKnoten:str) -> bool:
    return knoten in self.knoten
  
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

graph = Graph()
graph.addKnoten("A")
graph.addKnoten("B")
graph.addKnoten("C")
graph.addKnoten("D")

graph.addKante("A", "B")
graph.addKante("B", "B")
graph.addKante("B", "C")
graph.addKante("B", "D")
graph.addKante("C", "A")
graph.addKante("C", "B")

print(graph.getAlleNachbarn("B"))

