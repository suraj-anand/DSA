
def clamp(n):
    if n > -2 ** 31  and n < 2 ** 31:
        return n
    
    if n < -2 ** 31:
        return -2 ** 31

    if n > 2 ** 31 - 1:
        return 2 ** 31 - 1
    
    else:
        return n 
    

def atoi(s):
    sign = ""
    string = ""
    look_contigious = False
    
    for i in s:
        if i in ["+", "-"]:
            if sign == "" and string == "":
                sign = "positive" if i == "+" else "negative"
                look_contigious = True
                continue
            else:
                break
        
        if i.isdigit():
            look_contigious = True
            string += i
        
        elif i == " " and look_contigious == False:
            if string == "":
                continue
            else:
                break
        else:
            break
            
    if string == "":
        return 0
    result = int(string) if sign in ["", "positive"] else int(string) * -1
    return clamp(result)


print(atoi("  +413"))