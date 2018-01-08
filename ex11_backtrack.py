##############################################################################
# FILE : ex11_backtrack.py
# WRITER : Jason Greenspan , jasonmg , 336126362
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION: ****
##############################################################################

def general_backtracking(list_of_items, dict_items_to_vals, index,
                         set_of_assignments, legal_assignment_func, *args):
    """list_of_items: list of items we want to assign
    dict_items_to_vals: keys from list_of_items; values from set_of_assignments
    index: integer representing the place in list_of_items for current key
    set_of_assignments: permitted assignments (for instance, 1...9 for sudoku)
    args: additional other functions that can be passed throguh the function"""

    # Recursion base case: every item has been assigned.
    if index == len(list_of_items):
        return True
    
    current_item = list_of_items[index]
    # Save previous assignment in case new assignment is not legal.
    previous_assignment = dict_items_to_vals[current_item]
    for assignment in set_of_assignments:
        dict_items_to_vals[current_item] = assignment
        if legal_assignment_func(dict_items_to_vals, current_item):
            if general_backtracking(list_of_items, dict_items_to_vals, index+1,
                         set_of_assignments, legal_assignment_func):
                return True
                
    # Rewrite most recent entry and backtrack.
    dict_items_to_vals[current_item] = previous_assignment
    return False
