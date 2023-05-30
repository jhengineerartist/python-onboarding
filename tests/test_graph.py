import unittest
import logging
import logging.config
from os import path
from collections import namedtuple
from datastructures.graph import DirectedGraph, Node, DirectedEdge

TestCaseData = namedtuple(
    "TestCaseData", "graph orig_node_id dest_node_id can_path expected_path")

# Global logger init
log_file_path = path.join(path.dirname(
    path.abspath(__file__)), 'testlogging.conf')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger('testlogger')


class TestDirectedGraph(unittest.TestCase):
    def setUp(self):
        self.graph_forked = DirectedGraph()
        self.graph_circular = DirectedGraph()
        self.graph_split = DirectedGraph()

        # Forked Graph
        self.graph_forked.add_node("A")
        self.graph_forked.add_node("B")
        self.graph_forked.add_node("C")
        self.graph_forked.add_node("D")

        self.graph_forked.add_edge("A", "B", 1)
        self.graph_forked.add_edge("A", "C", 1)
        self.graph_forked.add_edge("B", "D", 1)
        self.graph_forked.add_edge("C", "D", 1)

        # Circular Graph
        self.graph_circular.add_node("A")
        self.graph_circular.add_node("B")
        self.graph_circular.add_node("C")
        self.graph_circular.add_node("D")

        self.graph_circular.add_edge("A", "B", 1)
        self.graph_circular.add_edge("B", "C", 1)
        self.graph_circular.add_edge("C", "D", 1)
        self.graph_circular.add_edge("D", "A", 1)

        # Not Fully Connected Graph
        self.graph_split.add_node("A")
        self.graph_split.add_node("B")
        self.graph_split.add_node("C")
        self.graph_split.add_node("D")
        self.graph_split.add_node("E")

        self.graph_split.add_edge("A", "B", 1)
        self.graph_split.add_edge("B", "C", 1)
        self.graph_split.add_edge("C", "A", 1)
        self.graph_split.add_edge("D", "E", 1)

    def test_directed_graph(self):
        graph_table = {"forked": self.graph_forked,
                       "circ": self.graph_circular,
                       "split": self.graph_split}

        test_cases = \
            [TestCaseData("forked", "A", "B", True,  ["A", "B", "C", "D"]),
             TestCaseData("forked", "B", "D", True,  ["B", "D"]),
             TestCaseData("forked", "A", "A", True,  ["A"]),
             TestCaseData("forked", "B", "A", False, []),
             TestCaseData("forked", "A", "E", False, []),
             TestCaseData("circ",   "A", "D", True,  ["A", "B", "C", "D"]),
             TestCaseData("circ",   "C", "A", True,  ["C", "D", "A", "B"]),
             TestCaseData("split",  "A", "E", False, []),
             TestCaseData("split",  "A", "C", True,  ["A", "B", "C"]),
             TestCaseData("split",  "D", "E", True,  ["D", "E"])]

        for test_case in test_cases:
            graph_name, o_id, d_id, expect_can_path, expected_path = test_case

            logging.info(
                f'TestCase: Graph:{graph_name}, o={o_id}, d={d_id}, can_path={expect_can_path}, exp_path={expected_path}')

            can_path, bfs_path = graph_table[graph_name].bfs_path_to_node(
                o_id, d_id)

            logging.info(
                f'{can_path, bfs_path}= {graph_name}.bfs_path_to_node({o_id}, {d_id})')

            self.assert_(can_path == expect_can_path)
            if (expect_can_path):
                self.assert_(bfs_path == expected_path)
