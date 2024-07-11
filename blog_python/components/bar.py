import reflex as rx


def bar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
                "Flora",
                font_size="3rem",
                padding=".5rem",
                color="gold",
                _hover={
                    "cursor": "pointer",
                    "color": "yellowgreen",
                },
                width="10rem",
            ),
        ),
        rx.box(
            rx.hstack(
                rx.text(
                    "Branco",
                    _hover={
                        "cursor": "pointer",
                        "color": "lawngreen",
                    },
                ),
                rx.text(
                    "Amarelo",
                    _hover={
                        "cursor": "pointer",
                        "color": "lawngreen",
                    },
                ),
                rx.text(
                    "Azul",
                    _hover={
                        "cursor": "pointer",
                        "color": "lawngreen",
                    },
                ),
                rx.text(
                    "Panorama",
                    _hover={
                        "cursor": "pointer",
                        "color": "lawngreen",
                    },
                ),
                rx.text(
                    "Macro",
                    _hover={
                        "cursor": "pointer",
                        "color": "lawngreen",
                    },
                ),
                justify_content="flex-end",
            ),
            align_item="flex-end",
            font_size="1.5rem",
            padding="1rem",
            padding_top="1.5rem",
            color="lightblue",
            margin_right="1.5rem",
        ),
        background_color="green",
        height="5rem",
        display="flex",
        grid_template_columns="5rem 80%",
        justify_content="space-between",
        width='100%',
        padding="0px",
        margin='0px'
    )
