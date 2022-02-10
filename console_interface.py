from consolemenu import *
from consolemenu.items import *

# Create the menu
from user_control import sign_in_up

menu = ConsoleMenu("Welcome to Spotipy!")
selection_menu = SelectionMenu(["Login", "Register"])
selection_menu.show()
function_item1 = FunctionItem("Login", sign_in_up.login())
function_item2 = FunctionItem("Register", sign_in_up.register())
selection_menu.append_item(function_item1)
selection_menu.append_item(function_item2)

# Create some items
menu.show()
selection_menu.show()
# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
function_item = FunctionItem("Login", sign_in_up.login(), ["Enter an input"])

# A CommandItem runs a console command
command_item = CommandItem("Run a console command", "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()

def main():
    menu = ConsoleMenu("Welcome to Spotipy!")
    selection_menu = SelectionMenu(["Login", "Register"])
    selection_menu.show()
    function_item1 = FunctionItem("Login", sign_in_up.login())
    function_item2 = FunctionItem("Register", sign_in_up.register())
    selection_menu.append_item(function_item1)
    selection_menu.append_item(function_item2)


if __name__ == '__main__':
    main()