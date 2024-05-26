from datetime import date,time,datetime

filename = "data.txt"
def file_io(recv_input,output):
    current_time = datetime.now().strftime("%Y:%m:%d-%H:%M:%S")
    money = recv_input.split('원')
    money = int(money[0])
    if output == False:
        money *= -1
    with open(filename, 'r',encoding = "Utf-8") as file:
        line = file.readlines()
        new_line = line[0].split()
        new_line = int(new_line[1])
        new_line += money
        line[0] = "잔액 "+str(new_line)+"\n"
        new_txt = ("입금 "if output else "출금 ") +recv_input+" "+current_time+"\n"
        line.append(new_txt)
    with open(filename, 'w',encoding = "Utf-8") as file:
        file.writelines(line)

def print_all_basic_fx():
    with open(filename,'r',encoding="Utf-8") as file:
        line = file.readlines()
        j=0
        new_line = []
        for i in line:
            new_line.append(("" if j == 0 else str(j)+"번: ")+i)
            j+=1
    return new_line

def input_money(recv_input):
    #recv_input = input("입금 내역을 입력하세요.\n입력형식 : x원\n:")
    file_io(recv_input,True)
    return

def output_money(recv_input):
    #recv_input = input("출금 내역을 입력하세요.\n입력형식 : x원\n:")
    file_io(recv_input,False)
    return

def modify_breakdown(recv_input):
    #recv_input = input("수정하고 싶은 내역 입력 \n입력형식 : x번 > 입금/출금 x원 년:월:일-시:분:초\n")
    recv_input = recv_input.split(">")
    cnt = recv_input[0].split("번")
    cnt = int(cnt[0])
    with open(filename,'r',encoding="Utf-8") as file:
        line = file.readlines()
        n_l =  recv_input[1][1:]
        n_2 = line[cnt]
        n_2 = n_2.split(' ')
        n_3 = n_2[1].split("원")
        n_3 = int(n_3[0])
        cm = line[0].split(' ')
        cm = int(cm[1])
        if n_2[0] == "입금":
            cm -= n_3
        else:
            cm += n_3
        n_4 = n_l.split(' ')
        n_5 = n_4[0]
        n_6 = n_4[1].split('원')
        n_6 = int(n_6[0])
        if n_5 == "입금":
            cm += n_6
        else:
            cm -= n_6
        line[0] = "잔액 "+str(cm)+"\n"
        line[cnt] = n_l + "\n"
    with open(filename,'w',encoding="Utf-8") as file:
        file.writelines(line)
    return