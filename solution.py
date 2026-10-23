def findDifferentBinaryString(nums):
    # Diagonal trick: flip the i-th character of the i-th string
    result = ""
    for i in range(len(nums)):
        result += "1" if nums[i][i] == "0" else "0"
    return result


print(findDifferentBinaryString(["01", "10"]))
print(findDifferentBinaryString(["00", "01"]))
print(findDifferentBinaryString(["111", "011", "001"]))
