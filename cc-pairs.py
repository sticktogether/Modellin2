def map(words):
    mapped = []
    for word1 in words:
        for word2 in words:
            if word1 != word2:
                mapped.append(((word1, word2), 1))
    return mapped


def shuffle(mapped_pairs):
    mapped_pairs.sort(key=lambda x: x[0])

    shuffled = []
    counts = []
    prev_pair = mapped_pairs[0][0]

    for pair, count in mapped_pairs:
        if pair == prev_pair:
            counts.append(count)
        else:
            shuffled.append((prev_pair, counts))
            prev_pair = pair
            counts = [count]
    else:
        shuffled.append((prev_pair, counts))
    return shuffled


def reduce(pair, counts):
    return pair, sum(counts)


file = open("./products_new.txt", encoding="utf8")

mapped_pairs = []

for line in file:
    words = line[:-1].split("  ")
    mapped_pairs.extend(map(words))

shuffled = shuffle(mapped_pairs)

reduced = []

for pair, counts in shuffled:
    reduced.append(reduce(pair, counts))

print(reduced)


file.close()


