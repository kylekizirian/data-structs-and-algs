package mergesort

import (
	"reflect"
	"testing"
)

func TestMergesort(t *testing.T) {

	got := Mergesort([]int{5, 4, 3, 2, 1})
	want := []int{1, 2, 3, 4, 5}

	if !reflect.DeepEqual(got, want) {
		t.Errorf("got %v want %v", got, want)
	}

}
