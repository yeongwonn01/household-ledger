from datetime import date,time,datetime

filename = "data.txt"
filename_category = "category_file.txt"

#입금과 출금 관리
def money_io(money:int, io_check:bool,category:str):
    category += "\n"
    total_money:int = 0
    current_time:str = datetime.now().strftime("%Y:%m:%d-%H:%M:%S")
    new_money_str:str = str(money) + " " + str(current_time)+"\n"
    with open(filename,'r',encoding="Utf-8") as file:
        line = file.readlines()
    i = 0
    does_inserted = False
    while i < len(line):
        if "카테고리" in line[i]:
            temp_cat = line[i].split(":")
            j = i
            while line[j] != "}\n":
                if line[j] == "입금\n":
                    loc,total_money_input = file_input_output(line,j+1)
                    total_money += total_money_input
                    if io_check == True and temp_cat[1] == category:
                        line.insert(loc,new_money_str)
                        does_inserted = True
                        total_money += money
                    j = loc
                elif line[j] == "출금\n":
                    loc,total_money_output = file_input_output(line,j+1)
                    total_money -= total_money_output
                    if io_check == False and temp_cat[1] == category:
                        line.insert(loc,new_money_str)
                        does_inserted = True
                        total_money -= money
                    j = loc
                else:
                    j+=1
            i = j
        else : 
            i += 1
    if does_inserted == False:
        new_line = file_create_category(category,new_money_str,io_check)
        for i in new_line:
            line.append(i)
    with open(filename,'w',encoding="Utf-8") as file:
        file.writelines(line)
    return total_money

def file_input_output(line:list, j:int):
    total_inputoutput = 0
    while line[j] != "]\n":
        new_line = line[j].split(" ")
        total_inputoutput += int(new_line[0])
        j+= 1
    return j, total_inputoutput

def file_create_category(category,money_str,io_check):
    new_line = []
    new_str = "카테고리:"+str(category)
    new_line.append(new_str)
    new_line.append("입금\n")
    if io_check == True:
        new_line.append(money_str)
    new_line.append("]\n")
    new_line.append("출금\n")
    if io_check == False:
        new_line.append(money_str)
    new_line.append("]\n")
    new_line.append("}\n")
    return new_line

#카테고리 리턴
def return_all_category_basic_fx():
    with open(filename_category,'r',encoding="Utf-8") as file:
        line = file.readlines()
    return line

if __name__ == "__main__":
    money_io(12000,False,"예시")
        