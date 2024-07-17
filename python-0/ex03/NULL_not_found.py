def NULL_not_found(object: any) ->int:
	if object == None:
		print(f"Nothing: None {type(object)}")
		return (0)
	elif type(object) == float:
		print(f"Cheese: nan {type(object)}")
		return(0)
	elif type(object) == int:
		print (f"Zero: 0 {type(object)}")
		return (0)
	elif type(object) == str and not object:
		print(f"Empty: {type(object)}")
		return(0)
	elif type(object) == bool:
		print(f"Fake: False {type(object)}")
	else:
		print("Type not Found")
		return(1)