import json, os


class Data:
    @classmethod
    def get_json_data(self, name):
        """
        读取json文件数据
        :param name: 文件名字 文件必须在当前Data文件夹
        :return:
        """
        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
            return json.load(f)
