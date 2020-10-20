input_text = input("Masukan data yang ingin dicetak: \n")
var_cetak = input("Masuk jumlah cetak: \n")

print("========================= Loop way")
for i in range(int(var_cetak)):
    print("%s" %input_text)

print("========================= Recursive way")
def cetak(text,n):
    if n == 1:
        return (text)
    else:
        return text + " " + cetak(text, n-1)

print("%s" %cetak(input_text, int(var_cetak)))

# Persamaan
# 1. Output sama
# 2. Proses sama
# 3. Sama sama crash jika tidak diberikan batasan yang benar

# Perbedaan
# 1. Logic
# 2. Batasan dan kondisi harus didefinisikan pada recursive, 
#    sedangkan perulangan bisa dibuat otomatis
