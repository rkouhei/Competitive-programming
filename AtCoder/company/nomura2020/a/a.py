#!/usr/bin/env python3

H1, M1, H2, M2, K = map(int, input().split())

min = (H2*60+M2) - (H1*60+M1)

print(min - K)