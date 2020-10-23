# Cara build in function / fungsi telah disediakan oleh python
str_input = input("Masukan kata: \n")
output = ""

reverse_input = str_input[::-1]
  
if str_input == reverse_input: 
  output = "Palindrome Sensitif"
elif str_input.lower() == reverse_input.lower():
  output = "Palindrome Tapi Ga Sensitif"
else:
  output = "Ga Palindrome"

print(output)
