import ctypes

class MyClass:
    
    def __init__(self):
        
        self.n = 0
        self.size = 1
        self.A = self._make_array(self.size)
        
    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()
    
    def __len__(self):
        return self.n
        
    def append(self, item):
        
        if self.n == self.size:
            
            self._resize(2 * self.size)
            
        self.A[self.n] = item
        self.n += 1
        
    def _resize(self, new_cap):
        B=self._make_array(new_cap)
        self.size = new_cap
        for i in range(self.n):
            B[i]=self.A[i]
        self.A=B
        
        
### After Shift+Enter, write these commands:- 1) arr = MyClass()   2) arr.append(1), then press Shift+Enter    3) len(arr), and last again press Shift+Enter respectively.....
### Thank you for your efforts.....
