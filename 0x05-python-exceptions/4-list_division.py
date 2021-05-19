#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for i in range(len(my_list)):
        try:
            res = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            res = 0x
            print("division by 0x")
        except TypeError:
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            list.append(res)

    return list
