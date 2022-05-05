import math

def check_posn(list, var, idx):

    if list[idx] == var:
        print('Found value  ',list[idx], ' at index : ', idx)

        return 'found'
    elif list[idx] < var:
        # print(idx +math.ceil(idx/2))
        return 'go high'
    else:
        print ( idx - math.ceil(idx/2))
        return 'go low'

def Binary_Search(list, var):

    start_idx = 0
    end_idx = len(list)

    loop_chk = 'Y'

    while loop_chk == 'Y':
        mid = math.ceil((start_idx + end_idx) / 2)
        print('in Loop', mid)
        out_val = check_posn(list, var, mid)

        if out_val == 'go high':
            start_idx = mid

        elif out_val == 'go low':
            end_idx = mid

        if out_val not in ('go high','go low'):
            loop_chk = 'N'

        if (mid < list[0] or mid > list[len(list)-1] ):
            loop_chk = 'N'

    # while position:
    #     position = check_posn(list, var, mid)
    #     print(position, mid)
    #
 


list_to_search  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_to_search_1= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
num = 3




Binary_Search(list_to_search, num)
