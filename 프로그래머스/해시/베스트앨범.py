def solution(genres, plays):
    musics = {}
    music_play = {}
    answer = []
    
    for i in range(len(genres)):
        if genres[i] in music_play.keys():
            music_play[genres[i]] += plays[i]
        else:
            music_play[genres[i]] = plays[i]
    music_play = sorted(music_play.items(), key = lambda x: -x[1])
    print(music_play)
    for i in range(len(genres)):
        if plays[i] in musics.keys():
            musics[plays[i]] += [genres[i], i]
        else:
            musics[plays[i]] = [genres[i], i]
            
    musics = dict(sorted(musics.items(), reverse=1))

    for i in music_play:
        count = 0
        for j in musics.items():
            if j[1][0] == i[0]:
                count += 1
                answer.append(j[1][1])
            if count > 1:
                break
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500]))