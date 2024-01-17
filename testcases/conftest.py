import pytest
# 添加fixture固件
# @pytest.fixture(scope='function', autouse=False)
@pytest.fixture(scope='function',params=['mysql','redis'],autouse=False, ids=['m','r'], name='conn')
def connection_mysql(request):
    print('之前：连接数据库')
    yield request.param
    print('之后：关闭数据库连接')

# 参数化fixture示例
@pytest.fixture(params=[("John", 25), ("Alice", 30), ("Bob", 22)])
def person_data(request):
    return {
        "name": request.param[0],
        "age": request.param[1]
    }