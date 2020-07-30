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

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('總共有', len(new),'筆資料，字數小於100。')

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('總共有', len(good), '筆留言提到 good 。')