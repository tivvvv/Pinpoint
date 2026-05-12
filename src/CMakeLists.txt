include_guard(GLOBAL)
set(SRC pinpoint.cpp ${CMAKE_SOURCE_DIR}/include/pinpoint.h)
set(MODULE_NAME "Pinpoint")

# 引入第三方库spdlog
add_subdirectory(third_party/spdlog-1.17.0)

# 编译动态库
if (BUILD_SHARED_LIBS)
    add_library(${MODULE_NAME} SHARED ${SRC})
    target_include_directories(${MODULE_NAME} PUBLIC ${CMAKE_SOURCE_DIR}/include)
    target_link_libraries(${MODULE_NAME} PRIVATE spdlog::spdlog)
endif ()

# 编译静态库
if (BUILD_STATIC_LIBS)
    add_library(${MODULE_NAME}_static STATIC ${SRC})
    target_include_directories(${MODULE_NAME}_static PUBLIC ${CMAKE_SOURCE_DIR}/include)
    target_link_libraries(${MODULE_NAME}_static PRIVATE spdlog::spdlog)
endif ()