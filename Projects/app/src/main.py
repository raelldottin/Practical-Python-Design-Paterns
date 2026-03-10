"""
Build one screen: title, subtitle, one button
"""
import flet as ft

def main(page: ft.Page):
    page.title = "app"
    page.appbar = ft.AppBar(
        title=ft.Column(
            [
                ft.Text("title", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("subtitle", size=12),
            ],
            spacing=0,
        )
    )
    page.add(
        ft.Button(
            "Button"
        )
    )


if __name__ == "__main__":
    ft.run(main)
