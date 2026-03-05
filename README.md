## Información de los Integrantes
* **Institución:** Instituto Politécnico Nacional (IPN)
* **Escuela:** Escuela Superior de Cómputo (ESCOM) 
* **Unidad de Aprendizaje:** Teoría de la Computación 
* **Programa Académico:** Ingeniería en Sistemas Computacionales / Plan 2020 
* **Grupo:** 4CM4
* **Alumnos:** 
   * Diego Ruperto Hernandez (Boleta: 2024630696)
   * Maria Jose Venegas Martinez (Boleta: 2024630831)

---

## Objetivo
El propósito de esta práctica es explorar los conceptos fundamentales de lenguajes formales mediante el desarrollo de una aplicación con interfaz gráfica. Se implementará un software para resolver problemas específicos sobre lenguajes y sus operaciones básicas.

## Introduccion 
En esta practica exploraremos los conceptos de: **Subcadenas, Prefijos y Sufijos** y **Cerraduras de Kleene y Positiva**, estos son conceptos basicos del tema de **Lenguajes Formales**, para recapitular tenemos las definiciones de ambos temas.

 1. **Subcadenas, Prefijos y Sufijos**

Una **subcadena** es una secuencia de caracteres que aparecen de manera consecutiva dentro de otra cadena de texto, respetando el orden original y sin saltarse ningún elemento.
Los **prefijos** están formados por los primeros símbolos de la cadena; y los **sufijos** por los últimos. Un prefijo o sufijo de una cadena que no sea la misma cadena es un prefijo y sufijos propios.

En palabras mas tecnicas se tiene que:

Una cadena *v* es una subcadena o una subpalabra de *u* si existen cadenas *x*, *y* tales que *u = xvy*. Nótese que *x* o/y pueden ser *λ* y, por lo tanto, **la cadena vacía es una subcadena de cualquier cadena**.
Un **prefijo** de *u* es una cadena v tal que u = vw para alguna cadena w ∈ Σ* Se dice que *v* es un **prefijo** propio si *v* *6 = u*.
Similarmente, un sufijo de *u* es una cadena v tal que *u = wv* para alguna cadena *w ∈ Σ**
**Obsérvese que *λ* es un prefijo y un sufijo de toda cadena u ya que uλ = λu = u.**
Por la misma razón, **toda cadena u es prefijo y sufijo de sí misma.**

 2. **Cerraduras de Kleene y Positiva**
 La cerradura de Kleene en un alfabeto se refiere a todas combinaciones de las cadenas de caracteres o palabras que se pueden formar incluyendo *λ* o conjunto vacío.
Por otro lado la cerradura positiva en un alfabeto se refiere a todas las combinasiones de las cadenas de caracteres o palabras que se pueden formar con ese alfabeto, excluyendo a *λ* o conjunto vacío.

En palabras mas tecnicas se tiene que:

La **clausura de Kleene o estrella de Kleene o simplemente la estrella de un lenguaje A**, A ⊆ Σ*, es la unión de todas las potencias de A y se denota por A*.
De manera similar se define la **clausura positiva de un lenguaje** A, A ⊆ Σ*, la cual se denota por A+.

## Funcionalidades del Sistema
La aplicación (desarrollada en Python con Tkinter) implementa los siguientes módulos:

1. **Subcadenas, Prefijos y Sufijos:**
   * Cálculo exhaustivo de todas las subcadenas, prefijos y sufijos de una cadena de entrada.
   * Interfaz gráfica organizada para la visualización de resultados.
   * Funcionalidad para guardar los resultados obtenidos en un archivo de texto (.txt).

2. **Cerraduras de Kleene y Positiva:** 
   * Cálculo de la cerradura de Kleene ($\Sigma^*$) y la cerradura positiva ($\Sigma^+$) para un alfabeto definido.
   * Opción para especificar la longitud máxima de las cadenas a generar.
   * Visualización interactiva y opción de exportación de resultados.

## Instalación de entorno virtual
 **Instalación y Configuración de Python:** Antes de comenzar a utilizar **Tkinter** para desarrollar la interfaz gráfica de la práctica, es necesario tener Python instalado y configurado. Para ello, siga los siguientes pasos:

1.**Instalar Python**

* Descargue Python: Visite la página oficial de Python en https://www.python.org/downloads/.
* Instale Python: Ejecute el instalador. Durante la instalación, asegúrese de marcar la casilla **"Add Python to PATH"** para que Python se pueda ejecutar desde cualquier terminal.
* Verifique la Instalación : Una vez instalado, abra una terminal (símbolo del sistema en Windows o terminal en macOS/Linux) y ejecute el siguiente comando:

```
python --version
```

