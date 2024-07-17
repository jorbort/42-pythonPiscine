
def give_bmi(height: list[int | float], weigth : list[int | float]) -> list[int | float]:
	ret = []
	if len(height) != len(weigth):
		raise AssertionError("AssertionError: invalid list size")
	for altura , peso in zip(height,weigth):
		ret.append(peso / (altura ** 2))
	return ret

def apply_limit(bmi: list[int|float], limit: int) -> list[bool]:
	ret = []
	for item in bmi:
		if item < limit:
			ret.append(False)
		else:
			ret.append(True)
	return ret

