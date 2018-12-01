from collections import Counter

with open('./file.txt') as file: text = file.read().replace('\n', ' ').lower().split(' ')
most_common, num_most_common = Counter(text).most_common(1)[0]
print(most_common, num_most_common)
