import pyautogui
import time

# 화면 크기 출력
print(pyautogui.size())

# 마우스 위치 출력
time.sleep(2)
print(pyautogui.position())

# 마우스 이동
mac = 손쉬운 사용 vscode 권한 설정
pyautogui.moveTo(164,362)
pyautogui.moveTo(164,362,2)

# 마우스 클릭
pyautogui.click()
pyautogui.click(button='right')
pyautogui.doubleClick()
pyautogui.click(clicks=3,interval=1) #3번 클릭하는데 1초마다 하기
