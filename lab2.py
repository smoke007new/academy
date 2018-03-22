CONV_NUMBER_TABLE = (
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    )

def roman_to_arab(roman_txt):
    '''
    Transform the Roman numerals into Arabic
    '''
    arab_number = 0
    for arab, roman in CONV_NUMBER_TABLE:
        while roman_txt.startswith(roman): 
# check to see if the string starts from the template
            arab_number += arab
            roman_txt = roman_txt[len(roman):]
    if len(roman_txt) != 0:
# if there is not a valid character        
        return 'Error argument'
    else:
        return arab_number

def arab_to_roman(number_arab):
    '''
    We transform the Arabic numerals into Roman numerals
    '''
# if there is not a valid character
    if  not isinstance(number_arab, int):
        return 'Error argument'
    if number_arab <= 0:
        return 'not a valid argument'
    roman_txt = ''
    for arab, roman in CONV_NUMBER_TABLE:
        while number_arab >= arab: 
# find the corresponding number or less to find the remainder
            roman_txt += roman
            number_arab -= arab
    return roman_txt

input_arab = input('Enter the Roman number: ')
out_arab = roman_to_arab(input_arab)
out_roman = arab_to_roman(out_arab)

print('Initial value: ' + input_arab)
print('Arab: ' + str(out_arab))
print('Roman: ' + out_roman)