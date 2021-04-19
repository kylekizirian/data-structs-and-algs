package honey

// merge two sorted arrays into one sorted array
func KWayMerge(arrs [][]int) []int {

	// divide and conquer k-way merge algorithm
	if len(arrs) == 0 {
		return []int{}
	}

	// our base case is if we just have one sorted array
	// then we are finished
	if len(arrs) == 1 {
		return arrs[0]
	}

	// If we have more than one sorted array, recursively
	// call this on the two halves of the list of sorted
	// arrays.
	mid := len(arrs) / 2
	return merge(KWayMerge(arrs[:mid]), KWayMerge(arrs[mid:]))
}