Esto debería mostrar la versión instalada de Python.

2.**Instalar Visual Studio Code**

Visual Studio Code (VS Code) es un entorno de desarrollo ligero y flexible que puede utilizar para programar en Python.
* Descargue VS Code: Diríjase al sitio oficial de Visual Studio Code y descargue la versión para su sistema operativo.
* Instale la Extensión de Python: Abra **VS Code**, diríjase a la pestaña de **Extensiones** (ícono de cubo en la barra lateral), busque e instale la extensión de **Python**. Esto habilitará herramientas adicionales como el resaltado de sintaxis y depuración para Python.

## Preparación del entorno virtual
1.**Crear un Entorno Virtual en Python**

Es recomendable trabajar en entornos virtuales para mantener las dependencias del proyecto aisladas. A continuación, se explica cómo crear un entorno virtual para su proyecto:
* Abra una terminal en Visual Studio Code.
* Navegue hasta la carpeta de su proyecto o cree una nueva carpeta para su proyecto con:

```
mkdir MiProyecto
cd MiProyecto
```

* Cree un entorno virtual ejecutando el siguiente comando:

```
python -m venv venv
```

Esto creará una carpeta llamada venv que contendrá su entorno virtual.

* Active el entorno virtual :
   * En Windows: ```venv\Scripts\activate```
   * En macOS/Linux: ```source venv/bin/activate```

* Verifique que el entorno está activado: El nombre del entorno (venv) debería aparecer al principio de la línea en su terminal.

2.**Instalar Tkinter**

Con el entorno virtual activado, instale el paquete de Tkinter, que es necesario para desarrollar la interfaz gráfica.
Para ello, ejecute el siguiente comando en la terminal:

   * En Windows: ```pip install tk```
   * En macOS/Linux: ```sudo apt-get install python3-tk   ```

**Probar un Programa Simple en Tkinter**
* Cree un archivo Python: En la carpeta de su proyecto, cree un archivo con el nombre **app.py**.
* Escriba el siguiente código básico en el archivo app.py para probar Tkinter:

 ```python
from tkinter import Tk, Label

app = Tk()
app.title("Hola mundo")
label = Label(app, text="¡Hola, mundo!")
label.pack()
app.mainloop()   
```

* Ejecute el archivo desde la terminal : ```python app.py```

* Verifique que se abre la aplicación: Esto debería abrir una ventana de navegador con el mensaje: **¡Hola Mundo!**

Recomendación
Asegúrese de activar el entorno virtual cada vez que trabaje en su proyecto, para garantizar que las dependencias se instalen correctamente en el entorno aislado.

Una vez listo nuestro compilador, nuestro lenguaje de programacion y las librerias que instalamos dentro de nuestro entorno virtual aislado pasaremos con la funcionalidad de nuestro codigo. 

# Funcionalidad del código
## Logica de las cadenas (Operaciones sobre cadenas)

### Prefijos: 
Un prefijo de una cadena $u$ es una cadena $v$ tal que existe una cadena $w$ donde $u = vw$. Por definición, la cadena vacía ($\lambda$) es el prefijo de toda cadena, y toda cadena es prefijo de sí misma.

**Implementacion del codigo**
```python
def get_prefixes(string):
    return [string[:i] for i in range(len(string) + 1)]
```
**Como funciona**
* La función ```range(len(string) + 1)``` genera índices desde $0$ hasta la longitud total de la cadena. El comando ```string[:i]``` (slicing) corta la palabra desde el inicio hasta la posición $i$.
* Cuando $i=0$, obtenemos una cadena vacía (representando $\lambda$). Cuando $i=n$, obtenemos la cadena completa.

### Sufijos: 
Un sufijo de una cadena $u$ es una cadena $v$ tal que existe una cadena $w$ donde $u = wv$. Al igual que los prefijos, $\lambda$ y la propia cadena $u$ son sufijos válidos.

**Implementacion del codigo**
```python
def get_suffixes(string):
    return [string[i:] for i in range(len(string) + 1)]
```
**Como funciona**: Similar a los prefijos, pero el corte se hace de forma inversa.
* El comando ```string[i:]``` le indica a Python: "toma todo desde la posición $i$ hasta el final".
* Al avanzar el índice $i$, el sufijo se va haciendo más pequeño hasta llegar a la posición final, donde el resultado es la cadena vacía.

### Subcadenas:
Una cadena $v$ es subcadena de $u$ si existen cadenas $x, y$ tales que $u = xvy$. En términos simples, es cualquier fragmento contiguo de la cadena original.

**Implementacion del codigo**
```python
def get_substrings(string):
    substrings = {""}  # Iniciamos con la cadena vacía (λ)
    n = len(string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(string[i:j])
    return sorted(list(substrings), key=len)
```

