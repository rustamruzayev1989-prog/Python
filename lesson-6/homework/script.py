def insert_underscores(txt: str) -> str:
    vowels = "aeiouyAEIOUY"
    result = []
    count = 0
    i = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1
        if count == 3:
            
            j = i + 1
            while j < len(txt) and (txt[j] in vowels or txt[j] == "_"):
                result.append(txt[j])
                j += 1
                i += 1
            if j < len(txt):  
                   result.append("_")
            count = 0
        i += 1
    return "".join(result)
print(insert_underscores("futbol")) 
print(insert_underscores("assalom"))
print(insert_underscores("hamshahar"))
