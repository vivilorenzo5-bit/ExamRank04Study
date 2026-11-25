def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []
    return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]


print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))