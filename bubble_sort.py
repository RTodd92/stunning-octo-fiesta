def bubble_sort(dataset):
    dataset_length = len(dataset)
    for i in range(dataset_length):
        for j in range(1, dataset_length - i):
            if dataset[j - 1] > dataset[j]:
                dataset[j], dataset[j - 1] = dataset[j - 1], dataset[j]
                print(dataset)

numbers = [10,15,18,5,26,100,1,4,2,8]
bubble_sort(numbers)