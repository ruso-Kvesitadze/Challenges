n = int(input())
arr = map(int, input().split())

new_list = list(arr)
new_list.sort()
list_set = set(new_list)
unique_list = (list(list_set))
print(unique_list[-2])