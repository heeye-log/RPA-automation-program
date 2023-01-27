import pyautogui
import pyperclip

# 키보드 입력(문자) / 한글 미지원
# pyautogui.write('startcoding',interval=0.25)

# 키보드 입력(키)
# pyautogui.press('enter')
# pyautogui.press('up')

# 키보드 입력(여러개 동시에)
# pyautogui.hotkey('command','c')

# 한글 입력 방법
pyperclip.copy('한글입력')
pyautogui.hotkey('command','v')

