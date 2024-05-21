sample_list = [8, 2, 3, -1, 7]

def total_list(sample_list):
    sum = 1 
    for num in sample_list:
        sum *= num
    return sum
print(total_list(sample_list))
        
