# Микроядро, которое управляет плагинами
class Microkernel:
    def __init__(self):
        self.plugins = {}


    def register_plugin(self, plugin_name, plugin):
        self.plugins[plugin_name] = plugin


    def run(self):
        for plugin in self.plugins.values():
            plugin.execute()


# Базовый интерфейс для плагинов
class Plugin:
    def execute(self):
        pass


# Конкретный плагин 1
class PrintPlugin(Plugin):
    def execute(self):
        print("Плагин для печати: Привет, мир!")


# Конкретный плагин 2
class LoggingPlugin(Plugin):
    def execute(self):
        print("Плагин логирования: Запись события")


# Использование
if __name__ == "__main__":
    kernel = Microkernel()


    # Регистрация плагинов
    print_plugin = PrintPlugin()
    logging_plugin = LoggingPlugin()


    kernel.register_plugin("print_plugin", print_plugin)
    kernel.register_plugin("logging_plugin", logging_plugin)


    # Запуск плагинов через ядро
    kernel.run()

