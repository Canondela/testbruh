import pyautogui
import time
import keyboard
import asyncio

time.sleep(3)


async def reach(field):
    time.sleep(1)
    keyboard.press("w")
    time.sleep(1)
    keyboard.release("w")
    keyboard.press("d")
    time.sleep(10)
    keyboard.press("space")
    time.sleep(0.2)
    keyboard.release("space")
    time.sleep(1)
    keyboard.release("d")
    time.sleep(0.5)
    keyboard.press("e")
    keyboard.release("e")
    if field == "mountain":
        time.sleep(3)
        keyboard.press("1")
        keyboard.release("1")
    if field == "strawberry":
        keyboard.press("d")
        time.sleep(1)
        keyboard.press("space")
        keyboard.release("space")
        time.sleep(0.7)
        keyboard.press("space")
        keyboard.release("space")
        time.sleep(1.7)
        keyboard.release("d")
        keyboard.press("space")
        keyboard.release("space")
        time.sleep(3)
        keyboard.press("1")
        keyboard.release("1")
    if field == "cactus":
        keyboard.press("d")
        time.sleep(0.4)
        keyboard.press("space")
        keyboard.release("space")
        time.sleep(1.3)
        keyboard.press("space")
        keyboard.release("space")
        time.sleep(4)
        keyboard.release("d")
        keyboard.press("space")
        keyboard.release("space")
        time.sleep(4)
        keyboard.press("1")
        keyboard.release("1")


async def convert():
    keyboard.press("7")
    time.sleep(0.5)
    keyboard.release("7")
    time.sleep(0.5)
    keyboard.press("e")
    keyboard.release("e")
    time.sleep(60)


async def collect(setting):
    for i in range(setting // 2):
        keyboard.press("w")
        time.sleep(0.5)
        keyboard.release("w")
        keyboard.press("d")
        time.sleep(0.5)
        keyboard.release("d")
        keyboard.press("s")
        time.sleep(0.5)
        keyboard.release("s")
        keyboard.press("a")
        time.sleep(0.5)
        keyboard.release("a")
        if keyboard.is_pressed("F6"):
            return


async def macro():
    while True and keyboard.is_pressed("F6") == False:
        task = asyncio.create_task(reach("strawberry"))
        await task
        if keyboard.is_pressed("F6"):
            return
        print("Field reached")
        task = asyncio.create_task(collect(600))
        await task
        if keyboard.is_pressed("F6"):
            return
        keyboard.release("w")
        keyboard.release("a")
        keyboard.release("s")
        keyboard.release("d")
        task = asyncio.create_task(convert())
        if keyboard.is_pressed("F6"):
            return
        await task


"""
asyncio.run(macro())
"""
"""
while True and keyboard.is_pressed("F6") == False:
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.mouseDown()
    time.sleep(300)


while True and keyboard.is_pressed("F6") == False:
    keyboard.press("w")
    time.sleep(2)
    keyboard.release("w")
    keyboard.press("d")
    time.sleep(2)
    keyboard.release("d")
    keyboard.press("s")
    time.sleep(2)
    keyboard.release("s")
    keyboard.press("a")
    time.sleep(2)
    keyboard.release("a")

"""

while True and keyboard.is_pressed("F6") == False:
    keyboard.press("w")
    time.sleep(0.5)
    keyboard.release("w")
    keyboard.press("d")
    time.sleep(0.5)
    keyboard.release("d")
    keyboard.press("s")
    time.sleep(0.5)
    keyboard.release("s")
    keyboard.press("a")
    time.sleep(0.5)
    keyboard.release("a")

"""

while True:
    # SPAM
    time.sleep(0.1)
    pyautogui.click()
    # End
    if keyboard.is_pressed("F6"):
        break
"""
