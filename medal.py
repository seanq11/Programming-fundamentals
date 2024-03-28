import csv
#read csv file
#golds = []
#silvers = []
#bronzes = []
header = ['Team,Gold,Silver,Bronze','\n']
file = csv.reader(open('medal.csv', 'r'))
next(file, None)
rows = [row for row in file]

col = 1
k = 0

#bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j][col] < arr[j + 1][col]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

list  = rows
ranked_golds = [', '.join(rows)+'\n' for rows in bubble_sort(rows)]

#def rank_team(file_name):
    #pass

len_rows = len(rows)-1
for i in range(3):
    k=0
    for i in range(len_rows):
        if rows[k][1] == rows[k+1][1]:
            if rows[k][2] == rows[k+1][2]:
                if rows[k][3] > rows[k+1][3]:
                    k+=1
                else:
                    rows[k],rows[k+1] = rows[k+1],rows[k]
                    k+=1
            elif rows[k][2] > rows[k+1][2]:
                k+=1
            else:
                rows[k],rows[k+1] = rows[k+1],rows[k]
                k+=1
        else:
            k+=1

# Program main --- Do not change the code below but feel free to comment out 
# Calling Task 1 function
ranked = [', '.join(rows)+'\n' for rows in rows]

list = []
with open('medal_table.csv', 'w+') as f:
    f.writelines(header)
    #f.writelines(ranked_golds)
    f.writelines(ranked)