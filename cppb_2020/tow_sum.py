def two_sum(input_list, target):
    '''Takes two arguments, an input list of integers, and a target integer.
    Checks through the list for  pairs of numbers that sum to the target and 
    returns a list of pairs of indecies that sum to the target.'''

    count = 0
    output = []
    for number in input_list:                        #Iterate over the list
        for position in range(count,len(input_list)):#Iterate over unchecked positions
            if number + input_list[position] == target:#Check if sum is equal to target
                output.append([count,position])      #Append indecies to output IF equal to target
        count += 1                                   #Increment count
    return output                                    #Return output


my_list = [1, 2, 3, 5, 4, 6, 4, 2, 3, 4, 1]

print(two_sum(my_list, 7))