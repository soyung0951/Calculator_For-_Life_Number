# 프로그램에 필요한 정보를 담은 딕셔너리

numberTypes = {1 : "선천수" , 2 : "후천수" , 3 : "직업수"}
BirthTypes = {1 : "음력 생일" , 2 : "양력 생일"}
# 타로카드 번호 : 타로카드 이름
tarotCard =  {0 : "0번 Fool (광대)" , 1 : "1번 Magician (마법사)" , 2 : "2번 The High Priestess (여사제)" , 3 : "3번 The Empress (여왕)", 4 : "4번 The Emperor (황제)", 5 : "5번 Hierophant (교황)" ,
              6 : "6번 The Lovers (연인들)" , 7 : "7번 The Chariot (전차)" , 8 : "8번 Strength (힘)" , 9  : "9번 The Hermit (은둔자)" , 10 : "10번 The Wheel Of Fortune (운명의 수레바퀴)" ,
              11  :  "11번 Justice  (정의)" , 12 : "12번 The Hanged Man (매달린 사람)" ,  13 : "13번 Death (죽음)" , 14 : "14번 Temperance (절제)" , 15 : "15번 Devil (악마)" ,
              16 : "16번 The Tower (탑)", 17 : "17번 The Star (별)" , 18 : "18번 The Moon (달)" , 19  :"19번 The Sun (태양)" , 20 : "20번 Judgement (심판)" , 21 : "21번 The World (세계)"}
