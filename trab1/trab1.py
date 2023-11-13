import time
import random

def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Função para gerar uma base de dados de teste com números aleatórios
def generate_test_data(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

# Função para gerar um valor alvo aleatório
def generate_random_target(nums):
    return random.randint(sum(nums) // 2, sum(nums) + max(nums))


def subset_sum_bruteforce(nums, target):
    def generate_subsets(nums):
        subsets = []
        for i in range(2 ** len(nums)):
            subset = [nums[j] for j in range(len(nums)) if (i >> j) & 1]
            subsets.append(subset)
        return subsets

    for subset in generate_subsets(nums):
        if sum(subset) == target:
            return subset
    return None

def subset_sum_backtracking(nums, target):
    def backtrack(subset, index, current_sum):
        if current_sum == target:
            return subset
        if current_sum > target or index >= len(nums):
            return None
        without_current = backtrack(subset, index + 1, current_sum)
        with_current = backtrack(subset + [nums[index]], index + 1, current_sum + nums[index])
        return with_current if with_current else without_current

    return backtrack([], 0, 0)

# Tamanho da base de dados de teste maior
test_data_size = 20

# Gerar uma base de dados de teste com números aleatórios entre 1 e 20
test_data = generate_test_data(test_data_size, 1, 20)

# Gerar um valor alvo aleatório com base na soma dos números
target = generate_random_target(test_data)

result_bruteforce, execution_time_bruteforce = measure_execution_time(subset_sum_bruteforce, test_data, target)
result_backtracking, execution_time_backtracking = measure_execution_time(subset_sum_backtracking, test_data, target)

print("Base de Dados de Teste:", test_data)
print("Valor Alvo:", target)
print("Força Bruta:", result_bruteforce)
print("Tempo de Execução (Força Bruta):", execution_time_bruteforce, "segundos")
print("Backtracking:", result_backtracking)
print("Tempo de Execução (Backtracking):", execution_time_backtracking, "segundos")