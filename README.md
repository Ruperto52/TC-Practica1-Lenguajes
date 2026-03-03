# Práctica 1: Operaciones Básicas sobre Lenguajes con Interfaz Gráfica

## Información de los Integrantes
* **Institución:** Instituto Politécnico Nacional (IPN)
* **Escuela:** Escuela Superior de Cómputo (ESCOM) 
* **Unidad de Aprendizaje:** Teoría de la Computación 
* **Programa Académico:** Ingeniería en Sistemas Computacionales / Plan 2020 
* **Grupo:** 4CM4
* **Alumnos:** * Diego Ruperto Hernandez (Boleta: 2024630696)
    * Maria Jose Venegas Martinez (Boleta: 2024630831)

---

## 🎯 Objetivo
El propósito de esta práctica es explorar los conceptos fundamentales de lenguajes formales mediante el desarrollo de una aplicación con interfaz gráfica.Se implementará un software para resolver problemas específicos sobre lenguajes y sus operaciones básicas.
## Introduccion 
En esta practica exploraremos los conceptos de: **Subcadenas, Prefijos y Sufijos** y **Cerraduras de Kleene y Positiva**, estos son conceptos basicos del tema de **Lenguajes Formales**, para recapitular tenemos las definiciones de ambos temas.
 1. **Subcadenas, Prefijos y Sufijos**
Una subcadena es una secuencia de caracteres que aparecen de manera consecutiva dentro de otra cadena de texto, respetando el orden original y sin saltarse ningún elemento.
Los prefijos están formados por los primeros símbolos de la cadena; y los sufijos, por los últimos.Un prefijo o sufijo de una cadena que no sea la misma cadena es un prefijo y sufijos propios.
En palabras mas tecnicas se tiene que:
Una cadena v es una subcadena o una subpalabra de u si existen cadenas x, y tales que u = xvy. Nótese que x o y pueden ser λ y, por lo tanto, la cadena vacía es una subcadena de cualquier cadena.
Un prefijo de u es una cadena v tal que u = vw para alguna cadena w ∈ Σ*
Se dice que v es un prefijo propio si v 6= u.
Similarmente, un sufijo de u es una cadena v tal que u = wv para alguna cadena w ∈ Σ*
Obsérvese que λ es un prefijo y un sufijo de toda cadena u ya que uλ = λu = u.
Por la misma razón, toda cadena u es prefijo y sufijo de sí misma.

 2. **Cerraduras de Kleene y Positiva**
La cerradura de Kleene en un alfabeto se refiere a todas combinaciones de las cadenas de caracteres o palabras que se pueden formar incluyendo λ o conjunto vacío.
Por otro lado la cerradura positiva en un alfabeto se refiere a todas las combinasiones de las cadenas de caracteres o palabras que se pueden formar con ese alfabeto, excluyendo a λ o conjunto vacío.
En palabras mas tecnicas se tiene que:
La clausura de Kleene o estrella de Kleene o simplemente la estrella de un lenguaje A, A ⊆ Σ*, es la unión de todas las potencias de A y se denota por A*.
De manera similar se define la clausura positiva de un lenguaje A, A ⊆ Σ*, la cual se denota por A+.

## 🛠️ Funcionalidades del Sistema
La aplicación (desarrollada en Python con Flet) implementa los siguientes módulos:

1. **Subcadenas, Prefijos y Sufijos:**
   * Cálculo exhaustivo de todas las subcadenas, prefijos y sufijos de una cadena de entrada.
   * Interfaz gráfica organizada para la visualización de resultados.
   * Funcionalidad para guardar los resultados obtenidos en un archivo de texto (.txt).

2. **Cerraduras de Kleene y Positiva:** 
   * Cálculo de la cerradura de Kleene ($\Sigma^*$) y la cerradura positiva ($\Sigma^+$) para un alfabeto definido.
   * Opción para especificar la longitud máxima de las cadenas a generar.
   * Visualización interactiva y opción de exportación de resultados.
