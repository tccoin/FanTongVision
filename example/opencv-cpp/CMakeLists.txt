cmake_minimum_required(VERSION 3.5)

if( MINGW )
  add_definitions(-D__STDC_FORMAT_MACROS)
  add_definitions(-D__USE_MINGW_ANSI_STDIO=1)
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=gnu99")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++11")
endif()

project( DisplayImage )
set(OpenCV_DIR $ENV{OpenCV_LIBS})
find_package( OpenCV REQUIRED)

add_executable( DisplayImage test.cpp )
include_directories( ${OpenCV_INCLUDE_DIRS} )
target_link_libraries( DisplayImage ${OpenCV_LIBS} )

message(STATUS "OpenCV library status:")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")