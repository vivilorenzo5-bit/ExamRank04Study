def array_rotation_detector(arr1: list, arr2: list) -> bool:
	n = len(arr1)
	if n != len(arr2):
		return False
	if n == 0:
		return True

	for shift in range(n):
		match = True
		for i in range(n):
			if arr1[(i + shift) % n] != arr2[i]:
				match = False
				break
		if match:
			return True
	return False
