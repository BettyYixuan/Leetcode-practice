panlindrome_or_not = str(input("Please input a number for us to determine: "))
if panlindrome_or_not == panlindrome_or_not[::-1]:
    print("true")
    print(f'{panlindrome_or_not} reads as {panlindrome_or_not} from left to right and from right to left.')
else:
    print("false")
    if panlindrome_or_not[::-1][0] == '0':
        print(f'Reads {panlindrome_or_not[::-1]} from right to left. Therefore it is not a palindrome.')
    else:
        print(f'From left to right, it reads {panlindrome_or_not}. From right to left, it becomes {panlindrome_or_not[::-1]}. Therefore it is not a palindrome.')    