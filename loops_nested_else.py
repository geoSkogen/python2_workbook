for num in range(10, 20): #go over a given range of integers and for each one,
    for i in range(2, num): #go over every number less than that integer--and for
        if num % i == 0: #each one of THOSE numbers, check for a remainder of
                          #zero when diving the integer-in-range by it;
            j = num/i #if the remainder is zero, find the product of that division
            print("%d is equal to %d * %d" % (num, i, j))#show the formula
            #go to next integer-in-range or 'else' clause will execute
            break#stop going over couting-up-to-it numbers
                 #flow control restored to outer loop;
    #if the number-in-range can't be evenly divided by any of the
    #numbers-counting-up-to-it, flow never encounters the break statement;
    #the inner iteration is complete, and the 'else' statement executes
    else:
        print(num, 'is a prime number')
    #afterward, the outer loop goes to the next integer in the given range
