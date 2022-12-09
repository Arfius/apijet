from {project_name}.models.{import_name} import {endpoint_name}Base


class {endpoint_name}Core:
    @staticmethod
    def reverse(data: {endpoint_name}Base) -> {endpoint_name}Base:
        data.text = data.text[::-1]
        return data
