import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# CSS 요소 클릭 함수
def cssSearch(findEl) :
    time.sleep(1)
    return driver.find_element(By.CSS_SELECTOR, findEl).click()

# 브라우저 강제종료 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# 브라우저 실행
driver.get("https://illuminarean.com/")

# 화면 최대화
driver.maximize_window()

# 팝업 닫기
cssSearch("body > div.ReactModalPortal > div > div > div > div > button.css-1lby940.e1iwydzj0 > svg > path")

# GNB Work 클릭
cssSearch("#__next > div > header > div > div > div > div > nav > ul > li:nth-child(2) > a > span")

# GOODVIBE WORKS 바로가기 > 클릭
cssSearch("#__next > div > main > div > div:nth-child(2) > div > div.css-s49xw9.edcyzk41 > div > a")

# 탭 이동 (https://works.goodvibe.kr/) > 무료체험신청서 클릭
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
cssSearch("#__next > div > div > header > div > div > ul > li:nth-child(2) > button")

# 무료체험신청 작성
# 1. 회사명 필드
txtInput = driver.find_element(By.ID, "companyName")
txtInput.click()
txtInput.send_keys("일루미나리안")
time.sleep(1.5)

# 2. 대표자명 필드
txtInput2 = driver.find_element(By.ID, "ceoName")
txtInput2.click()
txtInput2.send_keys("이영철")
time.sleep(1.5)

# 3. 사업자유형 필드
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#businessType > div").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[text()='개인']").click()
time.sleep(1)

# 4. 직원수 필드
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#scale > div").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[text()='51-100 명']").click()
time.sleep(1)

# 5. 담당자명 필드
txtInput3 = driver.find_element(By.ID, "name")
txtInput3.click()
txtInput3.send_keys("YoungCheol LEE")
time.sleep(1)

# 6. 이메일 필드
txtInput4 = driver.find_element(By.ID, "email")
txtInput4.click()
txtInput4.send_keys("zodiac0905@naver.com")
time.sleep(1)

# 7. 휴대폰번호 필드
txtInput5 = driver.find_element(By.ID, "mobile")
txtInput5.click()
txtInput5.send_keys("010-1234-5678")
time.sleep(1)

# 8. 담당업무 필드
driver.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4 > dl.duties > dd > div").click()
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/div/div[1]/button[28]").click()
time.sleep(1)

txtInput6 = driver.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4 > dl.duties > dd > div > div.css-y10ynn.el0tj999 > button > p > div > input[type=text]")
time.sleep(1)
txtInput6.send_keys("광고기획")
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/div/div[1]/button[19]").click()
time.sleep(1)

# 담덩업무 필드 內 등록 버튼 클릭
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/div/div[2]/button[2]").click()

# 신청취소 버튼
time.sleep(2)
cssSearch("body > div:nth-child(10) > button > span")
time.sleep(1)

# 해당 탭 닫기
driver.close()