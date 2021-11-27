import time #time 라이브러리 사용
import sys
import random
import pygame


name=input('** 당신의 이름은 무엇입니까... ** :   ') #이름 물어보기
print('\n \n' + '[ '+name+' ]'+' 님은 책을 읽으려 상명헌책방에 왔습니다.') #게임 배경 설명
time.sleep(1) #시간 간격을 두고 출력할 수 있도록 time 라이브러리 이용
print('\n \n어랏! 저기 수상한 책이 있네요.') #게임 배경 설명
time.sleep(1)
print('\n \n책 표지에는 <텔레vision>이라고 적혀있어요.') #게임 배경 설명


time.sleep(2)


import turtle as t #turtle 라이브러리 사용
scr=t.Screen( ) #t.Screen 입력을 scr로 대체해 간단하게 코딩할 수 있도록 scr 변수 생성
scr.setup(700, 700) #스크린 크기 지정
scr.title('Book') #스크린 이름 지정

music_file = "궁금.mp3"

pygame.mixer. init()
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()

t.hideturtle() #turtle 모양 숨기기
t.bgcolor('pink') #turtle 배경색깔 지정
t.pensize(5) # turtle 펜 굵기 지정
t.penup() #turtle 펜을 들어 그림이 그려지지 않도록 
t.goto(-90, 140) #해당좌표로 이동
t.pendown() #turtle 펜을 내려 그림이 그려지도록

t.color('rosybrown') #펜 색상 지정
t.begin_fill() #색깔 채우기 시작
t.forward(180) #turtle 이동
t.right(90) #turtle 방향 바꾸기
t.forward(240)
t.right(90)
t.forward(180)
t.right(90)
t.forward(240)
t.end_fill() # 색 채우기 끝

t.goto(-45, 175)
t.right(90)
t.forward(180)
t.goto(90, 140)
t.goto(135, 175)
t.right(90)
t.forward(240)
t.goto(90,-100)

t.color('black')
t.penup()
t.goto(-75, 50)
t.write("<텔레 vision>", font=('궁서', 17, "bold")) #책 이미지 속 제목 텍스트 출력
t.goto(-70, -30)
t.write("무엇이든 물어보세요", font=('궁서', 12)) #책 이미지 속 부제목 텍스트 출력
time.sleep(2)
t.bye() #자동으로 turtle 종료


while True: #답을 잘못 입력할 경우 다시 질문을 물어보기 위해 while문 사용
    time.sleep(1)
    answer=input('\n \n** 책을 열어보시겠습니까...? (네 아니요) ** :   ') #질문하기
    if answer=='네':
        time.sleep(1)
        print('\n \n당신의 고민을 해결해드립니다!') #네라고 대답할 경우 출력
        break #while문 탈출

    elif answer=='아니요':
        time.sleep(1)
        music_file = "빠밤.mp3"
        pygame.mixer. init()
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        print('\n \n이 책은 당신의 기억 속에서 사라집니다.....Bye....') #아니요라고 대답할 경우 출력
        sys.exit() #파이썬 종료

    else:
        time.sleep(1)
        print('\n \n답을 정확하게 입력해주세요') #네와 아니요가 아닌 다른 대답을 입력했을 때 출력

list= ['고민하지 않아도 된다', '옆에 있는 친구의 대답을 믿어라', '망설이지 말고 행동해라', '그러지 않는 편이 좋다', '다시 한번 생각해봐라',
       '후회하게 될 수 있다', '마음을 다잡고 나아가라', '10을 세고 다시 질문하여라', '꼭 해야한다', '끌리는대로 행동해라', '땅을 치고 후회한다', '본인의 생각을 믿어라',
       '확신이 들면 하되, 조금의 의심이 든다면 그만둬라', '선택지는 많다', '당신의 선택만이 정답이다', '코끼리코 3번 돌고 다시 생각해봐라', '이 일로 많은 것이 바뀔 것이다',
       '모든 것을 확신한 후 행하는 것은 늦다', '한 번에 떠오른 방법은 정답이 아닐 수도 있다', '기다릴 줄 알아야 한다', '여러 번 시도할 필요도 없다',
       '고민하지 말고 나아가야한다', '당신은 이미 정답을 알고 있다', '무조건 잘 될 것이다', 'gooooooooood', '너의 의지에 달려있다'] #답변 리스트
while answer=='네':
    time.sleep(1)                
    question=input('\n \n** 고민을 입력하세요! ** :  ') #고민 입력받기
    
    time.sleep(1)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    music_file = "삐빅.mp3"
    pygame.mixer. init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    print(random.choice(list)) #답변 리스트 중 랜덤 출력

    while True:
        time.sleep(1)
        answer=input('\n \n** 다시 질문하시겠습니까? (네 아니요) ** : ')
        if answer!="네" and answer!="아니요":
            print("\n \n답을 정확하게 입력해주세요")
            continue
        else:
            break
    if answer=="아니요":
        time.sleep(1)
        music_file = "빠밤.mp3"
        pygame.mixer. init()
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        print("\n \n이 책은 당신의 기억 속에서 사라집니다.....Bye....")
        sys.exit() # 파이썬 종료

