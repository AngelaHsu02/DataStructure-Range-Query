## 目標
比較sorted array、array of sorted arrays、skip list的range query所需時
間。 
## 實驗
實作3個function: range_query、equivalent、print，利用三個資料結構執行range_query，並測量時間。 
## 結論
Array of Sorted Array Range Query 的執行速度最快，k≦2^14，Skip List 的速度較快，search範圍更大後，Sorted Array 反而比較快。
