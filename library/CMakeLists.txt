include_directories(${ADEPT_SOURCE_DIR}/library/include)
add_definitions(-D__ADEPT_COMPILE_DLL)
add_library(adept SHARED ${ADEPT_SOURCE_DIR}/library/src/adept.cpp)