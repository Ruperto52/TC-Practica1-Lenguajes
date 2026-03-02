import flet as ft

def main(page: ft.Page):
    page.title = "Práctica 1: Operaciones sobre Lenguajes"
    page.add(ft.Text("Aplicación iniciada correctamente"))

if __name__ == "__main__":
    ft.app(target=main)