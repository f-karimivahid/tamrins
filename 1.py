def reverse(str):
    result=""
    for char in str:
        result=char+result
    return result
word=str(input("kalame vared konid :"))
print(reverse(word))
