def file_io(recv_input,output):
    money = recv_input.split('일')
    money = money[1].split('원')
    money = int(money[0])
    if output == False:
        money *= -1
    with open(filename, 'r',encoding = "Utf-8") as file:
        line = file.readlines()
        new_line = line[0].split()
        new_line = int(new_line[1])
        new_line += money
        line[0] = "잔액 "+str(new_line)+"\n"
        new_txt = "입금 "if output else "출금 "+recv_input+"\n"
        line.append(new_txt)
    with open(filename, 'w',encoding = "Utf-8") as file:
        file.writelines(line)

filename = "data.txt"
while True:
    recv = int(input("0 : 전체 내역 \n1 : 입금\n2 : 출금 \n3 : 내역 수정 \n-1 : 종료 \n원하는 번호를 입력 : "))
    if recv == 0:
        with open(filename,'r',encoding="Utf-8") as file:
            line = file.readlines()
        
        for i in line:
            print(i,end='')
    elif recv == 1:
        recv_input = input("입금 내역을 입력하세요.\n입력형식 : xxxx년 xx월 xx일 x원\n:")
        file_io(recv_input,True)
    elif recv == 2:
        recv_input = input("출금 내역을 입력하세요.\n입력형식 : xxxx년 xx월 xx일 x원\n:")
        file_io(recv_input,False)
    elif recv == 3:
        #내역 수정
        recv
    elif recv == -1:
        print("종료")
        break
    else:
        continue

