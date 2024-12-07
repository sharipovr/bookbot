def main():
  with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    return file_contents

def count_words(content):
  arr = content.split(' ')
  return len(arr)


def count_chars(content):
  char_map = {}

  for char in content.lower():
    char_map[char] = char_map.get(char, 0) + 1

  return char_map

def print_char_map(char_map):
  for key, value in char_map.items():
    print(f"The '{key}' character was found {value} times")

content = main()
# print(count_words(content))
# print(count_chars(content))
char_map = count_chars(content)
print_char_map(char_map)