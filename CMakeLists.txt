cmake_minimum_required(VERSION 3.10)
project(CppLeetCodeEnv)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Find all main.cpp files in subdirectories of src/
file(GLOB_RECURSE MAIN_FILES src/*/main.cpp)

# Check if MAIN_FILES is not empty
if(MAIN_FILES)
    # Create an executable for each main.cpp file, using the directory name for identification
    foreach(MAIN_FILE ${MAIN_FILES})
        get_filename_component(DIR_PATH ${MAIN_FILE} DIRECTORY)
        get_filename_component(DIR_NAME ${DIR_PATH} NAME)

        set(EXEC_NAME ${DIR_NAME}_main)  # Format: <directory>_main
        add_executable(${EXEC_NAME} ${MAIN_FILE})
        set_target_properties(${EXEC_NAME} PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

        # Add compiler options for this target
        target_compile_options(${EXEC_NAME} PRIVATE -Wall -Wextra -g -O0)
    endforeach()
else()
    message(WARNING "No main.cpp files found in src/ subdirectories.")
endif()