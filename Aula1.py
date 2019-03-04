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

def testGreedy(items, constraint, keyFunction):
	taken , val = greedy(items, constraint, keyFunction)
	print('Total value of items taken = ', val)
	for item in taken:
		print(' ', item)


n = ["a", "b", "c", "d"]
p = [20, 20,30,30]
v = [20,30,20,40]

menu = buildMenu(n, p, v)
testGreedy(menu, 50, lambda x: x.calories)