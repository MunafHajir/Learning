my_str='mam'

#my_str=my_str.toCasefold()

rev_str=reversed(my_str)

if list(my_str) == list(rev_str):
    print("Palindrome")

else:
    print("It is not palindrome")