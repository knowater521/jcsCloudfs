# coding: utf-8
__author__ = 'liuyf'
__date__ = '2018/6/28 16:52'

class DownloadFileRequestFeatures(object):
    """
    每天下载的文件量
    """
    def __init__(self):
        pass

    def test_no_download(self):
        print "测试，当天没有下载文件\n"
        customize_request_features_origin = {  # 初始1天的下载模式
            'aliyun-beijing': 3,
            # 'aliyun-shanghai': 1,
            # 'aliyun-shenzhen': 3,
        }
        customize_request_features_new = {  # 当前统计1天新的下载模式
            # 'aliyun-beijing': 3,
            # 'aliyun-shanghai': 1,
            # 'aliyun-shenzhen': 3,

        }
        return customize_request_features_origin, customize_request_features_new

    def test_no_operation(self):
        print "测试，不进行修改操作\n"
        customize_request_features_origin = {  # 初始1天的下载模式
            'aliyun-beijing': 5,
            'aliyun-shanghai': 1,
            # 'aliyun-shenzhen': 10,
        }
        customize_request_features_new = {  # 当前统计1天新的下载模式
            'aliyun-beijing': 2,
            'aliyun-shanghai': 2,
            # 'aliyun-shenzhen': 4,
        }
        return customize_request_features_origin, customize_request_features_new

    def test_update_metadata(self):
        print "测试,只更新元数据\n"
        customize_request_features_origin = {  # 初始1天的下载模式
            'aliyun-beijing': 3,
            'aliyun-shanghai': 1,
            'aliyun-shenzhen': 3,
        }
        customize_request_features_new = {  # 当前统计1天新的下载模式
            'aliyun-beijing': 3,
            # 'aliyun-shanghai': 3,
            'aliyun-shenzhen': 3,
        }
        return customize_request_features_origin, customize_request_features_new

    def test_data_block_migration(self):
        print "测试，进行数据迁移，并更新元数据\n"
        customize_request_features_origin = {  # 初始1天的下载模式
            'aliyun-beijing': 50,
            'aliyun-shanghai': 50,
            # 'aliyun-shenzhen': 3,
        }
        customize_request_features_new = {  # 当前统计1天新的下载模式
            # 'aliyun-beijing': 3,
            'aliyun-shanghai': 50,
            'aliyun-shenzhen': 50,
        }
        return customize_request_features_origin, customize_request_features_new
