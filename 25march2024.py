

class TrainingTask2():


     #this function take a string as input and returns True if all 
    # characters in the string are unique (i.e., no character appears more than once), 
    # and False otherwise. Consider uppercase and lowercase characters as different characters.

    def uniqueCharacterIdentifier(self,userString):

        for i in userString:
                
            if i in userString and userString.count(i)>1:
                return False
        
        return True
                    
   

        # this function that takes two strings as input and returns True if the two strings are anagrams 
        # of each other, and False otherwise.
        # Anagrams are strings that contain the same characters but may be in a different order.
 

    def anagramChecker(self,anagramStr1,anagramstr2):


        count1=0
        count2=0
        if len(anagramStr1) == len(anagramstr2):
            for i in anagramStr1:
                if i in anagramstr2:
                    count1+=1
            for i in anagramstr2:
                if i in anagramStr1:
                    count2+=1

        if count2 == len(anagramstr2) and count1 == len(anagramStr1):
            return True
        else:
            return False


    

   # this function that takes a string as input and returns True if the string is a palindrome, 
    # and False otherwise. A palindrome is a word, phrase, number, 
    # or other sequence of characters that reads the same forward and backward, 
    # ignoring spaces, punctuation, and capitalization.


    def palindromeChecker(self,s):
        s = s.lower().replace(" ", "")
        new_s = ''
        
        for char in s:
            if char.isalnum():
                new_s += char
                
        return new_s == new_s[::-1]



    
# this function that takes a list of integers from 1 to n (inclusive) with one integer missing and 
# returns the missing integer. 
# The list is unsorted and may contain duplicate elements.


    def find_missing_integer(self,nums):
        
        
        nums_unique = list(set(nums))
        print(nums_unique)
        n = len(nums_unique) + 1  
        expected_sum = n * (n + 1) // 2  
        actual_sum = sum(nums_unique)  
        missing_integer = expected_sum - actual_sum

        return missing_integer



  



# this function that takes two lists of integers as input and returns a list containing 
# the common elements between the two lists.
# The returned list should contain unique elements and can be in any order


    def commonElementFinder(self,l1,l2):
        common=[]
        for i in l1:
            if i in l2:
                common.append(i)
        
        
        new = set(common)
        return new
        
                
        
    

# this function that takes a list of tuples as input,
# where each tuple contains two elements: a key and a value. The function should
# return a dictionary that counts the occurrences of each value corresponding to a key.


    def count_occurrences(self,lst):
        result = {}
        
        for key, value in lst:
            if key not in result:
                result[key] = {}
            if value not in result[key]:
                result[key][value] = 1
            else:
                result[key][value] += 1
                
        return result


   




# this function that takes a string representing a Roman numeral as input 
# and returns the corresponding integer value.

    def roman_to_int(self,s):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        prev_value = 0
        
        for char in reversed(s):
            value = roman_values[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        
        return result


    




task2 =TrainingTask2()
print(task2.uniqueCharacterIdentifier("listen"))

print(task2.anagramChecker('listen','silent'))
print(task2.palindromeChecker("A man, a plan, a canal, Panama!"))
print("Output:", task2.find_missing_integer([3, 7, 1, 2, 8,8, 4, 6, 6]))
print(task2.commonElementFinder([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Output:", task2.count_occurrences([(1, 'a'), (2, 'b'), (1, 'c'), (2, 'a'), (3, 'b')]))
print("Input: 'LVIII' => Output:", task2.roman_to_int("LVIII"))