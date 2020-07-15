class Subject:
    """
    正如文档中提到的, RealSubject和Proxy的接口应该是相同的,
    因为客户端应该能够使用RealSubject或Proxy, 而不需要更改代码.
    并非所有时候都需要此接口. 关键是客户端应该能够互换使用RealSubject或Proxy,
    而无需更改代码
    """

    def do_the_job(self, user):
        raise NotImplementedError()


class RealSubject(Subject):
    """这是真正工作的对象."""

    def do_the_job(self, user):
        print("I am doing the job for {}".format(user))


class Proxy(Subject):
    """这个是代理对象"""

    def __init__(self):
        self._real_subject = RealSubject()

    def do_the_job(self, user):
        """
        记录和控制访问.
        """

        print("[log] Doing the job for {} is requested.".format(user))

        if user == "admin":
            self._real_subject.do_the_job(user)
        else:
            print("[log] I can do the job just for `admins`.")


def client(job_doer, user):
    job_doer.do_the_job(user)


proxy = Proxy()
real_subject = RealSubject()
client(proxy, 'admin')
client(proxy, 'anonymous')
client(real_subject, 'admin')
client(real_subject, 'anonymous')
