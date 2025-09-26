#menaruh / assigment nilai
a = 10
b = 5
panjang= 1000

print("Nilai a = ", a)
print("Nilai x = ", b)
print("Nilai panjang = ", panjang)
print("------------------------------------")

#penamaan 
nilai_z =  40 #penamaan harus menggunakan underscore
juta1 = 10000
nilaiF = 15.5 

#pemanggilan kedua
print("Nilai nilai_z = ", nilai_z)
print("Nilai juta1 = ", juta1)
print("Nilai nilaiF = ", nilaiF)

G = 20
print("Nilai G = ", G)
print("-----------------------")
F = G
print("Nilai F = ", F)
print("-----------------------")

#tipe data

#data Integer
data_int = 10
print("data: ", data_int)
print("- bertipe: ", type(data_int))
print("-----------------------")

#data float
data_float = 1.8
print("data: ", data_float)
print("- bertipe: ", type(data_float))
print("-----------------------")

#data string : kumpulan karakter Harus pakai petik dua
data_str = "Hizkia"
print("data: ", data_str)
print("- bertipe: ", type(data_str))
print("-----------------------")

#data boolean : True or False
data_bool = False
print("data: ", data_bool)
print("- bertipe: ", type(data_bool))
print("-----------------------")

#tipe data khusus
data_comp = complex(9,6)
print("data :", data_comp)
print("- bertipe :", type(data_comp))
print("-----------------------")

#tipe data dari bahasa c

from ctypes import c_double, c_char

data_c_double = c_double(5.7)
print("data :", data_c_double)
print("- bertipe :", type(data_c_double))
