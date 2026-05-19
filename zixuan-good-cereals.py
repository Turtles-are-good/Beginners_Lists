cerealList=[]
while True :
    ans = input("Enter a cereal").strip().lower()
    if ans == "sultana and bran" or ans == "weetbix" :
        break
    else :
        cerealList.append(ans)
print("Your cereals are\n", cerealList)