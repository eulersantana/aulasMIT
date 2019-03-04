# Problema de otimização 
# MINIMIZAÇÃO OU MAXIMIZAÇÃO


# PROBLEMA CLASSICO APRESENTADO

# PROBLEMA DA MOCHILA

# Soulução é da um peso para cada elemento que irá compora MOCHILA


class Food(object):
	"""docstring for Food"""
	def __init__(self, n, v, w):
		self.name = n
		self.value = v
		self.calories = w

	def getValue(self):
		return self.value

	def getCost(self):
		return self.calories

	def density(self):
		return self.getValue() / self.getCost()

	def __str__(self):
		return self.name + '< ' + str(self.value) + ' , '+ str(self.calories) + '>' 


def buildMenu(names, values, calories):
	menu = []
	for i in range(len(values)):
		menu.append(Food(names[i], values[i], calories[i]))
	return menu		

def greedy(items, maxCost, keyFunction):

	itemsCopy = sorted(items, key=keyFunction, reverse=True)
	result = []
	totalValue, totalCost = 0.0, 0.0 

	for i in range(len(itemsCopy)):
		if (totalCost+itemsCopy[i].getCost()) <= maxCost:
			result.append(itemsCopy[i])
			totalCost += itemsCopy[i].getCost()
			totalValue += itemsCopy[i].getValue()

	return (result, totalValue)

def greedyRecursive(items, maxCost, totalCost, totalValue, result=[]):
	if len(items) <= 0:
		return (result, totalValue)

	if (totalCost+items[0].getCost()) <= maxCost:
		result.append(items[0])
		totalCost += items[0].getCost()
		totalValue += items[0].getValue()
		return greedyRecursive(items[1:], maxCost, totalCost, totalValue, result)

	return (result, totalValue)

def testGreedy(items, maxCost, keyFunction):
	taken , val = greedy(items, maxCost, keyFunction)
	print('Total value of items taken = ', val)
	for item in taken:
		print(' ', item)

def testGreedyRecursive(items, maxCost):
	result = []
	itemsCopy = sorted(items, key=lambda x: x.calories, reverse=True)
	taken , val = greedyRecursive(itemsCopy, maxCost, 0.0, 0.0, result)
	print('Total value of items taken = ', val)
	for item in taken:
		print(' ', item)


n = ["a", "b", "c", "d"]
p = [20, 20,30,30]
v = [20,30,20,40]

menu = buildMenu(n, p, v)

# print(greedyRecursive(itemsCopy, 50, 0.0, 0.0, result))
testGreedyRecursive(menu, 150)
testGreedy(menu, 150, lambda x: x.calories)
