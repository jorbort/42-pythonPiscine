import time as tm

current_time = tm.time()
local_time = tm.strftime("%b %d %Y", tm.localtime())

print(f"Seconds since January 1, 1970: {current_time:,.4f}  or {current_time:.2e} in scientific notation")
print(local_time)