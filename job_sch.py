import numpy


def fitness_fun(indiv_chrom):
    out = numpy.array_str(indiv_chrom)
    string = ""
    for i in out:
        if i == '0' or i == '1':
            string += str(i)
    integer = int(string)

    i = res = 0
    while integer != 0:
        res = res+(integer % 10)*(2**i)
        integer = integer//10
        i += 1

    return res


def cal_pop_fitness(pop):
    qualities = numpy.zeros(pop.shape[0])
    for indv_num in range(pop.shape[0]):
        qualities[indv_num] = fitness_fun(pop[indv_num, :])
    return qualities


def select_mating_pool(pop, qualities, num_parents):
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_qual_idx = numpy.where(qualities == numpy.max(qualities))
        max_qual_idx = max_qual_idx[0][0]
        parents[parent_num, :] = pop[max_qual_idx, :]
        qualities[max_qual_idx] = -1
    return parents


def crossover(parents, n_individuals=4):
    new_pop = numpy.zeros((4, 4))
    new_pop[0:parents.shape[0], :] = parents
    new_pop[2, 0:2] = parents[0, 0:2]
    new_pop[2, 2:] = parents[1, 2:]
    new_pop[3, 0:2] = parents[1, 0:2]
    new_pop[3, 2:] = parents[0, 2:]
    # new_pop[4,0:2] = parents[0,0:2]
    # new_pop[4,2:4] = parents[1,2:4]
    # new_pop[4,4:] = parents[1,4:]
    # # new_pop[5,0:3] = parents[2,0:3]
    # # new_pop[5,3:] = parents[0,3:]
    return new_pop


def mutation(population):
    for idx in range(population.shape[0]):
        population[idx, 1] = population[idx, 3]
        population[idx, 3] = population[idx, 1]
    return population
