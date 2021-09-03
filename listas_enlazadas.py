# >>>Victor Andres Barilin<<<

'''la class nodo crea una celda que posee el dato de relevancia para el usuario (nombre) y puede
guardar en (sig) el dato que continua a el, en principio su valor es none'''
class Nodo():
    def __init__(self, dato, sig = None, ant = None):
        self.dato = dato
        self.sig = sig
        self.ant = ant

'''la lista simple se instancia con una cabeza que me indica el comienzo de esta
y la cola indica el final'''
class Lista_simple():
    def __init__(self):
        self.cabeza = None
        self.cola = None

    
    def add_nodo(self, element):
        if self.cabeza == None: #corroboro si existen datos en cabeza (si la lista contiene datos)
            self.cabeza = element #en caso de ser asi igualo la cabeza al primer dato
            self.cola = element #tambien lo gargo en la cola ya que aqui comienza y termina la lista

        elif self.cola == self.cabeza: #comparo si cabeza y cola son iguales si es verdadero es porque mi lista solo contiene un dato 
            if self.cabeza.dato < element.dato: #en esta instancia comparo los datos de los nodos para controlar cual es alfabeticamente menor
                self.cola = element #si la cabeza es alfabeticamente menor cargo el dato en la cola
                self.cabeza.sig = self.cola #y actualizo el siguiente al que apunta cabeza, en este caso es (cola)

            else: #en caso contrario coloco el nuevo elemento en la cabeza y actualizo el siguiente
                element.sig = self.cola
                self.cabeza = element
        
        elif self.cabeza.dato >= element.dato: #esta comparacion me sirve para corroborar que el nuevo dato no deba ponerse en la cabeza
            element.sig = self.cabeza # si es mas chico que la cabeza la reemplazo y actualizo el siguiente
            self.cabeza = element
        
        elif self.cola.dato <=  element.dato: #repito el mismo proceso que con el anterior pero con la cola
            self.cola.sig = element 
            self.cola = element

        else: #si no se cumple ninguna de las anteriores procedo a recorrer la lista
            c = self.cabeza
            aux = c
            cargado = False
            while c != None and aux != None and cargado == False:
                if c.dato > element.dato and c != None and cargado == False: #mientras recorro la lista comparo si el elemento actual es mas grande que el que se quiere cargar
                    aux.sig = element #si es asi actualizo el indice e incorporo el nuevo elemento alfabeticamenete 
                    element.sig = c 
                    cargado = True #cambio de estado la variable cargado para romper el loop
                aux = c
                c = c.sig
    
    """en primer lugar corroboro que el nodo a ser borrado sea igual a la cabeza o a la cola, ya que de ser asi
    sera asignada una nueva cola o cabeza, si no es el caso entonces recorro la lista en busca del Nodo
    que coincida con el dato buscado (para ser mas especifico podria ser con un id), una vez que lo encuentra 
    se posiciona detras de el y lo desvincula de la cadena """
    def del_nodo(self, name):
        c = self.cabeza
        aux = c
        if name == self.cabeza.dato:
            c = c.sig
            self.cabeza = c
        elif name == self.cola.dato:
            while c != None:
                if c == self.cola:
                    aux.sig = None
                    self.cola = aux
                aux = c
                c = c.sig
        else:
            while c != None:
                    if c.dato == name:
                        c = c.sig
                        aux.sig = c
                    aux = c
                    c = c.sig

    '''recorro la lista de nodos mientras imprimo su atributo dato, que en este caso es el nombre
    cuando c sea none quiere decir que la lista ah terminado y finalizo el loop'''
    def see_list(self):
        c = self.cabeza
        print('\nLista de nombres ascendentes:')
        while c != None:
             print('-'+c.dato)
             c = c.sig

'''en la lista doble se hace lo mismo que arriba pero cambia cuando tengo que vincular o desvincular
ya que esta  lista posee una vinculacion estra (la del nodo anterior) representada por el atributo (ant) '''
class Lista_doble():
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    #en este nodo se repiten las mismas tecnicas que en add_nodo() de Lista_simple() con la diferencia que cada vez
    #que se actualiza se actualiza tambien el dato anterior y no solo el siguiente
    def add_nodo(self, element):
        if self.cabeza == None:
            self.cabeza = element
            self.cola = element

        elif self.cola == self.cabeza:
            if self.cabeza.dato < element.dato:
                self.cola = element
                self.cabeza.sig = self.cola
                self.cola.ant = self.cabeza

            else:
                element.sig = self.cola
                self.cabeza = element
                self.cola.ant = self.cabeza
        
        elif self.cabeza.dato >= element.dato:
            element.sig = self.cabeza
            self.cabeza.ant = element
            self.cabeza = element
        
        elif self.cola.dato <=  element.dato:
            self.cola.sig = element
            element.ant = self.cola
            self.cola = element

        else:
            c = self.cabeza
            aux = c
            cargado = False
            while c != None and aux != None and cargado == False:
                if c.dato > element.dato and c != None and cargado == False:
                    aux.sig = element
                    element.sig = c 
                    element.ant = aux
                    c.ant = element
                    cargado = True
                aux = c
                c = c.sig
        
    def del_nodo(self, name):
        c = self.cabeza
        if name == self.cabeza.dato:
            c = c.sig
            self.cabeza = c
            self.cabeza.ant = None 
        elif name == self.cola.dato:
                    aux = self.cola.ant
                    aux.sig = None
                    self.cola = aux
        else:
            while c != None:
                if c.dato == name:
                    c = c.sig
                    c.ant = aux
                    aux.sig = c
                aux = c
                c = c.sig
                    
    def see_list(self):
        c = self.cabeza
        print('\nLista de nombres ascendentes:')
        while c != None:
             print('-'+c.dato)
             c = c.sig
        c = self.cola
        print('\nLista de nombres descendente:')
        while c != None:
             print('-'+c.dato)
             c = c.ant

        
