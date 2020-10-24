#!/usr/bin/env python3

T = list(input())

ans = ''
for i in range(len(T)) :
    if i+1 == len(T) :
        if T[i] != '?' :
            ans += T[i]
        else :
            ans += 'D'
        continue

    if i == 0 :
        if T[i] != '?' :
            ans += T[i]
        else :
            if T[i+1] == 'P' :
                ans += 'D'
            else :
                ans += 'P'
        continue
    
    if T[i] != '?' :
        ans += T[i]
        continue

    if ans[i-1] == 'P' :
        ans += 'D'
    elif ans[i-1] == 'D' :
        if T[i+1] == 'P' :
            ans += 'D'
        else :
            ans += 'P'

print(ans)