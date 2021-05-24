last = (1,2,5,8,1,5,2,6,3)
arithmetical_mean = sum(last) / len(last)
product_numbers_1 = 1
for i in range(len(last)):
    product_numbers_1 = 1 * last[i] * product_numbers_1    
Geometric_Mean = product_numbers_1 / len(last)
print(f"среднее арф равно {int(arithmetical_mean)} , среднее гео равно {Geometric_Mean}")
