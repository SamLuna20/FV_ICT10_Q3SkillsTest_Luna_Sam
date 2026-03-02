from pyscript import document, display

def check(e):
    document.getElementById('resultU').innerHTML = "" # resets resultU id data
    
    # accessing user's answer
    fullname = document.getElementById("name").value
    username = document.getElementById("user").value
    password = document.getElementById("pass").value

    # variables for checking
    pwdMessage = "" # for password error message
    isValidUsername = False
    hasLetter = False
    hasNumber = False

    # Check if fields are empty
    if fullname == "" or username == "" or password == "":
        document.getElementById('result').innerHTML = "Error: All fields are required."
        return

    # fullname requirement check
    if fullname != fullname.title():
        document.getElementById("resultN").innerHTML = "Error: Full Name must use Proper Capitalization (Title Case)."
    else:
        document.getElementById("resultN").innerHTML = "Valid name input."

    # username requirement check
    if len(username)>= 7:
        isValidUsername = True
        document.getElementById("resultU").innerHTML = "Valid username input."
    if not isValidUsername:
        document.getElementById("resultU").innerHTML = "Username is too short. Must be at least 7 characters long."

    # password requirement check
    for letter in password:
        if letter.lower() in "abcdefghijklmnopqrstuvwxyz": # check if there's a character present
            hasLetter = True
            document.getElementById("resultP").innerHTML = "Password contains character/s."
        if letter.isdigit(): # check if there's a number present
            hasNumber = True
            document.getElementById("resultP1").innerHTML = "Password contains number/s."
    if not hasNumber:
        pwdMessage += " Password does not contain at least one number."
    if not hasLetter:
        pwdMessage += " Password does not contain at least one letter."
    if len(password)<10:
        pwdMessage += f" Password too short. Add at least {10-len(password)} more character/s to proceed."
    document.getElementById("resultP2").innerHTML = pwdMessage