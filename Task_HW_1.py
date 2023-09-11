lst = [1,2,3,4,52,3,4,5,1,2,4,5,6,8, 'a', 'a']
res = []
print(lst)
for item in lst:
    if lst.count(item) > 1:
        if item not in res:
            res.append(item)
print(res)
