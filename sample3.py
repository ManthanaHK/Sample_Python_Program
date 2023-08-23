# 13. Write a function unique to find all the unique elements of a list.
def unique():
    lst = [12,12,12,3,3,4,5,12,4,7]
    unq = []
    for i in lst:
        if lst.count(i) == 1:
            unq.append(i)
    return unq

# 14. Write a function dups to find all duplicates in the list.
def dupElements():
    lst = [12,12,12,3,3,4,5,12,4,7]
    dup = []
    for i in lst:
        if lst.count(i) > 1:
            if i in dup:
                continue
            else:
                dup.append(i)
    return dup

# 15. Write  a  functiongroup(list,  size)  that  take  a  list  and splits  into  smaller  lists  of given size.
def split_list(original_list, chunk_size):
    nested_sublists = []
    for _ in range(0, len(original_list), chunk_size):
        nested_sublists.append(original_list[_:_ + chunk_size])
    return nested_sublists

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3

result = split_list(original_list, chunk_size)
print(result)