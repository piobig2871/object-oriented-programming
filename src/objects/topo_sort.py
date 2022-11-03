def topological_sort(jobs, deps):
    job_graph = create_graph(jobs, deps)
    return get_ordered_jobs(job_graph)


def create_graph(jobs, deps):
    """Create graph of jobs and add dependencies to every job node"""
    graph = JobGraph(jobs)
    for prereq, job in deps:
        graph.add_prereq(job, prereq)
    return graph


def get_ordered_jobs(graph):
    ordered_jobs = []
    nodes = graph.nodes
    while len(nodes):
        node = nodes.pop()
        print(node.job)
        contains_cycle = depth_first_search(node, ordered_jobs)
        if contains_cycle:
            return []
    return ordered_jobs


def depth_first_search(node, ordered_jobs):
    print(node.job)
    if node.visited:
        return False  # Node already processed
    if node.visiting:
        return True  # Cycle is detected
    node.visiting = True
    # Process all prerequisite nodes
    for prereq_node in node.prereqs:
        contains_cycle = depth_first_search(prereq_node, ordered_jobs)
        if contains_cycle:
            return True
    node.visited = True  # Mark node as processed
    node.visiting = False  # Finished processing the node
    ordered_jobs.append(node.job)
    print(ordered_jobs)
    return False


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []  # list of job nodes
        self.graph = {}  # Map job idx to job node
        for job in jobs:
            self.add_node(job)

    def add_prereq(self, job, prereq):
        job_node = self.get_node(job)
        # Every node keeps track on its prerequisites
        prereq_node = self.get_node(prereq)
        job_node.prereqs.append(prereq_node)

    def add_node(self, job):
        # update graph with a new node
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def get_node(self, job):
        if job not in self.graph:
            self.add_node(job)
        return self.graph[job]


class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visiting = False
        self.visited = False
