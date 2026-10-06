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
    
    
        
        
        