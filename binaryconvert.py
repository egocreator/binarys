number_in_binary=input('Enter your binary number!:')
def toDecimal(number_in_binary):
    
    number = []

    for letter in number_in_binary:
        number.append(letter)    

    number_turned = []

    for letter in number_in_binary:
        number_turned.append(number.pop())

    return number_turned





def multiply_position(binarys):
    binarys=toDecimal(binarys)
    decimalsum= 0
    for i in range (len(binarys)):
        decimalsum+= int(binarys[i]) *2 **i
    print(decimalsum)

multiply_position(number_in_binary)