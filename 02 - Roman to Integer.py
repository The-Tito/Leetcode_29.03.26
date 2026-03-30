

def romanToInt(s):
    roman_list = {"i":1, "v":5, "x":10, "l":50, "c":100, "d":500, "m":1000}
    s_characters = list(s.lower())
    print("lista ",s_characters)
    n = len(s_characters)
    print("n ", n)
    pre_number = 0
    temp = 0
    result = 0
    for i in range ( n - 1 ):
        for j in range ( n + 1, n):
            actual_number = roman_list.get(s_characters[i])
            post_number = roman_list.get(s_characters[j])
            print("actual:", actual_number)
            if actual_number < post_number and i > 0:
                temp = actual_number - pre_number;
                print("entre a temp:", temp)
                result = result + temp
            result = result + actual_number
            print("result", result)
    return result
    



def romanToInt_2(s):
    print(s)
    roman_list = {"i":1, "v":5, "x":10, "l":50, "c":100, "d":500, "m":1000}
    s_characters = list(s.lower())[::-1]
    print("lista ",s_characters)
    n = len(s_characters)
    print("n ", n)
    temp = 0
    result = 0
    flag = False
    j = 1
    k = 0
    for i in range ( n ):
        if ( j < n):
            print("j", j, "k", k)
            actual = roman_list.get(s_characters[k])
            print("actual", actual)
            if( j > n):
                post = 0
            else:
                post = roman_list.get(s_characters[j])
                print("post", post)
            print("flag", flag)
            if (actual >  post):
                temp = actual - post
                print("temp", temp)
                result = result + temp
                flag= True
            # elif(actual ==  post):
            #     result = result + (post + actual)
            elif(flag != True):
                result = result + (actual + post)
                print("result en flag", result)
            flag = False
            k = k + 2
            j = j + 2
            print("j", j, "k", k)
            print("result", result)
        else:
            actual = roman_list.get(s_characters[k])
            print("actual", actual)
            print("pre_final", result)
            return result + actual
    return result



def romanToInt_2_2(s):
    roman_list = {"i":1, "v":5, "x":10, "l":50, "c":100, "d":500, "m":1000}
    s_characters = list(s.lower())
    n = len(s_characters)
    final = 0
    k = 1
    for i in range ( n - 1 ):
        for j in range(i + 1, 2):
            new_list = s_characters
            print("k", k)
            post = roman_list.get(new_list[k])
            print("post", post)
            actual = roman_list.get(new_list[j])
            print("actual", actual)
            final = final + conditionals(actual, post)
            print("final", final)
            s_characters.pop(0)
            k = k + 1
        else:
            print("j", j)
            post = 0
            actual = roman_list.get(s_characters[j])
            print("actual", actual)
            final = final + conditionals(actual, post)
            print("final", final)   
    return final


    





def conditionals(actual, post):
    result = 0
    match actual:
        case 1:
            if(post == 5):
                result = post - actual
            elif(post == 10):
                result = post - actual
            result = actual 
        case 10:
            if(post == 50):
                result = post - actual
            elif(post == 100):
                result = post - actual
            result = actual 
        case 100:
            if(post == 500):
                result = post - actual
            elif(post == 1000):
                result = post - actual
            result = actual 
        case _:
            if(actual == post):
                result = post + actual
            else:
                result = actual
    print("result", result)
    return result
            
s = "CLIV"

def romanToInt_3(s):
    roman_list = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    result = 0
    for i in range ( len(s)):
        if (i + 1 < len(s) and roman_list[s[i]] < roman_list[s[i + 1]]):
            result -= roman_list[s[i]]
        else:
            result += roman_list[s[i]]
    return result

print(romanToInt_3(s))