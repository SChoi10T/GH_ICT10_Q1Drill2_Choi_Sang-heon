from pyscript import display, document # pyright: ignore[reportMissingImports]


def student_profile(e):
    document.getElementById('output').innerHTML = ""

    name = document.getElementById('name').value
    age = document.getElementById('age').value
    school = document.getElementById('school').value

    if not name or not age or not school:
        display("Enter the following information.", target="output")
        return

    message = f'''Student Profile
    Name:\t{name}
    Age:\t{age}
    School:\t{school}

    Notes:
    \"{name}\" is currently {age} years old and studies at {school}.
    This information was gathered through input fields and displayed using
    a multiline string in Python via Pyscript.
    '''
    
    display(message, target="output")