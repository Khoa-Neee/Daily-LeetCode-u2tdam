# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/?envType=daily-question&envId=2025-07-19
from typing import List

"""Easy approach, but not efficient 
O(n^3) => Time Limit Exceeded

def is_subfolder(a: str, b: str) -> bool:
     # b co phai con a khong
     part_a = a.split('/')
     part_b = b.split('/')
     if len(part_a) >= len(part_b): return False
     i = 0
     while i < len(part_a):
         if (part_a[i] != part_b[i]): return False
         i+=1
     return True
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        list_remove = []
        for i in range(len(folder)):
            for j in range(i + 1, len(folder)):
                if (is_subfolder(folder[i], folder[j])):
                    list_remove.append(folder[j])
        for f in list_remove:
            if f in folder:
                folder.remove(f)
        return folder"""

def is_subfolder(a: str, b: str) -> bool:
    # b co phai con a khong
    return b.startswith(a + '/')
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        prev = ""
        for path in folder:
            if not prev or not is_subfolder(prev, path):
                result.append(path)
                prev = path
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeSubfolders(["/ah/al/am","/ah/al"]))
    
