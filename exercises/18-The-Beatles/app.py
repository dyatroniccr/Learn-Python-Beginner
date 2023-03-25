# Your code here!!
def sing():
    var_1 = "let it be"
    var_2 = "whisper words of wisdom"
    var_3 = "there will be an answer"
    sing_total = "let it be"
    for i in range(11):
        if(i == 3):
            sing_total += ", " + var_2
        elif(i == 9):
            sing_total += ", " + var_3
        else:
            sing_total += ", " + var_1
    #print(f'{}')
    return sing_total


print(sing())