def main():
    nums = list(map(int,input("请输入一个数组：").split(",")))
    target = int(input("请输入目标数字："))
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i]+nums[j]==target:
                return [i, j], target, nums
    return None
result, target, nums = main()
print(result)
print(f'Because nums[{result[0]}] + nums[{result[1]}] == {target}, we return {result}.')
