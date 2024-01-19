
import os

import yaml


# 写入
def write_yaml(data):
    with open(os.getcwd() + '/extract.yaml', 'a+', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)


# 读取
def read_yaml(key):
    with open(os.getcwd() + '/extract.yaml', 'r', encoding='utf-8') as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_data[key]

# 清空
def clean_yaml():
    with open(os.getcwd() + '/extract.yaml', 'w', encoding='utf-8') as f:
        f.truncate()

# 读取测试用例
def read_yaml_testcase(yaml_path):
    with open(os.getcwd() + '/' + yaml_path, 'r', encoding='utf-8') as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_data