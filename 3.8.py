#anagram
from collections import defaultdict
def groupAnagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return list(ans.values())
strs=input('enter a string')
if(strs.isdigit()):
    print('invalid input')
else:
    print(groupanagrams(strs))

