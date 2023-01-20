def budgetShoppingdp(n, bundles, costs):
    dp = [0]*(n+1)
    books = [(b,c) for b,c in zip(bundles, costs)]
    res = 0
    for i in range(len(dp)):
        for j in range(len(books)):
            if books[j][1] > i:
                continue
            elif books[j][1] == i:
                dp[i] = max(books[j][0], dp[i])
            else:
                c = dp[i-books[j][1]]
                dp[i] = max(dp[i], c+books[j][0])
            res = max(res, dp[i])
    return res
    
print(budgetShoppingdp(50,[20,19],[24,20]))
print(budgetShoppingdp(7697,[15,12,13],[148,116,134]))

import math
def minProductSubarray(arr, k):
    sub_arrs = []
    path = []
    res = math.inf
    dfs(arr, k, path, sub_arrs)
    print(sub_arrs)
    for sub_arr in sub_arrs:
        res = min(res, sum(sub_arr))
    return res

def dfs(arr, k, path, sub_arrs):
   
    if len(arr) <k or k <= 0:
        return
    if len(arr) == k:
        for a in arr:
            path.append(a)
        sub_arrs.append(path)
        return
    if k == 1:
        path.append(max(arr)*len(arr))
        sub_arrs.append(path)
        return
    
    for i in range(1, len(arr)):
        m = max(arr[:i])*len(arr[:i])
        dfs(arr[i:], k-1, path+[m], sub_arrs)
print(minProductSubarray([1,1,2,1,5], 3))
