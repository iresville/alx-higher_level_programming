#include <Python.h>

void print_python_list_info(PyObject *p)
{
    long int size = PyList_Size(p);
    long int alloc = ((PyListObject *)p)->allocated;
    PyObject *item;
    Py_ssize_t i;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
