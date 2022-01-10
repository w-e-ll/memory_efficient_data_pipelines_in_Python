# memory_efficient_data_pipelines_in_Python
CSV reader - transformer - csv writer

Let’s think of a strategy:

    - Read every line of the file. -> O(1)
    - Split each line into a list of values. -> O(1)
    - Make List object from main generator object with all data -> O(n) time and space
    - Extract the column departments, leave only unique departments, make them as List. -> O(n) time and space
    - Filter lines by department -> Different departments can have multiple lines with sales values -> O(1)
    - Get total number of sales by department, sum every department sales O(1)
    - Use the departments and total number of sales combined together as one object. -> O(1)
    - Write this combined object to the output file -> O(n) time
    
    P.S.
    - I'm aren’t iterating through all these at once in the generator expression.
    - In fact, I'm aren’t iterating through anything until I actually use a for loop
        or a function that works on iterables, like sum(), list(). 
    - A zip object yielding tuples until an input is exhausted.
   
    The main place where I lose is in filter expression:
    - In my case: filter only works with list objects. 
    - If I use two generator objects (data_list, departments) it returns only one line instead of all filtered!
   
    ToDo:
    - Resolve how to filter with two nested generators.
   
    Big(O) time complexity: 
        data_list_obj + unique_departments + write_output = O(n+n+n) -> O(3n) -> dominant is "n" -> O(n)
    Big(O) space complexity: 
        data_list_obj + unique_departments = O(n+n) -> O(2n) -> dominant is "n" -> O(n)
