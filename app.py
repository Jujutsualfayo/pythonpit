def append_write(filename="", text=""):
    with open(filename, "a", encoding= "utf-8") as f:
        return f.append(text)

