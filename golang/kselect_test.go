package honey

import (
	"math/rand"
	"sort"
	"testing"
	"testing/quick"
)

func TestKSelect(t *testing.T) {

	check := func(arr []int) bool {
		if len(arr) == 0 {
			return true
		}

		k := rand.Intn(len(arr))
		res, err := KSelect(arr, k)

		if err != nil {
			return false
		}

		sort.Ints(arr)
		return res == arr[k]
	}

	if err := quick.Check(check, nil); err != nil {
		t.Error(err)
	}

}
