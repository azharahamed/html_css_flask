def alphabet_position(letter):
  char = letter.lower()
  return ord(char)-97

def rotate_character(char,rot):
  new_position = (alphabet_position(char)+rot)%26 if char.isalpha() else ord(char)
  return chr(new_position+97) if char.islower() else chr(new_position+65)  if char.isupper() else chr(new_position) 

def encrypt(text, rot):
  a_list = [char for char in text]
  return_text = ''.join(rotate_character(item,rot) for item in a_list)
  return return_text