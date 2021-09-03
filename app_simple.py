# >>>Victor Andres Barilin<<<
from listas_enlazadas import *

# instancio una lista simple
ln = Lista_simple()
# creo un menu infinito para agregar nombres y verlos 
while True:
    # menu
    print('\n   ~ Menu ~\n1- Agregar\n2- Ver lista\n3- Eliminar')
    # incerta opcion 'op'
    op = input('Ingresar numero de opcion: ')
    # igreso al if que sea igual al numero de op
    if op == '1':
        name = input('\nIngresar nombre: ')
        # luego de pedir el nombre instancio un nodo con el nombre 
        # escrito y lo agrego a la lista de nombres 'ln'
        node = Nodo(name)
        ln.add_nodo(node)
    elif op == '2':
        ln.see_list()
    elif op == '3':
        del_name = input('inserte nombre a borrar: ')
        ln.del_nodo(del_name)