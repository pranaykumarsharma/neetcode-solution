# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def insertionSort(self, pairs: list['Pair']) -> list[list['Pair']]:
        # Har step ka state store karne ke liye ek result array
        res = []
        
        for i in range(len(pairs)):
            j = i - 1
            
            # Jab tak previous element ki 'key' current element ki 'key' se badi hai
            # Tab tak hum unko swap karte jayenge
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                # Python mein directly dono ko swap karna aasaan hota hai
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
                
            # Har insertion ke baad (jab element apni sahi jagah par aa jaye), 
            # array ki ek copy banakar result mein add karenge.
            # pairs[:] use karne se current state ki exact copy ban jati hai.
            res.append(pairs[:])
            
        return res