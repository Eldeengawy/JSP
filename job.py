import numpy
import job_sch
import random

popSize = 4
numPrentMating = 2

new_pop = numpy.zeros((4, 4))
firstRandomList = []
secondRandomList = []
thirdRandomList = []
fourthRandomList = []

for i in range(0, 4):
    n = random.randint(0, 1)
    firstRandomList.append(n)
for i in range(0, 4):
    n = random.randint(0, 1)
    secondRandomList.append(n)
for i in range(0, 4):
    n = random.randint(0, 1)
    thirdRandomList.append(n)
for i in range(0, 4):
    n = random.randint(0, 1)
    fourthRandomList.append(n)

new_pop[0, :] = firstRandomList
new_pop[1, :] = secondRandomList
new_pop[2, :] = thirdRandomList
new_pop[3, :] = fourthRandomList


for iteration in range(6):

    quantiles = job_sch.cal_pop_fitness(new_pop)
    print(quantiles)
    parents = job_sch.select_mating_pool(new_pop, quantiles, numPrentMating)
    new_pop = job_sch.crossover(parents, n_individuals=popSize)
    new_pop = job_sch.mutation(new_pop)
    print(new_pop)
