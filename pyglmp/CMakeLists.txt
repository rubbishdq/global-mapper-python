find_package(global_mapper REQUIRED)

add_cython_target(_pyglmp CXX)
add_library(_pyglmp MODULE ${_pyglmp})
python_extension_module(_pyglmp)

install(TARGETS _pyglmp LIBRARY DESTINATION pyglmp)
