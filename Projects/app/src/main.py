"""
Build a login screen. Email field, password field, login button. No validation. No logic. UI only.
"""
import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=400,
            height=800,
            content=ft.Row(
        [
            ft.TextField(label="Email", filled=True),
            ft.TextField(label="Password", filled=True),
            ft.Button("Login")
        ],
        ))
    )


if __name__ == "__main__":
    ft.run(main)
