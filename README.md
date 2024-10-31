# 🌐 Simulación de Conmutación por Circuitos en Python

## 🎯 Descripción del Proyecto
Este programa simula el proceso de conmutación por circuitos en una red de comunicaciones, implementado en Python utilizando NetworkX para la visualización y manipulación de grafos. La simulación permite establecer una conexión dedicada entre dos nodos para la transmisión de mensajes, similar al funcionamiento tradicional de las redes telefónicas.

## 🛠️ Requisitos
```python
networkx
matplotlib
time
```

## 🏗️ Estructura del Grafo
- 📍 8 nodos en total: A, B, y nodos numerados del 1 al 6
- 🔗 10 conexiones (aristas) etiquetadas de 'a' hasta 'l'
- 🎨 Visualización usando disposición shell_layout de NetworkX

## ⚙️ Funcionalidades
1. 📝 Entrada interactiva de:
   - Mensaje a transmitir
   - Nodo de origen
   - Nodo de destino

2. 🔄 Proceso de transmisión:
   - Encuentra la ruta más corta entre origen y destino
   - Bloquea la ruta durante la transmisión
   - Simula el envío del mensaje por cada conexión
   - Libera la ruta después de la transmisión

3. 📊 Visualización:
   - Grafo completo con nodos en azul claro
   - Aristas en negro
   - Ruta utilizada resaltada en rojo

## 💻 Ejemplo de Uso
```bash
***SIMULACIÓN DE PROGRAMA DE ENVÍO***
***CONMUTACIÓN POR CIRCUITOS***

Ingrese el mensaje a enviar: Hola Mundo
Ingrese el nodo de origen: A
Ingrese el nodo de destino: B
```

## 🔄 Flujo del Programa
1. 📥 Solicita datos de entrada al usuario
2. 🔍 Calcula la ruta más corta
3. 🔒 Bloquea la ruta para transmisión
4. 📤 Simula el envío del mensaje
5. 🔓 Libera la ruta
6. 📊 Muestra el grafo con la ruta resaltada

## 🎨 Características de Visualización
- 🔵 Nodos: Color azul claro
- ⚫ Aristas normales: Color negro
- 🔴 Ruta activa: Color rojo
- 🏷️ Etiquetas: Visibles en todos los nodos

## 📝 Notas Técnicas
- ⏱️ Incluye retardos (time.sleep) para simular tiempo real de transmisión
- 🔍 Utiliza el algoritmo de ruta más corta de NetworkX
- 📍 Las posiciones de los nodos se calculan una sola vez para mantener consistencia visual

## 🚀 Mejoras Potenciales
1. 💡 Agregar verificación de disponibilidad de rutas
2. 📊 Implementar estadísticas de transmisión
3. 🔄 Añadir simulación de fallos en la red
4. 📱 Crear interfaz gráfica de usuario
5. 📈 Incluir métricas de rendimiento

## ⚡ Diferencias con Conmutación por Paquetes
- 🔒 Establece una conexión dedicada
- 🛣️ Utiliza una única ruta durante toda la transmisión
- 📨 El mensaje se envía completo, no fragmentado
- 🔄 La ruta permanece bloqueada durante toda la comunicación

## 🎓 Uso Educativo
Este proyecto es ideal para comprender:
- 📚 Fundamentos de conmutación por circuitos
- 🌐 Conceptos básicos de redes
- 🔄 Ruteo en redes de comunicaciones
- 📊 Visualización de grafos con Python
