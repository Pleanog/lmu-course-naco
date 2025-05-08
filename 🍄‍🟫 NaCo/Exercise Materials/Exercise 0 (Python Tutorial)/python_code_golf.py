from typing import Dict, List, Tuple, Union

#
# In a python editor of your choice, fill in the blanks to deepen 
# your understanding of Python. The questions structure will be:
# 
# [Topic](Code golf) Assignment ...
# 
# > Topic: The corresponding chapter in the slides, e.g. [Ch 2 Multiple Assignment]
#
# > Code golf: A little challenge to compress assignments into (at best) this amount 
#   of lines of code (LoC).
#
# > If given as parameters, use the given input in your solution and make sure to return your 
#   solution from the function! The return counts as 1 LoC, e.g.;
#   def example_add_two(inpt):
#       return inpt + 2 (== 1 LoC)
#  Refer to the function type-annotation hints and the test-case solutions at the bottom 
#  if you are stuck. Good luck! :)


# [Ch 1 Setup](/) Create a virtual environment (with `conda -n name python=_` or 
# `python_ -m venv name`) of a python3 version of your choice (we recommend >3.7).
# Enter your environment and install both the `matplotlib` and `numpy` packages. 
# Try to complete the following assignments in this environment.


# [Ch 2 Basic Op](1 LoC) Find the `power` operator and compute 2^10, first add 
# double the basis and then divide by half of the exponent. Make sure the result 
# is an int without using the `int()` cast or other module functions.
def basic_op()->int:
    return ((2**10) + 2+2)//5

# [Ch 2 Formatting](1 LoC) Format a string S of an integer, into the corresponding
# 8bit binary representation. Dont forget the 0 padding. (hint: see exercise 1)
def string_to_binary(S:str):
    pass # your code here

# [Ch 2 tuples/multiple assignments](2 LoC) Given some list L of 3 floats, return a tuple 
# (Triplet) with all items converted first to whole integers and then to strings. 
# Dont use list indexing.
def unpack_list(L:List[float])->Tuple[str,str,str]:
    pass # your code here

# [Ch 3 Slicing](1 LoC) Given a list L, return a new list containing the first two, and the last
# two items of L.
def slice_concat(L:List[int])->List[int]:
    pass # your code here

# [Ch 3 Slicing](1 LoC) Given a list L, return a Tuple lists. The first list contains only the
# values of L's even indices, the other only the values of uneven indices.
def slice_step(L:List[int])->Tuple[List[int], List[int]]:
    pass # your code here

# [Ch2 length/strings](1 LoC) Given two strings return the smaller one as list of characters.
def basic_strings(A:str, B:str)->List:
    pass # your code here

# [Ch 4 Error handling](4 LoC) Use the try-except construct to safely add items A and B,
# either of which could be an int or a string. Return `TypeError` for invalid combinations.
def error_handling(A:Union[str,int], B:Union[str,int]) -> Union[str,int]:
    pass # your code here

# [Ch 5 if/else] (1 LoC) Implement the "fizzbuzz" game: Given number N, return string "fizz" if 
# N is divisible by 3, "buzz" if N is divisible by 5, "fizzbuzz" if N divisible by 3 and 5, else 
# return "" (the empty string).
def fizzbuzz(N:int)->str:
    pass # your code here

# [Ch 5 while/not](3 LoC) Given some numbers N,M (N>M), decrement N until N=M. Dont use 
# the ">"or "<" operators. Return True when done.
def while_not(N:int, M:int)->bool:
    pass # your code here

# [Ch 7 List mutability](4 LoC) Given any list L, completely empty it, then
# add items A,B,C in order and D as the first element and return L (->[D,A,B,C])
def list_mutability(L:List, A:int, B:int, C:int, D:int) -> List[int]:
    pass # your code here

# [Ch 4 Error handling, Ch 7 List mutability](4 LoC) Given any list L that may(!) contain 
# the string "NaCo", remove that string, pop the first element and then delete the 
# last two items of L if you can.
def list_mutability_2(L:List)->List:
    pass # your code here

# [Ch 7 List comprehension](1 LoC) Use a list comprehension to create an array
# which items sum to input N. (hint: list comprehensions dont need a dynamic head...)
def list_comprehension(N:int)->List:
    pass # your code here

