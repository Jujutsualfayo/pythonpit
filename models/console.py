#!/usr/bin/python3
"""
This module contains the entry point for the HBNB command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program (e.g., Ctrl+D)."""
        print()  # Prints a newline for a clean exit
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def help_quit(self):
        """Help information for quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help information for EOF command."""
        print("EOF command to exit the program (Ctrl+D)")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
