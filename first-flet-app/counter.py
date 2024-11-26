import flet as ft

def main(page: ft.Page):
    page.title = "はじめてのFletアプリ"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # カウント表示用のテキストフィールド
    txt_number = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        width=100
    )

    # マイナスボタンの処理
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    # プラスボタンの処理
    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    # レイアウトの構築
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)