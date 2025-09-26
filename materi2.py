print("====--INTEGER--====")
#INTEGER
data_int = 9
print("data_int =", data_int, "type =", type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) #akan True bila berupa bilangan dan akan False bila berupa 0

print("data_float =", data_float,"type : ", type(data_float))
print("data_str =", data_str,"type : ", type(data_str))
print("data_bool =", data_bool, "type : ", type(data_bool))

print("====--FLOAT--====")
#FLOAT
data_float = 9.5
print("data_float =", data_float, "type =", type(data_float))

data_int   = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float) #akan True bila berupa bilangan dan akan False bila berupa 0

print("data_int =", data_int,"type : ", type(data_int))
print("data_str =", data_str,"type : ", type(data_str))
print("data_bool =", data_bool, "type : ", type(data_bool))

print("====--STRING--====")
#STRING
data_str = "10"
print("data_str =", data_str, "type =", type(data_str))

data_int   = int(data_str)
data_float = float(data_str)
data_bool  = bool(data_str) #akan True bila berupa bilangan dan akan False bila berupa 0

print("data_int =", data_int,"type : ", type(data_int))
print("data_floart =", data_float,"type : ", type(data_float))
print("data_bool =", data_bool, "type : ", type(data_bool))

print("====--BOOLEAN--====")
#BOOLEAN
data_bool = False; #harus memakai titik koma 
print("data_bool =", data_bool, "type =", type(data_bool))

data_int    = int(data_bool)
data_float  = float(data_bool)
data_str    = bool(data_bool) #akan True bila berupa bilangan dan akan False bila berupa 0

print("data_int =", data_int,"type : ", type(data_int))
print("data_floart =", data_float,"type : ", type(data_float))
print("data_str =", data_str, "type : ", type(data_str))