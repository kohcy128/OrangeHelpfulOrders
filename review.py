from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def run_review(url):
    # 1. Headless 옵션 (Render 전용)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # 2. 드라이버 실행
    driver = webdriver.Chrome(options=options)

    # 3. 체스닷컴 로그인 (나중에 계정 입력할 예정)
    # 3. 체스닷컴 로그인 (여기 수정)
    driver.get("https://www.chess.com/login")
    time.sleep(2)

    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys("mlllllilj")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("Koh1221##")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("로그인 완료")
    time.sleep(3)
    # ↓↓↓ 여기다 로그인 자동화 코드 넣을거임 (아이디, 비번 자동 입력)

    # 4. 경기 URL 들어가기
    driver.get(url)
    time.sleep(2)

    # 5. 리뷰 버튼 기다렸다가 클릭
    review_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Review')]")))
    review_btn.click()
    print("리뷰 버튼 클릭 완료!")

    time.sleep(5)  # 리뷰 결과 기다리기
    driver.quit()
