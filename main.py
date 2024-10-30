import time

begin = time.time()
def myfunction (n):
    for i in range(0,n+1):
        print ("First Loop")
        
    j=1
    while (j<=n+1):
        print ("Second Loop", j)
        j=j*2
        
    for i in range (0,100) :
        print( "Third loop")

time.sleep(1)
end = time.time()
print(f"Total runtime of the program is {end - begin}")