from typing import List
import re


def sum_numbers(nums: list[int]) -> int:
    pos=[]
    neg=[]
    for num in nums:
        if num >0:
            pos.append(num)  
        if num<0:
            neg.append(num*-1)
        print(pos, neg)
        return sum(pos)-sum(neg)
print(sum_numbers([2, -3, 5, -1]))
    # """
    # Takes a list of numbers and returns the result of:
    # - Adding all positive numbers
    # - Subtracting all negative numbers 

    # Example:
    #     sum_numbers([2, -3, 5, -1]) → (2 + 5) - (3 + 1) = 3
    # """
    # pass

def is_anagram(str1: str, str2: str) -> bool:
    string1=[]
    string2=[]
    for letter in str1:
        if letter.isalpha():
            string1.append(letter)
    for letter_2 in str2:
        string2.append(letter_2)
    string_1=sorted(string1)
    string_2=sorted(string2)
    if len(string_1)==len(string_2):
        if sorted(string1.lower()) ==sorted(string2.lower()):
            return True
        else:
            return False
    else:
        return False

    # symbols=r'[^a-zA-Z]'
    # # string1=re.findall(symbols,str1)
    # string1=re.sub(symbols,str1,"")
    # if len(string1)==len(str2):
    #     for letter in string1:
    #         if letter in str2:
    #             return True
    #         else:
    #             False
    # else:False 

print(is_anagram("hello","olleh"))

    
    # """
    # Check if two strings are anagrams (ignoring case and spaces).
    
    # Example:
    #     Input → str1 = "listen", str2 = "silent"
    #     Output → True
        
    #     Input → str1 = "hello", str2 = "world"
    #     Output → False
    # """
    # pass

def fibonacci_series(n_terms: int) -> List[int]:
    """
    Generate a Fibonacci series with n_terms.
    
    The series starts with 0, 1 and each subsequent term is the sum of the previous two.

    Example:
        Input → 10
        Output → [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    pass

def prime_factors(n: int) -> List[int]:
    """
    Return a list of all prime factors of a given number n.
    
    Example:
        Input → 84
        Output → [2, 2, 3, 7]
    """
    pass

def create_pyramid(n):
    
    for i in range(1,n+1):
        print("*"*i)
print(create_pyramid(5))
        
    # """
    # Returns a pyramid of '*' as a list of strings.

    # Example:
    #     Input → 3
    #     Output →['  *  ', ' *** ', '*****']
    # """
    # pass

def create_number_triangle(n):
    for i in range(1,n+1):
        print(str(i)*i)
print(create_number_triangle(5))
    # """
    # Returns a triangle of numbers as a list of strings.
    # Example  :      
    #     Input → 3
    #     Output →    ['  1  ', ' 2 2 ', '3 3 3']
    # """
    # pass

def create_multiplication_square(n: int) -> List[str]:

    for num in range(1,n+1):
        print(*[num*n for n in range(1,n+1)])
    # for row in list:
    #     print("".join(str(row)))


print(create_multiplication_square(3))


  
    # """
    # Returns a multiplication square as a list of strings.
    # Example:
    #     Input → 3
    #     Output → ['1 2 3', '2 4 6', '3 6 9']
    # """
pass


def create_diamond(n):
    for i in range(1,n):
        for j in range(n,0):
            print(j)
            print(""*j,"*"*i)
print(create_diamond(5))
    # """
    # Returns a diamond shape as a list of strings.
    # Example:
    #     Input → 3
    #     Output →    ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
    # """    
    # pass

def create_pascals_triangle(n: int) -> List[str]:
    """
    Return Pascal's triangle of height n as a list of strings.
        Example:
        Input → 5
        Output → ['    1    ', '   1 1   ',    '  1 2 1  ', ' 1 3 3 1 ', '1 4 6 4 1']
    """
    pass