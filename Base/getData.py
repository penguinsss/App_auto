import os
import yaml


class GetData:
    def get_yml_data(self, yml_name):
        """
        解析yml文件
        :param yml_name:文件名字
        :return: yml数据
        """
        with open('.' + os.sep + 'Data' + os.sep + yml_name) as f:
            return yaml.safe_load(f).values()
