def jaccard_similarity(set_x, set_y):
    intersection = 0

    for lhv in set_x:
        for rhv in set_y:
            if lhv == rhv:
                intersection += 1

    union = len(set_x) + len(set_y) - intersection

    return intersection / union


if __name__ == "__main__":
    set1 = {1, 4, 5, 9, 2}
    set2 = {1, 6, 5, 8, 2}
    print(jaccard_similarity(set1, set2))
