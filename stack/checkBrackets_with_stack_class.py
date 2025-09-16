from stack_class import ArrayStack

def checkBrackets(statement):
     pairs = {')' : '(', ']' : '[', '}' : '{'}
     openings = set(pairs.values())
     stack = ArrayStack(len(statement))

     for ch in statement:
        if ch in openings:
            stack.push(ch)
        elif ch in pairs:
            if stack.is_empty():
                return False
            if stack.peek() != pairs[ch]:
                return False
            stack.pop()
        else:
            pass

     return stack.is_empty()

    


def test_brackets():
    tests = [
        "{A[(i+1)]=0;}", # True}
        "if ((x<0) && (y<3)", # False
        "while (n < 8)) {n++;}",    # False
        "arr[(i+1])=0;", # False 
    ]
    for t in tests:
        print(t, "->", checkBrackets(t))
    

if __name__ == "__main__":
    test_brackets()


