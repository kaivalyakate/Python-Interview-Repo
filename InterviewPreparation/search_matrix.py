from typing import *


class Solution:
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        row = []
        low, high = 0, len(matrix)-1
        while low < high:
            mid = (low+high)/2
            if matrix[low][0] < target:
                high = mid
            elif matrix[low][0] > target:
                low = mid
            else:
                row = matrix[low]