def main():
    words = load_words_from_file("words.txt")
    unique_words = []
    for i in words:
        if not i in unique_words:
            unique_words.append(i)
    count = {}
    for i in unique_words:
        count.update({i: 0})
    for i in words:
        count[i] += 1
    for i in count:
        print_histogram_bar(i, count[i])


def print_histogram_bar(word, count):
    print(f"{word}: {'x' * count}")

    

def load_words_from_file(filepath):
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words

main()
