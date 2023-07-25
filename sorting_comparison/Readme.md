## code challnge 28:sortByYearDescending(movies): 
sortAlphabeticallyIgnoringArticles:
Approach:

The sortAlphabeticallyIgnoringArticles method sorts the list of Movie objects alphabetically based on their title attribute while ignoring leading articles like "A," "An," and "The."
It uses the sorted function with a custom key parameter, where a nested lambda function (remove_leading_articles) is used to remove leading articles from the movie titles.


##  Time Complexity: O(n log n) Space Complexity: O(n)

## sort_Alphabetically_Ignoring_Articles(movies):
sortAlphabeticallyIgnoringArticles:
Approach:

The sortAlphabeticallyIgnoringArticles method sorts the list of Movie objects alphabetically based on their title attribute while ignoring leading articles like "A," "An," and "The."
It uses the sorted function with a custom key parameter, where a nested lambda function (remove_leading_articles) is used to remove leading articles from the movie titles.
## Time Complexity: O(n log n) Space Complexity: O(n)
### solution:
[link to my code ](./sorting.py)
[link to my test ](./test/test_sorting.py)
