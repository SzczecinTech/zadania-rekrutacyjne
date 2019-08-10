def is_palindrome(arg):
  string = str(arg)
  string.strip(' ')
  return reverse(string) == string


def reverse(string): 
    string = string[::-1] 
    return string 

print(is_palindrome('kajak'))
print(is_palindrome('kajak kajak'))
