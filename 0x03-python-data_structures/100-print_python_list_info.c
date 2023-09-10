#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int list_size, alloc, n;
	PyObject *obj;

	list_size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", alloc);

	for (n = 0; n < list_size; n++)
	{
		printf("Element %d: ", n);

		obj = PyList_GetItem(p, n);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
