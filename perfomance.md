# Running 1m test @ http://fast-api-auth:80/user/ivan1
## 100 threads and 100 connections
    Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    34.64ms    6.54ms 128.22ms   89.40%
    Req/Sec    28.91      4.95    90.00     74.85%
    173664 requests in 1.00m, 62.94MB read
### Requests/sec:   2889.65
### Transfer/sec:      1.05MB
## ИТОГО С КЕШЕМ: 2889 rps, latency 34.64ms


# Running 1m test @ http://fast-api-auth:80/user/ivan1
## 100 threads and 100 connections
    Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   148.04ms   46.58ms 295.90ms   81.99%
    Req/Sec     7.02      2.65    40.00     50.93%
    36944 requests in 1.00m, 10.12MB read
    Socket errors: connect 0, read 8684, write 0, timeout 0
    Non-2xx or 3xx responses: 8694
### Requests/sec:    614.71
### Transfer/sec:    172.39KB
## ИТОГО БЕЗ КЕША: 614 rps, latency 148.04ms
## Кэш увеличил пропускную способность в 5 раз и уменьшил задержку в 5 раз