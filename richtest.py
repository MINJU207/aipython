from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

# 고양이 아스키 아트 3종류
cat1 = r"""
 /\_/\  
( o.o ) 
 > ^ <
"""

cat2 = r"""
 /\_/\  
( -.- ) zzz
 > 🍞 <
"""

cat3 = r"""
 /\   /\
( o   o )
(  =^=  )
(        )
(         )⸝⸝
"""

# 고양이 데이터 (아트만 있음)
cats = {
    "1": {"art": cat1},
    "2": {"art": cat2},
    "3": {"art": cat3},
}

# 반복 루프 시작
while True:
    # 예쁘게 질문 패널 출력
    question = Panel.fit(
        "[bold]어떤 고양이를 보고 싶나요?[/bold]\n[1], [2], [3] 중에 골라줘!\n[dim]([0]을 입력하면 종료할 수 있어요)[/dim]",
        title="고양이 셀렉터 🐱",
        border_style="bright_magenta",
    )
    console.print(question)

    # 유저 입력 받기
    choice = Prompt.ask("번호를 입력해 주세요")

    # 종료 조건
    if choice == "0":
        console.print(Panel.fit("안녕히 가세요! 🐾 다음에 또 만나요~", border_style="blue"))
        break

    # 고양이 출력
    elif choice in cats:
        cat = cats[choice]
        console.print(
            Panel.fit(
                cat["art"],
                title=f"귀여운 고양이 {choice}번 ✨",
                border_style="magenta"
            )
        )
    else:
        console.print("[red]앗! 0, 1, 2, 3 중에서 골라줘야 해![/red]")
