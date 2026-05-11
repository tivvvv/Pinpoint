include_guard(GLOBAL)
set(SRC pinpoint.cpp ${CMAKE_SOURCE_DIR}/include/pinpoint.h)
set(MODULE_NAME "Pinpoint")

# 编译动态库
if (BUILD_SHARED_LIBS)
    add_library(${MODULE_NAME} SHARED ${SRC})
    target_include_directories(${MODULE_NAME} PUBLIC ${CMAKE_SOURCE_DIR}/include)
endif ()

# 编译静态库
if (BUILD_STATIC_LIBS)
    add_library(${MODULE_NAME}_static STATIC ${SRC})
    target_include_directories(${MODULE_NAME}_static PUBLIC ${CMAKE_SOURCE_DIR}/include)
endif ()