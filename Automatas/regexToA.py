class automata:
    def __init__(self):
        self.nodos = []
        self.tablaTransiciones = []
        self.operadores = ["u", "n", "(", ")", "|", "*"]
        self.alfabeto = []
        self.crearNodo([2], 1)
        self.crearNodo([], 0)

    def crearNodo(self, nextNodes, state):
        nodo = {
            "identifier": len(self.nodos) + 1,
            "NFAstates": nextNodes,
            "state": 0,
        }
        self.nodos.append(nodo)
        return nodo

    def crearLenguaje(self, regex):
        for letter in regex:
            if letter not in self.operadores:
                self.lenguaje.append(letter)
        return self.lenguaje

automata1 = automata()
automata1.crearLenguaje("(ab)*E")