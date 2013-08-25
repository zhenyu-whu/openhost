import sublime, sublime_plugin

class HostCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		host = "C:\\Windows\\System32\\drivers\\etc\\hosts"
		self.view.window().open_file(host)


