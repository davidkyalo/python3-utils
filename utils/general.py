import importlib

def super_imports(names, package = None, namespace = None, callfunc = None, *args):
	""" Not Working. """
	modules = []
	package_mod = importlib.import_module(package)

	for name in names:
		module = importlib.import_module(name, package)
		setattr(package_mod, name, module)
		if callable(callfunc):
			callfunc(module, *args)
		modules.append(module)
	return modules

