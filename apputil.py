

# add code below ...
def palindrome(word):
    #step 1: convert to lowercase
    cleaned = word.lower()
    #step 2: remove non-alphanumeric characters
    cleaned = ''.join(c for c in cleaned if c.isalnum())
    #step 3: check if the cleaned word is equal to its reverse
    return cleaned == cleaned[::-1]


#finding balanced parentheses

    def parentheses_balanced(s):
        #initialize a stack
        stack = []
        #iterate over each character
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping.values():
                # If it's an opening bracket, push onto the stack
                stack.append(char)
            elif char in mapping.keys():
                # If it's a closing bracket, check for matching opening bracket
                if not stack or stack.pop() != mapping[char]:
                    # If not matched, return False
                    return False
        return not stack