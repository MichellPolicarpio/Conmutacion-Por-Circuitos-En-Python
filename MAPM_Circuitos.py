import networkx as nx
import matplotlib.pyplot as plt
import time

# Crear el grafo
G = nx.Graph()

# Agregar nodos
nodos = ["A", "1", "2", "3", "4", "5", "6", "B"]
for nodo in nodos:
    G.add_node(nodo)

# Agregar aristas
G.add_edge("1", "A", label="a")
G.add_edge("1", "2", label="e")
G.add_edge("1", "3", label="c")
G.add_edge("1", "4", label="d")
G.add_edge("5", "2", label="h")
G.add_edge("3", "6", label="f")
G.add_edge("4", "5", label="i")
G.add_edge("4", "3", label="g")
G.add_edge("6", "5", label="j")
G.add_edge("B", "6", label="l")

# Preguntar por el mensaje y los nodos de origen y destino
print("""\t***SIMULACIÓN DE PROGRAMA DE ENVÍO***
            ***CONMUTACIÓN POR CIRCUITOS***\n""")
mensaje = input("Ingrese el mensaje a enviar: ")
origen = input("Ingrese el nodo de origen: ").upper()
destino = input("Ingrese el nodo de destino: ").upper()

# Asignar el mensaje al nodo de origen
G.nodes[origen]['mensaje'] = mensaje

# Encontrar el camino más corto
camino = nx.shortest_path(G, source=origen, target=destino)

# Calcular la disposición de los nodos una vez
pos = nx.shell_layout(G)

# Bloquear y enviar mensaje
print(f"\nIniciando comunicación desde '{origen}' hasta '{destino}'...")
print("\t<<ENVIANDO MENSAJE, RUTA BLOQUEADA TEMPORALMENTE PARA EL ENVIO...>>")
for i in range(len(camino) - 1):
    u = camino[i]
    v = camino[i + 1]
    print(f"Enviando mensaje a través de la arista {u} -> {v}...")
    time.sleep(2)

# Asignar el mensaje al nodo de destino
G.nodes[destino]['mensaje'] = G.nodes[origen]['mensaje']

# Mostrar el mensaje en el nodo de destino
print(f"""\n¡¡¡MENSAJE ENVIADO EXITOSAMENTE!!!:
       
VISUALIZACIÓN EN NODO DESTINO DEL MENSAJE:
NODO: '{destino}': {G.nodes[destino]['mensaje']}""")

print("\n\t<<MENSAJE RECIBIDO, RUTA DISPONIBLE>>")

time.sleep(2)

# Dibujar el grafo completo con el camino resaltado
plt.figure()
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black')
nx.draw_networkx_edges(G, pos, edgelist=list(zip(camino[:-1], camino[1:])), edge_color='red', width=2)
plt.show()