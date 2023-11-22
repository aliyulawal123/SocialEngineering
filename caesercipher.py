
print("++++++++++++++++++++Output Caeser Cipher with 3 shifts++++++")
def caesar_cipher(text, shift):
  result = ''

  for char in text:
      if char.isalpha():
          # Determine whether the character is uppercase or lowercase
          is_upper = char.isupper()

          # Shift the character by the specified amount
          char_code = ord(char)
          char_code = (char_code - ord('A' if is_upper else 'a') + shift) % 26
          char_code += ord('A' if is_upper else 'a')

          result += chr(char_code)
      else:
          # If the character is not a letter, leave it unchanged
          result += char

  return result

# Example usage:
plaintext = "a"
shift_amount = 3
ciphered_text = caesar_cipher(plaintext, shift_amount)
print(f"Original text: {plaintext}")
print(f"Ciphered text: {ciphered_text}")
