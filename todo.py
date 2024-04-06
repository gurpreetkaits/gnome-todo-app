import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class TodoApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="To-Do App")
        self.set_border_width(10)

        self.task_list = Gtk.ListStore(str)
        self.task_view = Gtk.TreeView(model=self.task_list)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Tasks", renderer, text=0)
        self.task_view.append_column(column)

        self.task_entry = Gtk.Entry()
        self.task_entry.set_placeholder_text("Add a task")

        add_button = Gtk.Button(label="Add Task")
        add_button.connect("clicked", self.add_task)

        remove_button = Gtk.Button(label="Remove Task")
        remove_button.connect("clicked", self.remove_task)

        grid = Gtk.Grid()
        grid.attach(self.task_entry, 0, 0, 1, 1)
        grid.attach(add_button, 1, 0, 1, 1)
        grid.attach(self.task_view, 0, 1, 2, 1)
        grid.attach(remove_button, 0, 2, 2, 1)

        self.add(grid)

    def add_task(self, button):
        task = self.task_entry.get_text()
        self.task_list.append([task])
        self.task_entry.set_text("")

    def remove_task(self, button):
        selection = self.task_view.get_selection()
        model, iter = selection.get_selected()
        if iter is not None:
            model.remove(iter)

win = TodoApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
