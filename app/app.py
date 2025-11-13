import reflex as rx
from app.states.product_state import ProductState


def skeleton_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(class_name="bg-gray-200 rounded-lg aspect-[2/3] animate-pulse"),
        rx.el.div(class_name="mt-4 h-6 bg-gray-200 rounded w-3/4 animate-pulse"),
        rx.el.div(class_name="mt-2 h-4 bg-gray-200 rounded w-1/2 animate-pulse"),
        class_name="w-full",
    )


def product_card(product: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=product["image"], class_name="w-full h-full object-cover rounded-lg"
            ),
            class_name="bg-gray-100 rounded-lg overflow-hidden aspect-[2/3]",
        ),
        rx.el.h3(
            product["name"],
            class_name="mt-4 text-lg font-semibold text-gray-800 font-['Lora']",
        ),
        rx.el.p(
            "Product Page Colours Available ...",
            class_name="mt-1 text-sm text-gray-500",
        ),
        class_name="cursor-pointer group transform hover:scale-105 transition-transform duration-300",
    )


def search_modal() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
            ),
            rx.radix.primitives.dialog.content(
                rx.el.div(
                    rx.icon("search", class_name="h-5 w-5 text-gray-400"),
                    rx.el.input(
                        placeholder="Search for products...",
                        on_change=ProductState.set_search_term,
                        class_name="w-full bg-transparent focus:outline-none text-lg",
                        autofocus=True,
                    ),
                    class_name="flex items-center gap-4 border-b pb-4",
                ),
                rx.el.div(
                    rx.foreach(
                        ProductState.filtered_products,
                        lambda p: rx.el.a(
                            rx.el.div(
                                rx.image(
                                    src=p["image"],
                                    class_name="h-12 w-12 rounded-md object-cover",
                                ),
                                rx.el.div(
                                    rx.el.p(p["name"], class_name="font-semibold"),
                                    rx.el.p(
                                        "In Stock", class_name="text-sm text-gray-500"
                                    ),
                                ),
                            ),
                            href="#",
                            class_name="flex items-center gap-4 p-2 rounded-lg hover:bg-gray-50",
                        ),
                    ),
                    class_name="mt-4 max-h-[60vh] overflow-y-auto",
                ),
                class_name="fixed top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/4 bg-white rounded-xl shadow-2xl p-6 w-full max-w-2xl z-50",
            ),
        ),
        open=ProductState.show_search_modal,
        on_open_change=ProductState.set_show_search_modal,
    )


def mobile_drawer() -> rx.Component:
    return rx.radix.primitives.drawer.root(
        rx.radix.primitives.drawer.portal(
            rx.radix.primitives.drawer.overlay(
                class_name="fixed inset-0 bg-black/30 z-40"
            ),
            rx.radix.primitives.drawer.content(
                rx.el.div(
                    rx.el.div(
                        rx.icon("zap", class_name="h-6 w-6 text-yellow-400"),
                        rx.el.span(
                            "STYLESWAP", class_name="font-bold text-xl font-['Lora']"
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.radix.primitives.drawer.close(
                        rx.icon("x", class_name="h-6 w-6")
                    ),
                    class_name="flex justify-between items-center p-4 border-b",
                ),
                rx.el.div(
                    rx.el.a(
                        "HOME",
                        href="#",
                        class_name="block py-3 px-4 text-lg hover:bg-gray-50",
                    ),
                    rx.el.a(
                        "ABOUT",
                        href="#",
                        class_name="block py-3 px-4 text-lg hover:bg-gray-50",
                    ),
                    rx.el.a(
                        "CONTACT US",
                        href="#",
                        class_name="block py-3 px-4 text-lg hover:bg-gray-50",
                    ),
                    class_name="mt-4",
                ),
                class_name="bg-white h-full w-4/5 max-w-sm z-50",
            ),
        ),
        direction="left",
        open=ProductState.show_drawer,
        on_open_change=ProductState.set_show_drawer,
    )


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.button(
                rx.icon("menu", class_name="h-6 w-6"),
                on_click=ProductState.toggle_drawer,
                class_name="md:hidden",
            ),
            rx.el.div(
                rx.icon("zap", class_name="h-6 w-6 text-yellow-400"),
                rx.el.span("STYLESWAP", class_name="font-bold text-xl font-['Lora']"),
                class_name="flex items-center gap-2",
            ),
            rx.el.button(
                rx.icon("search", class_name="h-6 w-6"),
                on_click=ProductState.toggle_search_modal,
                class_name="",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16 border-b",
        )
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    "HOME",
                    href="#",
                    class_name="text-sm text-gray-600 hover:text-black",
                ),
                rx.el.a(
                    "ABOUT",
                    href="#",
                    class_name="text-sm text-gray-600 hover:text-black",
                ),
                rx.el.a(
                    "CONTACT US",
                    href="#",
                    class_name="text-sm text-gray-600 hover:text-black",
                ),
                class_name="flex items-center gap-6",
            ),
            rx.el.div(
                rx.el.p("© 2025", class_name="text-sm text-gray-600"),
                rx.icon("zap", class_name="h-4 w-4 text-yellow-400"),
                rx.el.span("STYLESWAP", class_name="font-bold text-sm font-['Lora']"),
                rx.el.p("| Designed by Ganesh", class_name="text-sm text-gray-600"),
                class_name="flex items-center gap-2 mt-4 md:mt-0",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-8 flex flex-col md:flex-row items-center justify-between border-t",
        )
    )


def index() -> rx.Component:
    return rx.el.main(
        header(),
        mobile_drawer(),
        search_modal(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Your One Stop Hub for Fashion, Trends, and Custom Designs.",
                    class_name="text-4xl md:text-5xl font-bold text-gray-900 text-center font-['Lora']",
                ),
                rx.el.p(
                    "Features stylish apparel, creative designs, and daily inspiration. Discover unique outfits and express your style with StyleSwap!",
                    class_name="mt-4 max-w-2xl mx-auto text-center text-gray-600",
                ),
                class_name="py-16 md:py-24",
            ),
            rx.el.div(
                rx.foreach(ProductState.products, product_card),
                rx.cond(
                    ProductState.is_loading,
                    rx.fragment(
                        skeleton_card(),
                        skeleton_card(),
                        skeleton_card(),
                        skeleton_card(),
                    ),
                    None,
                ),
                class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-6 gap-y-12",
            ),
            rx.el.div(
                rx.cond(
                    ProductState.products.length() < 14,
                    rx.el.button(
                        rx.cond(
                            ProductState.is_loading,
                            rx.el.span("Loading...", class_name="animate-pulse"),
                            rx.el.span("Load More"),
                        ),
                        on_click=ProductState.load_more,
                        disabled=ProductState.is_loading,
                        class_name="bg-yellow-400 text-gray-900 font-semibold px-8 py-3 rounded-full hover:bg-yellow-500 transition-colors shadow-md hover:shadow-lg disabled:opacity-50 disabled:cursor-not-allowed",
                    ),
                    rx.el.p("You've reached the end!", class_name="text-gray-500"),
                ),
                class_name="text-center mt-16",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 pb-16",
        ),
        footer(),
        class_name="font-['Inter'] bg-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Lora:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")