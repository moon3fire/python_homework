
class Duration:
    def __init__(self, start, end, span_list):
        self.class_start_time = start
        self.class_end_time = end
        self.data = span_list
    
    def validate_time(self, hour1, minute1, hour2, minute2, validate_hour, validate_minute):
        if minute1 + validate_minute > 59:
            hour1 += 1
        if minute2 - validate_minute < 0:
            hour2 -= 1
        if hour1 + validate_hour + 2 <= hour2 - validate_hour:
            return True
        return False
    
    def calculate_times(self):
        start_hour = self.class_start_time[0:2]
        start_minutes = self.class_start_time[3:5]
        end_hour = self.class_end_time[0:2]
        end_minutes = self.class_end_time[3:5]
        
        valid_times = []
        for i in range(0, len(self.data)):
            for time in self.data[i]["start_times"]:
                is_valid = self.validate_time(int(start_hour), int(start_minutes), int(end_hour), int(end_minutes), int(time[0:2]), int(time[3:5]))
                if is_valid:
                    valid_times.append((time, self.data[i]["break_duration"], self.data[i]["start_time_type"]))
        return valid_times