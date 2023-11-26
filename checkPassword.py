""" Check Password Strength"""

def check_password_strength(password):
  # Rule 1: Password length should be at least 8 characters
  if len(password) < 8:
      return "Weak: Password should be at least 8 characters long."

  # Rule 2: Password should contain a mix of uppercase and lowercase letters
  if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
      return "Moderate: Include a mix of uppercase and lowercase letters."

  # Rule 3: Password should contain at least one digit
  if not any(char.isdigit() for char in password):
      return "Moderate: Include at least one digit."

  # Rule 4: Password should contain at least one special character
  special_characters = "!@#$%^&*()-_+=<>,.?/:;{}[]|"
  if not any(char in special_characters for char in password):
      return "Strong: Include at least one special character."

  # If all rules are satisfied
  return "Very Strong: Password meets all criteria for strength."

# User Input
user_password = input("Enter your password: ")

# Check Password Strength
result = check_password_strength(user_password)

# Display Result
print("\nPassword Strength:", result)
