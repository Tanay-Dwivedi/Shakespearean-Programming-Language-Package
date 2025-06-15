def shakespearean_compiler(file_path):
    replacements = {
        "proclaim": "print",
        "hark": "input",
        "an ": "if ",
        "else, an ": "elif ",
        "else": "else",
        "whilst": "while",
        "for each": "for",
        "cease": "break",
        "onward": "continue",
        "declare a rite": "def",
        "deliver hence": "return",
        "trueth": "True",
        "falsehood": "False",
        "wholecount ": "",
        "driftcount ": "",
        "wordlace ": ""
    }

    with open(file_path, 'r') as file:
        code = file.read()

    for old, new in replacements.items():
        code = code.replace(old, new)

    exec(code, globals())


# Run the Shakespearean Program
shakespearean_compiler("prog.spl")
