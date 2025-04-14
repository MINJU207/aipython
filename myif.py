# 고양이 아스키 아트 출력 함수들
def print_cat1():
    cat = [
        " /\\_/\\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    for line in cat:
        print(line)

def print_cat2():
    cat = [
        " /\\_/\\  ",
        "( =^.^= )",
        ' (")(")  '
    ]
    for line in cat:
        print(line)

def print_cat3():
    cat = [
        " /\\_/\\  ",
        "( -.- ) ",
        " > ^ <  "
    ]
    for line in cat:
        print(line)

# 고양이 출력 선택 함수
def play_cat():
    print("고양이 그림 출력기")
    print("=====================")
    print("1. 고양이")
    print("2. 고양이")
    print("3. 고양이")
    print("=====================")
    try:
        n = int(input("선택: "))
        if n == 1:
            print("🐱 고양이 1번")
            print_cat1()
        elif n == 2:
            print("🐱 고양이 2번")
            print_cat2()
        elif n == 3:
            print("🐱 고양이 3번")
            print_cat3()
        elif n == 0:
            return False  # 종료 신호
        else:
            print("잘못 입력했습니다.")
    except ValueError:
        print("숫자로 입력해주세요.")
    return True

# 1단계: 5번 반복 실행
print("🐾 고양이 출력 프로그램 (5번 반복 시작)")
for i in range(5):
    play_cat()
print("🐾종료")

# 2단계: 무한 반복 (0 입력 시 종료)
print("🐾 고양이 출력 프로그램 (0 입력 시 종료)")
while True:
    if not play_cat():
        print("🐾 종료")
        break
