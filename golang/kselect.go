package honey

import (
	"errors"
	"math/rand"
)

var ErrInvalidK = errors.New("k out of bounds")

// Select's the k-th smallest element from unsorted array.
// k starts from 0 so the smallest element is k=0
func KSelect(arr []int, k int) (int, error) {

	if k < 0 || k >= len(arr) {
		return -1, ErrInvalidK
	}

	randIndex := rand.Intn(len(arr))
	pivot := arr[randIndex]

	// Split into slices less than, equal to, and greater
	// than the current element
	lt := []int{}
	eq := []int{}
	gt := []int{}

	for _, val := range arr {
		if val < pivot {
			lt = append(lt, val)
		} else if val == pivot {
			eq = append(eq, val)
		} else {
			gt = append(gt, val)
		}
	}

	// If k falls within the range of the "equal to" array,
	// then the pivot is our solution. Otherwise we recurse
	// on the less than or greater than array.
	if k < len(lt) {
		return KSelect(lt, k)
	} else if k < len(lt)+len(eq) {
		return pivot, nil
	} else {
		return KSelect(gt, k-len(lt)-len(eq))
	}
}
