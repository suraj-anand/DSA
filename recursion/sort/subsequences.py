def subsequences(string="", sub="", ds=[]):
    if len(string) == 0:
        if sub:
            ds.append(sub)
        return ds
    
    subsequences(string=string[1:], sub=f"{sub}{string[0]}")
    subsequences(string=string[1:], sub=f"{sub}")
    return ds

if __name__ == "__main__":
    string = "ast"
    ans = subsequences(string=string)
    print(ans)