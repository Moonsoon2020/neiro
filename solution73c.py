n = int(input())
array = map(chr, map(int, input().split()))
text = "".join(array).lower()
 
listL = ["ключ", "устройств", "механ"]    
listC = ["стен", "ров", "башн"]


def solve(txt):
    for w in listL:
        if (w in txt):
            return "NO"
    for w in listC:
        if (w in txt):
            return "YES"
    return "NO"

print(solve(text))

