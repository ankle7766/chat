def read_file(filename):
    lines = []
    with open(filename,'r',encoding = 'utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    allen_sc = 0
    allen_ic = 0
    allen_wc = 0
    viki_sc = 0
    viki_ic = 0
    viki_wc = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sc += 1
            elif s[2] == '圖片':
                allen_ic += 1
            else:
                for m in s[2:]:
                    allen_wc += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sc += 1
            elif s[2] == '圖片':
                viki_ic += 1
            else:
                for m in s[2:]:
                    viki_wc += len(m)
    print('allen說了',allen_wc,'個字')
    print('allen傳了',allen_sc,'張貼圖')
    print('allen傳了',allen_ic,'張圖片')

    print('viki說了',viki_wc,'個字')
    print('viki傳了',viki_sc,'張貼圖')
    print('viki傳了',viki_ic,'張圖片')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)  #呼叫convert函式



main() #進入點