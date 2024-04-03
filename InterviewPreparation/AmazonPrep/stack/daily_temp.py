def dailyTemperatures(temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        hottest = 0
        answer = [0] * n
        
        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]
            if current_temp >= hottest:
                hottest = current_temp
                continue
            
            days = 1
            while temperatures[curr_day + days] <= current_temp:
                # Use information from answer to search for the next warmer day
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer

if __name__ == "__main__":
    print(dailyTemperatures(temperatures=[73,74,75,71,69,72,76,73]))