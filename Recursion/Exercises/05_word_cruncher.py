def find_all_solutions(idx, target, words_by_idx, words_count, used_words):
    if idx >= len(target):
        print(' '.join(used_words))
        return

    if idx not in words_by_idx:
        return

    for word in words_by_idx[idx]:
        if words_count[word] == 0:
            continue

        used_words.append(word)
        words_count[word] -= 1

        find_all_solutions(idx + len(word), target, words_by_idx, words_count, used_words)

        used_words.pop()
        words_count[word] += 1


words = input().split(", ")
target = input()

words_by_idx = {}
words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
        continue

    words_count[word] = 1

    try:
        idx = 0
        while True:
            idx = target.index(word, idx)

            if idx not in words_by_idx:
                words_by_idx[idx] = []

            words_by_idx[idx].append(word)
            idx += len(word)

    except ValueError:
        pass

find_all_solutions(0, target, words_by_idx, words_count, [])


# def format_strings(strings, result, formatted_target, searched_strings, target, found_combs):
#     if result == target:
#         if searched_strings not in found_combs:
#             print(*searched_strings)
#             found_combs.append(searched_strings) #backtr
#             searched_strings.clear()
#         return
#
#     for string in strings:
#         if formatted_target.startswith(string):
#             result += string
#             strings.remove(string)
#             searched_strings.append(string)
#             format_strings(strings, result, formatted_target[len(string):], searched_strings, target, found_combs)
#
#
# strings = input().split(", ")
# target_string = input()
#
# found_combinations = []
#
# format_strings(strings, "", target_string, [], target_string, found_combinations)
#
