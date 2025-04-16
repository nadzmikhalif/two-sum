from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER
    for place in range(len(nums)):
        counter = 0
        for element in nums:
            if counter == place:
                counter += 1
                continue

            if nums[place] + element == target:
                print(f"[{place},{counter}]") 
                return
            
            counter += 1

    print("No combo")
    return