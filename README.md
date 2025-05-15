# AirBnB Clone - The Console

## 📘 Description

This project is the first step towards building a full-stack clone of the [AirBnB](https://www.airbnb.com) web application. It is part of the ALX Software Engineering program. 

The goal is to build a command-line interface (CLI) that serves as the foundation for managing data models, persisting data to files, and laying the groundwork for future API and frontend development.

The console interprets user commands to create, retrieve, update, and destroy instances of various data models including:

- `BaseModel`
- `User`
- `Place`
- `State`
- `City`
- `Amenity`
- `Review`

## 🖥️ The Command Interpreter

### 🔧 How to Start It

1. Clone the repository:
   ```bash
   git clone https://github.com/<jujutsualfayo>/AirBnB_clone.git
   cd AirBnB_clone

   Run the console:
./console.py
Or if not executable:

python3 console.py
💡 How to Use It
Once started, the console allows you to enter commands to interact with the backend models. It supports both standard and advanced command syntax.

Supported Commands:
Command	Description
create <class_name>	Creates a new instance of <class_name> and prints the id
show <class_name> <id>	Displays the string representation of an instance
destroy <class_name> <id>	Deletes an instance
all [<class_name>]	Displays all instances or all instances of a class
update <class_name> <id> <attr_name> <attr_value>	Updates an attribute of an instance
quit or EOF	Exits the program

You can also use the dot notation:

<class name>.all()

<class name>.count()

<class name>.show(<id>)

<class name>.destroy(<id>)

<class name>.update(<id>, <attribute name>, <attribute value>)

<class name>.update(<id>, <dictionary>)

✅ Examples

(hbnb) create User
<uuid>

(hbnb) show User 1234-1234-1234
[User] (1234-1234-1234) {'id': '1234-1234-1234', ...}

(hbnb) update User 1234-1234-1234 name "John Doe"

(hbnb) all User
["[User] (1234-1234-1234) {...}"]

(hbnb) destroy User 1234-1234-1234

(hbnb) quit
📂 File Storage
All data is stored in file.json and serialized using JSON format. This ensures persistence between sessions of the command interpreter.

✍️ Author
Benjamin Otieno Alfayo — GitHub: @Jujutsualfayo

📜 License
This project is part of the ALX SE curriculum and is intended for educational purposes.










