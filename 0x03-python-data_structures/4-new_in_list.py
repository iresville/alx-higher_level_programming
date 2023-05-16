def new_in_list(my_list, idx, element):
    # Create a new copy of the list
    new_list = my_list[:]
    
    # Check if idx is a valid index
    if idx >= 0 and idx < len(my_list):
        # Replace the element at idx
        new_list[idx] = element
    
    # Return the new list
    return new_list
