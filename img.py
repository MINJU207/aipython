from PIL import Image

try:
    # 'input.jpg' 파일 열기
    img = Image.open("input.jpg")

    # 이미지가 성공적으로 열렸는지 확인
    print("이미지 파일이 성공적으로 열렸습니다.")
    print(f"이미지 크기: {img.size}")
    print(f"이미지 형식: {img.format}")

    # 필요하다면 여기서 이미지 처리 작업을 수행할 수 있습니다.
    # 예:
    # resized_img = img.resize((200, 200))
    # resized_img.show()

except FileNotFoundError:
    print("오류: 'input.jpg' 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
except Exception as e:
    print(f"오류 발생: {e}")