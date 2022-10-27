population = [int(num) for num in input().split(", ")]
min_wealth = int(input())
countries_count = len(population)
if sum(population) < countries_count * min_wealth:
    print("No equal distribution possible")
else:
    while min(population) < min_wealth:
        for index, country in enumerate(population):
            if country < min_wealth:
                difference = min_wealth - country
                population[index] += difference
                max_population_index = population.index(max(population))
                population[max_population_index] -= difference
    print(population)