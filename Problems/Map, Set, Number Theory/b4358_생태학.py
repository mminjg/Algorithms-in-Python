import sys

total = 0
dc = dict()
for line in sys.stdin:
    if line == "\n":
        break
    line = line.rstrip()
    total += 1
    if not line in dc:
        dc[line] = 1
    else:
        dc[line] += 1

st = list()
for item in dc.items():
    st.append([item[0], item[1]/total*100])
st.sort()
for item in st:
    print(item[0], '%.4f' % item[1])