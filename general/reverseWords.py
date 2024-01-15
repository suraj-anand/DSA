def reverseWords(string: str):
    words = string.split(".")[::-1]
    return ".".join(words)

string = "much.very.program.this.like.i"
print(reverseWords(string))