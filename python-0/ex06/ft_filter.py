

def ft_filter(foo, param) -> list : 
	"""funcion que recibe como parametro una funcion y un iterable y aplica la funcion a cada miembre del iterable, y devuelve un nuevo iterable con todos los miembros que cumplieron el criterio de la funcion"""
	if foo == None :
		return [item for item in param if item]
	else:
		return [item for item in param if foo(item)]	
