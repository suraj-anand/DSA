def write_to_chars(chars, char, count, writer):
    if count == 1:
        chars[writer] = char
        writer += 1
        return writer
    chars[writer] = char
    writer += 1
    
    for num in str(count):
        chars[writer] = num
        writer += 1
    return writer 

def compress(chars: list) -> int:
    writer = 0
    currentChar = ""
    count = 0
    
    for char in chars:
        if currentChar == char or currentChar == "":
            currentChar = char
            count += 1
        else:
           writer = write_to_chars(chars, currentChar, count, writer)
           currentChar = char
           count = 1
    if count >= 1:
        writer = write_to_chars(chars, currentChar, count, writer)
    return writer

if __name__ == "__main__":
    # chars = ["a","a","b","b","c","c","c"]
    chars = ["a"]
    chars = ["a","a","a","a","a","b"]
    idx = compress(chars)
    print(idx)
    print(chars)