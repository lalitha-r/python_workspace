# Problem #2
# Same as above,but print the list in descending order
# input = [1,2,3,3,3,4,4,7,7,9]
# output = [9,7,4,3,2,1,_,_,_,_]

def remove_duplicates_and_append_underscore(input_list):
    # if input list is duplicate, return empty array
    if not input_list:
        return []
    # sort the input list in descending order
    input_list.sort(reverse=True)
    #  initialize result with the first element of the list
    result = [input_list[0]]
    # initialize prev_element with the first element so that we can compare it with the next element
    prev_element = input_list[0]

    # loop from the index 1 so that we can compare with the prev_element
    for i in range(1, len(input_list)):
        # if element in current index not equal to the prev_element then its unique
        # append it to the result
        if input_list[i] != prev_element:
            result.append(input_list[i])
            prev_element = input_list[i]

    # subtract the length of the input list with the length of the result
    # to get the remainig length to be filled with underscores
    for i in range(len(input_list)-len(result)):
        result.append('_')

    return result


input_list = [1, 2, 3, 3, 3, 4, 4, 7, 7, 9]
output_list = remove_duplicates_and_append_underscore(input_list)
print(output_list)
