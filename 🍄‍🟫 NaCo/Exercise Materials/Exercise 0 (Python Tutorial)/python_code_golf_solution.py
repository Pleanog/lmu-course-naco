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
    return ((2**10) + 2*2) // 5
# Explanation:
# Take care with the brakets (else division of 4 would take precedence),
# then utilize integer division "//" last for an integer result. (The normal
# division operator "/" does not round to int by default.)


# [Ch 2 Formatting](1 LoC) Format a string S of an integer, into the corresponding
# 8bit binary representation. Dont forget the 0 padding. (hint: see exercise 1)
def string_to_binary(S:str):
    return f"{int(S):08b}"
# Explanation:
# You could also use the "str".format() functionality, i.e., "{0:08b}".format(int(S)), 
# where the first 0 in "{0:08b}" is the 0th element to format in and so on. 
# The second part ":08b" (in order) means:
#     - pad with 0s to the left
#     - format to 8 digits
#     - convert to binary (b)


# [Ch 2 tuples/multiple assignments](2 LoC) Given some list L of 3 floats, return a tuple 
# (triplet) with all items converted first to whole integers and then to strings. 
# Dont use list indexing.
def unpack_list(L:List[float])->Tuple[str,str,str]:
    a,b,c = L
    return str(int(a)), str(int(b)), str(int(c))
# Explanation:
# You can use tuple (un)packing to shorten the assignment of every element in a colllection
# to a separate variable. In this example we unpack a list with three elements directly into
# the named variables a,b,c. While this is named "tuple packing", what is meant is that you can 
# unpack from any collection into tuples of variables (on the left of the assignment).
# E.g., something like this would also work (unpacking a string into character variables):
#   a, b, c = "def"
#   print(a,b,c)
#   > ('d', 'e', 'f')
# Note that this only works if you know in advance the number of elements to unpack, otherwise 
# you will get a ValueError ("too many items to unpack, expected <your number of variables 
# on the left of the assignment>, but got <missmatching number of elements in the collection>").
# Shortens code like:
#   a = L[0]
#   b = L[1]
#   c = L[2]
#   a = str(int(a))
#   b = str(int(b))
#   c = str(int(c))
#   return a, b, c


# [Ch 3 Slicing](1 LoC) Given a list L, return a new list containing the first two, and the last
# two items of L.
def slice_concat(L:List[int])->List[int]:
    return L[:2] + L[-2:]
# Explanation:
# Here we make use of two nice indexing features; Slicing and negative index access.
# - Slicing: Remember that slicing of any ordered collection (lists, strings, etc.) follows the form
#       list[start:int (inclusive), stop:int (exclusive), step:int]. If we do not specify start/stop/step,
#       then we indicate the whole array "so far", or "to the end".
#       => list[:2] everything from the start (not specified) to element-index 2 (stop, exclusive), i.e. [0,1]
#       => list[-2:] everything from the second to last element onwards to the end of the list (start, inclusive),
#       i.e., [-2, -1]
# - Negative index: Python can access the ith element from the back of the list with list[-i]. I.e., 
#       list[-1] is the last element of the list, list[-2] is the second to last and so on.
# Concatenation of lists is simply defined as "adding" both lists together.


# [Ch 3 Slicing](1 LoC) Given a list L, return a Tuple lists. The first list contains only the
# values of L's even indices, the other only the values of uneven indices.
def slice_step(L:List[int])->Tuple[List[int], List[int]]:
    return L[0::2], L[1::2]
# Explanation:
# Here we make use of the slicing step option and the insight that every other index will select either the
# even or odds elements, depending on where you start. Starting from 0, every second element is even (0,2,4...),
# while every second element from 1 onwards (1,3,5...) is odd.


# [Ch2 length/strings](1 LoC) Given two strings return the smaller one as list of characters.
def basic_strings(A:str, B:str)->List:
    return list(A) if len(A) < len(B) else list(B)
