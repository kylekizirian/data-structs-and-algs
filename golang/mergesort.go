package honey

// Given two sorted arrays, merge them together
func merge(arr1 []int, arr2 []int) []int {

	if len(arr1) == 0 {
		return arr2
	}

	if len(arr2) == 0 {
		return arr1
	}

	arr1_first := arr1[0]
	arr2_first := arr2[0]

	if arr1_first < arr2_first {
		return append([]int{arr1_first}, merge(arr1[1:], arr2)...)
	} else {
		return append([]int{arr2_first}, merge(arr1, arr2[1:])...)
	}
}

func Mergesort(arr []int) []int {

	if len(arr) <= 1 {
		return arr
	}

	mid := len(arr) / 2

	first_half := Mergesort(arr[:mid])
	second_half := Mergesort(arr[mid:])

	return merge(first_half, second_half)
}
