import numpy as np
from scipy.spatial import distance

all_words, count_words, res = [], [], []
count_lines, number_line = 0, 0
file = open('sentences.txt', 'r+')
for line in file:
    count_words = list([])
    line = line.lower()
    words = re.split('[^a-z]', line)
    while '' in words:
        words.remove('')
    for i in words:
        if i not in all_words:
            all_words.append(i)
    count_lines += 1
file.close()
count_matrix = np.zeros(shape=(count_lines, len(all_words)))
file = open('sentences.txt', 'r+')
for line in file:
    count_words = list([])
    line = line.lower()
    words = re.split('[^a-z]', line)
    while '' in words:
        words.remove('')
    for i in all_words:
        a = words.count(i)
        count_words.append(a)
    count_words = np.array(count_words)
    for i in range(len(count_words)):
        count_matrix[number_line][i] = count_words[i]
    number_line += 1
for i in range(len(count_matrix)):
    res.append(distance.cosine(count_matrix[0], count_matrix[i], w=None))
file.close()
res[0] = 1
res = list(res)
min1 = res.index(min(res))
res[res.index(min(res))] = 1
min2 = res.index(min(res))
file = open('submission-1.txt', 'w')
file.write(str(min1))
file.write(' ')
file.write(str(min2))
file.close()
