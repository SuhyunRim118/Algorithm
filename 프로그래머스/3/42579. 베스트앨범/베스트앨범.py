def solution(genres, plays):
    answer = []
    genre_play = {}
    genre_id = {}
    totalplay = {}
    
    for i in range(len(genres)):
        if genres[i] not in totalplay.keys():
            totalplay[genres[i]] = 0
            genre_play[genres[i]] = []
            genre_id[genres[i]] = []
        totalplay[genres[i]]+= plays[i]
        genre_play[genres[i]].append(plays[i])
        genre_id[genres[i]].append(i)
        
    totalplay = dict(sorted(totalplay.items(), key= lambda item:item[1], reverse=True))

    for genre in totalplay.keys():
        cnt = 0
        for play in sorted(genre_play[genre], reverse=True):
            for song_id in genre_id[genre]:
                if plays[song_id]==play:
                    answer.append(song_id)
                    genre_id[genre].remove(song_id)
                    plays[song_id]=0
                    cnt+=1
                    break
            if cnt==2:
                break
    
    return answer