
"""
user_id = {111, 112, 113, 114, 111}
user_id.add(115)                            #include add() method
user_id.update([115, 116, 117])             #include update() method
user_id.remove(113)                         #include remove() method
user_id_copy = user_id.copy()
print("Original set:", user_id)             #include copy() method
print("Copy of the set:", user_id_copy)
user_id.clear()                             #include clear() method
print(user_id)
"""


from telnetlib import AO


A = {"a","b","c","d","e"}
B = {"f","b","c","d","g"}

print(A.difference(B))
print(A.intersection(B))
print(A.isdisjoint(B))
print(A.issubset(B))

re = A.pop()
print(re)
y = {"a","b","c","d"}
rel = y.pop()
print(rel)
print(A.symmetric_difference(B))
print(A.union(B))