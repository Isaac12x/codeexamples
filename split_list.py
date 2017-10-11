def sub_split_list_by_reminder(list, splitter):
    """
   Function to create a nested list with length equal
   to the reminder of division

   This function splites the list into an amount of nested lists equally sized
   to the second parameter.
   It also spreads the contents of the first list in nested lists equals to
   that reminder.

   Parameters
   ----------
   list : list of ints
   splitter : int

   Returns
   -------
   nested list of ints


   >>> sub_split_list_by_reminder([1,2,3,4,5], 3)
   [[1,2], [3,4], [5]]

   >>> sub_split_list_by_reminder([21, 3123, 34], 2)
   [[21, 3123], [34]]
   """

    # Required variables
    list_length = len(list)
    new_list = []
    lower_end_slice = 0
    next_slice = 0

    # Calculate the length of each new nested list
    nested_list_length = list_length % splitter
    next_slice = nested_list_length

    # Use the splitter as the iterator - can also be accomplished with
    # list comprehension, but it seems clearer in this more verbose way
    while splitter >= 1:
        # Construct a new list by slicing the first one where required
        new_list.append(list[lower_end_slice:next_slice])

        # Update the slicers
        lower_end_slice += nested_list_length
        next_slice += nested_list_length

        # Once a list is created, substract that from the remaining to create
        splitter -= 1

    # Uncoment the following line if you want to see the results
    print new_list

    # Return the updated list
    return new_list


# You can check the otutputs by going to terminal and write in the directory
# python test.py and you'll see the results || alternatively you can use
# Doctest to test the input in the docstring.
sub_split_list_by_reminder([1, 2, 3, 4, 5], 3)
sub_split_list_by_reminder([21, 3123, 34], 2)
sub_split_list_by_reminder([21, 3123, 34], 30)
