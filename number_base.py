## RADIX ##
# (number)base
# Golden ratio base

def base(base, number):
    for n in range(number):
        print(base**(n))
        #if number < (base**(n))
        pass

def number(base, number):
    return "(%i)%i" % (number, base)

def convert_to_decimal(number, new_base):
    new_num = None
    num_feed = []
    if number % new_base == 0:
        num_feed.append(int(number / new_base))
    else:
        pass
    """while num_feed != 0:
        new_num.append(num_feed)"""

    #print(new_num)
    print(num_feed)


# Python program to convert a  
# number from any base to decimal 
  
# To return value of a char.  
# For example, 2 is returned  
# for '2'. 10 is returned for 'A',  
# 11 for 'B'  
def val(c):
    #print(ord(c), ord('0'))
    if c >= '0' and c <= '9': 
        return ord(c) - ord('0') 
    else: 
        return ord(c) - ord('A') + 10; 

# Function to convert a number  
# from given base 'b' to decimal  
def toDeci(str,base): 
    llen = len(str) 
    power = 1 #Initialize power of base 
    num = 0     #Initialize result 
  
    # Decimal equivalent is str[len-1]*1 +  
    # str[len-1]*base + str[len-1]*(base^2) + ...  
    for i in range(llen - 1, -1, -1): 
          
        # A digit in input number must  
        # be less than number's base  
        if val(str[i]) >= base: 
            print('Invalid Number') 
            return -1
        num += val(str[i]) * power 
        power = power * base 
    return num

#print(toDeci('30', 12))

# Driver code 
"""strr = "B"
base = 12
print('Decimal equivalent of', strr,  
              'in base', base, 'is',  
                 toDeci(strr, base)) """

#$base(8, 42)
#convert_decimal(36, 12)

# x*base^n ... x*base^0
