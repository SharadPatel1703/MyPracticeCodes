def containsDuplicate(self, nums):
    checks = []
    for ind, val in enumerate(nums):
        if val not in checks:
            checks.append(val)
        elif val in checks:
            return True
        elif ind == len(nums)-1 and val not in checks:
            return False

nums = [1,2,3,1]
ans = containsDuplicate(nums)
print(ans)
