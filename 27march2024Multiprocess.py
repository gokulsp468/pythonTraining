import multiprocessing

def Sq_List(num_list, result, sum_list):
    for idx, num in enumerate(num_list):
        result[idx] = num * num

    sum_list.value = sum(result)

def main():
    num_list = [1, 2, 3, 4, 5]
    result = multiprocessing.Array('i', 5)
    sum_list = multiprocessing.Value('i')

    p = multiprocessing.Process(target=Sq_List, args=(num_list, result, sum_list))
    p.start()
    p.join()

    print("Result(in main program): {}".format(result[:]))


    print("Sum of squares(in main program): {}".format(sum_list.value))

if __name__ == "__main__":
    main()