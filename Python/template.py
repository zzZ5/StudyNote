"""三种不同的获取数据方式"""


def get_text():
    return "plain-text"


def get_pdf():
    return "pdf"


def get_csv():
    return "csv"


# 转换数据格式
def convert_to_text(data):
    print("[CONVERT]")
    return "{} as text".format(data)


# 保存数据
def saver():
    print("[SAVE]")


def template_function(getter, converter=False, to_save=False):
    """模板方法, 根据自己的需要使用不同的方法, 基础的算法骨架是一样的"""
    data = getter()
    print("Got `{}`".format(data))

    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Skip conversion")

    if to_save:
        saver()

    print("`{}` was processed".format(data))


template_function(get_text, to_save=True)
template_function(get_pdf, converter=convert_to_text)
template_function(get_csv, to_save=True)
