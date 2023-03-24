def merge_sum(hs):
    result = hs[0]
    for h in hs[1:]:
        temp = {}
        for k in set(result) | set(h):
            temp[k] = result.get(k, 0) + h.get(k, 0)
        result = temp
    return result


def map(words):
    mapped = []
    for word1 in words:
        h = {}
        for word2 in words:
            if word1 != word2:
                if word2 in h:
                    h[word2] += 1
                else:
                    h[word2] = 1
                mapped.append((word1, h))
    return mapped


def shuffle(mapped_stripes):
    mapped_stripes.sort(key=lambda x: x[0])

    shuffled = []
    hs = []
    prev_word = mapped_stripes[0][0]

    for word, h in mapped_stripes:
        if word == prev_word:
            hs.append(h)
        else:
            shuffled.append((prev_word, hs))
            prev_word = word
            hs = [h]
    else:
        shuffled.append((prev_word, hs))
    return shuffled


def reduce(word1, hs):
    reduced = []
    h = merge_sum(hs)
    for word2, count in h.items():
        reduced.append(((word1, word2), count))
    return reduced


file = open("./products_new.txt", encoding="utf8")

mapped_stripes = []

for line in file:
    words = line[:-1].split("  ")
    mapped_stripes.extend(map(words))

shuffled = shuffle(mapped_stripes)

reduced = []

for word, hs in shuffled:
    reduced.extend(reduce(word, hs))

print(reduced)


file.close()

