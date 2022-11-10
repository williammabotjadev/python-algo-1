# Singleton Design Pattern

class SinEx:
   
    _sing = None 

    def __new__(self, *args, **kwargs):
        if not self._sing:
            self._sing = super(SinEx, self).__new__(self, *args, **kwargs)
            return self._sing 

sinEx = SinEx()

print(sinEx)

sinExNew = sinEx

print(sinExNew)
