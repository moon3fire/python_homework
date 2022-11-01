from class_.Break import Break

class Domaingenerator:
    def __init__(self, start_time, end_time, list_of_breaks):
        self.list = list_of_breaks
        self.start = start_time
        self.end = end_time
    
    def generate_domain(self):
        ret_list = []
        break_str = "Break("
        for item in self.list:
            hour = int(self.start[0:2]) + int(getattr(item, 'break_info')[0][0:2])
            minute = int(self.start[3:5]) + int(getattr(item, 'break_info')[0][3:5])
            if minute > 59:
                minute -= 60
                hour += 1
            if minute == 0:
                minute = "00"
            str1 = str(hour) + ":" + str(minute) + ":00, " 
            break_minutes = int(minute) + int(getattr(item, 'break_info')[1])
            if break_minutes > 59:
                hour += 1
                break_minutes -= 60
            
            if str(break_minutes) == "0":
                break_minutes = "00"
            str2 = str(hour) + ":" + str(break_minutes) + ":00, " + str(getattr(item, 'break_info')[1]) + ")"
            ret_list.append(break_str + str1 + str2)
        return ret_list