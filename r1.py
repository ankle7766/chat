def read_file(filename):
    lines = []
    with open(filename,'r',encoding = 'utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line =='ankle':
            person = 'ankle'
            continue
        elif line == 'ann':
            person = 'ann'
            continue
        if person:    #如果person有值得話就做這一行。
            new.append(person + ':' + line)
    return new

def write_file(filename,lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line +'\n')



def main():
    lines = read_file('input.txt')
    lines = convert(lines)  #呼叫convert函式
    write_file('output.txt',lines) #輸出的檔，檔名


main() #進入點