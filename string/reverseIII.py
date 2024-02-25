def reverseWords(s: str) -> str:
    result = ""
    left = 0

    for index, char in enumerate(s):
        if char == " ":
            rev_word = "".join(reversed(s[left:index]))
            result += rev_word + " "
            left = index + 1
    result += "".join(reversed(s[left:len(s)]))
    return result

if __name__ == "__main__":
    string = "Let's take LeetCode contest"
    res = reverseWords(string)
    print(f"Result = {res}")
