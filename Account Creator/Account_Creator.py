def generateUsername(fullName, startYear):
    # Generate the username based on the first name, last name, and starting year
    splitName = fullName.split()
    
    # Ensure there are at least two names (first and last)
    if len(splitName) < 2:
        return "Invalid name format"  # Handle cases with no last name

    firstName = splitName[0]
    lastName = splitName[1]

    # Create username in the format: "{lastName}{startYear[2:]}{firstName[0].upper()}"
    username = f"{startYear[2:]}{lastName.capitalize()}{firstName[0].upper()}"
    
    return username

def calculateYearGroup(username):
    # Calculate the year group based on the starting year extracted from the username
    try:
        startYear = int("20" + username[:2])  # Get the starting year from the username
        currentYear = 2024  # Update to the current year as needed
        yearGroup = currentYear - startYear + 7
        return f"Year {yearGroup}"
    except ValueError:
        return "Invalid username format"

def getPassword():
    # Ask the user to enter a password and check if it's secure
    password = input("Enter a password: ")
    while not isPasswordSecure(password):
        password = input("Password was not secure, please try again: ")
    return password

def isPasswordSecure(password):
    # Check if the password meets all required conditions
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in password):
        return False
    return True

def menu():
    fullName = input("Enter your full name (first and last name separated by a space): ")
    startYear = input("Enter your starting year (e.g. 2024): ")
    
    username = generateUsername(fullName, startYear)
    
    if "Invalid" in username:  # Check for errors in username generation
        print(username)
        return
    
    yearGroup = calculateYearGroup(username)
    password = getPassword()
    
    print(f"Username: {username}")
    print(f"Year Group: {yearGroup}")
    print("Password successfully set.")
    


menu()