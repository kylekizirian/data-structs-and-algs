package honey

import "math/rand"

func Quicksort(arr []int) []int {

	if len(arr) < 2 {
		return arr
	}

	// choose random element as the pivot
	randIndex := rand.Intn(len(arr))
	pivot := arr[randIndex]

	result := []int{}
	eq := []int{}
	gt := []int{}

	// split the splice into items less than the pivot, equal to the
	// pivot, and greater than the pivot
	for _, num := range arr {
		if num < pivot {
			result = append(result, num)
		} else if num == pivot {
			eq = append(eq, num)
		} else {
			gt = append(gt, num)
		}
	}

	// recursively sort the slices less than and greater than the pivot
	result = Quicksort(result)
	gt = Quicksort(gt)

	// concatenate all of the lists together
	result = append(result, eq...)
	result = append(result, gt...)

	return result
}
