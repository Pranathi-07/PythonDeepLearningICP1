input_file = open('E:\\pythondeeplearning\\ICP2\\input', 'r')
out_file = open('E:\\pythondeeplearning\\ICP2\\output', 'w')
wordcount = {}
for word in input_file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k, v in wordcount.items():
    out_file.write(k + " ")
    out_file.write(str(v) + "\n")
input_file.close()
out_file.close()