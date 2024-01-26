class RoseDictionary:
    def __init__(self):
        self.list1 = []
        self.list2 = []
    def __setitem__(self,key,value):
        self.list1.append(key)
        self.list2.append(value)
    def __getitem__(self,key):
        return self.list2[self.list1.index(key)]
    def get_item(self, key, default = None, error_msg= None, raise_error = False):
        lst = zip(self.list1,self.list2)
        x = dict(lst)
        try:
            return x[key]   
        except:
            if raise_error:
                print('KeyError:' + ' ' + (error_msg if error_msg is not None else "\n"))
            else:
                if default is not None:
                    return default
                else:
                    if error_msg is not None:
                        return error_msg
                    else:
                        print('Value was not found and no default value/message was specified.')
    def pop_item(self, default=None, error_msg = None, raise_error= False):
        try:
            value = self.list2[-1]
            self.list1.remove(self.list1[-1])
            self.list2.remove(self.list2[-1])
            return value
        except:
            if raise_error:
                print('KeyError:' + ' ' + (error_msg if error_msg is not None else "\n"))
            else:
                if default is not None:
                    print(default)
                else:
                    if error_msg is not None:
                        print(error_msg)
                    else:
                        print('Value was not found and no default value/message was specified.')
d = RoseDictionary() 
d["key1"] = "value1" 
d["key2"] = "value2" 
print(d["key1"]) 
print(d.get_item("key1")) 
print(d.get_item("key3", default = "Default Value")) 
d.get_item("key3") 
print(d.pop_item()) 
print(d.get_item("key1", error_msg = "error message")) 
print(d.get_item("key2", error_msg = "error message2")) 
d.pop_item() 
d.get_item("key3", default = "Default Value", raise_error = True, error_msg = "Hi")