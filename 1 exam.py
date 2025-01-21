d_str = input()
t_str = input()
d_hour, d_minute = map(int, d_str.split(':'))
t_hour, t_minute = map(int, t_str.split())
total_minutes = d_hour * 60 + d_minute + t_hour * 60 + t_minute
a_hour = (total_minutes // 60) % 24
a_minute = total_minutes % 60
print(f"{a_hour:02d}:{a_minute:02d}")   