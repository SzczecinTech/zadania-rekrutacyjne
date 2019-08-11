import re
def is_palindrome(arg):
  string = str(arg)
  re.compile('([^\w])')
  string = re.sub('([^\w])', '', string).lower()
  return reverse(string) == string


def reverse(string): 
    string = string[::-1] 
    return string 

print(is_palindrome('kajak'))
print(is_palindrome('Kajak, kajak'))
