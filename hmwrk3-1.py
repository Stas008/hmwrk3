my_list=[5, 4 , -17, 41, 0, 99, -27, 6, 1, -14]
def main_task (my_list):
    sum=0
    for i in range (1, len(my_list), 2):
        sum = sum + my_list[i]
    return(sum)
print (f"Сумма элементов на нечетных позициях = {main_task(my_list)}")