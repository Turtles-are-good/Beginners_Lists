OtherFood=[]
iLikePesto=[]
count = 0
while  count < 8 :
    ans = input("What is your favourite food").lower()
    if ans == "pesto" :
        iLikePesto.append(ans)
        count += 1
    else :
        OtherFood.append(ans)
        count += 1
print()
print("Pesto is loved by", len(iLikePesto), "people.")
print("I like pesto\n" * len(iLikePesto))
print("Other foods:")
for words in OtherFood :
    print(words)