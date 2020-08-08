import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value = 1000000)
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        bar.update(count)
print('檔案讀取完畢，共', len(data), '筆')

wc = {} # word_conut
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1  # 新增計數單字 

while True:
    word = input('請問你想查什麼字： ')
    if word == 'q':
        break
    elif word in wc:   
        print(word, '出現的次數為', wc[word])
    else:
        print('這個字沒有出現過哦！')

print('~~~~~~~~~~感謝使用查詢')

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
