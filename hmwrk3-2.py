my_list=[5, 4 , -17, 41, 0, 99, -27, 6, 12, 1, -14]
result_list=[]
half_array=int(len(my_list)/2)
if len(my_list) % 2 == 1:
    half_array+=1
def main_task (my_list):
    for i in range(0, half_array):
        temp=my_list[i] * my_list[len(my_list)-i-1]
        result_list.append(temp)
    print (result_list)

main_task(my_list)

    