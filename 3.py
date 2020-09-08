def isPalindrom(number):
  return number == int(str(number)[::-1]);

def largestPalindrom (digit):
  maxByDigit = 10 ** digit - 1;
  for i in range(maxByDigit, 0, -1):
    for j in range(i, 0, -1):
      if isPalindrom(i * j):
        return i * j;
  
# test cases
print(largestPalindrom(1));
print(largestPalindrom(2));
print(largestPalindrom(3));
