numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]
maxnum = max(numsList)
maxposition = numsList.index(maxnum)

mininum = min(numsList)
miniposition = numsList.index(mininum)

average = sum(numsList) / len(numsList)

print("Average = " , average, ". " , "Biggest number =" , maxnum, "and position is", maxposition, ". Lowest numer is", mininum, "and position is", miniposition, ".")