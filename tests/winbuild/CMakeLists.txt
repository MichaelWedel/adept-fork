include_directories(${ADEPT_SOURCE_DIR}/library/include)
link_directories(${ADEPT_BINARY_DIR}/library)

add_executable(winbuild main.cpp)

target_link_libraries(winbuild adept.lib)