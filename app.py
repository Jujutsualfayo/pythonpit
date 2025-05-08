def write_file(filename="", text=""):
    with open(filename, "w", encoding= "utf-8") as f:
        print(f.write(text))

