from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def run_login_test():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    # 로그인
    driver.get("https://www.chess.com/login")
    time.sleep(2)

    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys("너의_아이디")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("너의_비밀번호")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("로그인 완료")
    time.sleep(3)

    # 내 체스닷컴 홈 페이지 가기
    driver.get("https://www.chess.com/home")
    time.sleep(2)

    # 내 닉네임 출력 확인
    nickname = driver.find_element(By.CLASS_NAME,
                                   "user-username-component").text
    print("내 체스닷컴 닉네임:", nickname)

    driver.quit()
