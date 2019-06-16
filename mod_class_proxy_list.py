class ListOfProxies(list):

    def add_proxy(self, proxy):
        self.append(proxy)

    def show(self):
        for row in self:
            print(row)