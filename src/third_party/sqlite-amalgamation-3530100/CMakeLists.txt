# SQLite3 静态库
add_library(sqlite3 STATIC sqlite3.c)
target_include_directories(sqlite3 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# 启用线程安全模式
target_compile_definitions(sqlite3 PUBLIC SQLITE_THREADSAFE=1)