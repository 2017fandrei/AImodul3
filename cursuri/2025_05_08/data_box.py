class DataBox:

    def __init__(self):
        self.data = []
        self.amount_of_data = 0

    def add_data(self, data):
        if isinstance(data,int):
            self.data.append(data)
        elif isinstance(data,float):
            self.data.append(data)
        elif all(isinstance(n, int) or isinstance(n, float) for n in data): #verifica daca e o lista de float'uri
            self.data.extend(data)
        else:
            print('invalid value type')
        self.amount_of_data=len(self.data)

    def remove_data(self):
        self.data.clear()
        self.amount_of_data = 0

    def get_data(self):
        return self.data

    def get_amount_of_data(self):
        return self.amount_of_data

box = DataBox()
box.data = [3, 5, 6, 7]
box.add_data([1, 2, 3, 4, 5])


print(box.data)
