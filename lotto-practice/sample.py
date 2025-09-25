import tkinter as tk
import random

# 메인 창
root = tk.Tk()
root.title("로또 추첨기")
root.geometry("300x200")
root.attributes("-topmost", True)

# 안내 라벨
label = tk.Label(root, text="버튼을 눌러 로또 번호를 추첨하세요", font=("Arial", 11))
label.pack(pady=20)

# 결과 라벨
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# 버튼 클릭 이벤트
def pick_lotto():
    numbers = random.sample(range(1, 46), 6)  # 1~45 중 6개 뽑기 (중복X)
    numbers.sort()
    result_label.config(text="추첨 번호: " + " ".join(map(str, numbers)))

# 버튼
btn = tk.Button(root, text="로또 추첨!", command=pick_lotto)
btn.pack()

root.mainloop()


# always_on_top_window.py
import tkinter as tk

root = tk.Tk()
root.title("고정 창")
root.geometry("300x120")
root.attributes("-topmost", True)  # 항상 위

label = tk.Label(root, text="이 창은 항상 위에 떠요 👆")
label.pack(pady=15)

def toggle_topmost(event=None):
    cur = bool(root.attributes("-topmost"))
    root.attributes("-topmost", not cur)

btn = tk.Button(root, text="고정 토글(F2)", command=toggle_topmost)
btn.pack()

root.bind("<F2>", toggle_topmost)
root.mainloop()
