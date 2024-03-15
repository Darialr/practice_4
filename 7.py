krl, arn, srg = map(int, input().split())
if krl < srg and arn < srg:
    print(srg)
elif krl > arn and krl > srg:
    print(krl)
else:
    print(arn)
