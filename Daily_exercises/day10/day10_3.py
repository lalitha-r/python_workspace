# Problem #3
# Add two number represented in a list as reversed. print the sum also as a list in reverse order
# eg input list1 = [1,2,3] list2 = [5,6,7]
# answer= [6,8,0,1]
#  explanation (321 + 765 = 1086)


# reverse arrays
# join each reversed array as string
# cast string to number and add them
def add_two_num_list_reverse(input_list1, input_list2):
    # if input list is duplicate, return empty array
    if not input_list1 or not input_list2:
        return []
    # reverse the input list1 and list2
    input_list1.sort(reverse=True)
    input_list2.sort(reverse=True)

    # convert the reversed lists into an string
    result_string1 = ''.join(map(str, input_list1))
    result_string2 = ''.join(map(str, input_list2))

    # convert the two strings into number and add them
    sum = int(result_string1) + int(result_string2)

    # convert the sum into list
    str_result = list(str(sum))

    # initialize the result as empty array
    result = []
    # loop the reversed list
    for elm in str_result[::-1]:
        # append each element into the result
        result.append(int(elm))

    return result


input_list1 = [17, 24, 37]
input_list2 = [55, 60, 71]
output = add_two_num_list_reverse(input_list1, input_list2)
print(output)
