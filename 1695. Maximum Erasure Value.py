from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Sử dụng sliding window với set để đảm bảo tính duy nhất.
        """
        seen = set()
        left = 0
        current_sum = 0
        max_sum = 0

        for right, x in enumerate(nums):
            # Nếu x đã có trong cửa sổ, thu hẹp cửa sổ cho đến khi x không còn trùng
            while x in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            # Thêm x vào cửa sổ
            seen.add(x)
            current_sum += x
            # Cập nhật kết quả
            max_sum = max(max_sum, current_sum)

        return max_sum
        
        
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))  # Example usage