# 타로카드 번호 : 타로카드 해석
tarotCardMeaning = {0 : """정방향 : 새로운 시작, 순수함, 모험
- 새로운 시작과 모험, 순수함을 상징합니다. 새로운 여정을 시작하거나 삶에 새로운 접근 방식을 시도할 때 나타납니다.
역방향 : 무모함, 방황, 준비 부족
- 무모한 행동이나 준비 부족, 방황을 나타냅니다. 신중하게 계획하고 행동해야 할 때입니다.""" , 
1  : """정방향 : 창의성, 능력, 자원 활용
- 자신의 능력과 자원을 활용하여 목표를 이루는 시기입니다. 창의적으로 능력 있는 상태를 상징합니다.
역방향 : 기만, 잠재력 억제, 계획 실패
- 기만이나 잠재력 억제, 계획 실패를 나타냅니다. 자신의 능력을 제대로 발휘하지 못하고 있을 수 있습니다.""" , 
2  :"""정방향 : 직관, 잠재력, 신비
- 직관과 잠재력, 신비를 상징합니다. 내면이 지혜와 직관을 통해 문제를 해결할 때입니다.
역방향 : 비밀, 직관 부족, 감정 억제
- 비밀이나 직관 부족, 감정 억제를 나타냅니다. 내면의 목소리에 귀 기울여야 합니다.""" , 
3 : """정방향 : 풍요, 창조, 양육
- 풍요와 창조, 양육을 상징합니다. 물질적 풍요와 창의적 에너지가 넘치는 시기입니다.
역방향 : 결핍, 창의력 부족, 소외
- 결핍이나 창의력 부족, 소외를 나타냅니다. 자신을 돌보고 창의적 에너지를 회복해야 합니다.""" , 
4 : """정방향 : 권위, 구조, 안정
- 권위와 구조, 안정을 상징합니다. 강한 리더십과 체계적인 접근이 필요한 시기입니다.
역방향 : 독재, 권위 남용, 무질서
- 독재나 권위 남용, 무질서를 나타냅니다. 권력을 남용하지 않고 공정하게 행동해야 합니다.""" , 
5 : """정방향 : 전통, 지혜, 교육
- 전통과 지혜, 교육을 상징합니다. 전통적인 가치와 지혜를 통해 성장할 때입니다.
역방향 : 독단, 전통 거부, 지식 부족
- 독단적이거나 전통을 거부하는 태도, 지식 부족을 나타냅니다. 열린 마음으로 배우고 수용해야 합니다.""" , 
6 : """정방향 : 사랑, 조화, 선택
- 사랑과 조화, 선택을 상징합니다. 중요한 관계나 결정을 앞두고 있을 때 나타납니다.
역방향 : 불화, 갈등, 부적절한 선택
- 불화나 갈등, 부적절한 선택을 나타냅니다. 신중하게 선택하고 관계를 조화롭게 유지해야 합니다.""" , 
7 : """정방향 : 승리, 의지, 통제
- 승리와 의지, 통제를 상징합니다. 목표를 향해 의지를 가지고 나아가는 시기입니다.
역방향 : 통제 상실, 장애물, 실패
- 통제 상실이나 장애물, 실패를 나타냅니다. 계획을 재검토하고 장애물을 극복해야 합니다.""" , 
8 : """정방향 : 용기, 인내, 내면의 힘
- 용기와 인내, 내면의 힘을 상징합니다. 어려운 상황에서도 내면의 힘으로 극복할 때입니다.
역방향 : 두려움, 의지 부족, 감정적 불안정
- 두려움이나 의지 부족, 감정적 불안정을 나타냅니다. 자신감을 회복하고 용기를 가져야 합니다.""" , 
9 : """정방향 : 고독, 내면 탐구, 지혜
- 고독과 내면 탐구, 지혜를 상징합니다. 혼자서 내면의 지혜를 찾고자 할 때입니다.
역방향 : 고립, 외로움, 내면의 혼란
- 고립이나 외로움, 내면의 혼란을 나타냅니다. 자신을 돌보고 내면의 평화를 찾아야 합니다.""" , 
10 : """정방향 : 운명, 변화, 행운
- 운명과 변화, 행운을 상징합니다. 삶의 변화와 기회가 다가올 때입니다.
역방향 : 불운, 저항, 예상치 못한 변화
- 불운이나 변화에 대한 저항, 예상치 못한 변화를 나타냅니다. 유연하게 대처하고 긍정적인 마인드를 유지해야합니다.""" , 
11 : """정방향 : 공정성, 균형, 진실
- 공정성과 균형, 진실을 상징합니다. 공정한 판단과 균형 잡힌 결정을 내려야 할 때입니다.
역방향 : 불공정, 불균형, 법적 문제
- 불공정이나 불균형, 법적 문제를 나타냅니다. 공정하게 행동하고 균형을 찾는 것이 중요합니다.""" ,
12 : """정방향 : 희생, 관점 변화, 기다림
- 희생과 관점 변화, 기다림을 상징합니다. 상황을 새로운 시각에서 바라보고 희생이 필요한 때입니다.
역방향 : 지연, 저항, 희생의 무의미함
- 지연이나 저항, 희생의 무의미함을 나타냅니다. 불필요한 희생을 피하고 상황을 재평가해야 합니다.""" , 
13 : """정방향 : 끝, 전환, 새로운 시작
- 어떤 것의 끝과 전환, 새로운 시작을 상징합니다 .변화와 새로운 시작을 받아들여야 할 때입니다.
역방향 : 저항, 변화 회피, 중단
- 변화에 대한 저항이나 회피, 중단을 나타냅니다. 변화를 받아들이고 앞으로 나아가야 합니다.""" , 
14 : """정방향 : 균형, 조화, 절제
- 균형과 조화, 절제를 상징합니다. 조화로운 삶을 위해 균형을 유지해야 할 때입니다.
역방향 : 과도함, 불균형, 조화 부족
- 과도하거나 불균형 상태를 나타냅니다. 절제와 균형을 찾는 것이 중요합니다.""" , 
15 : """정방향 : 유혹, 속박, 물질적 집착
- 유혹과 속박, 물질적 집착을 상징합니다. 나쁜 습관이나 중독에서 벗어나야 할 때입니다.
역방향 : 해방, 자유, 통제력 회복
- 속박에서 해방되고 자유를 찾는 시기입니다. 통제력을 회복하고 긍정적인 변화를 추구해야 합니다.""" , 
16 : """정방향 : 갑작스러운 변화, 붕괴, 혁명
- 갑작스러운 변화와 붕괴, 혁명을 상징합니다. 예기치 않은 사건으로 인해 큰 변화를 맞이할 때입니다.
역방향 : 회복, 저항, 서서히 오는 변화
- 회복이나 저항, 서서히 오는 변화를 나타냅니다. 변화를 수용하고 회복하는 과정이 필요합니다.""" ,
17  : """정방향 : 희망, 영감, 치유
- 희망과 영감, 치유를 상징합니다. 긍정적인 에너지와 영감을 받는 시기입니다.
역방향 : 절망, 의심, 치유의 지연
- 절망이나 의심, 치유의 지연을 나타냅니다. 긍정적인 마음을 유지하고 희망을 잃지 않아야 합니다.""" ,
18 : """정방향 : 환상, 직관, 무의식
- 환상과 직관, 무의식을 상징합니다. 무의식의 메시지에 귀 기울이고 직관을 따를 때입니다.
역방향 : 혼란, 불안, 환상의 붕괴
- 혼란, 불안, 환상의 붕괴를 나타냅니다. 현실과 환상을 구분하고 감정적으로 안정될 필요가 있습니다.""" , 
19 : """정방향 : 성공, 행복, 긍정
- 성공과 행복, 긍정을 상징합니다. 밝고 긍정적인 에너지로 가득한 시기입니다.
역방향 : 지연된 성공, 자만, 일시적 좌절
- 성공의 지연이나 자만, 일시적 좌절을 나타냅니다. 긍정적인 마인드를 유지하고 목표를 향해 나아가야 합니다.""" ,
20 : """정방향 : 부활, 평가, 깨어남
- 부활과 평가, 깨어남을 상징합니다. 자신의 행동을 평가하고 새로운 시작을 준비할 때입니다.
역방향 : 회피, 후회, 자기 비판
- 평가나 후회, 자기 비판을 나타냅니다. 자신의 행동을 되돌아보고 교훈을 얻어야 합니다.""" , 
21 : """정방향 : 완성, 성취, 통합
- 완성과 성취, 통합을 상징합니다. 목표를 이루고 통합된 상태를 나타냅니다.
역방향 : 미완성, 좌절, 끝내지 못한 일
- 미완성이나 좌절, 끝내지 못한 일을 나타냅니다. 목표를 다시 설정하고 끝맺음을 지어야 합니다."""
}



