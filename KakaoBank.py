from pynput import keyboard
import os, sys

def week_26(pay):
    sum_money = 0
    for i in range(1, 27):
        sum_money += pay*i
    return sum_money

def on_press(key):
    # if key == keyboard.Key.esc:
    #     return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k == 'space':  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        return False  # stop listener; remove this if want more keys
    else :
        os._exit(0)

while True:
    money = [1000,2000,3000,5000,10000]
    print("+" * 48 + """
| 카카오뱅크 26주 적금 총 입금액 계산기 by KB  |
""" + "+" * 48)
    print("""
1.  1,000원
2.  2,000원
3.  3,000원
4.  5,000원
5. 10,000원\n""")
    while True:
        select = input("매주 증액 하려는 금액의 번호를 선택하세요. : ").strip()  # 입력된 공백 처리용
        if select in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("\n올바른 숫자를 입력하세요!")

    print("\n선택한 금액은", format(money[int(select)-1],","), "원 입니다")
    print("\n26주 적금 총 입금액 :", format(week_26(money[int(select)-1]), ","), "원 입니다.\n")

    print("아무키나 누르면 종료 됩니다. 다시 실행하려면 Space를 누르세요.\n")

    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys