'''
Implement a regular expression function isMatch that supports the '.' and
'*' symbols. The function receives two strings - text and pattern - and should
 return true if the text matches the pattern as a regular expression. For
  simplicity, assume that the actual symbols '.' and '*' do not appear in
  the text string and are used as special symbols only in the pattern string.
'''


"""
text = "a" pattern = "b*.*a"
return true

text = "a" pattern ="az"

a and a*b*

return true

ab a*b



"""

def _is_match(text,pattern,patIndex,textIndex):
  print(text[textIndex:],pattern[patIndex:])
  if textIndex>=len(text):
    if patIndex>=len(pattern):
      return True
    else:
      if patIndex+1<len(pattern) and pattern[patIndex+1]=='*':
        return _is_match(text,pattern,patIndex+2,textIndex)
      else:
        return False
  elif patIndex>=len(pattern) and textIndex<len(text):
    return False

  elif patIndex+1<len(pattern) and pattern[patIndex+1]=='*':
    if pattern[patIndex]=='.' or text[textIndex]== pattern[patIndex]:
      return (_is_match(text,pattern,patIndex+2,textIndex) or _is_match(text,pattern,patIndex,textIndex+1))
    else:
      return _is_match(text,pattern,patIndex+2,textIndex)

  elif pattern[patIndex]=='.' or pattern[patIndex]==text[textIndex]:
    return _is_match(text,pattern,patIndex+1,textIndex+1)

  else:
    return False


def is_match(text, pattern):
  return _is_match(text,pattern,0,0)
