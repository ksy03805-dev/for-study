from datetime import datetime
import re
import tkinter as tk
from bs4 import BeautifulSoup
import requests


def get_today_menu():
    """강릉캠 생협 표에서 오늘 날짜/요일 행의 마지막 식단 칸을 파싱합니다."""
    try:
        url = "https://coop.gwnu.ac.kr/contents.asp?page=847"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers, timeout=5)
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, "html.parser")

        now = datetime.now()
        day_idx = now.weekday()  # 0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일
        days_kor = ["월", "화", "수", "목", "금", "토", "일"]
        today_day = days_kor[day_idx]
        today_md = now.strftime("%m.%d").lstrip("0")  # 예: '10.29'

        # 주말인 경우
        if day_idx >= 5:
            return (
                f"• 오늘({today_day})은 주말입니다.",
                "• 운영 식단 없음",
            )

        tables = soup.find_all("table")
        target_cell_text = ""

        for table in tables:
            rows = table.find_all("tr")
            for row in rows:
                cells = row.find_all(["td", "th"])
                if not cells:
                    continue

                row_header = " ".join(
                    [c.get_text(strip=True) for c in cells[:2]]
                )

                if today_day in row_header or today_md in row_header:
                    target_cell_text = cells[-1].get_text(
                        separator="\n", strip=True
                    )
                    if len(target_cell_text) > 3:
                        break

            if target_cell_text:
                break

        if target_cell_text:
            baekban_raw = ""
            ilpum_raw = ""

            if "///일품///" in target_cell_text:
                parts = target_cell_text.split("///일품///")
                baekban_raw = parts[0]
                ilpum_raw = parts[1] if len(parts) > 1 else ""
            elif "일품" in target_cell_text:
                parts = target_cell_text.split("일품")
                baekban_raw = parts[0]
                ilpum_raw = parts[1] if len(parts) > 1 else ""
            else:
                baekban_raw = target_cell_text

            baekban_lines = [
                line.strip()
                for line in baekban_raw.splitlines()
                if line.strip()
                and not any(
                    k in line for k in ["백반", "식단", today_day, "요일"]
                )
            ]

            ilpum_lines = []
            for line in ilpum_raw.splitlines():
                for item in line.split(","):
                    clean = item.strip()
                    if clean and clean not in ilpum_lines:
                        ilpum_lines.append(clean)

            baekban_str = (
                "\n".join([f"• {b}" for b in baekban_lines[:8]])
                if baekban_lines
                else "• 등록된 식단 없음"
            )
            ilpum_str = (
                "\n".join([f"• {i}" for i in ilpum_lines[:8]])
                if ilpum_lines
                else "• 등록된 일품 없음"
            )

            return baekban_str, ilpum_str

        return "• 오늘 식단을\n  찾지 못했습니다.", "• 등록된 일품 없음"

    except Exception:
        return "• 식단 불러오기 오류", "• 네트워크 확인 필요"


def create_widget():
    root = tk.Tk()
    root.title("강릉캠 학식 위젯")

    root.overrideredirect(True)
    root.configure(bg="#1E1E24")
    root.attributes("-alpha", 0.92)
    root.wm_attributes("-topmost", True)

    now = datetime.now()
    days_kor = ["월", "화", "수", "목", "금", "토", "일"]
    today_day = days_kor[now.weekday()]
    today_str = now.strftime(f"%Y-%m-%d ({today_day})")

    # 상단 헤더
    header_label = tk.Label(
        root,
        text=f" 강릉캠 오늘의 학식 | {today_str}",
        font=("맑은 고딕", 9, "bold"),
        fg="#00E676",
        bg="#1E1E24",
        anchor="w",
    )
    header_label.pack(fill="x", padx=10, pady=(8, 4))

    content_frame = tk.Frame(root, bg="#1E1E24")
    content_frame.pack(fill="both", expand=True, padx=8, pady=(0, 8))

    baekban_text, ilpum_text = get_today_menu()

    # [백반] 영역
    left_frame = tk.Frame(content_frame, bg="#1E1E24")
    left_frame.pack(side="left", fill="both", expand=True)

    left_title = tk.Label(
        left_frame,
        text="[백반]",
        font=("맑은 고딕", 8, "bold"),
        fg="#FFD54F",
        bg="#1E1E24",
        anchor="w",
    )
    left_title.pack(fill="x", pady=(0, 2))

    left_body = tk.Label(
        left_frame,
        text=baekban_text,
        font=("맑은 고딕", 8),
        fg="#F0F0F5",
        bg="#1E1E24",
        justify="left",
        anchor="nw",
    )
    left_body.pack(fill="both", expand=True)

    # 구분선
    separator = tk.Frame(content_frame, width=1, bg="#33333F")
    separator.pack(side="left", fill="y", padx=8)

    # [일품] 영역
    right_frame = tk.Frame(content_frame, bg="#1E1E24")
    right_frame.pack(side="right", fill="both", expand=True)

    right_title = tk.Label(
        right_frame,
        text="[일품]",
        font=("맑은 고딕", 8, "bold"),
        fg="#4FC3F7",
        bg="#1E1E24",
        anchor="w",
    )
    right_title.pack(fill="x", pady=(0, 2))

    right_body = tk.Label(
        right_frame,
        text=ilpum_text,
        font=("맑은 고딕", 8),
        fg="#F0F0F5",
        bg="#1E1E24",
        justify="left",
        anchor="nw",
    )
    right_body.pack(fill="both", expand=True)

    # --- 텍스트 분량에 따른 동적 자동 크기 계산 ---
    baekban_lines = baekban_text.splitlines()
    ilpum_lines = ilpum_text.splitlines()

    max_line_cnt = max(len(baekban_lines), len(ilpum_lines), 1)

    # 가장 긴 단어 길이 계산
    max_len_b = (
        max([len(line) for line in baekban_lines]) if baekban_lines else 10
    )
    max_len_i = max([len(line) for line in ilpum_lines]) if ilpum_lines else 10

    # 동적 폭/높이 계산 (폰트 및 간격 기준)
    calc_width = max(260, (max_len_b + max_len_i) * 11 + 65)
    calc_height = max(140, max_line_cnt * 18 + 55)

    # 화면 위치 세팅
    root.geometry(f"{calc_width}x{calc_height}+1200+80")

    # 마우스 드래그 이동 기능
    def start_move(event):
        root.x = event.x
        root.y = event.y

    def do_move(event):
        deltax = event.x - root.x
        deltay = event.y - root.y
        x = root.winfo_x() + deltax
        y = root.winfo_y() + deltay
        root.geometry(f"+{x}+{y}")

    root.bind("<Button-1>", start_move)
    root.bind("<B1-Motion>", do_move)

    # 마우스 우클릭 시 종료
    root.bind("<Button-3>", lambda e: root.destroy())

    root.mainloop()


if __name__ == "__main__":
    create_widget()