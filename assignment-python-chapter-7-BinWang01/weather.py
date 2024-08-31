# Bin Wang
# Follow the instructions for coding a weather app
from statistics import mean

daily_highs = [62, 64, 79, 52, 46, 50, 58, 66, 71, 75, 78, 78, 76, 80, 77]
daily_lows = [42, 48, 47, 26, 28, 28, 32, 37, 43, 46, 48, 47, 48, 49, 50]
daily_humidity = [0.48, 0.53, 0.46, 0.44, 0.4, 0.6,
                  0.58, 0.5, 0.48, 0.43, 0.41, 0.39, 0.39, 0.3, 0.4]
avg_high = mean(daily_highs)
avg_low = mean(daily_lows)
avg_humidity = mean(daily_humidity)
highest = max(daily_highs)
lowest = min(daily_lows)
print(
    f"Weather forecast for the next 15 days: The average low will be {avg_low:.0f} and average high will be {avg_high:.0f}. The average humidity will be {avg_humidity:.2f}. The highest temperature will be {highest:.0f}. The lowest temperature will be {lowest:.0f}.")
