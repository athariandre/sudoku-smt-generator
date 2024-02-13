f = open('output.txt', 'w')

#declaring every boolean variable w/ the format P_col_row_num
for col in range(1,10):
    for row in range(1,10):
        for num in range(1,10):
            f.write("(declare-const P_" + str(row) + "_" + str(col) + "_" + str(num) + " Bool)\n")


# 4 rules to sudoku: 
# each column contains each possible num
# each row contains each possible num
# each 9x9 block contains each of the 9 nums
# each cell has only one num 
f.write("\n\n\n")

# checking rule 1 | format: P_col_row_num   
for col in range(1,10):
    for num in range(1,10):
        write = "(assert (or"
        for row in range(1,10):
            write += " P_" + str(row) + "_" + str(col) + "_" + str(num)
        write += "))\n"
        f.write(write)

f.write("\n\n\n")


# checking rule 2 | format: P_col_row_num           
for row in range(1,10):
    for num in range(1,10):
        write = "(assert (or"
        for col in range(1,10):
            write += " P_" + str(row) + "_" + str(col) + "_" + str(num)
        write += "))\n"
        f.write(write)



f.write("\n\n\n")

# checking rule 3 | format: P_col_row_num 
        
for box_col in range(3):
    for box_row in range(3):
        for num in range(1,10):
            write = "(assert (or"
            for box_col_col in range(1,4):
                for box_row_row in range(1,4):
                    write+= f" P_{box_row*3 + box_row_row}_{box_col*3 + box_col_col}_{num}"
            write += "))\n"
            f.write(write)


# checking rule 4 | format: P_col_row_num
            
for col in range(1,10):
    for row in range(1,10):
        for num1 in range(1,10):
            write = f"(assert (or (not P_{row}_{col}_{num1}) (not (or"
            for num2 in range(1,10):
                if num1 != num2:
                    write += f" P_{row}_{col}_{num2}"
            write += "))))\n"
            f.write(write)

f.write('(check-sat)\n(get-model)\n')
f.close()