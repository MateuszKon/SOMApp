# założenia:
3 pierwsze godziny każdego dnia
1-2 do wykrycia trendu, następna godzina żeby ocenić wynik 

# ilość danych
- interwał 5/15/30minut
- liczba pomiarów wszystkich danych [1, 2, 3, 5, 8, 13]

### MA
- [on/off, type=[SMA, EMA, WMA], x=3-7] MA (Moving Avarage)
- [on/off, type=[SMA, EMA, WMA], x=6-14] MA (Moving Avarage)
- [on/off, type=[SMA, EMA, WMA], x=range(30, 101, 10) MA (Moving Avarage)

### Bollinger Bands
- [on/off, ma_len=range(9, 26, 2), ma_type=[SMA, EMA, WMA], std_dev=[1.5, 2, 2.5]]
- [on/off, ma_len=range(9, 26, 2), ma_type=[SMA, EMA, WMA], std_dev=[1.5, 2, 2.5]]

### RSI
- [on/off, x=5-7]
- [on/off, x=8-10]
- [on/off, x=11-14]

### Stochastic Oscillator
- [on/off, look_back_period=range(9, 28, 3), k_line_period=range(9, 28, 3), d_line_period=range(3, 14, 2)]
- [on/off, look_back_period=range(9, 28, 3), k_line_period=range(9, 28, 3), d_line_period=range(3, 14, 2)]

### MACD
- [on/off, ma1_len=range(9, 16, 2), ma2_len=range(15, 34, 3), signal_line=ma_1_len-range(1, 6), ma_type=[SMA, EMA, WMA]]
- [on/off, ma1_len=range(9, 16, 2), ma2_len=range(15, 34, 3), signal_line=ma_1_len-range(1, 6), ma_type=[SMA, EMA, WMA]]

### OBV
- [on/off. period_len=[30min, 1h, 1day]] 

### VWMA
- [on/off, len=[5, 10, 20, 50]]]

### CMF
- [on/off, period=[30min, 1h, 1day]]

### ADL
- [on/off, period=[30min, 1h, 1day]]

### VPT
- [on/off, period=[30min, 1h, 1day]]

## może w późniejszym czasie:

### price/volume
- [on/off, x=1-100]
- cena otwarcia codziennie dzisiaj i x dni wcześniej 
- cena zamknięcia codziennie x dni wcześniej
- wolumen codziennie x dni wcześniej 

### high/low
- [on/off, x=1-100]
- high x dni wcześniej
- low x dni wcześniej

### obecny dzień
- cana zamknięcia danego dnia w interwałach 5/15/30min
- wolumen danego dnia w interwałach 5/15/30min
