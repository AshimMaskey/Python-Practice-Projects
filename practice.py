travel_log=[
	{
		"counter":"france",
		"visits":10,
		"cities":["parries", "etc"]
	}
]

def add_into(counter, visits, cities):
	obj={
		"counter":counter,
		"visits":visits,
		"cities":cities
	}
	travel_log.append(obj)



add_into("nepal", 10, ["eh", "bla", "bla"])
print(travel_log)