# Daftar operator
OPERATORS = set(['+', '-', '*', '/', '(', ')', '^']) 

# Daftar Prioritas
PRIORITAS = {'+':1, '-':1, '*':2, '/':2, '^':3}

#Fungsi pengubah notasi infix menjadi notasi postfix
def infix_to_postfix(notasi_infix): 
    # Membuat stack kosong
    stack = [] 

    # Variable untuk hasil ( notasi postfix )
    output = '' 


    for ch in notasi_infix:

	# Jika merupakan operand maka langsung letakkan di daftar postfix
        if ch not in OPERATORS:  

            output+= ch

	# Jika operator akan diletakkan di stack

        elif ch=='(':  

            stack.append('(')

        elif ch==')':

            while stack and stack[-1]!= '(':

                output+=stack.pop()

            stack.pop()

        else:

	    # Jika prioritas yang masuk lebih kecil dari prioritas yang ada distack

            # Keluarkan semua data dari stack dan masukan sebagai output

            while stack and stack[-1]!='(' and PRIORITAS[ch]<=PRIORITAS[stack[-1]]:

                output+=stack.pop()

            stack.append(ch)

    # Ketika sudah habis yang di scan, keluarkan semua data dari stack ke output
    while stack:

        output+=stack.pop()

    return output

 

notasi_infix = input('Masukan notasi infix')
print('Notasi Postfix: ',infix_to_postfix(notasi_infix))
