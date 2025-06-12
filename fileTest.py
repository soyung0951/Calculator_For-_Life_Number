for i in range(2): # 파일 내용 입력
    name = input("이름 : ")
    birthType = input("생일 유형 : ")
    birth = input("생년월일 : ")

    f = open("test1.txt",'w')

    f.write(f"{birthType}{name} {birth}")

    f.close()

for i in range(3): # 파일 내용 확인
    name = input("이름 : ")
    birthType = input("생일 유형 : ")
    is_not_in_file = True

    f = open("test1.txt", 'r')

    while True:
        line = f.readline()
        
        if line == '':
            break
        print(line[:4])
        if line[:4] == f"{birthType}{name}":
            print(line[5:])
            is_not_in_file = False
            break
        print(line[:4])
        
    if is_not_in_file:
        print("파일에 해당 내용이 들어있지 않습니다.")
    