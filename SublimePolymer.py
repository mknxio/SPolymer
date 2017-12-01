import sublime
import sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print('test')
