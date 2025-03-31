from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # 내 닉네임이 나올 때까지 기다리기
    try:
        # 여기서 기다리는 이유는 페이지가 완전히 로드될 때까지 대기하기 위해
        nickname = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "user-username-component"))).text
        print("내 체스닷컴 닉네임:", nickname)
    except Exception as e:
        print("닉네임을 찾을 수 없습니다:", e)

    driver.quit()
