def fun(name,n):
    if(n>1): #base condition to exit
        print(name , n)
        fun(name,n-2)

fun("AK",10)