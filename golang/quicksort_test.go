package honey

import (
	"reflect"
	"testing"
)

func TestQuicksort(t *testing.T) {

	got := Quicksort([]int{5, 4, 3, 2, 1})
	want := []int{1, 2, 3, 4, 5}

	if !reflect.DeepEqual(got, want) {
		t.Errorf("expected: %v, got: %v", want, got)
	}

}
