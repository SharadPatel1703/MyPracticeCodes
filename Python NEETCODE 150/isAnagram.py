string1 = "anagram"
string2 = "nagaram"

def isAnagram(str1, str2):
    counter = 0
    for i in range(len(str1)):
        if str1[i] in str2:
            counter += 1
        elif str1[i] not in str2:
            break
    if counter == len(str1):
        return True
    else:
        return False

ans = isAnagram(string1, string2)
print(ans)
