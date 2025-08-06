def outer():
    print("Outer function started")

    def inner():
        print("Inner Functon")


    return inner
    #return "Rahul"
    #return 100

inner=outer()
print(type(inner))  #<clss,function>
inner()
inner()
inner()