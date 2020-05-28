# -*- coding:utf-8 -*-
import time


class ObserverBase(object):
    def __init__(self):
        self._observered_list = []

    def attach(self, target):
        if target not in self._observered_list:
            self._observered_list.append(target)

    def detach(self, target):
        if target in self._observered_list:
            self._observered_list.remove(target)

    def notify(self, data):
        for item in self._observered_list:
            item.update(data)


class Observer_1(ObserverBase):
    def __init__(self, name):
        super(Observer_1, self).__init__()
        self.name = name
        self._MSG = ''

    @property
    def msg(self):
        return self._MSG

    @msg.setter
    def msg(self, content):
        self._MSG = content
        self.notify(content)


class ObserveredBase(object):
    def __init__(self):
        pass

    def update(self, data):
        pass


class Observered_1(ObserveredBase):
    def __init__(self, name):
        super(Observered_1, self).__init__()
        self.name = name

    def update(self, data):
        print('{0}:{1}'.format(self.name, data))


class Observered_2(ObserveredBase):
    def __init__(self, name):
        super(Observered_2, self).__init__()
        self.name = name

    def update(self, data):
        print('{0}:{1}'.format(self.name, data))


observer = Observer_1('观察者1')

observered_1 = Observered_1('被观察者1')
observered_2 = Observered_2('被观察者2')

observer.attach(observered_1)
observer.attach(observered_2)

for i in range(5):
    msg = '消息：{0}'.format(i)
    observer.msg = '消息：{0}'.format(i)
    # observer.notify(msg)
    time.sleep(1)
