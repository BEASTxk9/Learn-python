# `run "cd examples" then "py placeholders.py" in the terminal`
# Placeholders in strings
# _____________________________________

# name = "Jeff";                                             # variable, type string
# sentence = "%s is 15 years old";                           # variable, type string with place holder "%s"

# print(sentence % name);                                    # display variables and add placeholder 


# sentence1 = "%s %s was the president of the US";           # variable, type string with place holder "%"
# print(sentence1 % ("Barack", "Obama"));                    # display variables and add placeholder 


sentence2 = "%s is %d years old";                            # %s = string + %d = integer
print(sentence2 % ("Jeff", 15 ));