# 인생수 계산기 클래스

class LifeNumCalculator():
    
    def intro(self): # 프로그램 시작 안내 함수
        print("\n"+"="*80)
        print()
        print("인생을 읽는 숫자 프로그램이 시작됩니다.")
        print("다음 절차에 따라 생년월일을 입력하여 선천수와 후천수, 직업수를 알아보고 운명의 타로카드를 알 수 있습니다.")
        print()
        print("-"*80)
        print()
        
        
         
    def calculateLifeNumber(self): # 메인 스트림 함수 (프로그램 재시작 시 필요)
        self.getLifeNumber() # 인생수 생성
        self.printLifeNumber() # 인생수 출력
        self.checkTarotMeaning() # 타로카드 해석 열람
        self.checkRetry() # 프로그램 재시작 여부 확인
        
        
    
    def getLifeNumber(self): # 인생수 계산 함수
        self.numberType = self.getNumberType() # 인생수의 유형 입력
        if self.numberType == 3: # 직업수(선천수 + 후천수 -> 직업수)를 구하는 경우
            lunaBirthSum = self.getBirthSum(1)
            moonNumber = self.getNumberSum(lunaBirthSum) # 선천수 생성
            solarBirthSum = self.getBirthSum(2)
            sunNumber = self.getNumberSum(solarBirthSum) # 후천수 생성
            self.lifeNumber = self.getNumberSum(moonNumber + sunNumber)
            while self.lifeNumber > 9: # 직업수는 9 이하 이다.
                self.lifeNumber = self.getNumberSum(self.lifeNumber)
        elif 1 <= self.numberType <= 2 : # 선천수 또는 후천수를 구하는 경우
            birthSum = self.getBirthSum(self.numberType)
            self.lifeNumber = self.getNumberSum(birthSum)
        
    def getNumberType(self): # 인생수의 종류 입력 함수
        while True:
            try:
                print("알아볼 인생수의 유형을 입력해 주세요. (1 : 선천수 | 2 : 후천수 | 3 : 직업수)")
                numberType = int(input())
            except ValueError:
                self.printWorngInput()
                continue
            if 1 <= numberType <= 3:
                break
            self.printWorngInput()
        print()
        return numberType
      
    def getNumberSum(self, birthSum): # 수의 합 생성 함수
        birthSumString = str(birthSum)
        numberSum = 0
        for i in birthSumString:
            numberSum += int(i)
        if numberSum <= 22:
            return numberSum
        else:
            return self.getNumberSum(numberSum)
        
    def getBirthSum(self, birthType): # 생년월일 입력 및 합 생성 함수
        while True:
            try:
                print(f"당신의 {BirthTypes[birthType]}을 0000.00.00의 형태로 입력하세요.")
                year, month, day = map(int, input().split('.'))
            except ValueError:
                self.printWorngInput()
                continue
            if year > 0 and 12 >= month >= 1 and 31 >= day >= 1:
                break
            self.printWorngInput()
        print()
        birthSum = year + month + day
        return birthSum
    
    
    
    def printLifeNumber(self): # 인생수 출력 함수
        print("-"*83)
        print()
        # 계산한 인생수의 유형 + 인생수 + 운명의 타로카드 출력
        print(f"당신의 {numberTypes[self.numberType]}는 {self.lifeNumber}이고, 운명의 타로카드는 {tarotCard[self.lifeNumber % 21]}입니다.")
        print()
        
        
    
    def checkTarotMeaning(self): # 타로카드 해석 출력 함수
        while True:
            try:
                print("운명의 타로카드의 해석을 보시겠습니까? (1 : 예 | 2 : 아니오)")
                checkMeaning = int(input())
            except ValueError:
                self.printWorngInput()
                continue
            if 1 <= checkMeaning <= 2:
                break
            self.printWorngInput()
        print()
        if checkMeaning == 1:
            print(f"------------------ 운명의 타로카드 {tarotCard[self.lifeNumber % 21]}의 해석 ------------------")
            print(tarotCardMeaning[self.lifeNumber % 21])
            print("-"*83)
            print()
        else:
            print("-"*83)
            print()
        
        
        
    def checkRetry(self): # 프로그램 재시작 확인 함수
        while True:
            try:
                print("다른 운명수를 확인하시겠습니까? (1 : 예 | 2 : 아니오)")
                retry = int(input())
            except ValueError:
                self.printWorngInput()
                continue
            if 1 <= retry <= 2:
                break
            self.printWorngInput()
        print()
        if retry == 1:
            print()
            print("-"*83)
            print()
            self.calculateLifeNumber()
            
        
        
    def outro(self): # 프로그램 종료 안내 함수
        print("-"*83)
        print()
        print("인생을 읽는 숫자 프로그램이 종료됩니다.")
        print("="*83)
        
        
    
    def printWorngInput(self): # 오류 안내 함수
        print()
        print("잘못된 입력입니다.")
        print("다시 입력해 주세요.")
        print()
        
        
        
# main

lifeNumCalculator = LifeNumCalculator()
lifeNumCalculator.intro()
lifeNumCalculator.calculateLifeNumber()
lifeNumCalculator.outro()