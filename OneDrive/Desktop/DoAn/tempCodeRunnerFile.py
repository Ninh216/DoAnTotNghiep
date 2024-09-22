
        if num > maxOccur:
            maxOccur = num
            ans = label
    return ans

if __name__ == "__main__":
    trainSet, testSet = loadData("./dulieu.csv")
    numOfRightAnwser = 0