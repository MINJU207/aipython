import tkinter as tk
import webbrowser

# 이미지 웹 링크 (실제 링크로 변경해야 합니다!)
dog_url = "https://example.com/images/dog.jpg"
cat_url = "https://example.com/images/cat.jpg"
rabbit_url = "https://example.com/images/rabbit.jpg"

def open_webpage(url):
    """주어진 URL을 기본 웹 브라우저에서 엽니다."""
    webbrowser.open_new(url)

# 메인 윈도우 생성
window = tk.Tk()
window.title("동물 이미지 뷰어 (웹 링크)")

# 강아지 버튼
dog_button = tk.Button(window, text="강아지 보기", command=lambda: open_webpage(dog_url))
dog_button.pack(pady=5)

# 고양이 버튼
cat_button = tk.Button(window, text="고양이 보기", command=lambda: open_webpage(cat_url))
cat_button.pack(pady=5)

# 토끼 버튼
rabbit_button = tk.Button(window, text="토끼 보기", command=lambda: open_webpage(rabbit_url))
rabbit_button.pack(pady=5)

# 안내 메시지
info_label = tk.Label(window, text="버튼을 클릭하면 웹 브라우저에서 이미지를 볼 수 있습니다.")
info_label.pack(pady=10)

# 메인 이벤트 루프 시작
window.mainloop()