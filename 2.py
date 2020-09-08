
def breakStringIntoList (str_word, arr_words):
  result = [];

  totalStrWord = len(str_word);
  tmp_letter_combination = []
  for w in range(totalStrWord):
    for x in range(w,totalStrWord):
      tmp_word = '';
      for y in range(w, x+1):
        tmp_word += str_word[y];

      tmp_letter_combination.append(tmp_word);
      
  for word in arr_words:
    for letter_combination in tmp_letter_combination:
      if word == letter_combination:
        result.append(word);
    
  if len(result) <= 1:
    return "<no way>";
  else:
    return ', '.join(result);
    
# test cases
example_list = ['pro', 'gram', 'merit','program', 'it', 'programmer'];
print(breakStringIntoList("program", example_list));
print(breakStringIntoList("programit", example_list));
print(breakStringIntoList("programmerit", example_list));
print(breakStringIntoList("programlala", example_list));
print(breakStringIntoList("proletarian", example_list));
