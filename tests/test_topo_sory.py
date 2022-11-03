from src.objects.topo_sort import topological_sort


# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


def test():
    jobs = [1, 2, 3, 4]
    deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]

    print(topological_sort(jobs=jobs, deps=deps))

print(test())
