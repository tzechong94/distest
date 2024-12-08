'''
Write a function takes an input string and returns an expanded string, based on these rules:

1.  The string consists of letters and positive numbers and the opening and closing chevrons '<', and '>'. 
   Example: 2<xy>3<z>
2.  The number preceding an open chevron indicates the number of times that the letters within the pair of chevrons should be repeated.
   Example: 2<xy> indicates that the letters 'xy' should be repeated 2 times, resulting in "xyxy"
3.  The chevrons can be nested. Inner chevrons should be resolved before outer chevrons.
   Example: 3<x2<y>> results in 3<xyy>, results in "xyyxyyxyy"
4.  If a letter is not modifiable, it is included in the final string.
   Example: "2<x>z" results in "xxz"
Assume that the string is always valid, and the number indicating repetitions is greater than 0.
Test cases: 
expand("xx") // "xx"
expand("2<xy>")  // "xyxy"
expand("2<x>z") // "xxz"
expand("2<xy>3<z>")  // "xyxyzzz"
expand("3<x2<y>>")  // "xyyxyyxyy"
'''

def expand(s):
    '''
    result string = ""
    iterate through string
        - if alphabet, append to string
        - if number, store it in stack
        - if bracket, store inner string until next closing bracket in stack
    2 stacks, one for number one for alphabet
    if closed bracket, pop off number stack and multiply letters and number
    '''
    result = ''
    numstack = []
    letterstack = []
    workingstring = ""

    for char in s:
        # char.isdigit() isalpha()
        # print(char, 'cuurent char')
        if char.isalpha():
            workingstring += char
        if char.isdigit():
            if workingstring != "":
                letterstack.append(workingstring)
                workingstring = ""

            numstack.append(int(char))
        if char == "<":
            if workingstring != "":
                letterstack.append(workingstring)
                workingstring = ""
        if char == ">":
            if len(letterstack) != 0:
                if workingstring != "":
                    letterstack.append(workingstring)
                    # workingstring = ""
                # if no number default to 1 todo
    
                result = numstack.pop() * (letterstack.pop() + result)
            else:
                result += numstack.pop() * workingstring
            workingstring = ""

        # if char == ">" and len(letterstack) != 0:
        #     if workingstring != "":
        #         letterstack.append(workingstring)
        #         workingstring = ""

        #     if len(letterstack) != 0:
        #         # if no number default to 1 todo
    
        #         result = numstack.pop() * (letterstack.pop() + result)
        #         # substring = numstack.pop() * letterstack.pop()
        #         # print(substring, ' substring')
        # elif char == ">" and len(letterstack) == 0:
        #     result += numstack.pop() * workingstring
        #     workingstring = ""

        # print(result, ' result within loop')
        # print(workingstring, 'working string')
        # print(numstack, ' numstack')
        # print(letterstack, ' letterstack')

    result = result + workingstring
    print(result, ' result')
            


        

expand("xx") 
expand("3<x2<y>>")  #xyyxyyxyy
expand("2<xy>")  # xyxy
expand("2<x>z") # xxz
expand("2<xy>3<z>")  # xyxyzzz

# // "xx"
# // "xyxy"
# // "xxz"
# // "xyxyzzz"
# // "xyyxyyxyy"
