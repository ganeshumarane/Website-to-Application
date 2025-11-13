import reflex as rx
import asyncio


class ProductState(rx.State):
    _all_products: list[dict[str, str]] = [
        {"name": "Zenitsu's Thunder Breathing", "image": "/yellow_zenitsu_demon.png"},
        {"name": "Yuji's Cursed Strike", "image": "/energy_red_yuji.png"},
        {"name": "Sukuna's Cursed Smirk", "image": "/placeholder.svg"},
        {"name": "Gon's Determined Gaze", "image": "/placeholder.svg"},
        {"name": "Killua's Lightning Charge", "image": "/placeholder.svg"},
        {"name": "Kaneki's Half-Mask Portrait", "image": "/placeholder.svg"},
        {"name": "Ichigo's Zangetsu Blade", "image": "/placeholder.svg"},
        {"name": "Kakashi's Moonlit Reading", "image": "/placeholder.svg"},
        {"name": "Zoro's Three-Sword Style", "image": "/placeholder.svg"},
        {"name": "Mikasa's Windblown Scarf", "image": "/placeholder.svg"},
        {"name": "Eren Yeager's Titan Form", "image": "/placeholder.svg"},
        {"name": "Gojo Satoru's Infinity", "image": "/placeholder.svg"},
        {"name": "Naruto's Rasengan", "image": "/placeholder.svg"},
        {"name": "Sasuke's Chidori", "image": "/placeholder.svg"},
    ]
    products: list[dict[str, str]] = _all_products[:8]
    is_loading: bool = False
    show_drawer: bool = False
    show_search_modal: bool = False
    search_term: str = ""

    @rx.event
    def toggle_drawer(self):
        self.show_drawer = not self.show_drawer

    @rx.event
    def set_show_drawer(self, value: bool):
        self.show_drawer = value

    @rx.event
    def toggle_search_modal(self):
        self.show_search_modal = not self.show_search_modal

    @rx.event
    def set_show_search_modal(self, value: bool):
        self.show_search_modal = value

    @rx.event
    async def load_more(self):
        self.is_loading = True
        yield
        await asyncio.sleep(1.5)
        current_len = len(self.products)
        if current_len < len(self._all_products):
            self.products.extend(self._all_products[current_len : current_len + 4])
        self.is_loading = False

    @rx.var
    def filtered_products(self) -> list[dict[str, str]]:
        if not self.search_term:
            return self._all_products
        return [
            p
            for p in self._all_products
            if self.search_term.lower() in p["name"].lower()
        ]