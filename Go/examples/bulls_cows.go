package main

import (
	"fmt"
	"math/rand"
	"time"
	"bufio"
	"os"
	"strings"
	"unicode/utf8"
)

var reader *bufio.Reader
//                     0      1        2        3        4
var words = []string{"cat", "dog", "gopher", "apple", "whale"}

func init(){
	fmt.Println("Want to play a game?")
	rand.Seed(time.Now().UnixNano())
	reader = bufio.NewReader(os.Stdin)
}

func main() {
	the_word := words[rand.Intn(len(words))]

	fmt.Printf("Guess a word of length %d:", len(the_word))
	
	for {		
		str, err := read_user_input()
		if err != nil {
			return
		}

		if you_win(the_word, strings.TrimSpace(str)) {
			return
		}
	}
}


func you_win(the_winner, guess string) bool {
		if guess == the_winner {
			fmt.Println("YOU WIN!")
			return true
		}else{
			if len(the_winner) != len(guess) {
				fmt.Printf("Guess a word of length %d:", len(the_winner))
			}else{
				bulls, cows := 0, 0
				for i, c := range guess{
					win_rune,_ := utf8.DecodeRuneInString(the_winner[i:])
					if c == win_rune {
						bulls += 1
					}else if strings.ContainsRune(the_winner, c) {
						cows += 1
					}
				}
				fmt.Printf("Bulls:%d Cows:%d :",bulls, cows)
			}
			return false
		}
}

func read_user_input() (string, error){
	str, err := reader.ReadString('\n')
	if err != nil {
		fmt.Printf("ERROR!!!!: %v\n",err)
		return "", err
	}
	return str, nil
}
