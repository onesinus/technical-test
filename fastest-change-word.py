def getTotalDiffLetter(word, second_word):
  arrDiffLetter = [];
  arr_words = zip(word, second_word);
  for i,j in arr_words:
    if i != j:
      arrDiffLetter.append('*');

  return len(arrDiffLetter);

def fastestChangeWord (arr_two_words):
  first_word  = arr_two_words[0];
  second_word = arr_two_words[1];

  arr_words = ["hot", "dot", "dog", "lot", "log"];
  result = [first_word];
  

  for word in arr_words:
    if word not in result :
      result.append(word);
  
    totalDifferentLetter = getTotalDiffLetter(word, second_word);
    if totalDifferentLetter <= 1:
      result.append(second_word);
      return ' '.join(result);
  
  return "<no way>";

# test cases
print(fastestChangeWord(["hot", "dog"]));
print(fastestChangeWord(["hit", "dog"]));
print(fastestChangeWord(["hit", "dig"]));
print(fastestChangeWord(["dot", "red"]));
