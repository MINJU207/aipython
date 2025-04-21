import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import os

def display_image(file_path):
    """주어진 파일 경로의 이미지를 창에 표시합니다."""
    try:
        img = Image.open(file_path)
        photo = ImageTk.PhotoImage(img)

        # 이전 이미지 라벨이 있다면 제거
        for widget in window.winfo_children():
            if isinstance(widget, tk.Label) and hasattr(widget, "image"):
                widget.destroy()

        image_label = tk.Label(window, image=photo)
        image_label.image = photo  # Label이 photo 객체를 참조하도록 유지
        image_label.pack(padx=10, pady=10)

        window.title(os.path.basename(file_path)) # 창 제목을 파일 이름으로 설정

    except FileNotFoundError:
        tk.messagebox.showerror("오류", f"파일을 찾을 수 없습니다: {file_path}")
    except Exception as e:
        tk.messagebox.showerror("오류", f"이미지 로딩 오류: {e}")

def open_file_dialog():
    """파일 탐색 창을 열고 선택된 이미지 파일을 표시합니다."""
    file_path = filedialog.askopenfilename(
        title="이미지 파일 선택",
        filetypes=(("JPEG 파일", "*.jpg;*.jpeg"), ("PNG 파일", "*.png"), ("GIF 파일", "*.gif"), ("모든 파일", "*.*"))
    )
    if file_path:
        display_image(file_path)

# 메인 윈도우 생성
window = tk.Tk()
window.title("이미지 뷰어")

# 파일 열기 버튼 생성
open_button = tk.Button(window, text="이미지 열기", command=open_file_dialog)
open_button.pack(pady=10)

# 초기 메시지 레이블
initial_label = tk.Label(window, text="이미지 파일을 열어주세요.")
initial_label.pack(pady=5)

# 메인 이벤트 루프 시작
window.mainloop()