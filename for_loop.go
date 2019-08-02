# e175745/main/

package main

import(
	"fmt"
	"time"
	"sync"
//	"log"
//	"runtime"
)

func main() {

	for le:=0; le<100000; {
		le = le+100000

			fmt.Printf("%d",le)
		// 配列作成
		ally := make([]int, le)
		total := make([]int, le)

		i := 0
		for i < le {
			i++
			ally[i-1] = i
		}
		//fmt.Println(ally[0:1000000])
		fmt.Println("allay length = ",len(ally))

		// 並列化なし
		fmt.Println("Start : NonPallalel")

		start := time.Now()

		for _, x := range ally {
			total[x-1] = exe_total(x)
		}
		//fmt.Println(total[:])

		end := time.Now()
		fmt.Printf(", %f",(end.Sub(start)).Seconds())
		fmt.Println("Heat End")

		// 並列化した方
		// チャネルを使って変数をじゅばんに渡すべき？

		var wg sync.WaitGroup
//		c := make(chan bool, 1)
		fmt.Println("Start : Pallalization")
		start = time.Now()

		for _, x := range ally {
//			c <- true // もしcが一杯ならこの行で待たされる
			wg.Add(1)
			go func(y int){
				defer wg.Done()
			//	defer func() { <-c }()
				total[y-1] = exe_total(y)
			}(x)
		}
		//log.Println(runtime.NumGoroutine())
		//fmt.Println(total[:])
		wg.Wait()

		end = time.Now()
		fmt.Printf(", %f\n",(end.Sub(start)).Seconds())
		fmt.Println("Heat End")
	}
}

func exe_total(n int) int{
	sum := 0
	i := 0
	for i < n+1{
		sum += i
		i++
	}
	return sum
}