**Como funciona**:
* **Inicializacion**: Se crea un conjunto (set) llamado substrings inicializado con "". Esto cumple con la propiedad de que la cadena vacía es subcadena de cualquier cadena.
* **Doble Ciclo Anidado**: El ciclo exterior i marca el punto de partida del corte, mientras que el ciclo interior j marca el punto final.
* **Método** .add(): Al usar un conjunto, el programa garantiza que no habrá subcadenas repetidas (por ejemplo, en la palabra "banana").
* **Ordenamiento**: Finalmente, se convierte el conjunto en una lista y se aplica sorted(..., key=len) para organizar los resultados por tamaño, permitiendo una visualización jerárquica en la interfaz.

## Logica de las lenguajes (Operaciones sobre Lenguajes)
Este módulo implementa las operaciones de potencias de un alfabeto $\Sigma$ para generar conjuntos de cadenas según las reglas de los lenguajes formales.

### Detalles tecnicos de Implementacion
* **Uso de ```itertools```**: Se eligió esta librería estándar de Python porque es altamente eficiente para manejar combinaciones y permutaciones, evitando el uso de múltiples ciclos anidados manuales que aumentarían la complejidad computacional.
* **Concatenación**: Debido a que ```itertools.product``` devuelve tuplas $(ej: ('a', 'b'))$, utilizamos ```''.join(c)``` para unir esos caracteres en una sola cadena de texto $("ab")$ antes de mostrarla en la interfaz.

### Cerradura de Kleene
La cerradura de Kleene (o estrella de Kleene) de un alfabeto $\Sigma$, denotada como $\Sigma^*$, es el conjunto de todas las cadenas posibles que pueden formarse con los símbolos de $\Sigma$, incluyendo la cadena vacía ($\lambda$). Matemáticamente, es la unión infinita de todas las potencias del alfabeto:

$$\Sigma^* = \Sigma^0 \cup \Sigma^1 \cup \Sigma^2 \cup \dots \cup \Sigma^n$$

**Implementacion del codigo**
```python
def get_kleene_closure(alphabet, max_len):
    result = ["λ"] # Sigma^0: La cadena vacía siempre es el primer elemento
    for i in range(1, max_len + 1):
        # Genera el producto cartesiano del alfabeto elevado a la i
        combinations = itertools.product(alphabet, repeat=i)
        # Convierte las tuplas resultantes en cadenas y las agrega al conjunto
        result.extend([''.join(c) for c in combinations])
    return result
```

**Como funciona**:
* **Base ($\Sigma^0$)**: Se inicializa la lista con "λ", cumpliendo la definición de que la potencia cero de cualquier alfabeto es el conjunto que contiene únicamente la cadena vacía.
* **Producto Cartesiano**: Se utiliza itertools.product(alphabet, repeat=i). En matemáticas discretas, esto equivale a realizar el producto de $\Sigma$ consigo mismo $i$ veces ($\Sigma \times \Sigma \times \dots \times \Sigma$).
* **Iteración**: El ciclo for genera todas las palabras de longitud 1, luego todas las de longitud 2, y así sucesivamente hasta alcanzar el límite max_len.

### Cerradura Positiva
La cerradura positiva de un alfabeto $\Sigma$, denotada como $\Sigma^+$, es el conjunto de todas las cadenas posibles de longitud mayor o igual a 1. Formalmente, es la cerradura de Kleene excluyendo la cadena vacía:

$$\Sigma^+ = \Sigma^* - \{\lambda\} = \bigcup_{i=1}^{\infty} \Sigma^i$$

**Implementacion del codigo**
```python
def get_positive_closure(alphabet, max_len):
    result = [] # Se omite la cadena vacía al inicio
    for i in range(1, max_len + 1):
        combinations = itertools.product(alphabet, repeat=i)
        result.extend([''.join(c) for c in combinations])
    return result
```

**Como funciona**:
* **Diferencia Fundamental**: A diferencia de la función anterior, la lista result comienza vacía.
* **Generacion**: El proceso de combinación es idéntico, pero al iniciar el rango en 1, garantizamos que todas las cadenas generadas tengan al menos un símbolo del alfabeto original.

## Interfaz Grafica (main.py)
### Inicializacion y Estructura de la clase ```App```

El uso de una clase permite encapsular el estado de la aplicación (los datos de entrada y las áreas de resultado) y organizar el código siguiendo el paradigma de Programación Orientada a Objetos (POO).

**Implementacion del codigo**
```python
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Practica 1: Teoria de la Computacion - ESCOM")
        self.root.geometry("800x700")
        self.root.configure(bg="#0f172a")
```

