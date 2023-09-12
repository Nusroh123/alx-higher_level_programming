#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - print out Python list information
 * @p: pointer to a python object
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
        Py_ssize_t size, allocate, j;
        PyObject *item;

        size = PyList_Size(p);
        allocate = ((PyListObject *)p)->allocated;

        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", allocate);

        for (j = 0; j < size; j++)
        {
                item = PyList_GetItem(p, j);
                printf("Element %ld: %s\n", j, Py_TYPE(item)->tp_name);
	}
}	
