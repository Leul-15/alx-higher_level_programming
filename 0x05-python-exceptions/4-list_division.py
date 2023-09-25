#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            new_list[i] = 0
        except ZeroDivisionError:
            print("division by 0")
            new_list[i] = 0
        except IndexError:
            print("out of range")
            new_list[i] = 0
        finally:
            pass
    return (new_list)
