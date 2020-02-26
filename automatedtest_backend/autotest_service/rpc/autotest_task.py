class AutoTestTask(object):
    def callBack(self,fun):
        def wrapper(*args,**kwargs):

            return fun(*args,**kwargs)

        return wrapper
