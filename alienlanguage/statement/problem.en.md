# Alien Language
**Gaba Goo? Hunka!**

You are a translator that was sent out into deep space to study a new alien language. You have been entrusted with a small dictionary with some alien words that are known to you. The alien language uses a 2D structure to represent their language as some sort of cost-saving measure.

Each letter is a branch to another letter. When the branch ends, that is considered a word. Each word may be repeated more than once. Some words are considered special as they end with `.` or `+`. There is only one word that ends with `.` but there are multiple words that end with `+`.

There is one problem, your radio antenna has low bandwidth which means simply sending the word back to Earth will take too long. You will have to return a coded message using the index of your on board dictionary.

The coded message is prefixed with digit `0`. Any valid word index is appended to the coded message and must be sorted. Once all words have been appended, any valid word that ends with `+` should be added to the prefix and the valid word that ends with `.` should be appended to the end of the coded message.

## Input

## Output

## Sample Input 1

## Sample Output 1