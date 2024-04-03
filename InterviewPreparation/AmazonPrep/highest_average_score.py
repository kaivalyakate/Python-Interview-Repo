def highest_average(scores: list[tuple[str, int]]):
    score_repo: dict[str, list[int]] = {}
    for score in scores:
        temp = score_repo.get(score[0], [])
        temp.append(score)
        score_repo[score[0]] = temp
    
    highest_avg = 0
    for k, v in enumerate(score_repo):
        temp = sum(score_repo[k])//len(score_repo[k])
        if temp >= highest_average:
            highest_avg = temp
    
    return highest_avg

if __name__ == "__main__":
    highest_average([("Bob", 97), ("")])