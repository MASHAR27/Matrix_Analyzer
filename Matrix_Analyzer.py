row_numbers = int(input("Please enter the number of rows you want in the matrix: "))
col_numbers = int(input("Please enter the number of columns you want in the matrix: "))

# After I get the desired dimensions I iterate over each row to fill it up with the values
matrix = []
for row in range(row_numbers):
    current_row = []
    print(f"Row number {row +1} :")
    for row_values in range(col_numbers):
        val = int(input("Please enter your value "))
        current_row.append(val)
    matrix.append(current_row)    

# After populating the matrix I display it to the user
print("This is your entered matrix:  ")

for row in matrix:
    for val_row in row:
        print(val_row,end= " ")
    print()
    
    

print("Statistics time:  ")

print()

print("Matrix as a whole wise: ")
      
total = 0
largest = matrix[0][0]
smallest = matrix[0][0]   
count = 0

for row in matrix:
    for row_val in row:
        if row_val > largest:
            largest = row_val
        if row_val < smallest:
            smallest = row_val
        count+= 1
        total += row_val
        
print(f"For the whole matrix the largest value is {largest}, while the smallest value is {smallest} , the sum of all the values is {total} and the average of all the values is {total/count}")                         

print()

print("Rows wise: ")
row_count = 0
for  row in matrix:
    row_total = 0
    for values in row:
        row_total += values
            
    print(f" For row {row_count+1}:  the total is {row_total}")  
    row_count +=1 
    
    
print()

print("Columns  wise: ")
col_count = 0
for col in range(col_numbers):
    col_total = 0
    for row_values in range(row_numbers):
        val = matrix[row_values][col]
        col_total += val
        
    print(f"The column total for column {col_count+1 } is :  {col_total}")
    col_count+=1
    
    
        
    
    