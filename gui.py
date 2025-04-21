import tkinter as tk
from PIL import Image, ImageTk
import os
import random  # 랜덤 모듈 추가

# --- 함수 정의 ---
def show_image(filename):
    """지정된 파일 이름의 이미지를 로드해서 표시"""
    global photo_image

    try:
        pil_image = Image.open(filename)
        pil_image.thumbnail((600, 500), Image.Resampling.LANCZOS)
        photo_image = ImageTk.PhotoImage(pil_image)

        image_label.config(image=photo_image, text='')  # 텍스트 지우고 이미지 표시
        image_label.image = photo_image
        window.title(f"이미지 뷰어 - {os.path.basename(filename)}")

    except FileNotFoundError:
        image_label.config(text=f"파일을 찾을 수 없습니다: {filename}", image='')
        window.title("이미지 뷰어")
    except Exception as e:
        image_label.config(text=f"이미지 로드 오류: {e}", image='')
        window.title("이미지 뷰어")

def show_random_image():
    """이미지 리스트 중에서 랜덤으로 하나 선택해서 표시"""
    random_image = random.choice(["dog.jpg", "cat.jpg", "sudal.jpg"])
    show_image(random_image)

# --- GUI 설정 ---
window = tk.Tk()
window.title("이미지 뷰어")
window.geometry("700x600")

photo_image = None

# 버튼 프레임 생성
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# 버튼 생성 (각 버튼에 이미지 파일 연결)
dog_button = tk.Button(button_frame, text="🐶 강아지", command=lambda: show_image("dog.jpg"),
                       bg="#FFDDC1", fg="black", font=("Helvetica", 12, "bold"), padx=10, pady=5)

cat_button = tk.Button(button_frame, text="🐱 고양이", command=lambda: show_image("cat.jpg"),
                       bg="#C1E1FF", fg="black", font=("Helvetica", 12, "bold"), padx=10, pady=5)

rabbit_button = tk.Button(button_frame, text="🦦 수달", command=lambda: show_image("sudal.jpg"),
                          bg="#D1FFC1", fg="black", font=("Helvetica", 12, "bold"), padx=10, pady=5)

random_button = tk.Button(button_frame, text="🎲 랜덤", command=show_random_image,
                          bg="#FFFACD", fg="black", font=("Helvetica", 12, "bold"), padx=10, pady=5)


# 버튼 배치
dog_button.grid(row=0, column=0, padx=10)
cat_button.grid(row=0, column=1, padx=10)
rabbit_button.grid(row=0, column=2, padx=10)
random_button.grid(row=0, column=3, padx=10)  # 랜덤 버튼 추가

# 이미지 표시 레이블
image_label = tk.Label(window, text="버튼을 눌러 이미지를 보세요!", compound=tk.CENTER)
image_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# 메인 루프 시작
window.mainloop()
