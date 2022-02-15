class MyHashMap(object):

    def __init__(self):
        self.keys = []
        self.hash = []
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # check if key doesn't exists 
        # otherwise update
        if key not in self.keys:
            # add new pair and key
            self.hash.append([key, value])
            self.keys.append(key)
        else:
            for i in range(len(self.hash)):
                if self.hash[i][0] == key:
                    self.hash[i] = [key, value]
                    break
            
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # check if key exists and return -1
        # otherwise return value
        if key not in self.keys:
            return -1
        for i in range(len(self.hash)):
            if self.hash[i][0] == key:
                return self.hash[i][1]
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        # check if key doesn't exist 
        # otherwise remove from both
        if key not in self.keys:
            pass
        else:
            self.keys.remove(key)
            for i in range(len(self.hash)):
                if self.hash[i][0] == key:
                    self.hash.remove(self.hash[i])
                    break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
