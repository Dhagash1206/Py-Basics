def list_to_hashmap(lst):
    hashmap = {}

    for i, val in enumerate(lst):
        if val in hashmap:
            hashmap[val].append(i)
        else:
            hashmap[val] = [i]

    return hashmap


# Example usage
lst = [10, 20, 10, 30, 20, 10]

result = list_to_hashmap(lst)

print("Input list:", lst)
print("Hashmap:", result)

# Output:
# Input list: [10, 20, 10, 30, 20, 10]
# Hashmap: {10: [0, 2, 5], 20: [1, 4], 30: [3]}