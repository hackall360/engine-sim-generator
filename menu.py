import curses
from curses import wrapper

class Item:
    def __init__(self, name, submenu):
        self.name = name
        self.submenu = submenu



def main(stdscr):
    # Desativar o cursor
    curses.curs_set(0)

    camshaft = Item("< Camshaft >", ["camshaft-submenu-item1", "camshaft-submenu-item2", "camshaft-submenu-item3", "camshaft-submenu-item4"])
    bank = Item("< Bank >", ["bank-submenu-item1", "bank-submenu-item2", "bank-submenu-item3"])
    transmission = Item("< Transmission >", ["transmission-submenu-item1", "transmission-submenu-item2"])
    engine = Item("< Engine >", ["engine-submenu-item1", "engine-submenu-item2"])
    vehicle = Item("< Vehicle >", ["vehicle-submenu-item1", "vehicle-submenu-item2"])


    # Obter altura e largura da tela
    h, w = stdscr.getmaxyx()

    # Criar uma nova janela para o menu
    menu_win = curses.newwin(h, w, 0, 0)

    # Opções do menu
    menu_items = [camshaft.name, bank.name, transmission.name, engine.name, vehicle.name]

    current_item = 0

    # Função para desenhar o menu
    def draw_menu(menu_items, edit_mode = False):
        menu_win.clear()
        for i, item in enumerate(menu_items):
            if i == current_item:
                menu_win.addstr(i, 0, item, curses.A_REVERSE)
            else:
                menu_win.addstr(i, 0, item)
            menu_win.refresh()

    # Desenhar o menu inicial
    draw_menu(menu_items)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_item = max(0, current_item - 1)
        elif key == curses.KEY_DOWN:
            current_item = min(len(menu_items) - 1, current_item + 1)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_item == len(menu_items) - 1:
                break

        draw_menu()

wrapper(main)
