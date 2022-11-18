user_phrase = input()

split_phrase = user_phrase.replace(' ', '')

if split_phrase == split_phrase[::-1]:
    
    print(f'{user_phrase} is a palindrome')
    
else:
    
    print(f'{user_phrase} is not a palindrome')
