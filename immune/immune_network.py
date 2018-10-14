from numpy.random import rand
from math import sqrt, log, exp


def objective_function(vector):
    res = 0.0
    for element in vector:
        res += element**2
    return res

def random_vector(minmax):
    return [minmax[i][0] + ((minmax[i][1] - minmax[i][0]) * rand()) for i in range(len(minmax))]

def random_gaussian(mean=0.0, stdev=1.0):
    u1 = u2 = w = 0
    while True:
        u1 = 2 * rand() - 1
        u2 = 2 * rand() - 1
        w = u1 * u1 + u2 * u2
        if w < 1:
            break
    w = sqrt((-2.0 * log(w)) / w)
    return mean + (u2 * w) * stdev

def clone(parent):
    v = [parent["vector"][i] for i in range(len(parent["vector"]))]
    return {"vector": v}

def mutation_rate(beta, normalized_cost):
    return (1.0/beta) * exp(-normalized_cost)

def mutate(beta, child, normalized_cost):
    for i, v in enumerate(child["vector"]):
        alpha = mutation_rate(beta, normalized_cost)
        child["vector"][i] = v + alpha * random_gaussian()

def clone_cell(beta, num_clones, parent):
    clones = [clone(parent) for i in range(num_clones)]
    [mutate(beta, c, parent["norm_cost"]) for c in clones]
    for i_clone in clones:
        i_clone["cost"] = objective_function(i_clone["vector"])
    clones.sort(key=lambda x: x["cost"])
    return clones[0]

def calculate_normalized_cost(pop):
    pop.sort(key=lambda x: x["cost"])
    range = pop[-1]["cost"] - pop[0]["cost"]
    if range == 0.0:
        for p in pop:
            p["norm_cost"] = 1.0
    else:
        for p in pop:
            p["norm_cost"] = 1.0 - (p["cost"] / range)

def average_cost(pop):
    sum = 0.0
    for x in pop:
        sum += x["cost"]
    return sum / float(len(pop))

def distance(c1, c2):
    sum = 0.0
    for i in range(len(c1)):
        sum += (c1[i] - c2[i])**2.0
    return sqrt(sum)

def get_neighborhood(cell, pop, aff_thresh):
    neighbors = []
    for p in pop:
        if distance(p["vector"], cell["vector"]) < aff_thresh:
            neighbors.append(p)
    return neighbors

def affinity_supress(population, aff_thresh):
    pop = []
    for cell in population:
        neighbors = get_neighborhood(cell, population, aff_thresh)
        neighbors.sort(key=lambda x: x["cost"])
        if (not len(neighbors)) or (cell == neighbors[0]):
            pop.append(cell)
    return pop

def search(search_space, max_gens, pop_size, num_clones, beta, num_rand, aff_thresh):
    pop = [{"vector": random_vector(search_space)} for i in range(pop_size)]
    for c in pop:
        c["cost"] = objective_function(c["vector"])
    best = None
    for gen in range(max_gens):
        for c in pop:
            c["cost"] = objective_function(c["vector"])
        calculate_normalized_cost(pop)
        pop.sort(key=lambda x: x["cost"])
        if best is None or pop[0]["cost"] < best["cost"]:
            best = pop[0]
        avgCost, progeny = average_cost(pop), None
        while True:
            progeny = [clone_cell(beta, num_clones, pop[i]) for i in range(len(pop))]
            if average_cost(progeny) < avgCost:
                break
        pop = affinity_supress(progeny, aff_thresh)
        [pop.append({"vector": random_vector(search_space)}) for i in range(num_rand)]
        print(f" > gen #{gen+1}, popSize=#{len(pop)}, fitness=#{best['cost']}")
    return best


if __name__ == '__main__':
    problem_size = 2
    search_space = [[-5, 5] for i in range(problem_size)]
    # algorithm configuration
    max_gens = 150
    pop_size = 20
    num_clones = 10
    beta = 100
    num_rand = 2
    aff_thresh = (search_space[0][1]-search_space[0][0])*0.05
    # execute the algorithm
    best = search(search_space, max_gens, pop_size, num_clones, beta, num_rand, aff_thresh)
    print(f"done! Solution: f=#{best['cost']}, s=#{best['vector']}")
