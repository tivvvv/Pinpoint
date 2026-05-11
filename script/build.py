import shutil
import os
import argparse

# 脚本路径和构建输出目录
SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0]
BUILD_DIR_PATH = SCRIPT_PATH + '/../build'


# 清理构建目录
def clear():
    if os.path.exists(BUILD_DIR_PATH):
        shutil.rmtree(BUILD_DIR_PATH)


# 编译mac平台(arm64)
def build_mac(config='Release', args=None):
    platform_dir = '%s/%s-%s' % (BUILD_DIR_PATH, 'arm64', config)
    os.makedirs(platform_dir, exist_ok=True)

    os.chdir(platform_dir)

    # 拼接cmake配置命令
    build_cmd = 'cmake ../.. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=%s -DCMAKE_OSX_ARCHITECTURES=arm64' % config

    if args.test:
        build_cmd += ' -DBUILD_TEST=ON'

    if args.demo:
        build_cmd += ' -DBUILD_DEMO=ON'

    # 执行cmake配置
    print("build cmd: " + build_cmd)
    ret = os.system(build_cmd)
    if ret != 0:
        print('!!!!!!!!!!!!!!!!!!cmake configure fail')
        return False

    # 执行编译
    build_cmd = 'cmake --build . --config %s --parallel 8' % config
    ret = os.system(build_cmd)
    if ret != 0:
        print('build fail!!!!!!!!!!!!!!!!!!!!')
        return False
    return True


def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='build mac')
    parser.add_argument('--test', action='store_true', default=False,
                        help='build unittest')
    parser.add_argument('--demo', action='store_true', default=False,
                        help='build demo')
    parser.add_argument('--config', type=str, default='Release',
                        choices=['Debug', 'Release'],
                        help='build configuration (Debug/Release)')
    parser.add_argument('--no-clean', action='store_true', default=False,
                        help='skip clean before build')
    args = parser.parse_args()

    # 清理旧的构建产物
    if not args.no_clean:
        clear()

    os.makedirs(BUILD_DIR_PATH, exist_ok=True)

    # 开始编译
    if not build_mac(config=args.config, args=args):
        exit(1)


if __name__ == '__main__':
    main()
