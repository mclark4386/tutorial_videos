package main

import (
	"fmt"
	"math/rand"
	"time"
	"bufio"
	"os"
	"strconv"
	"strings"
)

var reader *bufio.Reader

func main() {
	initialize()
	the_number := rand.Intn(100)

	for {		
		i, err := read_user_input()
		if err != nil {
			if strings.Contains(fmt.Sprintf("%v",err),"strconv.Atoi") {
				continue
			}
			return
		}

		if you_win(the_number, i) {
			return
		}
	}
}


func you_win(the_number, i int) bool {
		if i == the_number {
			fmt.Println("YOU WIN!")
			return true
		}else if i > the_number {
			fmt.Println("Too High")
			return false
		}else{
			fmt.Println("Too Low")
			return false
		}
}

func read_user_input() (int, error){
	str, err := reader.ReadString('\n')
	if err != nil {
		fmt.Printf("ERROR!!!!: %v\n",err)
		return 0, err
	}

	i, err2 := strconv.Atoi(strings.TrimSpace(str))
	if err2 != nil{
		fmt.Println("Please only enter a number 1-100!")
		return i, err2
	}
	return i, nil
}

func initialize(){
	fmt.Println("Want to play a game?")
	fmt.Println("Try to guess the number(1-100):")
	rand.Seed(time.Now().UnixNano())
	reader = bufio.NewReader(os.Stdin)
}
