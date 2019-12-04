import time
ans = 0
zero = [1]*10**6
zero.append(0)
cnt = 1
#処理1の実行時間計測
tik1 = time.time()

tok1 = time.time()
#処理2の実行時間計測
tik2 = time.time()

tok2 = time.time()
tiktok1 = tok1 - tik1
tiktok2 = tok2 - tik2
print(tiktok1,tiktok2)