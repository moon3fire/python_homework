import json
from class_.Break import Break
from class_.Domaingenerator import Domaingenerator
from class_.Duration import Duration
from collections import defaultdict

with open('data.json', 'r') as file:
    data = json.load(file)

times_dict = defaultdict(list)

for i in range(1, len(data)):
    for j in range(0, len(data[str(i)])):
        times_dict[str(i)].append(data[str(i)][j])

start_time = input()
end_time = input()
span_id = input()

duration = Duration(start_time, end_time, times_dict[str(span_id)])
times = duration.calculate_times()

list_of_breaks = []

for item in times:
    list_of_breaks.append(Break(start_time, end_time, item))

solution = Domaingenerator(start_time, end_time, list_of_breaks)
my_solution_list = solution.generate_domain()
for items in my_solution_list:
    print(items)