# Explanation:
# Many python constructs can be inlined without breaking the syntax rules. Sometimes this makes code more compact
# and easier to read (especially since python syntax is very close to spoken english), other times its just confusing.
# Use with decretion, just like in other languages. (E.g., Ternary operators in Java/Javascript work similarly.)
# The basic form is:
#   if len(A) < len(B):
#       return list(A)
#   else:
#       return list(B)


# [Ch 4 Error handling](4 LoC) Use the try-except construct to safely add items A and B,
# either of which could be an int or a string. Return `TypeError` for invalid combinations.
def error_handling(A:Union[str,int], B:Union[str,int]) -> Union[str,int]:
    try:
        return A + B
    except TypeError:
        return TypeError
# Explanation:
# The try/except is one of the few python constructs that is not inlineable. Its also possible to
# directly return from either of the blocks, like we do here. Note that A+B gets computed before(!)
# the return, meaning if there is a TypeError occuring in the addition then we fall trough to the except
# block even if this computation stands in the same line as the return statement. From there we can simply
# return the class "TypeError".


# [Ch 5 if/else] (1 LoC) Implement the "fizzbuzz" game: Given number N, return string "fizz" if 
# N is divisible by 3, "buzz" if N is divisible by 5, "fizzbuzz" if N divisible by 3 and 5, else 
# return "" (the empty string).
def fizzbuzz(N:int)->str:
    return "fizzbuzz" if (N % 3 == 0) and (N % 5 == 0) else "buzz" if N % 5 == 0 else "fizz" if N % 3 == 0 else ""
# Explanation:
# Another example of the inlinability of if/else statements, as well as the modulo operator. Note that we cant inline
# "elif" cases, but if/else scoping does work. Except for code-golfing, the simple version is more readable:
#   if N % 3 == 0 and N % 5 == 0:
#       return "fizzbuzz"
#   elif N % 5 == 0:
#       return "buzz"
#   elif N % 3 == 0:
#       return "fizz"
#   else:
#       return ""


# [Ch 5 while/not](3 LoC) Given some numbers N,M (N>M), decrement N until N=M. Dont use 
# the ">"or "<" operators. Return True when done.
def while_not(N:int, M:int)->bool:
    while N is not M:
        N -= 1
    return True
# Explanation:
# "While" loops are fairly simple in Python, a keyword and a condition. 
# Although "for" loops are mostly used, while loops are needed in some cases 
# where neither the length nor the termination condition can be easily 
# defined before the loop itself. In this case we run the loop
# until the condition N != M is hit. "is not" is great syntactic sugar for testing 
# specific equality that excludes every other possibility (except N is M). In most cases
# you can use "==" and "is" interchangeably, check the slides for the exception.
# Also interesting, you can decrement the N value from the parameter, even though it is
# not explicitly defined otherwise. This is because the function parameter values are in
# scope of the function body (and modifiable) as soon (and as long) as the function gets
# executed.  

# [Ch 7 List mutability](4 LoC) Given any list L, completely empty it, then
# add items A,B,C in order and D as the first element and return L (->[D,A,B,C])
def list_mutability(L:List, A:int, B:int, C:int, D:int) -> List[int]:
    L.clear()
    L.extend([A,B,C])
    L.insert(0,D)
    return L
# Explanation:
# Important to know is that list functions do not reassign the list in memory, but a new
# assignment, e.g., L = [] would. Especially for lists that grow large every iteration, reassignment
# and growing is one of the classic bottlenecks that make python run slower than it could.
# The list comprehension simply shortens a "for" loop, that would otherwise look like:
#   for item in [A,B,C]:
#        L.append(item)
# with a "throwaway" list construction. (We can do anything in the head of the comprehension, even 
# modifying other lists.)


# [Ch 4 Error handling, Ch 7 List mutability](4 LoC) Given any list L that may(!) contain 
# the string "NaCo", remove that string, pop the first element and then delete the 
# last two items of L if you can.
def list_mutability_2(L:List)->List:
    L.remove("NaCo") if "NaCo" in L else None
    L.pop(0) if L else None
    del L[-2:]
    return L
