''' class test '''
import CC
#类定义
class People:
    """定义类 people"""
    name = "zhangsan"
    age = 24
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age
    def __getname__(self):
        """私有方法 获取名字"""
        print(self.name)
    def __getage__(self):
        """私有方法 获取年龄"""
        print(self.age)
    def getname(self):
        """获取名字"""
        print(self.name)

    def getage(self):
        """get age"""
        print(self.age)


class Student(People, CC.Children):
    """类的单继承"""
    def getstudentname(self):
        """获取学生名字"""
        print(self.name)

if __name__ == "__main__":
    P = People("李煜", 32)
    P.getname()

    S = Student("ls", 20)
    S.getstudentname()
    S.cray()

    Z = CC.test11()
    SAW = CC.Children()
    SAW.cray()
    CC.ok()
    print(Z)
