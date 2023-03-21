import numpy as np
import collections
def permute(nums) ->list[list[int]]:
    if len(nums) <= 1:
        return [nums]
    
    permutations = []
    dfs(nums, [], permutations)
    return permutations


def dfs(nums, path, res):
    if not nums:
        res.append(path)
        return 
    
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

def get_random_from_permute(permutations):

    idx = np.random.randint(0, len(permutations))
    return permutations[idx]

def test_random_permu(k, nums):
    permutations = permute(nums)
    print(permutations)
    res = [0]*len(permutations)
    for i in range(k):
        key = get_random_from_permute(permutations)
        for j, p in enumerate(permutations):
            if p == key:
                res[j] += 1
    res = [x/k for x in res]
    return res


print(permute([1,2,3]))
print(test_random_permu(100000, [1,2,3]))
