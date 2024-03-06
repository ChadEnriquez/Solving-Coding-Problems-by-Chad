# count occurrences in a given list
# implementation is done using dictionary

def count_occurrences(my_list):
    count = {}
    for i in my_list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

# Example usage
my_list = [1, 2, 3, 2, 1, 3, 3, 4, 5, 4, 4]
occurrences = count_occurrences(my_list)
print(occurrences)