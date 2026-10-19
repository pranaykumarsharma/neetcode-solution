class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # Fixed size array ko simulate karne ke liye zeros se initialize karenge
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        # Index i ki value return karenge
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # Index i par value update karenge
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # Agar array bhar gaya hai, toh pehle resize karenge
        if self.size == self.capacity:
            self.resize()
            
        # Nayi value last mein add karein aur size badhayenge
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # Hum element ko actual delete nahi karenge (soft delete),
        # sirf size kam kar dete hain taaki agla pushback usko overwrite karenge.
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        # Capacity ko double karenge
        self.capacity *= 2
        new_arr = [0] * self.capacity
        
        # Purane elements ko naye array mein copy karenge
        for i in range(self.size):
            new_arr[i] = self.arr[i]
            
        # Reference update karenge
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity