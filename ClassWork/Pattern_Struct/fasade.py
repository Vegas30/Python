# Подсистема 1
class SubsystemA:
    def operation_a1(self):
        return "SubsystemA: Выполнение операции A1"

    def operation_a2(self):
        return "SubsystemA: Выполнение операции A2"

    # Подсистема 2


class SubsystemB:
    def operation_b1(self):
        return "SubsystemB: Выполнение операции B1"

    def operation_b2(self):
        return "SubsystemB: Выполнение операции B2"

    # Фасад


class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def operation(self):
        results = []
        results.append(self._subsystem_a.operation_a1())
        results.append(self._subsystem_a.operation_a2())
        results.append(self._subsystem_b.operation_b1())
        results.append(self._subsystem_b.operation_b2())
        return "\n".join(results)

    # Клиент


facade = Facade()
print(facade.operation())