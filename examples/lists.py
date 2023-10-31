# `run "cd examples" then "py lists.py" in the terminal`
# lists
# _____________________________________


# basically an array
shopping_list = [
  "apples",
  "bananas",
  "oranges",
  "cheese",  
];

# print(shopping_list);                       # display array
# print(shopping_list[0]);                    # display item in the array
# print(shopping_list[2]);                    # display item in the array
# print(shopping_list[0:3]);                  # display items from index 0 - 3 in the array however the last item will be ignored



# add items to list
# shopping_list.append("blueberries");

# # updating items in list
# shopping_list[0] = "cherries";

# # delete item from list
# del shopping_list[1];

# print(shopping_list);


# lenth of list
# print(len(shopping_list));


shopping_list2 = [
  "bread",
  "jam",
  "pb",  
];

new_list = shopping_list+shopping_list2;


# print(new_list);
# print(len(new_list));



list_num = [1, 2, 3, 4, 5, 10, 9];

print(max(list_num));
print(min(list_num));
