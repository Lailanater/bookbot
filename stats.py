def words(book_txt):
    print("----------- Word Count ----------")
    num_words = len(book_txt.split())
    print(f"Found {num_words} total words")


def char_count(book_txt):
    count = {}
    for char in book_txt:
        char = char.lower()
        if char not in count:
            count[char] = 0
        count[char] += 1
    return count


def sort_on(items):
    return items["num"]


def print_char_count(count):
    print("--------- Character Count -------")
    sort = []
    for key in count:
        if key.isalpha():
            d = {}
            d["key"] = key
            d["num"] = count[key]
            sort.append(d)
    sort.sort(reverse=True, key=sort_on)
    for obj in sort:
        print(f"{obj['key']}: {obj['num']}")
