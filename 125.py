#valid palindrom

s = "race car"

# approach #1
# add all alphanumeric characters to a new list
# two points converge from both sides

def isPalindrome1(s):
    bank = []
    for x in list(s):
        if x.isalnum():
            bank.append(x)
    for i in range(len(bank)//2):
        if bank[i].lower() != bank[-i-1].lower():
            return False
    return True


# approach #2
# two pointers
# points increment/decrement if on non alphanumeric character
# returns false characters at the pointer index don't match 
# if pointers made it all the way to the center, return true

def isPalindrome2(s):    
    l = 0 
    r = len(s)-1

    while l<r:
        if not s[l].isalnum():
            l += 1
        
        elif not s[r].isalnum():
            r -= 1

        elif s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        
        else:
            return False

    return True