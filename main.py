def main():
  path_to_file = "books/frankenstein.txt"
  text = get_book_text(path_to_file)
  num_words = get_num_words(text)
  chars_dict = get_chars_dict(text)
  create_report(chars_dict, path_to_file, num_words)


def get_num_words(phrase):
  words = phrase.split()
  return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
  count_dict = {}
  for t in text:
    lower_t = t.lower()
    if lower_t in count_dict:
      count_dict[lower_t] += 1
    else:
      count_dict[lower_t] = 1
  return count_dict

def sort_on(dict):
    return dict["num"]

def create_report(chars_dict, file_name, num_words):
  print(f"--- Begin report of {file_name} ---")
  print(f"{num_words} words found in the document")
  print(" ")
  list_of_dicts = [{"char": k, "num": v} for k, v in chars_dict.items()]
  list_of_dicts.sort(reverse=True, key=sort_on)
  for d in list_of_dicts:
    if d["char"].isalpha():
      print(f"The '{d['char']}' character was found {d['num']} times")
  print("--- End report ---")
  

   

   
main()