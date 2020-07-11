#!usr/bin/python3
# -*- coding: utf-8 -*-
# author zzZ5

class Observable:
    '''
    Observable类追踪所有的观察者并通知他们
    '''

    def __init__(self):
        # 初始化时创建观察者列表
        self._observers = []

    def register_observer(self, observer):
        # 注册观察者到需要通知的观察者列表
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        # 将观察者移除需要通知的观察者列表
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify_observers(self):
        # 数据发生变化时通知所有观察者
        for observer in self._observers:
            observer.update(self)


class Data(Observable):
    '''
    Data类继承自Observable, 不同类型的消息可以使用同样的方法通知
    '''

    def __init__(self):
        # 初始化时设置数据为''
        Observable.__init__(self)
        self._data = ''

    @property
    def data(self):
        # get 信息
        return self._data

    @data.setter
    def data(self, value):
        # set 信息
        self._data = value
        # 设置信息后调用修改信息方法以通知各个观察者.
        self.notify_observers()


class Observer():
    '''
    观察者父类
    '''

    def __init__(self, name=''):
        # 初始化时为每个观察者单独设置一个名字
        self.name = name

    def update(self, Observable):
        # 当消息更新时调用该方法
        pass


class OrdinaryObserver(Observer):

    def update(self, Observable):
        # 为各类观察者重写不同的update()方法
        print('Observer {} has data {}'.format(
            self.name, Observable.data))


class VipObserver(Observer):

    def update(self, Observable):
        # 为各类观察者重写不同的update()方法
        print('Distinguished observer {} has data {}'.format(
            self.name, Observable.data))


data1 = Data()
data2 = Data()
observer1 = OrdinaryObserver('A')
observer2 = VipObserver('B')
data1.register_observer(observer1)
data1.register_observer(observer2)
data2.register_observer(observer1)
data2.register_observer(observer2)


data1.data = "Big news"
data2.data = "Missing person notice"
data1.data = "Latest news"
data2.data = "Lawyer's letter"
data1.remove_observer(observer1)
data2.remove_observer(observer2)
data1.data = "Live news"
data2.data = "Wanted order"
