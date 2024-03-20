import sys

f = sys.float_info.max
print(f)
# 1.7976931348623157e+308
f = f-1
print(f == f + 1)
# True
f += 1
print(f)
# 1.7976931348623157e+308