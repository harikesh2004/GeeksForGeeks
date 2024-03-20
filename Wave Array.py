
class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        # code here
        for i in range(0, n - 1, 2):
            if i > 0 and a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], arr[i]
            if i < n - 1 and a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        

