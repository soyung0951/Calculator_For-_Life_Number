def getNumberType(): # 인생수의 종류 입력
    print("숫자를 입력하세요. (1 : 선천수 | 2 : 후천수 | 3 : 직업수)")
    numberType = int(input())
    if 1 <= numberType <= 3:
        return numberType
    else:
        print("잘못된 입력입니다.")
        print("다시 입력해 주세요.")
        return getNumberType()
    

def getNumber(birthSum): # 선천수, 후천수 계산
    numString = str(birthSum)
    sum = 0
    for i in numString:
        sum += int(i)
    if sum <= 22:
        return sum
    else:
        return getNumber(sum)
    
def getBirth(birthType): # 생년월일을 입력받아 합을 계산
    print(f"당신의 {BirthTypes[birthType]}을 0000.00.00의 형태로 입력하세요.")
    year, month, day  = map(int,input().split('.'))
    sum = year + month + day
    return sum
    
def getCareerNumber(): # 직업수 (선천수 + 후천수) 계산
    lunarBirth = getBirth(1) # 음력 생일 합
    solarBirth = getBirth(2) # 양력 생일 합
    moonNumber = getNumber(lunarBirth) # 선천수 계산
    sumNumber = getNumber(solarBirth) # 후천수 계산
    birthSum = moonNumber + sumNumber
    while True:
        sum = getBirth(birthSum)
        if sum <= 9:
            print(1)
            break
    return sum  

numberTypes = {1 : "선천수" , 2 : "후천수" , 3 : "직업수"}
BirthTypes = {1 : "음력 생일" , 2 : "양력 생일"}
tarotCard =  {0 : "0번 Fool (광대)" , 1 : "1번 Magician (마법사)" , 2 : "2번 The High Priestess (여사제)" , 3 : "3번 The Empress (여왕)", 4 : "4번 The Emperor (황제)", 5 : "5번 Hierophant (교황)" ,
              6 : "6번 The Lovers (연인들)" , 7 : "7번 The Chariot (전차)" , 8 : "8번 Strength (힘)" , 9  : "9번 The Hermit (은둔자)" , 10 : "10번 The Wheel Of Fortune (운명의 수레바퀴)" ,}

############################################### main ###############################################

print("\n","="*40)
print("인생수 계산기 프로그램 입니다.")
print("생년월일을 입력하여 선천수와 후천수, 직업수를 알아볼 수 있습니다.")
print("-"*40)

numberType = getNumberType()
if numberType == 3:
    number = getCareerNumber()
else:
    birthSum = getBirth(numberType)
    number = getNumber(birthSum)
    
print("-"*40)

print(f"당신의 {numberTypes[numberType]}는 {number}이고, 운명의 타로카드는 {tarotCard[number % 21]}입니다.")