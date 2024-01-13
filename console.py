#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the console."""
        return True

    def do_EOF(self, arg):
        """Exit the console on EOF (Ctrl+D)."""
        print("")  # Print a new line before exiting
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key in instances:
            print(instances[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key in instances:
            del instances[instance_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        instances = storage.all()
        if not args:
            print([str(obj) for obj in instances.values()])
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in instances.items() if args[0] in key])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = instances[instance_key]
        attr_name = args[2]
        attr_value = args[3]
        if hasattr(instance, attr_name):
            attr_value = type(getattr(instance, attr_name))(attr_value)
            setattr(instance, attr_name, attr_value)
            storage.save()
        else:
            setattr(instance, attr_name, attr_value)
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
