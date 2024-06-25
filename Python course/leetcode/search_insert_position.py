def search_position(nums :list, target : int):
    if target in nums:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)


nums = [1, 3, 5, 6]
target = 7

print(search_position(nums, target))
