class automata:
    def __init__(self, regex):
        # Define the variables of the automata
        self.nodos = []
        self.tablaTransiciones = []
        self.operadores = ["u", "n", "(", ")", "|", "*"]
        self.alfabeto = []

        # Initialize the automata
        self.alfabeto = self.definirAlfabeto(regex)
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

    def definirAlfabeto(self, regex):
        for letter in regex:
            if letter not in self.operadores:
                self.alfabeto.append(letter)
        return self.alfabeto

automata1 = automata("(ab)*E")