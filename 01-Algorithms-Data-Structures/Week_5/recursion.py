# Exercise 1:
# Write a recursive function ispalindrome(word) that returns true if the string word is a palindrome, false otherwise.
# You can start with an implementation that does not deal with punctuation, and then refactor your code to
# consider punctuation.

def ispalindrome(word):
    # Base case: if the word is 0 or 1 character, it's a palindrome
    if len(word) <= 1:
        return True
    # If first and last characters don't match, it's not a palindrome
    if word[0] != word[-1]:
        return False
    # Recurse on the substring excluding first and last characters
    return ispalindrome(word[1:-1])

def palindrome_punctuation(word):
    # Step 1: Make everything lowercase
    word = word.lower()

    # Step 2: Keep only letters and numbers
    clean_word = ""
    for char in word:
        if char.isalnum():  # Check if it's a letter or a number
            clean_word += char

    # Step 3: Define a helper function to use recursion
    def check(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return check(s[1:-1])

    return check(clean_word)

print(palindrome_punctuation("No lemon, no melon"))             # True
print(palindrome_punctuation("Was it a car or a cat I saw?"))    # True
print(palindrome_punctuation("hello"))                           # False

# Exercise 2:
# To compute the sum of all elements in a list, you can use the built-in function sum.
# For example:
# >>> sum([1,2,3,4])
# 10
# >>> sum([])
# 0
# Write a recursive function rec_sum(numbers) that take a list of integers as a parameter
# and returns the sum of all the elements in the list. The function should return 0 if the list is empty.

def rec_sum(numbers):
    if len(numbers)<1:
        return 0
    else:
        return sum(numbers)

def rec_sum(numbers):
    # Base case: if the list is empty, return 0
    if not numbers:
        return 0
    # Recursive case: sum of first element + sum of the rest of the list
    return numbers[0] + rec_sum(numbers[1:])

print(rec_sum([1,2,3,4,5]))

# Exercise 3: (from week 3 practical)
# During week 3, we implemented the function sum_digits(number) to calculate and return the sum of digits of
# a given whole number (int) given as parameter. For example,
# >>> print(sum_digits(1234))
# 10
# At the time we used loops in our implementation. This time you must use recursion.
# In addition, you are not allowed to convert the int into a list or a string.

def sum_digits(number):
    # Base case: if the number is a single digit, return that digit
    if number < 10:
        return number
    # Recursive case: sum the last digit + sum of the remaining digits
    return number % 10 + sum_digits(number // 10)

# Exercise 4:
# Write a recursive function flatten(mlist) where mlist is a multidimensional list that returns all the element
# from mlist into a one-dimensional list. Note, empty lists are ignored.
#
# For examples:
# >>> flatten([1,[2,3],4])
# [1,2,3,4]
# >>> flatten([1,[2,[3,[4]]]])
# [1,2,3,4]
# >>> flatten([1,2,3,4])
# [1,2,3,4]
# >>> flatten([1,[]])
# [1]

def flatten(mlist):
    # Initialize the result list
    result = []

    # Iterate through each item in the list
    for item in mlist:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            result.extend(flatten(item))  # Add the flattened result
        else:
            result.append(item)  # Otherwise, just add the element

    return result

print(flatten([1, [2, 3], 4]))
print(flatten([1, [2, [3, [4]]]]))
print(flatten([1, 2, 3, 4]))
print(flatten([1, []]))
print(flatten([[[[1]]]]))

# Exercise 5:
# Write a recursive function merge(sorted_listA, sorted_listB) that merges the two sorted lists into a single
# sorted list and returns it. The two parameters are list of comparable objects that are sorted in ascending order.
# For example, the lists contain only strings, or the lists contain only numbers.
# Neither of the two lists in the parameters must be modified.


def merge(sorted_listA, sorted_listB):
    # Base cases: if one list is empty, return the other
    if not sorted_listA:
        return sorted_listB
    if not sorted_listB:
        return sorted_listA

    # Recursive case: compare the first element of each list
    if sorted_listA[0] < sorted_listB[0]:
        # Add the smaller element to the result and merge the rest of the lists
        return [sorted_listA[0]] + merge(sorted_listA[1:], sorted_listB)
    else:
        # Add the smaller element from sorted_listB and merge the rest
        return [sorted_listB[0]] + merge(sorted_listA, sorted_listB[1:])

print(merge([1, 3, 5], [2, 4, 6]))
print(merge(['apple', 'banana'], ['cherry', 'date']))



# Exercise 6: An unexpected coding journey
# A word is considered elfish if it contains all the letters: e, l, and f in it, in any order. For example,
# we would say that the following words are elfish: whiteleaf, tasteful, unfriendly, and waffles,
# because they each contain those letters.
#
# a)	Write a predicate function called iselfish(word) that, given a word, tells us if that word is elfish or not.
# The function must be recursive.
#
# b)	Write something_ish(pattern, word)a more generalized predicate function that, given two words, returns true
# if all the letters of pattern are contained in word.

def iselfish(word):
    def helper(word, found_letters):
        # Base case: If we found all required letters, return True
        if len(found_letters) == 3:
            return True

        # If the word is empty and we haven't found all required letters, return False
        if not word:
            return False

        # If the current character is one of 'e', 'l', or 'f', add it to found_letters
        if word[0] in 'elf' and word[0] not in found_letters:
            found_letters.add(word[0])

        # Continue checking the rest of the word
        return helper(word[1:], found_letters)

    # Call helper with an empty set of found letters
    return helper(word, set())

print(iselfish("whiteleaf"))
print(iselfish("tasteful"))
print(iselfish("unfriendly"))
print(iselfish("waffles"))
print(iselfish("hello"))


def something_ish(pattern, word):
    # Base case: if pattern is empty, return True
    if not pattern:
        return True

    # If the first letter of the pattern is in the word
    if pattern[0] in word:
        # Remove that character from the word and continue checking the rest of the pattern
        return something_ish(pattern[1:], word.replace(pattern[0], '', 1))

    # If the first letter of the pattern is not in the word, return False
    return False

print(something_ish("elf", "whiteleaf"))    # True
print(something_ish("abc", "acbbac"))       # True
print(something_ish("hello", "helo"))       # False
print(something_ish("grape", "orange"))     # False
