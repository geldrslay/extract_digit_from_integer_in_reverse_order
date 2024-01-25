#  Write a Program to extract each digit from an integer in the reverse order.

# Display the given number
given_number =1024589
print ('The given number is:',given_number)

# Reverse given number using a while loop
while given_number > 0:
    digit = given_number % 10
    given_number = given_number // 10
    # Display the result 
    print (digit, end=" ")
    