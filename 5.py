digit_text = {'00':'Zero',
              '01': 'One',
              '02': 'Two',
              '03': 'Three',
              '04': 'Four',
              '05': 'Five',
              '06': 'Six',
              '07': 'Seven',
              '08': 'Eight',
              '09': 'Nine',
              '10': 'Ten',
              '11': 'Eleven',
              '12': 'Twelve',
              '13': 'Thirteen',
              '14': 'Fourteen',
              '15': 'Fifteen',
              '16': 'Sixteen',
              '17': 'Seventeen',
              '18': 'Eighteen',
              '19': 'Nineteen',
              '20': 'Twenty',
              '30': 'Thirty',
              '40': 'Forty',
              '50': 'Fifty',
              '60': 'Sixty',
              '70': 'Seventy',
              '80': 'Eighty',
              '90': 'Ninety'}

def convert(num) :
    if len(num) < 2 :
        num = '0'+ num
    if num[0]== '1' or num[1]== '0' :
        print(digit_text[num])
    else :
        if int(num)> 20 :
            print(digit_text[num[0]+ '0']+' '+ digit_text['0'+ num[1]])

def convert_hundred(num) : 
    sectin_1 = print(digit_text['0'+ num[0]]+' '+"Hundred ",end="")
    section_2 = convert(num[1:])

def convert_thousand(num) :
    sectin_1 = print(digit_text['0'+ num[0]]+' '+"Thousand ",end="")
    section_2 = convert_hundred(num[1:])
    
number = input("please enter a number : ")

if len(number)==1 or len(number)==2 :
    convert(number)
elif len(number)==3 :
    convert_hundred(number)
else  :
    convert_thousand(number)
    




     


