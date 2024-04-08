# Dorlens Janvier chapter 2 question 3

newVideoCost = 3.00
oldVideoCost = 2.00

totalVideoBrought = int(input("Enter the total videos brought: "))
oldVideosRented = int(input("Enter how many old videos you you rent: "))
newVideosRented = int(input("Enter how many new videos you rent: "))


finalCosOldVideo = oldVideoCost * oldVideosRented
finalCostNewVideo = newVideoCost * newVideosRented

total = finalCosOldVideo + finalCostNewVideo

print(total)