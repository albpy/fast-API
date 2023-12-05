def reverse_str(string):
    str_len = len(string)
    rev = ""
    i = str_len - 1
    while(i>=0):
        rev+=string[i]
        i-=1
    return(rev)

# print(reverse_str("Albin"))

def recursive_reverse(string, itered = 0):
    str_len = len(string)
    if str_len == 0 | str_len == 1:
        return string
    if itered == str_len//2:
        return string
    # Python strings are immutable, you cannot change their individual characters directly using indexing and assignment.
    # Convert the string to a list
    str_list = list(string)
    temp = string[itered]
    str_list[itered] = str_list[str_len-itered-1]
    
    str_list[str_len-itered-1] = temp

    # Convert the list back to a string
    reversed_string = ''.join(str_list)

    return recursive_reverse(reversed_string, itered+1)

print(recursive_reverse("mala"))
