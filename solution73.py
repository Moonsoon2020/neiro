n = int(input())
array = map(chr, map(int, input().split()))
text = "".join(array)

if "ключ" in text:
    print("NO")
else:
    print("YES")

