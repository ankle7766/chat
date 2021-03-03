
lines = []
with open('3.txt','r',encoding = 'utf-8-sig') as f: #utf-8-sig去掉開頭的空格
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    print(name)
