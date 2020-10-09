def jaccard_similarity(set_x, set_y):
    intersection = 0

    for num in set_x:
        if num in set_y:
            intersection += 1

    union = len(set_x) + len(set_y) - intersection

    return intersection / union


if __name__ == "__main__":
    set1 = {1, 4, 5, 9, 2}
    set2 = {1, 6, 5, 8, 2}
    print(jaccard_similarity(set1, set2))
