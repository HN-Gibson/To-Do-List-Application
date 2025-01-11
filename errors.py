#created a custom error to catch empty inputs
class UserInputEmpty(Exception):
    pass
    def handle_user_input_empty():
        print("\nInput was empty.\nPlease enter a command.\n")

#created a custom error to catch when user inputs a command not on the list
class CommandNotFound(Exception):
    pass
    def handle_command_not_found():
        print("\nInput doesn't match available commands.\nPlease enter command from menu.\n")