**Como funciona**:
* El constructor __init__ define las propiedades de la ventana principal, como el título de la práctica, el tamaño inicial y el esquema de colores "Dark Mode" para mejorar la estética y legibilidad.

### Navegación por Pestañas ```Attk.Notebookp```

En interfaces de usuario, un Notebook permite la multitarea organizada. Cada pestaña representa un contexto lógico diferente (en este caso, Cadenas vs. Lenguajes).

**Implementacion del codigo**
```python
self.notebook = ttk.Notebook(self.root)
style.configure("TNotebook.Tab", background="#1e293b", foreground="white")
```

**Como funciona**:
* Se crea el control de pestañas y se personaliza mediante ```ttk.Style```. Se definen dos marcos ```(tab1 y tab2)``` que separan el cálculo de Subcadenas de la generación de Cerraduras.

### Captura de Datos y Ejecución de Lógica
Un sistema computacional sigue el ciclo: Entrada $\rightarrow$ Procesamiento $\rightarrow$ Salida. Aquí, la entrada son objetos ```tk.Entry``` y el procesamiento son las funciones importadas de los archivos ```logic```.

**Implementacion del codigo**
```python
def solve_ej1(self):
    s = self.entry_string.get() # Entrada
    if not s:
        messagebox.showwarning("Error de entrada", "Debes ingresar una cadena...")
        return
    
    pref = get_prefixes(s) # Procesamiento (Lógica de cadenas)
    # ... (Sufijos y Subcadenas)
    
    self.text_res1.insert(tk.END, res_txt) # Salida (Interfaz)
```

**Como funciona**:
* **Validacion**: Se verifica que la entrada no esté vacía para evitar errores matemáticos sobre el conjunto nulo no deseado.
* **Calculo**: Se mandan llamar las funciones que ya explicamos en los módulos de lógica.
* **Visualizacion**: Se utiliza un componente ```tk.Text``` con fuente Consolas para mostrar los resultados de manera monospaciada, ideal para ver conjuntos de cadenas.

### Persistencia y Ventanas Emergentes ```messagebox```
La robustez de un software se mide en cómo maneja errores y cómo informa al usuario sobre el estado del sistema.

**Implementacion del codigo**
```python
try:
    with open("ejercicio1_cadenas.txt", "w", encoding="utf-8") as f:
        f.write(res_txt)
    messagebox.showinfo("Operacion Exitosa", "Los calculos se guardaron...")
except Exception as e:
    messagebox.showerror("Error de Archivo", f"No se pudo guardar: {e}")
```

**Como funciona**:
* **Manejo de Archivos**: Se utiliza el manejador de contexto ```with``` para abrir y escribir archivos ```.txt```. Esto asegura que los resultados se guarden físicamente en el disco.
* **Manejo de mensajes**: Se utilizan ```messagebox.showinfo``` (ventanas azules) para confirmar el éxito y ```messagebox.showerror``` (ventanas rojas) si ocurre un error inesperado (como falta de permisos en la carpeta).

### Resumen Estetico
* **Estilos Dinamicos** Se utilizó ```style.map``` para que las pestañas cambien de color al ser seleccionadas (#38bdf8), indicando visualmente al usuario en qué ejercicio se encuentra.

## Como es que se debe ejecutar y utilizar
### Primeros pasos
Lo primero que haremos sera como anteriormente lo habiamos explicado crear nuestro entorno virtual, instalar Tkinter dentro de nuestro entorno virtual para estar listos para poder ejecutar el programa y asi ver la interfaz grafica.

Una vez creado nuestro entorno virtual y la libreria de Tkinter estamos listos para ejecutar el comando dentro de la terminal para compilar asi nuestro archivo principal que seria el comando: 

```
python3 main.py
```

Se desplegara la interfaz grafica con la pestaña de logica de cadenas, que nos permitira calcular el **sufijo, prefijo y subcadena**.
* El usuario debera introducir una cadena de la longitud que sea necesaria. 
* Una vez ingresada la cadena se mostraran los resultados dentro de la misma interfaz grafica e importarlos dentro de un documento de texto, ```.txt```.

Dentro de la otra pestaña tenemos la de logica de lenguajes que nos permitira calcular **Cerradura de Kleene y la Cerradura Positiva**.
* El usuario debera introducir el  alfabeto separado por comas cada uno de los simbolos que se introduzcan, para despues pedir la longitud maxima que se podran tener en las cadenas. 
* Una vez ingresada la informacion generaremos los lenguajes que se mostraran dentro de la interfaz grafica e igual se exportaran dentro de un documento de texto ```.txt```.
