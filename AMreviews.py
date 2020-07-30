data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完畢，共', len(data), '筆')

sun_len = 0
for d in data:
    sun_len += len(d)
print('平均留言長度為', sun_len / len(data))