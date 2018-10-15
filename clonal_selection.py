from immune import ClonalSelection



def objective_function(vector):
    sum = 0.0
    for x in vector:
        sum += (x**2.0)
    return sum


def decode(bitstring, search_space, bits_per_param):
    vector = []
    for i, bounds in enumerate(search_space):
        off, r_sum = i*bits_per_param, 0.0
        param = list(reversed(bitstring[off:off+bits_per_param]))
        for j in range(len(param)):
            r_sum += (float(param[j])*(2.0**float(j)))
        r_min, r_max = bounds
        vector.append(
            r_min + ((r_max-r_min)/((2.0**float(bits_per_param))-1.0)) * r_sum)
    return vector


def evaluate(pop, search_space, bits_per_param):
    for p in pop:
        p["vector"] = decode(p["bitstring"], search_space, bits_per_param)
        p["cost"] = objective_function(p["vector"])


def random_bitstring(num_bits):
    res = []
    for i in range(num_bits):
        res.append("0" if rand() < 0.5 else "1")
    return res


def point_mutation(bitstring, rate):
    child = []
    for i in range(len(bitstring)):
        bit = bitstring[i]
        child.append(("0" if bit == "1" else "1") if rand() < rate else bit)
    return child


def calculate_mutation_rate(antibody, mutate_factor=-2.5):
    return exp(mutate_factor * antibody["affinity"])


def num_clones(pop_size, clone_factor):
    return floor(pop_size * clone_factor)


def calculate_affinity(pop):
    pop.sort(key=lambda x: x["cost"])
    range = pop[-1]["cost"] - pop[0]["cost"]
    if range == 0.0:
        for p in pop:
            p["affinity"] = 1.0
    else:
        for p in pop:
            p["affinity"] = 1.0 - (p["cost"] / range)


def clone_and_hypermutate(pop, clone_factor):
    clones = []
    num_c = num_clones(len(pop), clone_factor)
    calculate_affinity(pop)
    for antibody in pop:
        m_rate = calculate_mutation_rate(antibody)
        for i in range(num_c):
            clone = {}
            clone["bitstring"] = point_mutation(antibody["bitstring"], m_rate)
            clones.append(clone)
    return clones


def random_insertion(search_space, pop, num_rand, bits_per_param):
    if num_rand == 0:
        return pop
    rands = [{"bitstring": random_bitstring(len(search_space) * bits_per_param)}
             for i in range(num_rand)]
    evaluate(rands, search_space, bits_per_param)
    return sorted((pop + rands), key=lambda x: x["cost"])[0:len(pop)]


def search(search_space, max_gens, pop_size, clone_factor, num_rand, bits_per_param=16):
    pop = [{"bitstring": random_bitstring(
        len(search_space) * bits_per_param)} for i in range(pop_size)]
    evaluate(pop, search_space, bits_per_param)
    best = min(pop, key=lambda x: x["cost"])
    for gen in range(max_gens):
        clones = clone_and_hypermutate(pop, clone_factor)
        evaluate(clones, search_space, bits_per_param)
        pop = sorted((pop + clones), key=lambda x: x["cost"])[0:pop_size]
        pop = random_insertion(search_space, pop, num_rand, bits_per_param)
        best = min((pop + [best]), key=lambda x: x["cost"])
        print(f" > gen {gen+1}, f={best['cost']}, s={best['vector']}")
    return best


if __name__ == '__main__':
    # problem configuration
    problem_size = 2
    search_space = [[-5, 5] for i in range(problem_size)]
    # algorithm configuration
    max_gens = 100
    pop_size = 100
    clone_factor = 0.1
    num_rand = 2
    # execute the algorithm
    best = search(search_space, max_gens, pop_size, clone_factor, num_rand)
    print(f"done! Solution: f={best['cost']}, s={best['vector']}")
