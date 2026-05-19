stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]
num = sum(1 for s in stringsList if s and s[0].lower() == s[-1].lower())
print(num)