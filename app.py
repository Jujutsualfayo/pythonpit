import cmd
class HelloWorld(cmd.Cmd):
    def greet(self, line):
        print("Hello Benjamin")
    def EoF(self, line):
        return True
if __name__ == "__main__":
    HelloWorld().cmdloop()