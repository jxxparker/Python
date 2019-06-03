class MathDojo(object):
    def __init__ (self):
        self.value = 0

    def add(self, *num): #tuples into list
        num_list = list(num)
        temp_str = str(self.value)

        if len(num_list) > 1: # check if the list has more than one
            temp = 0
            for number in num_list:
                temp_str += ' + ' + str(number)
                temp += number
            self.value += temp

        else:
            temp_str += ' + ' + str(num_list[0])
            self.value += num_list[0]
        print temp_str
        return self

    def subtract(self, *num):
        num_list = list(num)
        temp_str = str(self.value)
        if len(num_list) > 1:
            temp = 0
            for number in num_list:
                temp_str += ' - ' + str(number)
                temp += number

            self.value -= temp
        
        else:
            temp_str += ' - ' + str(num_list[0])
            self.value -= num_list[0]
        print temp_str
        return self

md = MathDojo()
md.add(2).add(2,5).subtract(1,1)
print md.value