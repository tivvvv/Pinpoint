# 单元测试可执行文件
add_executable(pinpoint_test test.cpp)
target_link_libraries(pinpoint_test PRIVATE Pinpoint_static GTest::gtest_main)

# 注册到ctest
include(GoogleTest)
gtest_discover_tests(pinpoint_test)
