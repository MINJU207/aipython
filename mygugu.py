# 숫자 두개를 입력을 받아서
# +, -, * / 를 출력 하는 프로그램을 만들어 보자

# 사용자에게 숫자를 입력하도록 명령
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하고 출력
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

# 결과 출력 단, 0으로 나눌 수 없도록 설정
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("0으로 나눌 수 없습니다.")
