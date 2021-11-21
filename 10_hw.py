string = "The way to get started is to quit talking and begin doing";  
count = 0;  
   
for i in range(0, len(string)):  
    if(string[i] != ' '):  
        count = count + 1;  
    
print("Total number of characters in a string: " + str(count));  