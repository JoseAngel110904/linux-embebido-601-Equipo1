def suma(x: int, y:int) -> int:
    '''
    Esta función suma() dos enteros y regresa la suma de ambos
    
    entrada
    x: int
    y: int
    
    salida 
    x+y
    '''
    return x+y

def power_of(*args, **kwargs) -> int:
    x = args[0]
    power = kwargs.get('power',0)
    return x**power

if __name__== '__main__':
    xor_dict={
        (0,0):0,
        (0,1):1,
        (1,0):1,
        (1,1):0,
    }                           #Esto es un dict

my_set = {1,2,3,4}              #Esto es un set
my_tuple = (1,2,3,False,True)   #Esto es un tupla
my_list = ['hola', 1,False]     #Esto es una lista

var_input=(0,1)
print(f"el resultado de xor de {var_input} es {xor_dict[var_input]}")

x=3
y=7
print("el resultado de {} + {} es {}".format(x,y,suma(x,y)))

#result 1
result1 = power_of(x,1,2,4,8, power = y, k=6)
print(f"{x=} elevado a {y=} es {result1}")

var2 = {'power': 3}
var1 = (2,3,4)

#result 2
result2 = power_of(*var1, **var2)
print(f"{var1[0]} elevado a {var2} es {result2}")