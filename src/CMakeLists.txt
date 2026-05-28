include_guard(GLOBAL)
set(SRC pinpoint.cpp ${CMAKE_SOURCE_DIR}/include/pinpoint.h)
set(MODULE_NAME "Pinpoint")

# 引入第三方库spdlog
add_subdirectory(third_party/spdlog-1.17.0)

# 引入第三方库SQLite3
add_subdirectory(third_party/sqlite-amalgamation-3530100)

# 引入第三方库sqlite_orm
add_library(sqlite_orm INTERFACE)

target_include_directories(sqlite_orm INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/third_party/sqlite_orm-1.9.1/include)
target_link_libraries(sqlite_orm INTERFACE sqlite3)

# 引入第三方库mbedtls
add_subdirectory(third_party/mbedtls/library)

# 引入第三方库Boost
find_package(Threads REQUIRED)
add_library(boost INTERFACE)

target_include_directories(boost INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/third_party)
target_link_libraries(boost INTERFACE Threads::Threads)

# 编译动态库
if (BUILD_SHARED_LIBS)
    add_library(${MODULE_NAME} SHARED ${SRC})
    target_include_directories(${MODULE_NAME} PUBLIC ${CMAKE_SOURCE_DIR}/include)
    target_link_libraries(${MODULE_NAME} PRIVATE spdlog::spdlog sqlite_orm boost mbedtls_static)
endif ()

# 编译静态库
if (BUILD_STATIC_LIBS)
    add_library(${MODULE_NAME}_static STATIC ${SRC})
    target_include_directories(${MODULE_NAME}_static PUBLIC ${CMAKE_SOURCE_DIR}/include)
    target_link_libraries(${MODULE_NAME}_static PRIVATE spdlog::spdlog sqlite_orm boost mbedtls_static)
endif ()