# Explanation:
# Inline "if condition else None" error handling is also commonly used in python, but a clean try/except
# would also work (and explicitly defining the error to catch is more readable in most cases):
#   try:
#       L.remove("NaCo")
#   except ValueError:
#       pass
# Similarly, after testing if L is truthy (i.e., only empty lists are falsey) with "if L" (== True) we can
# savely pop element at index 0. Short for:
#   try:
#       L.pop(0)
#   except IndexError:
#       pass


# [Ch 7 List comprehension](1 LoC) Use a list comprehension to create an array
# which items sum to input N. (hint: list comprehensions dont need a dynamic head...)
def list_comprehension(N:int)->List:
    return [1 for _ in range(N)]
# Explanation:
# Again, we do not have to do anything list-related in the head of the list-comprehension,
# simply putting a static value into the list for each iteration of the range lets us quickly
# reserve filled lists of constant values. The sum() of size N [1,1,1 ...] lists fulfills the assert.  


# [Ch 7 List comprehension](1 LoC) Create a nested 2d array of R rows, 
# each with C columns containing the row index as items, e.g., 
# [[0,0,0 ...], [1,1,1, ...], etc]
def nested_list_comprehension(R:int,C:int)->List:
    return [[j for _ in range(C)] for j in range(R)]
# Explanation:
# Since we can do anything in the head of the comprehension, including another list
# as elements in the outer list is very simple. To initialize values directly inplace,
# we utilize the index-iterator variable "j" (we could name this anything) to 
# fulfill the requirement. I am "throwing away" the row-iterator here with a wildcard,
# simply because we dont need it (preference). Short for:
#   outer_list = []
#   for row_idx in range(R):
#       inner_list = []
#       for col_idx in range(C):
#           inner_list.append(row_idx)
#       outer_list.append(inner_list)


# [Ch 7 Dictionary comprehension](1 LoC) Create a dictionary with N items, where 
# each key is a string of the n-th index, and the value is the index^index, e.g.,
# {"0":0^0, "1":1^1, ... etc}
def dict_comprehension(N:int)->Dict:
    return {str(idx):idx**idx for idx in range(N)}
# Explanation:
# Dictionary comprehensions work analogously to list comprehensions, but instead of inserting
# just one element into square brackets [elem_to_add for x in y] we add key:value pairs
# in curly brackets {key:value for x in y}. In this case we use the idx-iterator variable
# in both the key and the value, but this is not a requirement. Short for:
#   dictionary = {}
#   for item_idx in range(N):
#       dictionary[str(item_idx)] = item_idx**item_idx


# [Ch 7 Dictionary access](1 LoC) Given a dict{str:int} input, return all keys 
# concatenated as string. (hint: str.join() might work well here. Try using d.keys())
def dict_keys(input:Dict)->str:
    return "".join(key for key in input.keys())
# Explanation:
# Using iterators is Pythons preferred method of dealing with collections of unknown
# length. If we knew that the input dict had only x items (and their names), then you could
# manually add the strings "item1" + "item2" but this does not work for arbitrary length
# problems with unknown names. In this case we use the join function. It joins together 
# everything given as parameters (here, all elements (keys) returned by the .keys() generator)
# with the initial string in between. So "_".join(["a", "b", "c"]) would yield "a_b_c",
# "OhNo!".join(["a", "b", "c"]) = "aOhNo!bOhNo!c" etc. Since we want to directly concatenate the
# keys, we don't intersperce anything and simply join with empty strings (nothing) in between.
# The dict.keys() method returns all keys in a iterables generator, so {"a":1, "b":2, "c":3}.keys() 
# would return a dict_keys(['a', 'b', 'c']) object. To unpack from their generator status, you could
# wrap/cast the object as list, i.e. list({"a":1, "b":2, "c":3}.keys()) = ['a', 'b', 'c']. When
# functions take generators as input too, casting to list is generally not neccessary, Python
# knows what to do.  


