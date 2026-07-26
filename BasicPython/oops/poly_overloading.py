class example:

    def method(self,a ,b=None):
        if b is None:
            print(f"single argument :{a}")
        elif isinstance(a,int) and isinstance(b,int):
            print(f"two are int {a},{b}")
        elif isinstance(a,str) and isinstance(b,str):
            print(f"two are string {a}, {b}")
        else:
            print("mixed")

obj = example()
obj.method(1)
obj.method(1,2)
obj.method("hello","world")
obj.method(1,"hello")

