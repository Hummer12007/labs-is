import random

POPULATION_SIZE = 100
  
geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = 'Random text for lab'
  
class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome 
        self.fitness = self.cal_fitness()
  
    @classmethod
    def mutated_genes(self):
        global geneset
        gene = random.choice(geneset)
        return gene
  
    @classmethod
    def create_gnome(self):
        global target
        gnome_len = len(target)
        return [self.mutated_genes() for _ in range(gnome_len)]
  
    def mate(self, par2):
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):    
            prob = random.random()
  
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())

        return Individual(child_chromosome)
  
    def cal_fitness(self):
        global target
        fitness = 0
        for gs, gt in zip(self.chromosome, target):
            if gs == gt: fitness+= 1
        return fitness
  
def main():
    global POPULATION_SIZE
  
    generation = 1
  
    found = False
    population = []
  
    for _ in range(POPULATION_SIZE):
                gnome = Individual.create_gnome()
                population.append(Individual(gnome))
  
    while not found:
        population = sorted(population, key = lambda x:x.fitness, reverse=True)

        if population[0].fitness >= len(target):
            found = True
            break
  
        new_generation = []

        s = int((10*POPULATION_SIZE)/100)
        new_generation.extend(population[:s])
  
        s = int((90*POPULATION_SIZE)/100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)
  
        population = new_generation
  
        print("Generation: {}\tString: {}\tFitness: {}".\
              format(generation,
              "".join(population[0].chromosome),
              population[0].fitness))
  
        generation += 1
  
      
    print("Generation: {}\tString: {}\tFitness: {}".\
          format(generation,
          "".join(population[0].chromosome),
          population[0].fitness))
  
if __name__ == '__main__':
    main()
