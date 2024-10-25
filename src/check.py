def check0(arg: str) -> str:
    if arg == "":
        return "请先输入地图画的编号!"
    elif not arg.isnumeric() or int(arg) < 0:
        return "地图画编号应为非负整数!"
    else:
        return str(int(arg))


def check1(arg: str) -> str:
    if arg == "":
        return "请输入地图画遍历的数量!"
    elif not arg.isdecimal() or int(arg) <= 0:
        return "地图画数量应为正整数!"
    else:
        return str(int(arg))


def check2(arg1: str, arg2: str) -> str:
    if arg1 == "" or arg2 == "":
        return (
            "请输入地图画的"
            + ("长" if arg1 == "" else "")
            + ("宽" if arg2 == "" else "")
            + ("" if arg1 == "" and arg2 == "" else "度")
        )

    elif not arg1.isdecimal() or not arg2.isdecimal() or int(arg1) * int(arg2) <= 0:
        return "地图画面积应为正整数!"
    else:
        return str(int(arg1) * int(arg2))


def check3(arg1: str, arg2: str) -> str:
    if arg1 == "" or arg2 == "":
        return (
            "请输入"
            + ("" if arg1 == "" and arg2 == "" else "第")
            + ("一" if arg1 == "" else "")
            + ("二" if arg2 == "" else "")
            + "幅地图画的编号!"
        )
    elif not arg1.isdecimal() or not arg2.isdecimal() or int(arg2) - int(arg1) <= 0:
        return "地图画之差应为正整数!"
