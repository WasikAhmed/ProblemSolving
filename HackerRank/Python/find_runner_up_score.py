if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scores = list(arr)
    max_score = max(scores[0], scores[1])
    second_max_score = min(scores[0], scores[1])

    for i in range(2, n):
        if scores[i] > max_score:
            second_max_score = max_score
            max_score = scores[i]
        elif second_max_score < scores[i] != max_score:
            second_max_score = scores[i]
        elif max_score == second_max_score and second_max_score != scores[i]:
            second_max_score = scores[i]

    print(second_max_score)
