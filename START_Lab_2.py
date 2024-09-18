def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    is_palindrome = False
    reverse_word = word[::-1]
    print(reverse_word)
    if word == reverse_word:
        is_palindrome = True
    return is_palindrome

# print(lab2Question1('racecar'))

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    fib_seq = []
    for number in list(range(0,number_val+1)):
        if number == 0 or number == 1:
            fib_seq.append(number)
        else:
            new_num = fib_seq[number - 1] + fib_seq[number - 2]
            fib_seq.append(new_num)
    return fib_seq

#print(lab2Question2(7))

def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    counter = 0
    found = 0 
    str1 = str1.lower()
    print(str1)
    # find where the first one is, add counter, then delete and do it again till index/list is empty or no st2 is found
    while found != -1:
        found = str1.find(str2)
        print(found)
        if found != -1:
            counter += 1 
            print(found)
            str1 = str1[found + len(str2):]
            print(str1)
    return counter

#print(lab2Question3('Coding is cool, cooking with cockatool', 'oo'))

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    sum_list = []
    if len(list1) == len(list2):
        for index in range(0,len(list1)):
            sum_list.append(list1[index]+list2[index])
    return sum_list

#print(lab2Question4([1, 2, 3, 4, 10], [5, 6, 7, 8]))

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    isValid = {
        'length': False,
        'upper' : False,
        'lower' : False,
        'number': False,
    }

    if len(password) >= 8:
        isValid['length'] = True
        for letter in password:
            if letter.isupper():
                isValid['upper'] = True
            if letter.islower():
                isValid['lower'] = True
            if letter.isdigit():
                isValid['number'] = True

    result = all(item == True for item in isValid.values())
    return result

def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    password = input('Please enter a valid password: ')
    while isValidPassword(password) == False:
        print('')
        print(password + ' is invalid')
        print('The passowrd must meet the criteria: ')
        print('- At least 8 characters long')
        print('- Contains at least one uppercase letter')
        print('- Contains at least one lowercase letter')
        print('- Contains at least one number')
        print('')
        password = input('Please enter a valid password: ')
    print('Password created successfully')
    return password

lab2Question5()





    

