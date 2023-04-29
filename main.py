import random

def getFitness(candidate, target):
   fitness = 0
   for i in range(0, len(candidate)):
       if target[i] == candidate[i]:
           fitness += 1
   return(fitness)

def mutate(candidate):
   geneIndex = random.randint(0, len(geneset) -1)
   index = random.randint(0, len(candidate) - 1)
   genes = list(candidate)
   genes[index] = geneset[geneIndex]
   return(''.join(genes))

def generateParent(length):
    genes = list("")
    for i in range(0,length):
        geneIndex = random.randint(0, len(geneset) -1)
        genes.append(geneset[geneIndex])
    return(''.join(genes))

def display(candidate):
    fitness = getFitness(candidate, target)
    print ("%i\t%s" % (fitness, candidate))


geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = 'Some random long text for lab genetic algorithm'

random.seed()
bestParent = generateParent(len(target))
bestFitness = getFitness(bestParent, target)
display(bestParent)

while bestFitness < len(bestParent):
   child = mutate(bestParent)
   childFitness = getFitness(child, target)

   if childFitness > bestFitness:
      bestFitness = childFitness
      bestParent = child
      display(bestParent)