# [Ch 7 List comprehension](1 LoC) Create a nested 2 array of R rows, 
# each with C columns containing the row index as items, e.g., 
# [[0,0,0 ...], [1,1,1, ...], etc]
def nested_list_comprehension(R:int,C:int)->List:
    pass # your code here

# [Ch 7 Dictionary comprehension](1 LoC) Create a dictionary with N items, where 
# each key ist a string of the n-th index, and the value is the index^index, e.g.,
# {"0":0^0, "1":1^1, ... etc}
def dict_comprehension(N:int)->Dict:
    pass # your code here

# [Ch 7 Dictionary access](1 LoC) Given a dict{str:int} input, return all keys 
# concatenated as string. (hint: str.join() might work well here. Try using d.keys())
def dict_keys(input:Dict)->str:
    pass # your code here

# [Ch 7 Dictionary access](1 LoC) Given a dict{str:int} input, return a tuple of (min,sum,max) 
# of all values. (hint: try using d.values())
def dict_values(input:Dict)->Tuple[int,int,int]:
    pass # your code here

# [Ch 7 List enumeration](1 LoC) Given a list L, return the product of the first instance, where
# value * index > some parameter M. (hint: try using enumerate())
def enumerate_list(L:List[dict], M:int)->int:
    pass # your code here

# [Ch 7 Zipping](1 LoC) Given two iterables of the same size I,L, concatenate
# the item pair of each index together and return a new list, e.g., 
# [I[0]+L[0], I[1]+L[1]...]. Use your error_handling functions from above.
def concat_zip_lists(I:List[Union[str,int]], L:List[Union[str,int]])->List[Union[str,int]]:
    pass # your code here

# [Ch 7 Sets](1 LoC) Given a list L of strings, return L with all unique items.
def unique_filter(L:List[str])->List[str]:
    pass # your code here



# Below you can find the "unit-test"-like assertions of test cases that should hold,
# as well as their solutions. If you are stuck, print() your intermediate solution
# and compare to passing solution. No need to modify anything here.
if __name__ == "__main__":
    assert basic_op() == 205
    assert string_to_binary("100") == '01100100'
    assert unpack_list([0.6, 1.3, 2.6]) == ('0','1','2')
    assert slice_concat(list(range(10))) == [0, 1, 8, 9]
    assert slice_step(list(range(10))) == ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])
    assert basic_strings("mamma", "mia") == ['m','i','a']
    assert error_handling(4, "head") == TypeError
    assert error_handling(2, 2) == 4
    assert error_handling("ping", "pong") == "pingpong"
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(15) == "fizzbuzz"
    assert len(fizzbuzz(17)) == 0
    assert while_not(50,20)
    L = ["this", "is", 4, True, "MESS"]
    assert id(L) == id(list_mutability(L, 0, 1, 2, 3))
    L = ["this", "is", 4, True, "MESS"]
    assert list_mutability(L, 0, 1, 2, 3) == [3, 0, 1, 2]
    L = ["this", "is", 4, True, "MESS"]
    assert list_mutability_2(L) == ['is', 4]
    assert len(list_mutability_2(["NaCo"])) == 0
    assert sum(list_comprehension(10)) == 10
    assert len(nested_list_comprehension(7,9)) == 7
    assert len(nested_list_comprehension(7,9)[0]) == 9
    assert dict_comprehension(5)["4"] == 256
    assert dict_keys({"the":0,"meaning":1,"of":2,"life":3,"is":42}) == 'themeaningoflifeis'
    assert dict_values({"the":0,"meaning":1,"of":2,"life":3, "is":42}) == (0, 48, 42)
    assert enumerate_list(list(range(0,20,5)), 12) == 20
    assert concat_zip_lists([1, "str", "oops"],[2, "int", 3]) == [3, 'strint', TypeError]
    assert unique_filter(["a", "ab", "a", "c", "ab", "bc", "cd", "c", "b", "abc", "abc", "bcd", "abcd"]) == {'a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd'}
    
    # If all assertions about your implementation have passed, chances are good that you did complete the tasks
    # (or you have found good edge-cases that trick the assertions). Can you make your solutions more concise?
    print("Everything was correct. Well done! :)")