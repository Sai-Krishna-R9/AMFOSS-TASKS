#########task-09-multiplication showdown###########

####algorithms used#######
1)naive multiplication method- the standard matrix multiplication we do in mathematics..
2)divide and conquer- splits entire matrix in to four quarters multiplies them individually and combines them to get one result
3)Strassen's Algorithm-Normal Divide and Conquer splits each matrix into 4 quarters and needs 8 multiplications to combine them into the final answer. Strassen's algorithm
 will combine the quarters in a specific way using only 7 multiplication.



########approach##########
used pythons `time.time()` to measure and compare real world time taken after each algorithm to run the input matrices and further converting them into milli seconds 
and therefore comparing them in terms of speed.


##########concepts used######
-recursion, divide and conquer pattern
-usage of strassen's 7-multiplication formula
-python timing calculation with tim.time()

