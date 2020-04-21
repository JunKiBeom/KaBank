def week_26(pay):
    sum_money=0
    for i in range(1,27):
        sum_money+=pay*i
    return sum_money

while True:
    chk=-1
    money=[1000,2000,3000,5000,10000]
    print("+"*41+"""
| 카카오뱅크 26주 적금 총 입금액 계산기 |
"""+"+"*41)
    print("""
1.  1000원
2.  2000원
3.  3000원
4.  5000원
5. 10000원""")
    while True:
        select=input("매주 증액 하려는 금액의 번호를 선택세요. : ")
        if select in ['1','2','3','4','5']:
            break
        else:
            print("\n올바른 숫자를 입력하세요!")

    print("\n26주 적금 총 입금액 : %d원 입니다.\n"%week_26(money[int(select)-1]))

    chk=input("아무키나 누르면 종료 됩니다. 다시 실행하려면 1을 입력하세요.\n")

    if chk=='1':
        print()
    else:
        exit()