# [Ch 7 Dictionary access](1 LoC) Given a dict{str:int} input, return a tuple of (min,sum,max) 
# of all values. (hint: try using d.values())
def dict_values(input:Dict)->Tuple[int,int,int]:
    return min(input.values()), sum(input.values()), max(input.values())
# Explanation:
# Similary, dict.values() returns a generator with all values, i.e., {"a":1, "b":2, "c":3}.values()
# = dict_values([1, 2, 3]). The built-in functions min(iterable),max(iterable) and sum(iterable) 
# also work directly with such generated objects, allowing for this clean one-liner.


# [Ch 7 List enumeration](1 LoC) Given a list L, return the product of the first instance, where
# value * index > some parameter M. (hint: try using enumerate())
def enumerate_list(L:List[Dict], M:int)->int:
    return [i*val for i,val in enumerate(L) if i*val > M][0]
# Explanation:
# The built-in enumerate(iterable) function is Pythons syntactic sugar to make the upkeep of
# some external index counting value redundant. So instead of:
#   idx = 0
#   for item in [object, object, object]:
#       object[idx] = ...
#       idx += 1
# we can simply enumerate any iterable and get the index value as well. Note that the unpack
# syntax in the for loop changes depending on the elements contained (!) in the
# construct you are trying to enumerate:
# - Lists (just values one by one, e.g., our_list=[val, val2, val3]):
#   for idx,val in enumerate(our_list):
#       print(idx,val)
#   > 0, val
#   > 1, val2 etc. 
# - Dicts (key, value tuples, e.g., our_dict=[k:v, k2:v2, k3:v3]):
#    for idx,(key,val) in enumerate(our_dict):
#       print(idx,key,val)
#   > 0, k, v
#   > 1, k2, v2 etc.
# - Tuples of other sizes (e.g. our_tuple_list=[(a,b,c), (d,e,f), ...])
#   for idx,(first,second,third) in enumerate(our_tuple_list):
#       print(idx, first, second, third)
#   > 0, a, b, c    etc.
# We then test with an inline "if" as comprehension condition if the current head expression
# should be added (here only if i*val > M) and add the expression i*val if the condition
# evaluates to true (or is truthy). The "first instance" simply means the first expression
# that has passed the condition filter and got added to the list, i.e., element at index 0.


# [Ch 7 Zipping](1 LoC) Given two iterables of the same size I,L, concatenate
# the item pair of each index together and return a new list, e.g., 
# [I[0]+L[0], I[1]+L[1]...]. Use your error_handling functions from above.
def concat_zip_lists(I:List[Union[str,int]], L:List[Union[str,int]])->List[Union[str,int]]:
    return [error_handling(i,l) for i,l in zip(I,L)]
# Explanation:
# Zipping lists together into tuples may also be considered syntactic sugar, but is very
# helpful for both organizing, naming and scoping the access of different collections all
# at once. Note that you can technically zip lists of different lengths, but only fully
# matching sets get returned from the zip iterator. E.g., 
# zip([1], [1,2,3]) = <zip at 0x110092980> (the generator location)
# list(zip([1], [1,2,3])) = [(1, 1)] (all matched pairs of the casted generator)
# Here we zip two single valued lists, but as long as the correct unpack syntax is
# used you can zip and unpack anything, e.g., you could zip three tuples at once:
#   for first,second,third in zip(("a","b"), ("c","d"), ("e","f")):
#       print(first, second, third)
#   > a c e
#   > b d f


# [Ch 7 Sets](1 LoC) Given a list L of strings, return L with all unique items.
def unique_filter(L:List[str])->List[str]:
    return set(L)
# Explanation:
# Finally, sets and the set() cast work on most hashable collections and will
# represent a collection containing only unique items. This is straightforward
# with single valued lists, like here, but in some cases maybe not completely
# intuitive, e.g, set({"a":1, "b":2, "c":3, "a":4}) returns the set of unique
# keys {'a', 'b', 'c'}, and not unique values or even unique key:value pairs.
# In those cases, the documentation or a quick peek at stackoverflow should help 
# if you are stuck. :)


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