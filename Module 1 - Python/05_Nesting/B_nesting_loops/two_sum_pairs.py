# Write a function `two_sum_pairs(numbers, target)` that returns all unique pairs from
# numbers that sum to target.

def two_sum_pairs(numbers, target):
    sum_pairs = []
    for i in range(len(numbers)):
        pairs = []
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.extend([numbers[i],numbers[j]])
                sum_pairs.append(pairs)

    return sum_pairs
   

print(two_sum_pairs([2, 3, 4, 6, 5], 8))  # [[2, 6], [3, 5]]
print(two_sum_pairs([10, 7, 4, 5, 2], 12))  # [[10, 2], [7, 5]]
print(two_sum_pairs([3, 9, 8], 11))  # [[3, 8]]
print(two_sum_pairs([3, 9, 8], 10))  # []

