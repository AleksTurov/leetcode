class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}  # Создаем пустой словарь для хранения чисел и их индексов
        
        for i, num in enumerate(nums):
            complement = target - num  # Вычисляем комплементарное значение
            
            if complement in num_to_index:
                return [num_to_index[complement], i]  # Если комплемент найден, возвращаем индексы
            
            num_to_index[num] = i  # Добавляем текущее число и его индекс в словарь
        
        return []  # Если решение не найдено, возвращаем пустой список (но по условию задачи всегда есть решение)

# Пример использования
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Ожидаемый вывод: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Ожидаемый вывод: [1, 2]
print(solution.twoSum([3, 3], 6))          # Ожидаемый вывод: [0, 1]
