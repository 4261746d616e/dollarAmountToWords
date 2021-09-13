# Written by Achala Samarasekara 12/09/2021
# My first proper python program!
# Enter a $ and Cents amount up to 9999.99 and this program will convert it to a string of words.

def numberToWords(value):
    # Check value is less than 10,000 as that is all the logic operates up to.
    if value > 9999.99:
        return 'enter value below 9999.99'

    # If user enters only an integer, turn it into a float with 2dp to account for cents.
    if type(value) == int:
        value = round(float(value),2)

    # Create all variables
    onesDict= {'0':'','1': 'One', '2': 'Two','3' : 'Three', '4' : 'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight','9':'Nine','10': 'Ten'}
    tensDict= {'0':'','2': 'Twenty','3' : 'Thirty', '4' : 'Fourty', '5':'Fifty', '6':'Sixty', '7':'Seventy', '8':'Eighty','9':'Ninety','1' : 'One Hundred'}
    teensDict= {'10':'Ten','11': 'Eleven', '12': 'Twelve','13' : 'Thirteen', '14' : 'Fourteen', '15':'Fifteen', '16':'Sixteen', '17':'Seventeen', '18':'Eighteen','19':'Nineteen'}
    otherWords = {100:'hundred', 1000:'Thousand'}
    centHundreds=''
    centTens=''
    dollarsOnes = ''
    dollarsTens = ''
    dollarsHundreds = ''
    dollarsThousands = ''
    cent0 = '0'
    cent1 = '0' 
    ones = '0'
    tens = '0' 
    hundreds = '0' 
    thousands = '0'

    #Take the value user has input, break it up into a list
    value = str(value)
    valueList = list(value)
    

    # If value had a zero at the end, it is lost when converting to list, so add that zero back.
    if valueList[-2] == '.':
        valueList.append('0')
    

    #Start from cents and work up as we know there will always only 0 and -1 for cents but dollar amount can vary.
    valueList.reverse()
    
    

    #DEAL WITH CENTS IN THIS SECTION
    #---------------------------------------------------#
    # Assign cents to variables based on list position
    cent0 = valueList[0]
    cent1 = valueList[1]

     # Account of cents only being "teen" numbers  
    if cent1 == '1' and cent0 != 0:
        cent1 = cent1+valueList[0]     
        centTens = teensDict[cent1]
        
    # Account for no cents
    elif cent0 == '0' and cent1 == '0':
        centTens = ''
        centHundreds = ''

    # All other cents combinations
    else:
        centTens = tensDict[cent1]
            
        centHundreds = onesDict[cent0]
        
    

    #---------------------------------------------------#
    #Deal with dollars here
    #Go through the list, starting after the decimal point which is always at position 3.
    #---------------------------------------------------#
    # Check the ones position
    for i in range(3,len(valueList)):
        if i == 3:
            ones = valueList[i]
            dollarsOnes = onesDict[ones]

        # Chcek the tens position, if statement to check for "teens"
        if i == 4:
            tens = valueList[i]
            if tens == '1':
                tens = tens+valueList[3]     
                dollarsTens = teensDict[tens]               
            
            # If no "teens" numbers present then...
            else:
                dollarsTens = tensDict[tens]
                
                ones = valueList[3]
                
                dollarsOnes = onesDict[ones]
        # Check hundreds position
        if i == 5:
            hundreds = valueList[i]
            dollarsHundreds = onesDict[hundreds] + ' ' + otherWords[100]
        
        # Check thousands position
        if i == 6:
            thousands = valueList[i]
            dollarsThousands = onesDict[thousands] +' ' + otherWords[1000]
        
        # Special case if thousands value exists, remove the "hundred" word from the string displayed to user.
        if dollarsThousands != '':
            dollarsHundreds = onesDict[hundreds]
            

    # Print out all variables, just for troubleshooting

    """ print('centhundreds',centHundreds,'\n'
    'centTens', centTens,'\n'
    'dollarsOnes', dollarsOnes,'\n'
    'dollarsTens', dollarsTens,'\n'
    'dollarsHundreds', dollarsHundreds,'\n'
    'dollarsThousands',dollarsThousands ,'\n'
    'cent0', cent0 ,'\n'
    'cent1',cent1 , '\n'
    'ones', ones ,'\n'
    'tens', tens ,'\n'
    'hundreds', hundreds ,'\n'
    'thousands', thousands,'\n')
 """
    #---------------------------------------------------#
     # Print the correct statements
    #---------------------------------------------------#
    
          
   # Set the word to use for singular or plural of cents and dollars
    if cent0 == '1' and cent1 =='0':
        centWord = 'Cent'
    else:
        centWord = 'Cents'

    if   ones == '1' and tens == '0' and hundreds == '0' and thousands == '0' :
        dollarWord = 'Dollar'
    else:
        dollarWord = 'Dollars'

    # if no thousands digit is present, the word "and" is used to join the hundreds word to the string.
    if dollarsThousands == '' and dollarsHundreds !='':
            dollarsHundreds = dollarsHundreds + ' ' + 'and'
    


    # cases If dollars and cents are zero
    if  ones == '0' and tens == '0' and hundreds == '0' and thousands == '0' and cent0 == '0' and cent1 == '0' :
        return (f'Zero dollars')  

    # cases If dollar amount is zero but cents are not
    if ones == '0' and  tens == '0' and hundreds == '0' and thousands == '0' and (cent0 != '0' or cent1 != '0'):
        if cent0 == '1' and cent1 == '0':
            return (f'{centHundreds} {centWord}')
            
        else:
            # make the string all lower case because I'm lazy and the testing words were all lower case.
            mystring = " ".join((f'{centTens} {centHundreds} {centWord}').split())
            return mystring
        
            
    #If dollars are NOT zero and cents are zero
    if cent0 == '0' and cent1 == '0' :
        
        mystring = " ".join((f'{dollarsThousands} {dollarsHundreds} {dollarsTens} {dollarsOnes} {dollarWord}').split())
        return mystring
    
    #If only single dollar(s) and cents    
    if tens == '0' and hundreds == '0' and thousands == '0' and ones != '0' and cent0 != '0' and cent1 != '0':
        
        mystring = " ".join((f'{dollarsOnes} {dollarWord} and {centTens} {centHundreds} {centWord}').split())
        return mystring
    
    
    else:      
        
        mystring = " ".join((f'{dollarsThousands} {dollarsHundreds} {dollarsTens} {dollarsOnes} {dollarWord} and {centTens} {centHundreds} {centWord}').split())       
        return mystring