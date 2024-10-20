"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""
text = input("Text: ").strip().lower()
word_counts = {}
words_list = text.split()

# Count word occurrences
for word in words_list:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


longest_word_length = max(len(word) for word in words_list)

sorted_word_counts = sorted(word_counts.items())

for word, count in sorted_word_counts:
    print(f"{word:{longest_word_length}} : {count}")
