class jValue:

    def __init__(self,j):
        self.j = j

    def __getOne(self,j,arg):
        if type(j) == type({}):
            return j.get(arg)
        if type(j) == type([]):
            try:
                return j[arg]
            except IndexError:
                return 0

    def get(self,*args):
        value = self.j
        for i in args:
            value = self.__getOne(value,i)
            if not value:
                break
        return value

    def getJ(self,*args):
        return (lambda v : jValue(v) if v else None)(self.get(*args))