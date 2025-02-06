def user_name():
    email = input("Enter your email: ").strip()  # Get email input and remove extra spaces
    if "@" in email:
        username = email.split("@")[0]  # Extract the part before '@'
        print("Your username is:", username)
        return username
    else:
        print("Invalid email format. Please enter a valid email.")
        return None

# Call the function
user_name()