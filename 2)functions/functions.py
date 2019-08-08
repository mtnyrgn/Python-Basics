#Built in functions
float1=10.6
round(float1)
int(float1)
type(int(float1))
#user defined fuctions
var1=10
var2=20

output=float((var1*var2)/(var1-var2)*2/3)

def output_result(var1,var2):
    """Function declaration"""
    return float((var1*var2)/(var1-var2)*2/3)

output_function=output_result(10,20)
print(output_function)

#DEFAULT AND FLEXİBLE FUNCTİONS
def calculate_area(r,pi=3.14):
#Default parametrele(pi) en sağdaki parametre olarak yazılmalıdır.
      return 2*pi*r
area=calculate_area(2)

def calculate(height,weight,*args):
    print(len(args))
    return (height+weight)*args[0]

#def calculate(height,weight,age):
#    return int(weight*height/age)
#    
def print_info(name,surname,age,number=10):
    print("Name:",name,"Surname:",surname,"Age:",age,"Number:",number)
    string_mul=name*2
    print(string_mul)
#Stringler bir sayıyla çarpılınca çarpıldığı sayı kadar tekrar yazılır.
print_info("metin","yorgun",21)