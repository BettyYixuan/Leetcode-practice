def main():
    nums = list(input("请输入一个数组：").split(","))
    target = int(input("请输入目标数字："))
    length = len(nums)
    for i in range(length):
        for j in range(length):
            if ((nums[i]+nums[j])==target) and i != j:
                return [i, j]

print(main())
#Q1--two sum
