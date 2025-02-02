nums = map(int,input().split())
dict = {num : "честное" for num in nums if num % 2 == 0}
print(dict)