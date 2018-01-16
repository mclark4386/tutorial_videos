package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	fmt.Println("Hello world!")
	rand.Seed(time.Now().UnixNano())
	fmt.Printf("random: %v\n", rand.Intn(100))
}
