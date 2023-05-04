package main

import (
	"bytes"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
)

func TestRenderPage(t *testing.T) {
	sleepCalled := 0
	sleep := func(_ time.Duration) { sleepCalled++ }
	buf := bytes.NewBuffer(nil)

	renderPage(sleep, buf)
	results := string(buf.Bytes())

	assert.Equal(t, 4, sleepCalled)
	assert.Contains(t, results, loreIpsum)
}
