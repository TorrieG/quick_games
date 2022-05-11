"""
TASK-1
Create a method called noSpace()
This method will take one String argument and it will return a new String with all spaces removed from the original String
"""
def no_space(word):  
    print(word.replace(" ", ""))


"""
TASK-2
Create a method called replaceFirstLast()
-This method will take one String argument and it will return a new String with first and last characters replaced

NOTE: if the length is less than 2, then return empty String
NOTE: Ignore all before and after spaces (get actual String only)
"""
def replaceFirstLast(word):    
    word = word.strip()
    if len(word) < 2:
        print(word)
    else:
        print(word[-1]+word[1:-1]+word[0])







no_space("    Hello    ")
replaceFirstLast("    Hello   ")