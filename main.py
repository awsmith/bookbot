def main():
        pathToBook = "./books/frankenstein.txt"
        data = get_book_text(pathToBook)
        print(f"--- Begin report of {pathToBook}")
        print(f"{count_words(data)} words found in the document\n")
        report_alpha_characters(count_characters(data))

def get_book_text(pathToBook):
    with open(pathToBook) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_dict = {}
    characters = list(text.lower())
    for character in characters:
        if(character in character_dict):
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def report_alpha_characters(text):
    new_list = []
    def sortFunc(e):
        return e["num"]

    for key in text.keys():
        if key.isalpha():
            new_list.append({"key": key, "num": text[key]})
    new_list.sort(reverse=True, key=sortFunc)
    for char in new_list:
        print(f"The '{char['key']}' character was found {char['num']} times")
    print("--- End Report ---")
main()
