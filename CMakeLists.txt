# 最小cmake版本要求
cmake_minimum_required(VERSION 4.1)

# 项目名称和版本
project(Pinpoint VERSION 1.0.0)

# c++标准
set(CMAKE_CXX_STANDARD 20)

# 构建选项
option(BUILD_SHARED_LIBS "build shared library" ON)
option(BUILD_STATIC_LIBS "build static library" ON)
option(BUILD_DEMO "build demo" OFF)
option(BUILD_TEST "build unittest" OFF)

# 打印构建信息
message(STATUS "CMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}")
message(STATUS "CMAKE_SYSTEM_NAME=${CMAKE_SYSTEM_NAME}")

if ("${CMAKE_BUILD_TYPE}" STREQUAL "Debug")
    add_definitions(-DDEBUG)
else ()
    add_definitions(-DNDEBUG)
endif ()

# 添加源代码目录
add_subdirectory(src)

# 添加demo目录
if (BUILD_DEMO)
    add_subdirectory(demo)
endif ()

# 添加test目录
if (BUILD_TEST)
    add_subdirectory(googletest-1.17.0)
    add_subdirectory(test)
endif ()