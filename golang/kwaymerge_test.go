package honey

import (
	"reflect"
	"testing"
)

func TestKWayMerge(t *testing.T) {

	got := KWayMerge([][]int{
		[]int{1, 3, 5, 7, 9},
		[]int{2, 4, 6, 8, 10},
	})

	want := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

	if !reflect.DeepEqual(got, want) {
		t.Errorf("got %v want %v", got, want)
	}

}
