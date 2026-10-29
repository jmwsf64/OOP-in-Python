import json
import os
import shutil
import sys

import nbformat as nbf
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QTreeWidget,
    QTreeWidgetItem,
    QWidget,
)


class Main(QMainWindow):
    """
    Object-Oriented Programming Lecture control program
    """

    # ==================================================================================================================
    #                                                                                                       init methods
    # ==================================================================================================================
    def __init__(self):
        super().__init__()

        # window properties
        self.setWindowTitle("OOP Lecture")
        self.layout = QGridLayout()  # type: ignore
        self.setMinimumHeight(650)

        # shortcuts
        menu = self.menuBar()
        assert menu is not None
        fileMenu = menu.addMenu("&File")

        rstAct = QAction("Reset Lecture", self)
        rstAct.setShortcut("Ctrl+r")
        rstAct.triggered.connect(self.reset)
        assert fileMenu is not None
        fileMenu.addAction(rstAct)

        # functional attributes
        self.write_code = ""
        self.write_markdown = ""
        self.write_file = "oopDemo.py"
        self.write_shared_file = ""

        # central widget and layout
        widget = QWidget()
        widget.setLayout(self.layout)  # type: ignore
        self.setCentralWidget(widget)

        # lecture progress json file
        self.progressFile = "place.json"
        if not os.path.exists(self.progressFile):
            with open(self.progressFile, "w", newline="\n") as f:
                json.dump(
                    {
                        "0": {
                            "expanded": True,
                            "children": {
                                "0": False,
                                "1": False,
                            },
                        },
                        "1": {
                            "expanded": False,
                            "children": {
                                "0": False,
                                "1": False,
                                "2": False,
                                "3": False,
                                "4": False,
                                "5": False,
                                "6": False,
                                "7": False,
                            },
                        },
                        "2": {
                            "expanded": False,
                            "children": {
                                "0": False,
                                "1": False,
                                "2": False,
                                "3": False,
                                "4": False,
                                "5": False,
                                "6": False,
                                "7": False,
                                "8": False,
                            },
                        },
                        "3": {
                            "expanded": False,
                            "children": {
                                "0": False,
                                "1": False,
                                "2": False,
                                "3": False,
                                "4": False,
                                "5": False,
                                "6": False,
                                "7": False,
                                "8": False,
                                "9": False,
                                "10": False,
                                "11": False,
                                "12": False,
                            },
                        },
                        "4": {
                            "expanded": False,
                            "children": {
                                "0": False,
                                "1": False,
                                "2": False,
                                "3": False,
                                "4": False,
                                "5": False,
                                "6": False,
                                "7": False,
                                "8": False,
                                "9": False,
                                "10": False,
                                "11": False,
                                "12": False,
                                "13": False,
                            },
                        },
                        "5": {
                            "expanded": False,
                            "children": {
                                "0": False,
                                "1": False,
                                "2": False,
                                "3": False,
                                "4": False,
                                "5": False,
                                "6": False,
                            },
                        },
                        "6": {
                            "expanded": False,
                            "children": {
                                "0": False,
                                "1": False,
                                "2": False,
                                "3": False,
                                "4": False,
                                "5": False,
                                "6": False,
                                "7": False,
                                "8": False,
                                "9": False,
                                "10": False,
                            },
                        },
                        "7": {
                            "expanded": False,
                            "children": {
                                "0": False,
                                "1": False,
                                "2": False,
                                "3": False,
                                "4": False,
                                "5": False,
                                "6": False,
                                "7": False,
                            },
                        },
                        "8": {
                            "expanded": False,
                            "children": {
                                "0": False,
                                "1": False,
                                "2": False,
                                "3": False,
                                "4": False,
                            },
                        },
                        "9": {
                            "expanded": False,
                            "childred": {
                                "0": False,
                                "1": False,
                                "2": False,
                                "3": False,
                                "4": False,
                                "5": False,
                                "6": False,
                                "7": False,
                                "8": False,
                            },
                        },
                    },
                    f,
                    indent="\t",
                )
        with open(self.progressFile, "r") as f:
            self.progressDict = json.load(f)

        # create tree and set properties
        self.tree = QTreeWidget()
        self.tree.header().hide()  # type: ignore
        self.tree.itemClicked.connect(self.itemSelected)
        self.layout.addWidget(self.tree)  # type: ignore

        # top level items
        self.topLevel0 = QTreeWidgetItem(self.tree)
        self.topLevel1 = QTreeWidgetItem(self.tree)
        self.topLevel2 = QTreeWidgetItem(self.tree)
        self.topLevel3 = QTreeWidgetItem(self.tree)
        self.topLevel4 = QTreeWidgetItem(self.tree)
        self.topLevel5 = QTreeWidgetItem(self.tree)
        self.topLevel6 = QTreeWidgetItem(self.tree)
        self.topLevel7 = QTreeWidgetItem(self.tree)
        self.topLevel8 = QTreeWidgetItem(self.tree)
        self.topLevel9 = QTreeWidgetItem(self.tree)

        # top level 0 children
        self.topLevel0_Child0 = QTreeWidgetItem(self.topLevel0)
        self.topLevel0_Child1 = QTreeWidgetItem(self.topLevel0)

        # top level 1 children
        self.topLevel1_Child0 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child1 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child2 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child3 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child4 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child5 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child6 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child7 = QTreeWidgetItem(self.topLevel1)

        # top level 2 children
        self.topLevel2_Child0 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child1 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child2 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child3 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child4 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child5 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child6 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child7 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child8 = QTreeWidgetItem(self.topLevel2)

        # top level 3 children
        self.topLevel3_Child0 = QTreeWidgetItem(self.topLevel3)
        self.topLevel3_Child1 = QTreeWidgetItem(self.topLevel3)
        self.topLevel3_Child2 = QTreeWidgetItem(self.topLevel3)
        self.topLevel3_Child3 = QTreeWidgetItem(self.topLevel3)
        self.topLevel3_Child4 = QTreeWidgetItem(self.topLevel3)
        self.topLevel3_Child5 = QTreeWidgetItem(self.topLevel3)
        self.topLevel3_Child6 = QTreeWidgetItem(self.topLevel3)
        self.topLevel3_Child7 = QTreeWidgetItem(self.topLevel3)
        self.topLevel3_Child8 = QTreeWidgetItem(self.topLevel3)
        self.topLevel3_Child9 = QTreeWidgetItem(self.topLevel3)
        self.topLevel3_Child10 = QTreeWidgetItem(self.topLevel3)
        self.topLevel3_Child11 = QTreeWidgetItem(self.topLevel3)
        self.topLevel3_Child12 = QTreeWidgetItem(self.topLevel3)

        # top level 4 children
        self.topLevel4_Child0 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child1 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child2 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child3 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child4 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child5 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child6 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child7 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child8 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child9 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child10 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child11 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child12 = QTreeWidgetItem(self.topLevel4)
        self.topLevel4_Child13 = QTreeWidgetItem(self.topLevel4)

        # top level 5 children
        self.topLevel5_Child0 = QTreeWidgetItem(self.topLevel5)
        self.topLevel5_Child1 = QTreeWidgetItem(self.topLevel5)
        self.topLevel5_Child2 = QTreeWidgetItem(self.topLevel5)
        self.topLevel5_Child3 = QTreeWidgetItem(self.topLevel5)
        self.topLevel5_Child4 = QTreeWidgetItem(self.topLevel5)
        self.topLevel5_Child5 = QTreeWidgetItem(self.topLevel5)
        self.topLevel5_Child6 = QTreeWidgetItem(self.topLevel5)

        # top level 6 children
        self.topLevel6_Child0 = QTreeWidgetItem(self.topLevel6)
        self.topLevel6_Child1 = QTreeWidgetItem(self.topLevel6)
        self.topLevel6_Child2 = QTreeWidgetItem(self.topLevel6)
        self.topLevel6_Child3 = QTreeWidgetItem(self.topLevel6)
        self.topLevel6_Child4 = QTreeWidgetItem(self.topLevel6)
        self.topLevel6_Child5 = QTreeWidgetItem(self.topLevel6)
        self.topLevel6_Child6 = QTreeWidgetItem(self.topLevel6)
        self.topLevel6_Child7 = QTreeWidgetItem(self.topLevel6)
        self.topLevel6_Child8 = QTreeWidgetItem(self.topLevel6)
        self.topLevel6_Child9 = QTreeWidgetItem(self.topLevel6)
        self.topLevel6_Child10 = QTreeWidgetItem(self.topLevel6)

        # top level 7 children
        self.topLevel7_Child0 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child1 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child2 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child3 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child4 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child5 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child6 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child7 = QTreeWidgetItem(self.topLevel7)

        # top level 8 children
        self.topLevel8_Child0 = QTreeWidgetItem(self.topLevel8)
        self.topLevel8_Child1 = QTreeWidgetItem(self.topLevel8)
        self.topLevel8_Child2 = QTreeWidgetItem(self.topLevel8)

        # top level 9 children
        self.topLevel9_Child0 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child1 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child2 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child3 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child4 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child5 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child6 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child7 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child8 = QTreeWidgetItem(self.topLevel9)

        # init methods
        self.initTreeTopLevel()
        self.initTopLevel0Children()
        self.initTopLevel1Children()
        self.initTopLevel2Children()
        self.initTopLevel3Children()
        self.initTopLevel4Children()
        self.initTopLevel5Children()
        self.initTopLevel6Children()
        self.initTopLevel7Children()
        self.initTopLevel8Children()
        self.initTopLevel9Children()

    def initTreeTopLevel(self):

        self.topLevel0.setText(0, "How to set up a Class")
        self.topLevel0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel0.setExpanded(self.progressDict["0"]["expanded"])
        self.tree.addTopLevelItem(self.topLevel0)

        self.topLevel1.setText(0, "Class Attributes")
        self.topLevel1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.setExpanded(self.progressDict["1"]["expanded"])
        self.tree.addTopLevelItem(self.topLevel1)

        self.topLevel2.setText(0, "Methods")
        self.topLevel2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.setExpanded(self.progressDict["2"]["expanded"])
        self.tree.addTopLevelItem(self.topLevel2)

        self.topLevel3.setText(0, "__init__() and Instance Attributes")
        self.topLevel3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.setExpanded(self.progressDict["3"]["expanded"])
        self.tree.addTopLevelItem(self.topLevel3)

        self.topLevel4.setText(0, "Subclassing")
        self.topLevel4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.setExpanded(self.progressDict["4"]["expanded"])
        self.tree.addTopLevelItem(self.topLevel4)

        self.topLevel5.setText(0, "Dunder Methods")
        self.topLevel5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.setExpanded(self.progressDict["5"]["expanded"])
        self.tree.addTopLevelItem(self.topLevel5)

        self.topLevel6.setText(0, "Objects, Objects, Everywhere")
        self.topLevel6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.setExpanded(self.progressDict["6"]["expanded"])
        self.tree.addTopLevelItem(self.topLevel6)

        self.topLevel7.setText(0, "Creating a new array data type")
        self.topLevel7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.setExpanded(self.progressDict["7"]["expanded"])
        self.tree.addTopLevelItem(self.topLevel7)

        self.topLevel8.setText(0, "Miscellaneous")
        self.topLevel8.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel8.setExpanded(self.progressDict["8"]["expanded"])
        self.tree.addTopLevelItem(self.topLevel8)

        self.topLevel9.setText(0, "PyQt6")
        self.topLevel9.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.setExpanded(self.progressDict["9"]["expanded"])
        self.tree.addTopLevelItem(self.topLevel9)

    def initTopLevel0Children(self):

        self.topLevel0_Child0.setText(0, "Basic Class")
        if self.progressDict["0"]["children"]["0"]:
            self.topLevel0_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel0_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel0.addChild(self.topLevel0_Child0)

        self.topLevel0_Child1.setText(0, "Initialize an object")
        if self.progressDict["0"]["children"]["1"]:
            self.topLevel0_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel0_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel0.addChild(self.topLevel0_Child1)

        self.update_topLevel0_checkbox()

    def initTopLevel1Children(self):

        self.topLevel1_Child0.setText(0, "Create a Class Attribute")
        if self.progressDict["1"]["children"]["0"]:
            self.topLevel1_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child0)

        self.topLevel1_Child1.setText(0, "Accessing Class Attributes")
        if self.progressDict["1"]["children"]["1"]:
            self.topLevel1_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child1)

        self.topLevel1_Child2.setText(0, "Memory Allocation 1")
        if self.progressDict["1"]["children"]["2"]:
            self.topLevel1_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child2)

        self.topLevel1_Child3.setText(0, "Memory Allocation 2")
        if self.progressDict["1"]["children"]["3"]:
            self.topLevel1_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child3)

        self.topLevel1_Child4.setText(0, "Memory Allocation 3")
        if self.progressDict["1"]["children"]["4"]:
            self.topLevel1_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child4)

        self.topLevel1_Child5.setText(0, "Memory Allocation 4")
        if self.progressDict["1"]["children"]["5"]:
            self.topLevel1_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child5)

        self.topLevel1_Child6.setText(0, "Memory Allocation 5")
        if self.progressDict["1"]["children"]["6"]:
            self.topLevel1_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child6)

        self.topLevel1_Child7.setText(0, "Private and Protected Attributes")
        if self.progressDict["1"]["children"]["7"]:
            self.topLevel1_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child7)

        self.update_topLevel1_checkbox()

    def initTopLevel2Children(self):

        self.topLevel2_Child0.setText(0, "Define a Method")
        if self.progressDict["2"]["children"]["0"]:
            self.topLevel2_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child0)

        self.topLevel2_Child1.setText(0, "Run a Method")
        if self.progressDict["2"]["children"]["1"]:
            self.topLevel2_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child1)

        self.topLevel2_Child2.setText(0, "Methods Operation 1")
        if self.progressDict["2"]["children"]["2"]:
            self.topLevel2_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child2)

        self.topLevel2_Child3.setText(0, "Methods Operation 2")
        if self.progressDict["2"]["children"]["3"]:
            self.topLevel2_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child3)

        self.topLevel2_Child4.setText(0, "Methods Operation 3")
        if self.progressDict["2"]["children"]["4"]:
            self.topLevel2_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child4)

        self.topLevel2_Child5.setText(0, "Methods Operation 4")
        if self.progressDict["2"]["children"]["5"]:
            self.topLevel2_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child5)

        self.topLevel2_Child6.setText(0, "Static Methods")
        if self.progressDict["2"]["children"]["6"]:
            self.topLevel2_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child6)

        self.topLevel2_Child7.setText(0, "Assigning New Methods")
        if self.progressDict["2"]["children"]["7"]:
            self.topLevel2_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child7)

        self.topLevel2_Child8.setText(0, "Private and Protected Methods")
        if self.progressDict["2"]["children"]["8"]:
            self.topLevel2_Child8.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child8.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child8)

        self.update_topLevel2_checkbox()

    def initTopLevel3Children(self):

        self.topLevel3_Child0.setText(0, "__init__() 1")
        if self.progressDict["3"]["children"]["0"]:
            self.topLevel3_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child0)

        self.topLevel3_Child1.setText(0, "__init__() 2")
        if self.progressDict["3"]["children"]["1"]:
            self.topLevel3_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child1)

        self.topLevel3_Child2.setText(0, "__init__() 3")
        if self.progressDict["3"]["children"]["2"]:
            self.topLevel3_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child2)

        self.topLevel3_Child3.setText(0, "Instance Attributes")
        if self.progressDict["3"]["children"]["3"]:
            self.topLevel3_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child3)

        self.topLevel3_Child4.setText(0, "__init__() 4")
        if self.progressDict["3"]["children"]["4"]:
            self.topLevel3_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child4)

        self.topLevel3_Child5.setText(0, "__init__() 5")
        if self.progressDict["3"]["children"]["5"]:
            self.topLevel3_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child5)

        self.topLevel3_Child6.setText(0, "__init__() 6")
        if self.progressDict["3"]["children"]["6"]:
            self.topLevel3_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child6)

        self.topLevel3_Child7.setText(0, "More Memory Allocation 1")
        if self.progressDict["3"]["children"]["7"]:
            self.topLevel3_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child7)

        self.topLevel3_Child8.setText(0, "More Memory Allocation 2")
        if self.progressDict["3"]["children"]["8"]:
            self.topLevel3_Child8.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child8.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child8)

        self.topLevel3_Child9.setText(0, "More Memory Allocation 3")
        if self.progressDict["3"]["children"]["9"]:
            self.topLevel3_Child9.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child9.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child9)

        self.topLevel3_Child10.setText(0, "More Memory Allocation 4")
        if self.progressDict["3"]["children"]["10"]:
            self.topLevel3_Child10.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child10.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child10)

        self.topLevel3_Child11.setText(0, "More Memory Allocation 5")
        if self.progressDict["3"]["children"]["11"]:
            self.topLevel3_Child11.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child11.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child11)

        self.topLevel3_Child12.setText(0, "More Memory Allocation 6")
        if self.progressDict["3"]["children"]["12"]:
            self.topLevel3_Child12.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child12.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child12)

        self.update_topLevel3_checkbox()

    def initTopLevel4Children(self):

        self.topLevel4_Child0.setText(0, "Basic Child Class 1")
        if self.progressDict["4"]["children"]["0"]:
            self.topLevel4_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child0)

        self.topLevel4_Child1.setText(0, "Basic Child Class 2")
        if self.progressDict["4"]["children"]["1"]:
            self.topLevel4_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child1)

        self.topLevel4_Child2.setText(0, "Basic Child Class 3")
        if self.progressDict["4"]["children"]["2"]:
            self.topLevel4_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child2)

        self.topLevel4_Child3.setText(0, "Basic Child Class 4")
        if self.progressDict["4"]["children"]["3"]:
            self.topLevel4_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child3)

        self.topLevel4_Child4.setText(0, "Inheritance 1")
        if self.progressDict["4"]["children"]["4"]:
            self.topLevel4_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child4)

        self.topLevel4_Child5.setText(0, "Inheritance 2")
        if self.progressDict["4"]["children"]["5"]:
            self.topLevel4_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child5)

        self.topLevel4_Child6.setText(0, "Inheritance 3")
        if self.progressDict["4"]["children"]["6"]:
            self.topLevel4_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child6)

        self.topLevel4_Child7.setText(0, "Child Methods 1")
        if self.progressDict["4"]["children"]["7"]:
            self.topLevel4_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child7)

        self.topLevel4_Child8.setText(0, "Child Methods 2")
        if self.progressDict["4"]["children"]["8"]:
            self.topLevel4_Child8.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child8.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child8)

        self.topLevel4_Child9.setText(0, "Protected vs. Private")
        if self.progressDict["4"]["children"]["9"]:
            self.topLevel4_Child9.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child9.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child9)

        self.topLevel4_Child10.setText(0, "Overriding __init__()")
        if self.progressDict["4"]["children"]["10"]:
            self.topLevel4_Child10.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child10.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child10)

        self.topLevel4_Child11.setText(0, "super().__init__()")
        if self.progressDict["4"]["children"]["11"]:
            self.topLevel4_Child11.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child11.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child11)

        self.topLevel4_Child12.setText(0, "Multilevel Inheritance")
        if self.progressDict["4"]["children"]["12"]:
            self.topLevel4_Child12.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child12.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child12)

        self.topLevel4_Child13.setText(0, "Multiple Inheritance")
        if self.progressDict["4"]["children"]["13"]:
            self.topLevel4_Child13.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child13.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child13)

        self.update_topLevel4_checkbox()

    def initTopLevel5Children(self):

        self.topLevel5_Child0.setText(0, "__init__()")
        if self.progressDict["5"]["children"]["0"]:
            self.topLevel5_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child0)

        self.topLevel5_Child1.setText(0, "Printing an Object 1")
        if self.progressDict["5"]["children"]["1"]:
            self.topLevel5_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child1)

        self.topLevel5_Child2.setText(0, "Printing an Object 2")
        if self.progressDict["5"]["children"]["2"]:
            self.topLevel5_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child2)

        self.topLevel5_Child3.setText(0, "Adding Objects 1")
        if self.progressDict["5"]["children"]["3"]:
            self.topLevel5_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child3)

        self.topLevel5_Child4.setText(0, "Adding Objects 2")
        if self.progressDict["5"]["children"]["4"]:
            self.topLevel5_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child4)

        self.topLevel5_Child5.setText(0, "Adding Objects 3")
        if self.progressDict["5"]["children"]["5"]:
            self.topLevel5_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child5)

        self.topLevel5_Child6.setText(0, "Other Dunder Methods")
        if self.progressDict["5"]["children"]["6"]:
            self.topLevel5_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child6)

        self.update_topLevel5_checkbox()

    def initTopLevel6Children(self):

        self.topLevel6_Child0.setText(0, "And")
        if self.progressDict["6"]["children"]["0"]:
            self.topLevel6_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child0)

        self.topLevel6_Child1.setText(0, "I")
        if self.progressDict["6"]["children"]["1"]:
            self.topLevel6_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child1)

        self.topLevel6_Child2.setText(0, "Mean")
        if self.progressDict["6"]["children"]["2"]:
            self.topLevel6_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child2)

        self.topLevel6_Child3.setText(0, "Everywhere")
        if self.progressDict["6"]["children"]["3"]:
            self.topLevel6_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child3)

        self.topLevel6_Child4.setText(0, "Quiz 1")
        if self.progressDict["6"]["children"]["4"]:
            self.topLevel6_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child4)

        self.topLevel6_Child5.setText(0, "Quiz 2")
        if self.progressDict["6"]["children"]["5"]:
            self.topLevel6_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child5)

        self.topLevel6_Child6.setText(0, "Quiz 3")
        if self.progressDict["6"]["children"]["6"]:
            self.topLevel6_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child6)

        self.topLevel6_Child7.setText(0, "Quiz 4")
        if self.progressDict["6"]["children"]["7"]:
            self.topLevel6_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child7)

        self.topLevel6_Child8.setText(0, "Quiz 5")
        if self.progressDict["6"]["children"]["8"]:
            self.topLevel6_Child8.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child8.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child8)

        self.topLevel6_Child9.setText(0, "Quiz 6")
        if self.progressDict["6"]["children"]["9"]:
            self.topLevel6_Child9.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child9.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child9)

        self.topLevel6_Child10.setText(0, "Quiz 7")
        if self.progressDict["6"]["children"]["10"]:
            self.topLevel6_Child10.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child10.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child10)

        self.update_topLevel6_checkbox()

    def initTopLevel7Children(self):

        self.topLevel7_Child0.setText(0, "Lists 1")
        if self.progressDict["7"]["children"]["0"]:
            self.topLevel7_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child0)

        self.topLevel7_Child1.setText(0, "Lists 2")
        if self.progressDict["7"]["children"]["1"]:
            self.topLevel7_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child1)

        self.topLevel7_Child2.setText(0, '"array" class 1')
        if self.progressDict["7"]["children"]["2"]:
            self.topLevel7_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child2)

        self.topLevel7_Child3.setText(0, '"array" class 2')
        if self.progressDict["7"]["children"]["3"]:
            self.topLevel7_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child3)

        self.topLevel7_Child4.setText(0, '"array" class 3')
        if self.progressDict["7"]["children"]["4"]:
            self.topLevel7_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child4)

        self.topLevel7_Child5.setText(0, '"array" class 4')
        if self.progressDict["7"]["children"]["5"]:
            self.topLevel7_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child5)

        self.topLevel7_Child6.setText(0, '"array" class 5')
        if self.progressDict["7"]["children"]["6"]:
            self.topLevel7_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child6)

        self.topLevel7_Child7.setText(0, '"array" class 6')
        if self.progressDict["7"]["children"]["7"]:
            self.topLevel7_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child7)

        self.update_topLevel7_checkbox()

    def initTopLevel8Children(self):

        self.topLevel8_Child0.setText(0, "Inner Classes")
        if self.progressDict["8"]["children"]["0"]:
            self.topLevel8_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel8_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel8.addChild(self.topLevel8_Child0)

        self.topLevel8_Child1.setText(0, "JSON Serialization")
        if self.progressDict["8"]["children"]["1"]:
            self.topLevel8_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel8_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel8.addChild(self.topLevel8_Child1)

        self.topLevel8_Child2.setText(0, "Pickle Serialization")
        if self.progressDict["8"]["children"]["2"]:
            self.topLevel8_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel8_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel8.addChild(self.topLevel8_Child2)

        self.update_topLevel8_checkbox()

    def initTopLevel9Children(self):

        self.topLevel9_Child0.setText(0, "Create an Application")
        if self.progressDict["9"]["children"]["0"]:
            self.topLevel9_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child0)

        self.topLevel9_Child1.setText(0, "Add a Widget")
        if self.progressDict["9"]["children"]["1"]:
            self.topLevel9_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child1)

        self.topLevel9_Child2.setText(0, "Connect Button Signals")
        if self.progressDict["9"]["children"]["2"]:
            self.topLevel9_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child2)

        self.topLevel9_Child3.setText(0, "Long Running Task 1")
        if self.progressDict["9"]["children"]["3"]:
            self.topLevel9_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child3)

        self.topLevel9_Child4.setText(0, "Long Running Task 2")
        if self.progressDict["9"]["children"]["4"]:
            self.topLevel9_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child4)

        self.topLevel9_Child5.setText(0, "Long Running Task 3")
        if self.progressDict["9"]["children"]["5"]:
            self.topLevel9_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child5)

        self.topLevel9_Child6.setText(0, "Emit Error Signals to Main Thread")
        if self.progressDict["9"]["children"]["6"]:
            self.topLevel9_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child6)

        self.topLevel9_Child7.setText(0, "Other GUI Elements")
        if self.progressDict["9"]["children"]["7"]:
            self.topLevel9_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child7)

        self.topLevel9_Child8.setText(0, "Subclassing GUI Elements")
        if self.progressDict["9"]["children"]["8"]:
            self.topLevel9_Child8.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child8.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child8)

        self.update_topLevel9_checkbox()

    # ==================================================================================================================
    #                                                                                                    rewrite methods
    # ==================================================================================================================
    def itemSelected(self, selection):

        # Section 0 - How to set up a Class
        if selection == self.topLevel0_Child0:
            if self.topLevel0_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel0_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["0"]["children"]["0"] = True
            self.update_topLevel0_checkbox()
            self.topLevel0_Child0_text()
            self.write_shared_file = "scripts/section0_item0.ipynb"
            self.writeText()
        elif selection == self.topLevel0_Child1:
            if self.topLevel0_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel0_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["0"]["children"]["1"] = True
            self.update_topLevel0_checkbox()
            self.topLevel0_Child1_text()
            self.write_shared_file = "scripts/section0_item1.ipynb"
            self.writeText()

        # Section 1 - Class Attributes
        elif selection == self.topLevel1_Child0:
            if self.topLevel1_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["1"]["children"]["0"] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child0_text()
            self.write_shared_file = "scripts/section1_item0.ipynb"
            self.writeText()
        elif selection == self.topLevel1_Child1:
            if self.topLevel1_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["1"]["children"]["1"] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child1_text()
            self.write_shared_file = "scripts/section1_item1.ipynb"
            self.writeText()
        elif selection == self.topLevel1_Child2:
            if self.topLevel1_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["1"]["children"]["2"] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child2_text()
            self.write_shared_file = "scripts/section1_item2.ipynb"
            self.writeText()
        elif selection == self.topLevel1_Child3:
            if self.topLevel1_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["1"]["children"]["3"] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child3_text()
            self.write_shared_file = "scripts/section1_item3.ipynb"
            self.writeText()
        elif selection == self.topLevel1_Child4:
            if self.topLevel1_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["1"]["children"]["4"] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child4_text()
            self.write_shared_file = "scripts/section1_item4.ipynb"
            self.writeText()
        elif selection == self.topLevel1_Child5:
            if self.topLevel1_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["1"]["children"]["5"] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child5_text()
            self.write_shared_file = "scripts/section1_item5.ipynb"
            self.writeText()
        elif selection == self.topLevel1_Child6:
            if self.topLevel1_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["1"]["children"]["6"] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child6_text()
            self.write_shared_file = "scripts/section1_item6.ipynb"
            self.writeText()
        elif selection == self.topLevel1_Child7:
            if self.topLevel1_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["1"]["children"]["7"] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child7_text()
            self.write_shared_file = "scripts/section1_item7.ipynb"
            self.writeText()

        # Section 2 - Methods
        elif selection == self.topLevel2_Child0:
            if self.topLevel2_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["2"]["children"]["0"] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child0_text()
            self.write_shared_file = "scripts/section2_item0.ipynb"
            self.writeText()
        elif selection == self.topLevel2_Child1:
            if self.topLevel2_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["2"]["children"]["1"] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child1_text()
            self.write_shared_file = "scripts/section2_item1.ipynb"
            self.writeText()
        elif selection == self.topLevel2_Child2:
            if self.topLevel2_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["2"]["children"]["2"] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child2_text()
            self.write_shared_file = "scripts/section2_item2.ipynb"
            self.writeText()
        elif selection == self.topLevel2_Child3:
            if self.topLevel2_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["2"]["children"]["3"] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child3_text()
            self.write_shared_file = "scripts/section2_item3.ipynb"
            self.writeText()
        elif selection == self.topLevel2_Child4:
            if self.topLevel2_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["2"]["children"]["4"] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child4_text()
            self.write_shared_file = "scripts/section2_item4.ipynb"
            self.writeText()
        elif selection == self.topLevel2_Child5:
            if self.topLevel2_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["2"]["children"]["5"] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child5_text()
            self.write_shared_file = "scripts/section2_item5.ipynb"
            self.writeText()
        elif selection == self.topLevel2_Child6:
            if self.topLevel2_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["2"]["children"]["6"] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child6_text()
            self.write_shared_file = "scripts/section2_item6.ipynb"
            self.writeText()
        elif selection == self.topLevel2_Child7:
            if self.topLevel2_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["2"]["children"]["7"] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child7_text()
            self.write_shared_file = "scripts/section2_item7.ipynb"
            self.writeText()
        elif selection == self.topLevel2_Child8:
            if self.topLevel2_Child8.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child8.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["2"]["children"]["8"] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child8_text()
            self.write_shared_file = "scripts/section2_item8.ipynb"
            self.writeText()

        # Section 3 - __init__() and Instance Attributes
        elif selection == self.topLevel3_Child0:
            if self.topLevel3_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["0"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child0_text()
            self.write_shared_file = "scripts/section3_item0.ipynb"
            self.writeText()
        elif selection == self.topLevel3_Child1:
            if self.topLevel3_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["1"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child1_text()
            self.write_shared_file = "scripts/section3_item1.ipynb"
            self.writeText()
        elif selection == self.topLevel3_Child2:
            if self.topLevel3_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["2"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child2_text()
            self.write_shared_file = "scripts/section3_item2.ipynb"
            self.writeText()
        elif selection == self.topLevel3_Child3:
            if self.topLevel3_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["3"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child3_text()
            self.write_shared_file = "scripts/section3_item3.ipynb"
            self.writeText()
        elif selection == self.topLevel3_Child4:
            if self.topLevel3_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["4"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child4_text()
            self.write_shared_file = "scripts/section3_item4.ipynb"
            self.writeText()
        elif selection == self.topLevel3_Child5:
            if self.topLevel3_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["5"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child5_text()
            self.write_shared_file = "scripts/section3_item5.ipynb"
            self.writeText()
        elif selection == self.topLevel3_Child6:
            if self.topLevel3_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["6"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child6_text()
            self.write_shared_file = "scripts/section3_item6.ipynb"
            self.writeText()
        elif selection == self.topLevel3_Child7:
            if self.topLevel3_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["7"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child7_text()
            self.write_shared_file = "scripts/section3_item7.ipynb"
            self.writeText()
        elif selection == self.topLevel3_Child8:
            if self.topLevel3_Child8.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child8.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["8"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child8_text()
            self.write_shared_file = "scripts/section3_item8.ipynb"
            self.writeText()
        elif selection == self.topLevel3_Child9:
            if self.topLevel3_Child9.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child9.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["9"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child9_text()
            self.write_shared_file = "scripts/section3_item9.ipynb"
            self.writeText()
        elif selection == self.topLevel3_Child10:
            if self.topLevel3_Child10.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child10.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["10"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child10_text()
            self.write_shared_file = "scripts/section3_item10.ipynb"
            self.writeText()
        elif selection == self.topLevel3_Child11:
            if self.topLevel3_Child11.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child11.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["11"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child11_text()
            self.write_shared_file = "scripts/section3_item11.ipynb"
            self.writeText()
        elif selection == self.topLevel3_Child12:
            if self.topLevel3_Child12.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child12.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["3"]["children"]["12"] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child12_text()
            self.write_shared_file = "scripts/section3_item12.ipynb"
            self.writeText()

        # Section 4 - Parents and Children
        elif selection == self.topLevel4_Child0:
            if self.topLevel4_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["0"] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child0_text()
            self.write_shared_file = "scripts/section4_item0.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child1:
            if self.topLevel4_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["1"] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child1_text()
            self.write_shared_file = "scripts/section4_item1.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child2:
            if self.topLevel4_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["2"] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child2_text()
            self.write_shared_file = "scripts/section4_item2.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child3:
            if self.topLevel4_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["3"] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child3_text()
            self.write_shared_file = "scripts/section4_item3.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child4:
            if self.topLevel4_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["4"] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child4_text()
            self.write_shared_file = "scripts/section4_item4.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child5:
            if self.topLevel4_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["5"] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child5_text()
            self.write_shared_file = "scripts/section4_item5.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child6:
            if self.topLevel4_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["6"] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child6_text()
            self.write_shared_file = "scripts/section4_item6.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child7:
            if self.topLevel4_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["7"] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child7_text()
            self.write_shared_file = "scripts/section4_item7.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child8:
            if self.topLevel4_Child8.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child8.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["8"] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child8_text()
            self.write_shared_file = "scripts/section4_item8.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child9:
            if self.topLevel4_Child9.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child9.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["9"] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child9_text()
            self.write_shared_file = "scripts/section4_item9.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child10:
            if self.topLevel4_Child10.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child10.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["10"] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child10_text()
            self.write_shared_file = "scripts/section4_item10.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child11:
            if self.topLevel4_Child11.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child11.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["11"] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child11_text()
            self.write_shared_file = "scripts/section4_item11.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child12:
            if self.topLevel4_Child12.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child12.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["12"] = True
            self.update_topLevel8_checkbox()
            self.topLevel4_Child12_text()
            self.write_shared_file = "scripts/section4_item12.ipynb"
            self.writeText()
        elif selection == self.topLevel4_Child13:
            if self.topLevel4_Child13.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child13.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["4"]["children"]["13"] = True
            self.update_topLevel8_checkbox()
            self.topLevel4_Child13_text()
            self.write_shared_file = "scripts/section4_item13.ipynb"
            self.writeText()

        # Section 5 - Dunder Methods
        elif selection == self.topLevel5_Child0:
            if self.topLevel5_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["5"]["children"]["0"] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child0_text()
            self.write_shared_file = "scripts/section5_item0.ipynb"
            self.writeText()
        elif selection == self.topLevel5_Child1:
            if self.topLevel5_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["5"]["children"]["1"] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child1_text()
            self.write_shared_file = "scripts/section5_item1.ipynb"
            self.writeText()
        elif selection == self.topLevel5_Child2:
            if self.topLevel5_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["5"]["children"]["2"] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child2_text()
            self.write_shared_file = "scripts/section5_item2.ipynb"
            self.writeText()
        elif selection == self.topLevel5_Child3:
            if self.topLevel5_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["5"]["children"]["3"] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child3_text()
            self.write_shared_file = "scripts/section5_item3.ipynb"
            self.writeText()
        elif selection == self.topLevel5_Child4:
            if self.topLevel5_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["5"]["children"]["4"] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child4_text()
            self.write_shared_file = "scripts/section5_item4.ipynb"
            self.writeText()
        elif selection == self.topLevel5_Child5:
            if self.topLevel5_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["5"]["children"]["5"] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child5_text()
            self.write_shared_file = "scripts/section5_item5.ipynb"
            self.writeText()
        elif selection == self.topLevel5_Child6:
            if self.topLevel5_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["5"]["children"]["6"] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child6_text()
            self.write_shared_file = "scripts/section5_item6.ipynb"
            self.writeText()

        # Section 6 - Object, Objects, Everywhere
        elif selection == self.topLevel6_Child0:
            if self.topLevel6_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["6"]["children"]["0"] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child0_text()
            self.write_shared_file = "scripts/section6_item0.ipynb"
            self.writeText()
        elif selection == self.topLevel6_Child1:
            if self.topLevel6_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["6"]["children"]["1"] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child1_text()
            self.write_shared_file = "scripts/section6_item1.ipynb"
            self.writeText()
        elif selection == self.topLevel6_Child2:
            if self.topLevel6_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["6"]["children"]["2"] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child2_text()
            self.write_shared_file = "scripts/section6_item2.ipynb"
            self.writeText()
        elif selection == self.topLevel6_Child3:
            if self.topLevel6_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["6"]["children"]["3"] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child3_text()
            self.write_shared_file = "scripts/section6_item3.ipynb"
            self.writeText()
        elif selection == self.topLevel6_Child4:
            if self.topLevel6_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["6"]["children"]["4"] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child4_text()
            self.write_shared_file = "scripts/section6_item4.ipynb"
            self.writeText()
        elif selection == self.topLevel6_Child5:
            if self.topLevel6_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["6"]["children"]["5"] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child5_text()
            self.write_shared_file = "scripts/section6_item5.ipynb"
            self.writeText()
        elif selection == self.topLevel6_Child6:
            if self.topLevel6_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["6"]["children"]["6"] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child6_text()
            self.write_shared_file = "scripts/section6_item6.ipynb"
            self.writeText()
        elif selection == self.topLevel6_Child7:
            if self.topLevel6_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["6"]["children"]["7"] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child7_text()
            self.write_shared_file = "scripts/section6_item7.ipynb"
            self.writeText()
        elif selection == self.topLevel6_Child8:
            if self.topLevel6_Child8.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child8.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["6"]["children"]["8"] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child8_text()
            self.write_shared_file = "scripts/section6_item8.ipynb"
            self.writeText()
        elif selection == self.topLevel6_Child9:
            if self.topLevel6_Child9.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child9.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["6"]["children"]["9"] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child9_text()
            self.write_shared_file = "scripts/section6_item9.ipynb"
            self.writeText()
        elif selection == self.topLevel6_Child10:
            if self.topLevel6_Child10.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child10.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["6"]["children"]["10"] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child10_text()
            self.write_shared_file = "scripts/section6_item10.ipynb"
            self.writeText()

        # Section 7 - Create a new array data type
        elif selection == self.topLevel7_Child0:
            if self.topLevel7_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["7"]["children"]["0"] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child0_text()
            self.write_shared_file = "scripts/section7_item0.ipynb"
            self.writeText()
        elif selection == self.topLevel7_Child1:
            if self.topLevel7_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["7"]["children"]["1"] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child1_text()
            self.write_shared_file = "scripts/section7_item1.ipynb"
            self.writeText()
        elif selection == self.topLevel7_Child2:
            if self.topLevel7_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["7"]["children"]["2"] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child2_text()
            self.write_shared_file = "scripts/section7_item2.ipynb"
            self.writeText()
        elif selection == self.topLevel7_Child3:
            if self.topLevel7_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["7"]["children"]["3"] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child3_text()
            self.write_shared_file = "scripts/section7_item3.ipynb"
            self.writeText()
        elif selection == self.topLevel7_Child4:
            if self.topLevel7_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["7"]["children"]["4"] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child4_text()
            self.write_shared_file = "scripts/section7_item4.ipynb"
            self.writeText()
        elif selection == self.topLevel7_Child5:
            if self.topLevel7_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["7"]["children"]["5"] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child5_text()
            self.write_shared_file = "scripts/section7_item5.ipynb"
            self.writeText()
        elif selection == self.topLevel7_Child6:
            if self.topLevel7_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["7"]["children"]["6"] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child6_text()
            self.write_shared_file = "scripts/section7_item6.ipynb"
            self.writeText()
        elif selection == self.topLevel7_Child7:
            if self.topLevel7_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["7"]["children"]["7"] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child7_text()
            self.write_shared_file = "scripts/section7_item7.ipynb"
            self.writeText()

        # Section 8 - miscellaneous
        elif selection == self.topLevel8_Child0:
            if self.topLevel8_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel8_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["8"]["children"]["0"] = True
            self.update_topLevel8_checkbox()
            self.topLevel8_Child0_text()
            self.write_shared_file = "scripts/section8_item0.ipynb"
            self.writeText()
        elif selection == self.topLevel8_Child1:
            if self.topLevel8_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel8_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["8"]["children"]["1"] = True
            self.update_topLevel8_checkbox()

            self.topLevel8_Child1a_text()
            self.write_shared_file = "scripts/section8_item1a.ipynb"
            self.writeText()

            self.topLevel8_Child1b_text()
            self.write_shared_file = "scripts/section8_item1b.ipynb"
            self.write_file = "oopDemo-b.py"
            self.writeText()
            self.write_file = "oopDemo.py"
        elif selection == self.topLevel8_Child2:
            if self.topLevel8_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel8_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["8"]["children"]["2"] = True
            self.update_topLevel8_checkbox()

            self.topLevel8_Child2a_text()
            self.write_shared_file = "scripts/section8_item2a.ipynb"
            self.writeText()

            self.topLevel8_Child2b_text()
            self.write_shared_file = "scripts/section8_item2b.ipynb"
            self.write_file = "oopDemo-b.py"
            self.writeText()
            self.write_file = "oopDemo.py"

        # Section 9 - PyQt6
        elif selection == self.topLevel9_Child0:
            if self.topLevel9_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["9"]["children"]["0"] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child0_text()
            self.write_shared_file = "scripts/section9_item0.ipynb"
            self.writeText()
        elif selection == self.topLevel9_Child1:
            if self.topLevel9_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["9"]["children"]["1"] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child1_text()
            self.write_shared_file = "scripts/section9_item1.ipynb"
            self.writeText()
        elif selection == self.topLevel9_Child2:
            if self.topLevel9_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["9"]["children"]["2"] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child2_text()
            self.write_shared_file = "scripts/section9_item2.ipynb"
            self.writeText()
        elif selection == self.topLevel9_Child3:
            if self.topLevel9_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["9"]["children"]["3"] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child3_text()
            self.write_shared_file = "scripts/section9_item3.ipynb"
            self.writeText()
        elif selection == self.topLevel9_Child4:
            if self.topLevel9_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["9"]["children"]["4"] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child4_text()
            self.write_shared_file = "scripts/section9_item4.ipynb"
            self.writeText()
        elif selection == self.topLevel9_Child5:
            if self.topLevel9_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["9"]["children"]["5"] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child5_text()
            self.write_shared_file = "scripts/section9_item5.ipynb"
            self.writeText()
        elif selection == self.topLevel9_Child6:
            if self.topLevel9_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["9"]["children"]["6"] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child6_text()
            self.write_shared_file = "scripts/section9_item6.ipynb"
            self.writeText()
        elif selection == self.topLevel9_Child7:
            if self.topLevel9_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["9"]["children"]["7"] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child7_text()
            self.write_shared_file = "scripts/section9_item7.ipynb"
            self.writeText()
        elif selection == self.topLevel9_Child8:
            if self.topLevel9_Child8.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child8.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict["9"]["children"]["8"] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child8_text()
            self.write_shared_file = "scripts/section9_item8.ipynb"
            self.writeText()

    def writeText(self):

        # create directory
        os.makedirs("scripts/", exist_ok=True)

        # write demo file
        with open(self.write_file, "w", newline="\n") as f:
            f.write(self.write_code)

        # write shared notebook
        nb = nbf.v4.new_notebook()
        nb["cells"] = [
            nbf.v4.new_markdown_cell(self.write_markdown),
            nbf.v4.new_code_cell(self.write_code),
        ]
        with open(self.write_shared_file, "w", encoding="utf-8", newline="\n") as f:
            nbf.write(nb, f)

        # update progress tracker
        with open(self.progressFile, "w", newline="\n") as f:
            json.dump(self.progressDict, f, indent="\t")

    def reset(self):
        if os.path.exists("scripts/"):
            shutil.rmtree("scripts/", ignore_errors=True)
        self.progressDict = {
            "0": {"expanded": True, "children": {"0": False, "1": False}},
            "1": {
                "expanded": False,
                "children": {
                    "0": False,
                    "1": False,
                    "2": False,
                    "3": False,
                    "4": False,
                    "5": False,
                    "6": False,
                    "7": False,
                },
            },
            "2": {
                "expanded": False,
                "children": {
                    "0": False,
                    "1": False,
                    "2": False,
                    "3": False,
                    "4": False,
                    "5": False,
                    "6": False,
                    "7": False,
                    "8": False,
                },
            },
            "3": {
                "expanded": False,
                "children": {
                    "0": False,
                    "1": False,
                    "2": False,
                    "3": False,
                    "4": False,
                    "5": False,
                    "6": False,
                    "7": False,
                    "8": False,
                    "9": False,
                    "10": False,
                    "11": False,
                    "12": False,
                },
            },
            "4": {
                "expanded": False,
                "children": {
                    "0": False,
                    "1": False,
                    "2": False,
                    "3": False,
                    "4": False,
                    "5": False,
                    "6": False,
                    "7": False,
                    "8": False,
                    "9": False,
                    "10": False,
                    "11": False,
                    "12": False,
                    "13": False,
                },
            },
            "5": {
                "expanded": False,
                "children": {
                    "0": False,
                    "1": False,
                    "2": False,
                    "3": False,
                    "4": False,
                    "5": False,
                    "6": False,
                },
            },
            "6": {
                "expanded": False,
                "children": {
                    "0": False,
                    "1": False,
                    "2": False,
                    "3": False,
                    "4": False,
                    "5": False,
                    "6": False,
                    "7": False,
                    "8": False,
                    "9": False,
                    "10": False,
                },
            },
            "7": {
                "expanded": False,
                "children": {
                    "0": False,
                    "1": False,
                    "2": False,
                    "3": False,
                    "4": False,
                    "5": False,
                    "6": False,
                    "7": False,
                },
            },
            "8": {"expanded": False, "children": {"0": False, "1": False, "2": False}},
            "9": {
                "expanded": False,
                "children": {
                    "0": False,
                    "1": False,
                    "2": False,
                    "3": False,
                    "4": False,
                    "5": False,
                    "6": False,
                    "7": False,
                    "8": False,
                },
            },
        }
        with open(self.progressFile, "w", newline="\n") as f:
            json.dump(self.progressDict, f, indent="\t")
        self.initTreeTopLevel()
        self.initTopLevel0Children()
        self.initTopLevel1Children()
        self.initTopLevel2Children()
        self.initTopLevel3Children()
        self.initTopLevel4Children()
        self.initTopLevel5Children()
        self.initTopLevel6Children()
        self.initTopLevel7Children()
        self.initTopLevel8Children()
        self.initTopLevel9Children()

    # ==================================================================================================================
    #                                                                                             topLevel0 text methods
    # ==================================================================================================================
    def topLevel0_Child0_text(self):
        self.write_code = "class ExampleA:\n    pass\n"
        self.write_markdown = (
            "* Let's set up the most simple Class we can\n"
            "* This class does nothing and has no information associated with it\n"
            "* How do we initialize an Object (or Instance) of this Class?\n"
        )

    def topLevel0_Child1_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "    pass\n"
            "\n"
            "\n"
            'if __name__ == "__main__":\n'
            "    a = ExampleA()\n"
            "    print(isinstance(a, ExampleA))\n"
        )
        self.write_markdown = (
            "* All we have to do in Python is call this class as shown\n"
            "* Here is a built-in function that can be useful:\n"
            "  * `isinstance(<var>, <class>)` will return a boolean value if a given variable is an instance of the given class\n"
            "* We can see that `isinstance()` returns `True` so `a` is an instance of our class `ExampleA`\n"
            "* Now that we know how the basics of using a class, let's make them actually do something\n"
        )

    # ==================================================================================================================
    #                                                                                             topLevel1 text methods
    # ==================================================================================================================
    def topLevel1_Child0_text(self):
        self.write_code = "class ExampleA:\n    x = 5\n"
        self.write_markdown = (
            "* Here is how we create a Class Attribute\n"
            "  * Looks almost exactly the same as creating a variable\n"
            "* Now `x` is an Attribute of the Class `ExampleA`\n"
            "* How can our main script access `x`?\n"
        )

    def topLevel1_Child1_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "    x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    print(ExampleA.x)\n"
            "\n"
            "    a = ExampleA()\n"
            "    print(a.x)\n"
        )
        self.write_markdown = (
            "* We have two ways of accessing Class Attributes:\n"
            "  * We can access it by `<class name>.<attribute name>`\n"
            "  * Or we can create an instance of the class and access it by `<instance variable>.<attribute name>`\n"
            "* A very important aspect of Object-Oriented Programming in Python is understanding how Python is managing memory\n"
            "  * Let's see how Python is allocating memory for these objects\n"
        )

    def topLevel1_Child2_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "    x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(id(a) == id(ExampleA))\n"
        )
        self.write_markdown = (
            "* Python has this interesting built in `id()` function\n"
            "* This function returns the memory address of whatever is passed to it\n"
            "\n"
            "POLL: True or False: An instance of this class has the same memory address as the class itself\n"
            "\n"
            "Answer: False\n"
            "\n"
            "Explanation: The class will have a location in memory, but it is essentially acting as a blueprint to create unique instances\n"
        )

    def topLevel1_Child3_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "    x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(id(a.x) == id(ExampleA.x))\n"
        )
        self.write_markdown = (
            "* What about the memory address of the `x` attribute of this instance and directly accessing the `x` attribute?\n"
            "\n"
            "POLL: True or False: The `x` attribute of the object and the class will have the same memory address\n"
            "\n"
            "Answer: True\n"
            "\n"
            "Explanation: the attribute has a different memory address than the class and the object, and it has not changed\n"
        )

    def topLevel1_Child4_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "    x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(id(a.x) == id(ExampleA.x))\n"
        )
        self.write_markdown = (
            "* Now what will happen if I change the value of `x` for the instance of `ExampleA`?\n"
            "\n"
            "POLL: True or False: Changing the value of the `x` attribute will change the memory address of the attribute\n"
            "\n"
            "Answer: False\n"
            "\n"
            "Explanation: A memory location won't hold two sets of information, so it must move to a different memory location to hold the new value of `a.x`\n"
        )

    def topLevel1_Child5_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    a.x = 5\n"
            "    print(id(a.x) == id(ExampleA.x))\n"
        )
        self.write_markdown = (
            "* What happens if I set `a.x` to a value, but it is the same value as the default in the class?\n"
            "\n"
            "POLL: True or False: Setting the `x` attribute to its original value will not change the memory address\n"
            "\n"
            "Answer: True\n"
            "\n"
            "Explanation: The value of the attribute does not change so Python will not change the memory address of the attribute\n"
        )

    def topLevel1_Child6_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "    x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    a.x = 10\n"
            "    a.x = 5\n"
            "    print(id(a.x) == id(ExampleA.x))\n"
        )
        self.write_markdown = (
            "* What happens if we set `a.x` to a different value and the set it back to the original value?\n"
            "\n"
            "POLL: True or False: Setting the attribute back to the original value will restore its original memory address\n"
            "\n"
            "Answer: True\n"
            "\n"
            "Explanation: There is already a location in memory for the original value of `a.x` so Python will return it to the same address\n"
        )

    def topLevel1_Child7_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "    _x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print('a._x', a._x)\n"
            "    # print('a.__y', a.__y)\n"
            "\n"
            "\n"
            "\n"
        )
        self.write_markdown = (
            "* If we want to create a Protected Attribute in Python we can add a single `_` prefix to the attribute name\n"
            "* We can still access this outside of the class but we should not be doing so\n"
            "* We can add a new method with a `property` decorator that returns the value of the protected attribute\n"
            "  * Now we are still getting the value of the `x` attribute, but we are not accessing the protected attribute directly\n"
            "  * This seems like a lot of extra work to add a seemingly unnecessary workaround, but this allows us to adhere to the Encapsulation Principle of Object-Oriented Programming\n"
            "* To make a Private Attribute we simply add a `__` prefix to the attribute name\n"
            "  * We can not access this attribute at all when our scope is outside the class\n"
            "  * Now we can set the visibility of our information and choose what we share outside the scope of the object following the Principle of Encapsulation\n"
            "* We will get into the differences between Private and Protected attributes in the `Parents and Children` section\n"
        )

    # ==================================================================================================================
    #                                                                                             topLevel2 text methods
    # ==================================================================================================================
    def topLevel2_Child0_text(self):
        self.write_code = (
            "class ExampleA:\n    x = 5\n\n    def printX(self):\n        print(self.x)\n"
        )
        self.write_markdown = (
            "Attributes are analogous to variables, and Methods are analogous to functions. Methods are special in that they have access to all attributes and other methods of the same class\n"
            "\n"
            "* Here we see how to create a method\n"
            "* As I just mentioned, methods are analogous to functions and they are defined\n"
            "\n"
            "* The key aspect to remember for methods is that you still have to pass this\n"
            "* This is the first time we have seen `self` so far, and it is very important\n"
            "  * `self` is how an object refers to...itself within the class\n"
            "  * Passing `self` to a method may seem somewhat redundant but doing so is what gives the method access to all attributes and other methods of the class\n"
            "* How do we access/run a method of a class?\n"
        )

    def topLevel2_Child1_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "    x = 5\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    a.printX()\n"
        )
        self.write_markdown = (
            "* If we are going to run a method we first have to create an instance of the class\n"
            "* Then we run it with the syntax `<instance name>.<method name>()`\n"
            "* What can we do with methods?\n"
        )

    def topLevel2_Child2_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def updateX(self):\n"
            "        self.x = 10\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(a.x)\n"
            "    a.updateX()\n"
            "    print(a.x)\n"
        )
        self.write_markdown = "* We can use methods to modify attributes of the object like this\n"

    def topLevel2_Child3_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def updateX(self, val):\n"
            "        self.x = val\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(a.x)\n"
            "    a.updateX(10)\n"
            "    print(a.x)\n"
        )
        self.write_markdown = "* We can pass outside values into a method\n"

    def topLevel2_Child4_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "    def updateX(self, val):\n"
            "        self.x = val\n"
            "        self.printX()\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(a.x)\n"
            "    a.updateX(10)\n"
        )
        self.write_markdown = "* Methods can call other methods of the class\n"

    def topLevel2_Child5_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def getX(self):\n"
            "        return self.x\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(a.getX())\n"
        )
        self.write_markdown = (
            "* Methods can also return values outside the class\n"
            "* This is another way that Objects interact with each other and also another way to access attributes, _even private and protected attributes_\n"
        )

    def topLevel2_Child6_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    @staticmethod\n"
            "    def printHW():\n"
            "        print('Hello World!')\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    ExampleA.printHW()\n"
        )
        self.write_markdown = (
            "* Static methods are a special kind of method that do not have access to the class attributes and other methods but still belong to the class\n"
            "* Notice that we no longer pass `self` as an argument into the method\n"
            "  * This is why we pass it to other methods even though it seems redundant\n"
            "* One interesting aspect of static methods is that we can access them without creating an instance of the class\n"
        )

    def topLevel2_Child7_text(self):
        self.write_code = (
            "import numpy as np\n"
            "\n"
            "\n"
            "class ExampleA:\n"
            "\n"
            "    arr = np.array\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    arr = a.arr([0, 1, 2, 3])\n"
            "    print(type(arr))\n"
            "    print(id(a.arr) == id(np.array))\n"
        )
        self.write_markdown = (
            "* You can assign outside functions or methods to an attribute like this\n"
            "* Also notice that doing this does not change the memory address of the function\n"
        )

    def topLevel2_Child8_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    __x = 5\n"
            "    __y = 10\n"
            "\n"
            "    def _printX(self):\n"
            "        print('__x', self.__x)\n"
            "\n"
            "    def __printY(self):\n"
            "        print('__y', self.__y)\n"
            "\n"
            "    def print_params(self):\n"
            "        self._printX()\n"
            "        self.__printY()\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    a._printX()\n"
            "    # a.__printY()\n"
            "    # a.print_params()\n"
        )
        self.write_markdown = (
            "* Using the same syntax as private and protected attributes, we can create private and protected methods with the `_` and `__` prefix convention\n"
            "* Notice that both attributes here are Private Attributes\n"
            "* We can run a protected method from outside the class with no issue, but this is a protected method and we should not do that\n"
            "* Similarly to private attributes, we do not have access to private methods outside the class\n"
            "* However, we can create a public method that can be accessed outside the class and has access to all protected and private information of the class\n"
            "* Remember back to the `Abstraction` Principle of Object-Oriented Programming\n"
            "  * We create Public methods that allow interaction with our object, but we hide the internal mechanisms of the object that we want to remain hidden\n"
        )

    # ==================================================================================================================
    #                                                                                             topLevel3 text methods
    # ==================================================================================================================
    def topLevel3_Child0_text(self):
        self.write_code = "class ExampleA:\n\n    def __init__(self):\n        pass\n"
        self.write_markdown = (
            "Now that we know how to create Class Attributes and Methods, we can get into the real nitty-gritty of classes; starting with a special method named `__init__()`\n"
            "* Here is what it will look like when we define `__init__()`\n"
            "* It does not look any different from any other method except for the double underscores\n"
            "* We still pass `self` as the first argument\n"
            "* So how do we run this `__init__()` method?\n"
        )

    def topLevel3_Child1_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        print('Hello World!')\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
        )
        self.write_markdown = (
            "* Turns out we don't have to worry about it!\n"
            "* When we _initialize_ an object, Python will run the `__init__()` method automatically\n"
            "* But when does Python run `__init__()`?\n"
        )

    def topLevel3_Child2_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        print(self.x)\n"
            "\n"
            "    x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
        )
        self.write_markdown = (
            "* After all Class Attributes and other methods have been initialized too\n"
            "* `__init__()` can still access the `x` attribute even though it is defined above `x`\n"
            "* All methods and class attributes will be compiled during the initialization process before `__init__()` is executed\n"
            "* All this time I have been saying _Class_ attribute because there is another type of attribute called the Instance Attribute\n"
        )

    def topLevel3_Child3_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print('x:', a.x)\n"
            "    print('y:', a.y)\n"
            "    # print('x:', ExampleA.x)\n"
            "    # print('y:', ExampleA.y)\n"
        )
        self.write_markdown = (
            "* Here we are defining another attribute `y` in the `__init__()` method\n"
            "* They are accessed the same way as class attributes\n"
            "* What makes Instance Attributes different from Class Attributes?\n"
            "  * For starters, we _have_ to create an instance of this class to access the attribute\n"
            "  * We can not run this commented out line because `y` is an _Instance_ attribute\n"
            "* Let's see what else we can do with the `__init__()` method\n"
        )

    def topLevel3_Child4_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self, value):\n"
            "        self.x = value\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA(5)\n"
            "    print(a.x)\n"
        )
        self.write_markdown = (
            "* If we want to initialize an object with a value we can pass it into `__init__()` like this\n"
            "* Since we never directly call the `__init__()` method, this is how Python handles these passed values\n"
            "* This is another key difference between Instance and Class Attributes\n"
            "  * Class Attributes will be the same for all objects initialized from the class, unless intentionally changed\n"
            "  * Instance Attributes do not necessarily have to be the same\n"
        )

    def topLevel3_Child5_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.initX()\n"
            "\n"
            "    def initX(self):\n"
            "        self.x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(a.x)\n"
        )
        self.write_markdown = (
            "* Like other methods, `__init__()` can call other methods\n"
            "* If the class I am writing has many attributes or needs to perform many actions during construction, I like to move some initialization procedure to other methods for readability\n"
        )

    def topLevel3_Child6_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        pass\n"
            "\n"
            "    def setX(self):\n"
            "        self.x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(a.x)\n"
        )
        self.write_markdown = (
            "* A note on best practices\n"
            "* All attributes that the class will use should be in `__init__()` so that a new reader knows all attribute of the class from only inspecting `__init__()`\n"
            "* This also contributes to better usability\n"
            "  * If an attribute only gets defined in another method, and we forget to call that method then it will not exist\n"
        )

    def topLevel3_Child7_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    id_a = id(a)\n"
            "    a.x = 10\n"
            "    print(id_a == id(a))\n"
        )
        self.write_markdown = (
            "* What happens when we change an attribute of this instance; will the memory address change?\n"
            "\n"
            "POLL: True or False: Changing the value of an Instance Attribute will _not_ change the memory address of the object\n"
            "\n"
            "Answer: True\n"
            "\n"
            "Explanation: We are only changing an attribute of this object. Python does not need to create an entirely new object in memory just because of this small change so the memory address will remain the same.\n"
        )

    def topLevel3_Child8_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "        print('Hello World!')\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    b = a\n"
            "    print(id(a) == id(b))\n"
        )
        self.write_markdown = (
            "* Let's create an instance of a class, and then assign another variable as equal to the first instance\n"
            "* Do we think that Python is going to run `__init__()` again? Will `a` and `b` have memory address?\n"
            "\n"
            "POLL: What will the printed output of this script?\n"
            "\n"
            "Answer: Hello World!\\nTrue\n"
            "\n"
            "Explanation: Assigning `b` as equal to `a` does not run `__init__()` again, and they will have the same memory address\n"
        )

    def topLevel3_Child9_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "        print('Hello World!')\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    b = a\n"
            "    b.x = 10\n"
        )
        self.write_markdown = (
            "* What about if we change the `x` attribute of `b`?\n"
            "\n"
            "POLL: What will the printed output of this script?\n"
            "\n"
            "Answer: Hello World!\n"
            "\n"
            "Explanation: Just changing the instance attribute will not run `__init__()` again\n"
        )

    def topLevel3_Child10_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        print('Hello World!')\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    b = a\n"
            "    b.x = 10\n"
        )
        self.write_markdown = (
            "* What if we change a Class Attribute instead? Will that run `__init__()` again?\n"
            "\n"
            "POLL: What will the printed output of this script?\n"
            "\n"
            "Answer: Hello World!\n"
            "\n"
            "Explanation: No. Changing any attribute of `b` will not run `__init__()` again\n"
        )

    def topLevel3_Child11_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    b = a\n"
            "    b.x = 10\n"
            "    print(id(a) == id(b))\n"
        )
        self.write_markdown = (
            "* Let's compare the memory addresses of `a` and `b`\n"
            "* We create and instance of our class, set `b` equal to `a`, then change `b.x`\n"
            "\n"
            "POLL: What will the output be?\n"
            "\n"
            "Answer: True\n"
            "\n"
            "What is going on here? We only changed the `x` attribute of `b`, not `a`. And I told you earlier that a memory address is not going to hold two sets of information, so that would mean that `a.x` must be equal to `10`, right?\n"
        )

    def topLevel3_Child12_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    b = a\n"
            "    b.x = 10\n"
            "    print(a.x)\n"
        )
        self.write_markdown = (
            "* It _is_ equal to 10!\n"
            "  * But we didn't change `a.x` so what is going on?\n"
            "* It turns out that by declaring `a = ExampleA()` what we are really doing is telling Python:\n"
            '  * "When I use the variable `a`, I am referring to something at a specific memory address"\n'
            "* Then, when we say that `b = a`, we are telling Python that `b` refers to the same memory address as `a`\n"
            "* So if we modify _any_ attribute of either `a` or `b`, we are modifying that attribute in both!\n"
            "* This can be useful if you understand what is going on and soooooooooo frustrating when you don't and have to learn this on your own\n"
            "* Now that we understand core fundamentals of classes, let's start looking at some more advanced aspects of OOP\n"
        )

    # ==================================================================================================================
    #                                                                                             topLevel4 text methods
    # ==================================================================================================================
    def topLevel4_Child0_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "    def printY(self):\n"
            "        print(self.y)\n"
            "\n"
            "\n"
            "class ExampleB(ExampleA):\n"
            "    pass\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    b = ExampleB()\n"
        )
        self.write_markdown = (
            "* Here we have defined two classes, `ExampleA` and `ExampleB`\n"
            "* `ExampleB`  is considered a Child of the Parent class, `ExampleA`\n"
            "  * This relationship is also referred to as superclass and subclass, or base class and derived class\n"
            "  * I will also use subclass as a verb; such as `ExampleB` is subclassing `ExampleA`\n"
            "* We create an instance of `ExampleB` the same as we would any other class, but what is going on with `ExampleB`?\n"
        )

    def topLevel4_Child1_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "    def printY(self):\n"
            "        print(self.y)\n"
            "\n"
            "\n"
            "class ExampleB(ExampleA):\n"
            "    pass\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    b = ExampleB()\n"
            "    print(isinstance(b, ExampleB))\n"
        )
        self.write_markdown = "* We set the variable `b` to be an instance of `ExampleB` so the return of `isinstance()` here will obviously be `True`\n"

    def topLevel4_Child2_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "    def printY(self):\n"
            "        print(self.y)\n"
            "\n"
            "\n"
            "class ExampleB(ExampleA):\n"
            "    pass\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    b = ExampleB()\n"
            "    print(isinstance(b, ExampleA))\n"
        )
        self.write_markdown = (
            "* Is it an instance of `ExampleA` though?\n"
            "\n"
            "POLL: True or False: `b` is an instance of `ExampleA`\n"
            "\n"
            "Answer: True\n"
        )

    def topLevel4_Child3_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "    def printY(self):\n"
            "        print(self.y)\n"
            "\n"
            "\n"
            "class ExampleB(ExampleA):\n"
            "    pass\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(isinstance(a, ExampleB))\n"
        )
        self.write_markdown = (
            "* Are instances of parent classes also instances of their children?\n"
            "\n"
            "POLL: True or False: `a` is an instance of `ExampleB`\n"
            "\n"
            "Answer: False\n"
        )

    def topLevel4_Child4_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "    def printY(self):\n"
            "        print(self.y)\n"
            "\n"
            "\n"
            "class ExampleB(ExampleA):\n"
            "    pass\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    b = ExampleB()\n"
            "    print(b.x)\n"
        )
        self.write_markdown = (
            "* Child classes inherit all Class Attributes and methods of their parent\n"
            "* When we run this script, it will print `5` because `ExampleB` has inherited the `x` class attribute\n"
        )

    def topLevel4_Child5_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "    def printY(self):\n"
            "        print(self.y)\n"
            "\n"
            "\n"
            "class ExampleB(ExampleA):\n"
            "    pass\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    b = ExampleB()\n"
            "    print(b.y)\n"
        )
        self.write_markdown = (
            "* We do not have an `__init__()` method in `ExampleB` though\n"
            "* Does `b` have a `y` attribute?\n"
            "\n"
            "POLL: What will be the output of this script?\n"
            "\n"
            "Answer: 10\n"
            "\n"
            "Explanation: `ExampleB` inherits the `__init__()` method from `ExampleA` so it will still run when we create an instance of `ExampleB`\n"
        )

    def topLevel4_Child6_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "    def printY(self):\n"
            "        print(self.y)\n"
            "\n"
            "\n"
            "class ExampleB(ExampleA):\n"
            "    pass\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    b = ExampleB()\n"
            "    b.printX()\n"
            "    b.printY()\n"
        )
        self.write_markdown = (
            "* As mentioned earlier, child classes inherit all methods from their parent so `ExampleB` has the `printX()` and `printY()` methods\n"
            "* All of this so far is fine, but we still have not done anything with `ExampleB`\n"
            "  * It is still exactly like `ExampleA` so what is the point of creating a child class?\n"
        )

    def topLevel4_Child7_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "    def printY(self):\n"
            "        print(self.y)\n"
            "\n"
            "\n"
            "class ExampleB(ExampleA):\n"
            "\n"
            "    def printSumXY(self):\n"
            "        print(self.x + self.y)\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    b = ExampleB()\n"
            "    b.printSumXY()\n"
        )
        self.write_markdown = (
            "* For starters, we can create new methods in the child class\n"
            "* In `ExampleB` here we have this `printSumXY()` method that prints the sum of the `x` and `y` attributes\n"
        )

    def topLevel4_Child8_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "    def printY(self):\n"
            "        print(self.y)\n"
            "\n"
            "\n"
            "class ExampleB(ExampleA):\n"
            "\n"
            "    def printAddXY(self):\n"
            "        print(self.x + self.y)\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    a.printAddXY()\n"
        )
        self.write_markdown = (
            "* What about if we create an instance of `ExampleA` and run the `printSumXY() ` method?\n"
            "\n"
            "POLL: What will the output of this script be?\n"
            "\n"
            "Answer: AttributeError\n"
            "\n"
            "Explanation: Parents do not have access to methods or attributes of the child class\n"
        )

    def topLevel4_Child9_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    _x = 5\n"
            "    __y = 10\n"
            "\n"
            "    def _printX(self):\n"
            "        print('__x', self._x)\n"
            "\n"
            "    def __printY(self):\n"
            "        print('__y', self.__y)\n"
            "\n"
            "\n"
            "class ExampleB(ExampleA):\n"
            "\n"
            "    def print_params(self):\n"
            "        self._printX()\n"
            "        self.__printY()\n"
            "        # print('__y', self.__y)\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    b = ExampleB()\n"
            "    b._printX()\n"
            "    # b.print_params()\n"
        )
        self.write_markdown = (
            "* Now that we are on Inheritance, we can finally demonstrate the difference between Protected and Private attributes and methods\n"
            "* Note that we have one protected and one private attribute and method in our parent class\n"
            "* Our child class only defines one public method\n"
            "* If we try to run this protected method on an instance of our child class...\n"
            "  * ...it runs without issue\n"
            "  * `ExampleB` has inherited the protected methods and attributes and still tracks it as protected\n"
            "* Now let's run the `print_params` public method of our child class...\n"
            "  * ...and we see that we get an `AttributeError` trying to access the private method\n"
            "  * This is the difference between Protected and Private\n"
            "  * Child classes will still inherit Protected methods but will not inherit Private ones\n"
            "* If we change the `__printY` method in our parent class to be Protected...\n"
            "  * Then we see that we can also access the new `_printY` method, and we can even access the Private attribute of our parent class\n"
            "  * But if we were to try to access the Private attribute directly in the child class with this commented out line in our `print_params` public method...\n"
            "  * ...then we get an `AttributeError` because the Private Attribute is not accessible directly by the child class\n"
            "  * If we move the `_printY` method to the child class, we still get the `AttributeError`\n"
            "  * This is a kind of tricky aspect about inheriting attributes and methods\n"
            "    * If we are inheriting a method that can access a private method of the parent class that will still work, even though the child class does not have direct access to that attribute\n"
        )

    def topLevel4_Child10_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "    def printY(self):\n"
            "        print(self.y)\n"
            "\n"
            "\n"
            "class ExampleB(ExampleA):\n"
            "\n"
            "    def __init__(self):\n"
            "        pass\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    b = ExampleB()\n"
            "    print(b.y)\n"
        )
        self.write_markdown = (
            "* If we want `ExampleB` to have its own `__init__()` method, we are free to do so\n"
            "\n"
            "POLL: What will the output of this script be?\n"
            "\n"
            "Answer: AttributeError\n"
            "\n"
            "Explanation: Here we are _overriding_ the parent method and this is the only aspect of the Polymorphism Principle of Object-Oriented Programming that is\n"
            "implemented by default in Python. Since we have overridden the `__init__()` method, Python will no longer run  the `__init__()` method of `ExampleA` when\n"
            "we create an instance of `ExampleB` unless we do something special.\n"
        )

    def topLevel4_Child11_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    x = 5\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "    def printY(self):\n"
            "        print(self.y)\n"
            "\n"
            "\n"
            "class ExampleB(ExampleA):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    b = ExampleB()\n"
            "    print(b.y)\n"
        )
        self.write_markdown = (
            "* We can access the parent from the child with this `super()` call\n"
            "* So when we add this `super().__init__()` call to the child `__init__()` method, we are telling Python to run the parent `__init__()` method and then continue with the rest of this `__init__()` method\n"
            "* Now if we run this script, we see that `b` does have the `y` attribute\n"
            "* We have seen this `__init__()` method quite a bit now, and you maybe be wondering what is going on with the name of it\n"
            "  * `__init__()` is only one of a specific kind of methods called `Dunder Methods`\n"
        )

    def topLevel4_Child12_text(self):
        self.write_code = (
            "class A:\n"
            "\n"
            "    def __init__(self):\n"
            "        print('A.__init__()')\n"
            "\n"
            "\n"
            "class B(A):\n"
            "\n"
            "    def __init__(self):\n"
            "        print('B.__init__()')\n"
            "        super().__init__()\n"
            "\n"
            "\n"
            "class C(B):\n"
            "\n"
            "    def __init__(self):\n"
            "        print('C.__init__()')\n"
            "        super().__init__()\n"
            "        print('Done')\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    c = C()\n"
            "    print()\n"
            "    print(isinstance(c, C))\n"
            "    print(isinstance(c, B))\n"
            "    print(isinstance(c, A))\n"
        )
        self.write_markdown = (
            "* Multilevel Inheritance is kind of like setting up a chain of inheritance with classes\n"
            "* In this example, `class C` inherits from `class B` which inherits from `class A`\n"
            "* We can see from the printed output that when we create an instance of `C`, we:\n"
            "  * Call the `__init__()` method of `B`,\n"
            "  * which calls the `__init__()` method of `A` before we finish the initialization of `C`\n"
            "* We also see the our instance of `C` is also an instance of `class B` and `class A` we would expect\n"
        )

    def topLevel4_Child13_text(self):
        self.write_code = (
            "class A:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "\n"
            "    def printX(self):\n"
            "        print(self.x)\n"
            "\n"
            "\n"
            "class B:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.y = 10\n"
            "\n"
            "    def printY(self):\n"
            "        print(self.y)\n"
            "\n"
            "\n"
            "class C:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.z = 15\n"
            "\n"
            "    def printZ(self):\n"
            "        print(self.z)\n"
            "\n"
            "\n"
            "class D(A, B):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    d = D()\n"
            "    d.printX()\n"
            "    # d.printY()\n"
            "    # print(d.z)\n"
            "    # d.printZ()\n"
        )
        self.write_markdown = (
            "* Child classes can have multiple parents\n"
            "* For now in this example ignore the `class C`, we will cover that one later\n"
            "* We see that `class D` inherits from `class A` and `class B`\n"
            "* When we run this code, we see that has indeed inherited the `printX()` method from `class A` and ran `class A`'s `__init__()` method with the `super()` call\n"
            "* What if we try to run the `printY()` method from `class B`?\n"
            "\n"
            "POLL: What will the output of this script be?\n"
            "a. 10\n"
            "b. AttributeError: 'D' object has no attribute 'printY'\n"
            "c. AttributeError: 'D' object has no attribute 'y'\n"
            "\n"
            "Answer: C. AttributeError: 'D' object has no attribute 'y'\n"
            "\n"
            "Explanation: We inherit the `printY()` method, but `super()` only runs the `__init__()` method of `A`\n"
            "\n"
            "* How can we run the `__init__()` method of `B`? We have to do it manually by adding `B.__init__(self)` to the `__init__()` method of `class D`\n"
            "* Now if we try to run the `printY` method, we see that `D` does have the attribute `y`\n"
            "* For a moment, this may not seem like we are truly inheriting from `class B`, but remember that we still inherit the methods of `class B`\n"
            "  * We can add `C.__init__(self)` and now our `class D` will have access to the `z` attribute, but not the `printZ()` method because we did not inherit from `class C`\n"
            "* If we also subclass `class C`, then we will have access to the `printZ()` method\n"
        )

    # ==================================================================================================================
    #                                                                                             topLevel5 text methods
    # ==================================================================================================================
    def topLevel5_Child0_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(a.x)\n"
        )
        self.write_markdown = (
            "* Dunder methods get their name from the double underscores at the beginning and end of the method name\n"
            "* There is nothing inherently special about Dunder methods, they get defined the same way as other methods but with a different naming scheme\n"
            "* The reason they have any importance at all is that many of Python's built-in functions and operators know to call these Dunder methods\n"
            "* The reason they were given double underscores is to make them more difficult to override\n"
            "  * You have to go out of your way a bit to be able to override them which makes Python's operation more stable\n"
            "* So what are some other Dunder methods and how are they used?\n"
            "\n"
            "* We've already seen `__init__()` in operation\n"
            "* Python knows to look for an `__init__()` method when creating an instance of a class\n"
        )

    def topLevel5_Child1_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(a)\n"
        )
        self.write_markdown = (
            "* If we print an Object then we might get something like this\n"
            "* We see that it is an object of `__main__.ExampleA` and we have the memory address of the object\n"
            "* This is not really useful for anything though, so why don't we help out `print()`?\n"
        )

    def topLevel5_Child2_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "\n"
            "    def __str__(self):\n"
            "        return 'An instance of class ExampleA'\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(a)\n"
        )
        self.write_markdown = (
            "* In Python, `print()` is actually calling the `__str__()` Dunder method of the class\n"
            "* `__str__()` has to return a string, otherwise we will get a `TypeError`\n"
            "* Now if we run this script, we can get an output that is more informative\n"
        )

    def topLevel5_Child3_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "\n"
            "    def __add__(self, other):\n"
            "        return self.x + other\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(a + 5)\n"
        )
        self.write_markdown = (
            "* Another common built-in operation is `+`\n"
            "* The `+` operator calls the `__add__()` Dunder method of the object\n"
            "* If we tried to add objects together that did not have `__add__()` defined, we would get a `TypeError`\n"
        )

    def topLevel5_Child4_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "\n"
            "    def __add__(self, other):\n"
            "        return self.x + other\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(5 + a)\n"
        )
        self.write_markdown = (
            "* What if we swap the order of `5` and `a`?\n"
            "\n"
            "POLL: What is the printed output of this script?\n"
            "\n"
            "Answer: TypeError\n"
            "\n"
            "Explanation: `5` is not an object so it does not have a `__add__()` method, and we need a different Dunder method when `a` is in the second place\n"
        )

    def topLevel5_Child5_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "\n"
            "    def __add__(self, other):\n"
            "        return self.x + other\n"
            "\n"
            "    def __radd__(self, other):\n"
            "        return self.x + other\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(5 + a)\n"
        )
        self.write_markdown = "* This `__radd__()` method is called when we need to add in the reverse direction. For adding two numbers it does not seem necessary but...\n"

    def topLevel5_Child6_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "\n"
            "    def __str__(self):\n"
            "        return 'An instance of class ExampleA'\n"
            "\n"
            "    def __add__(self, other):\n"
            "        return self.x + other\n"
            "\n"
            "    def __radd__(self, other):\n"
            "        return other + self.x\n"
            "\n"
            "    def __sub__(self, other):\n"
            "        return self.x - other\n"
            "\n"
            "    def __rsub__(self, other):\n"
            "        return other - self.x\n"
            "\n"
            "    def __mul__(self, other):\n"
            "        return self.x * other\n"
            "\n"
            "    def __rmul__(self, other):\n"
            "        return  other * self.x\n"
            "\n"
            "    def __truediv__(self, other):\n"
            "        return self.x / other\n"
            "\n"
            "    def __floordiv__(self, other):\n"
            "        return self.x // other\n"
            "\n"
            "    def __mod__(self, other):\n"
            "        return self.x % other\n"
            "\n"
            "    def __pow__(self, other):\n"
            "        return self.x ** other\n"
            "\n"
            "    def __lt__(self, other):\n"
            "        return self.x < other\n"
            "\n"
            "    def __le__(self, other):\n"
            "        return self.x <= other\n"
            "\n"
            "    def __eq__(self, other):\n"
            "        return self.x == other\n"
            "\n"
            "    def __ne__(self, other):\n"
            "        return self.x != other\n"
            "\n"
            "    def __gt__(self, other):\n"
            "        return self.x > other\n"
            "\n"
            "    def __ge__(self, other):\n"
            "        return self.x >= other\n"
            "\n"
            "    def __bool__(self):\n"
            "        return bool(self.x)\n"
            "\n"
            "    def __len__(self):\n"
            "        return 1\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(a)\n"
            "    print('a + 5:', a + 5)\n"
            "    print('5 + a:', 5 + a)\n"
            "    print('a - 2:', a - 2)\n"
            "    print('2 - a:', 2 - a)\n"
            "    print('a * 2:', a * 2)\n"
            "    print('2 * a:', 2 * a)\n"
            "    print('a / 2:', a / 2)\n"
            "    print('a // 2:', a // 2)\n"
            "    print('a % 2:', a % 2)\n"
            "    print('a ** 2:', a ** 2)\n"
            "    print('a < 5:', a < 5)\n"
            "    print('a <= 5:', a <= 5)\n"
            "    print('a == 5:', a == 5)\n"
            "    print('a != 5:', a != 5)\n"
            "    print('a > 5:', a > 5)\n"
            "    print('a >= 5:', a >= 5)\n"
            "    print('bool(a)', bool(a))\n"
            "    print('len(a)', len(a))\n"
        )
        self.write_markdown = (
            "* ...it makes sense for other mathematical operations\n"
            "* Every basic mathematical operation in Python is controlled by these Dunder Methods\n"
            "* Even Boolean comparisons are controlled by Dunder methods\n"
            "* This is not every Dunder method that Python uses\n"
            "* Now you may have noticed that there is something strange going on here which is that the `__add__()` Dunder method has a `+` in it\n"
            "  * Is this `+` behaving differently? No it's not. It is calling the `__add__()` method of the `x` attribute\n"
            "  * But for that to be true, that means that the `x` attribute has to be an instance of some class, right?\n"
        )

    # ==================================================================================================================
    #                                                                                             topLevel6 text methods
    # ==================================================================================================================
    def topLevel6_Child0_text(self):
        self.write_code = (
            "class ExampleA:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.x = 5\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = ExampleA()\n"
            "    print(dir(a.x))\n"
        )
        self.write_markdown = (
            "* That's exactly what it is\n"
            "* The `x` attribute is an instance of the `int` class\n"
            "* Python has this neat built-in `dir()` function\n"
            "  * This function will return a list of all methods and attributes of the object that is passed to it\n"
            "  * Now we can see the structure of Python's built-in `int` class\n"
        )

    def topLevel6_Child1_text(self):
        self.write_code = "x = 5\n\nprint(isinstance(x, int))\nprint(type(x))\n"
        self.write_markdown = (
            "* Every time we create a variable, we are creating an instance of a class\n"
            "* All the data types that you are familiar with like integers, floats, lists, etc. are all classes\n"
            "* The `isinstance()` function checks if a variable is an instance of a class\n"
            "* The `type()` function basically just returns the name of the class that the object is initialized from\n"
            "  * And note that it is also printing out `class` here\n"
        )

    def topLevel6_Child2_text(self):
        self.write_code = "x = 5\n\nprint(dir(x))\n"
        self.write_markdown = "* Just like when we used the `dir()` built-in function on the attribute `x`, we can use it on this variable `x` and see the same attributes and methods of the integer class\n"

    def topLevel6_Child3_text(self):
        self.write_code = "x = 5\ny = 10\n\nprint(x + y)\n"
        self.write_markdown = (
            "* In this script we end up creating three instances of the `int` class\n"
            "* By adding `x` and `y` together we call the `__add__()` Dunder method of `x`\n"
            "* And when we print, we are calling the `__str__()` method of the object resulting from the summation\n"
            "* _Everything_ in Python is an object which means that if anyone asks if you are an Object-Oriented programmer, you can _technically_ say yes because you work with Python\n"
            "  * They are really asking if you know how to create your own classes and objects, so you should wait until the end of this course, and _then_ you can say yes\n"
        )

    def topLevel6_Child4_text(self):
        self.write_code = "x = 5\ny = 6.315\nz = x + y\n"
        self.write_markdown = (
            "POLL: Not including objects in the base classes, how many unique objects are created by this script?\n"
            "\n"
            "Answer: 3\n"
        )

    def topLevel6_Child5_text(self):
        self.write_code = "x = 5\ny = 0\nz = x + y\n"
        self.write_markdown = (
            "POLL: Not including objects in the base classes, how many unique objects are created by this script?\n"
            "\n"
            "Answer: 2\n"
            "\n"
            "Explanation: `x` and `y` are both unique objects but because the value of `y` is `0`, `x` and `z` are actually the same object\n"
            "  * We can add `print(id(x) == id(z))` to verify this\n"
        )

    def topLevel6_Child6_text(self):
        self.write_code = "x = 5\ny = x + 0\n"
        self.write_markdown = (
            "POLL: Not including objects in the base classes, how many unique objects are created by this script?\n"
            "\n"
            "Answer: 1\n"
            "\n"
            "Explanation: `0` is not an object here, and because we are adding `0` to an integer, `y` will be identical to `x`\n"
            "  * We can add `print(id(x) == id(y))` to verify this\n"
        )

    def topLevel6_Child7_text(self):
        self.write_code = "x = 5\ny = 10 + 25\n"
        self.write_markdown = (
            "POLL: Not including objects in the base classes, how many unique objects are created by this script?\n"
            "\n"
            "Answer: 3\n"
            "\n"
            "Explanation: 10 is an object\n"
        )

    def topLevel6_Child8_text(self):
        self.write_code = "x = 1\ny = 1\n"
        self.write_markdown = (
            "POLL: Not including objects in the base classes, how many unique objects are created by this script?\n"
            "\n"
            "Answer: 1\n"
            "\n"
            "Explanation: even though we initialize two different variables, since they are the same value Python will assign them the same memory address\n"
            "  * Again, we can check this using `print(id(x) == id(y))`\n"
        )

    def topLevel6_Child9_text(self):
        self.write_code = 'x = 4\ny = 4.178\n\n"Demo script"\n'
        self.write_markdown = (
            "POLL: Not including objects in the base classes, how many unique objects are created by this script?\n"
            "\n"
            "Answer: 3\n"
            "\n"
            "Explanation: The string is also an object, even though it does not get assigned to a variable\n"
        )

    def topLevel6_Child10_text(self):
        self.write_code = (
            "def Foo(aX, aY):\n    return aX + aY\n\n\nx = 3\ny = 4\n\nz = Foo(x, y)\n"
        )
        self.write_markdown = (
            "POLL: Not including objects in the base classes, how many unique objects are created by this script?\n"
            "\n"
            "Answer: 4\n"
            "\n"
            "Explanation: This one is tricky because some might not be sure if `aX` and `aY` have different memory addresses in the function scope\n"
            "  * They do _not_ have unique addresses but even this is not the only trick\n"
            "  * `Foo` is _also_ an object; it is an instance of the `function` class\n"
            "    * `print(type(Foo))`\n"
            "  * Methods are also instances of the `function` class\n"
        )

    # ==================================================================================================================
    #                                                                                             topLevel7 text methods
    # ==================================================================================================================
    def topLevel7_Child0_text(self):
        self.write_code = "arr  = [1, 2, 3]\narr += [4, 5, 6]\nprint(arr)\n"
        self.write_markdown = (
            "* Now that we understand how Python is operating at a lower level, we have the power to do some interesting things with classes\n"
            "* There is a version of Python called MicroPython that is used on microcontrollers\n"
            "* This is kind of like a lite version of Python because it does not have access to all the existing Python modules\n"
            "  * Disappointingly, this includes `numpy`\n"
            "  * As you probably know, `numpy` is very good at mathematical operations on arrays so not having access to this module can be difficult\n"
            "  * Why don't we create a class that manages a 1D Array and works with the basic mathematical operations in Python?\n"
            "\n"
            "* Lists would be a good starting point, but they are obviously not exclusive to numbers, so they do not use the mathematical operators for math\n"
            "* For instance, `+` does not add the elements of this list together, it combines the two lists into one\n"
            "  * It is functioning like the `extend()` method of the `list` class\n"
        )

    def topLevel7_Child1_text(self):
        self.write_code = "arr  = [1, 2, 3]\narr *= [4, 5, 6]\nprint(arr)\n"
        self.write_markdown = (
            "* And if we tried to multiply these two lists together we get a `TypeError`\n"
            "* We can still use lists, but we need to change their behavior when using Python's operators\n"
        )

    def topLevel7_Child2_text(self):
        self.write_code = (
            "class array:\n"
            "\n"
            "    def __init__(self, arr):\n"
            "\n"
            "        if not isinstance(arr, list):\n"
            "            arr = list(arr)\n"
            "\n"
            "        for i in arr:\n"
            "            if not isinstance(i, (int, float, complex)):\n"
            "                raise TypeError('All elements must be of type int, float, or complex')\n"
            "\n"
            "        self.array = arr\n"
            "        self.len   = len(arr)\n"
            "        self.range = range(self.len)\n"
            "\n"
            "    def append(self, val):\n"
            "        if isinstance(val, (int, float, complex)):\n"
            "            self.array.append(val)\n"
            "        else:\n"
            "            self.array.extend(val)\n"
            "\n"
            "    def __str__(self):\n"
            "        return str(self.array)\n"
            "\n"
            "    def __getitem__(self, item):\n"
            "        return self.array[item]\n"
            "\n"
            "    def __setitem__(self, key, value):\n"
            "        self.array[key] = value\n"
            "\n"
            "    def __add__(self, other):\n"
            "        tmp = array([])\n"
            "        for i in self.range:\n"
            "            tmp.append(self.array[i] + other[i])\n"
            "        return tmp\n"
            "\n"
            "    def __radd__(self, other):\n"
            "        tmp = array([])\n"
            "        for i in self.range:\n"
            "            tmp.append(other[i] + self.array[i])\n"
            "        return tmp\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = array([0, 1, 2])\n"
            "    b = array([3, 4, 5])\n"
            "\n"
            "    print(a + b)\n"
        )
        self.write_markdown = (
            "* A lot just showed up at once, so let's break this down method by method\n"
            "* We create a class named `array`\n"
            "  * We will be using lists to store our numbers, so we could have subclassed `list`, but we would be overriding so much that it would probably hinder us to do that\n"
            "  * And we would inherit attributes and methods we do not need so we would end up using more memory than we need which is not great on microcontrollers\n"
            "* In the `__init__()` method we are passing in the `arr` argument, then converting it to a list if required\n"
            "  * We then iterate through every element in the `arr` argument to make sure it is a number, or else we raise a `TypeError`\n"
            "  * Then we assign `arr` to an attribute, get its length, and then create a range that we will use in our other methods\n"
            "* We define the `append` behavior of this `array` class\n"
            "  * We are only going to be working with one dimensional arrays for the demo so we will add them to the end of the array\n"
            "  * We could have done 2D arrays but that would just increase the complexity\n"
            "* We define the `__str__()` method to give ourselves a nice print statement\n"
            "* We define `__getitem__()` and `__setitem__()` so that we can index into the array and assign new values to specific elements\n"
            "* Then we have our `__add__()` and `__radd__()` methods, so we can add arrays together\n"
            "* We _could_ add a type check for `other` to make sure it is compatible, but if it is not compatible Python will already handle that\n"
            "  * Best to keep our class as light as possible if we are going to use it with a microcontroller\n"
        )

    def topLevel7_Child3_text(self):
        self.write_code = (
            "class array:\n"
            "\n"
            "    def __init__(self, arr):\n"
            "\n"
            "        if not isinstance(arr, list):\n"
            "            arr = list(arr)\n"
            "\n"
            "        for i in arr:\n"
            "            if not isinstance(i, (int, float, complex)):\n"
            "                raise TypeError('All elements must be of type int, float, or complex')\n"
            "\n"
            "        self.array = arr\n"
            "        self.len   = len(arr)\n"
            "        self.range = range(self.len)\n"
            "\n"
            "    def append(self, val):\n"
            "        if isinstance(val, (int, float, complex)):\n"
            "            self.array.append(val)\n"
            "        else:\n"
            "            self.array.extend(val)\n"
            "\n"
            "    def __str__(self):\n"
            "        return str(self.array)\n"
            "\n"
            "    def __getitem__(self, item):\n"
            "        return self.array[item]\n"
            "\n"
            "    def __setitem__(self, key, value):\n"
            "        self.array[key] = value\n"
            "\n"
            "    def __add__(self, other):\n"
            "        tmp = array([])\n"
            "        for i in self.range:\n"
            "            tmp.append(self.array[i] + other[i])\n"
            "        return tmp\n"
            "\n"
            "    def __radd__(self, other):\n"
            "        tmp = array([])\n"
            "        for i in self.range:\n"
            "            tmp.append(other[i] + self.array[i])\n"
            "        return tmp\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = array([0, 1, 2])\n"
            "    b = array([0, 0, 0])\n"
            "    c = a + b\n"
            "\n"
            "    print('a:', a)\n"
            "    print('c:', c)\n"
            "    print(id(a) == id(c))\n"
        )
        self.write_markdown = (
            "* But what happens when we try to add an array of zeros to an existing array?\n"
            "  * `a` and `c` have identical contents, but not the same memory address\n"
            "* This is because in our `__add__()` and `__radd__()` methods we are creating entirely new instances of our class and then appending values to it\n"
            "* All of the questions about how Python manages memory has led to this. Do we want our array class to keep `a` and `c` as unique objects?\n"
            "\n"
            "POLL: True or False: The individual elements of `a` and `c` share the same memory address. (Will this loop print out all `True` or all `False`?)\n"
            "\n"
            "Answer: A. True\n"
            "\n"
            "Explanation: We change the address of the class overall, but the address of the individual elements remain the same, meaning we are not heavily consuming more memory.\n"
            'Even though "a" and "c" have identical elements that share memory, they are still unique arrays and we can manipulate them individually.\n'
        )

    def topLevel7_Child4_text(self):
        self.write_code = (
            "class array:\n"
            "\n"
            "    def __init__(self, arr):\n"
            "\n"
            "        if not isinstance(arr, list):\n"
            "            arr = list(arr)\n"
            "\n"
            "        for i in arr:\n"
            "            if not isinstance(i, (int, float, complex)):\n"
            "                raise TypeError('All elements must be of type int, float, or complex')\n"
            "\n"
            "        self.array = arr\n"
            "        self.len   = len(arr)\n"
            "        self.range = range(self.len)\n"
            "        self.any   = any(arr)\n"
            "\n"
            "    def append(self, val):\n"
            "        if isinstance(val, (int, float, complex)):\n"
            "            self.array.append(val)\n"
            "        else:\n"
            "            self.array.extend(val)\n"
            "\n"
            "    def __str__(self):\n"
            "        return str(self.array)\n"
            "\n"
            "    def __getitem__(self, item):\n"
            "        return self.array[item]\n"
            "\n"
            "    def __setitem__(self, key, value):\n"
            "        self.array[key] = value\n"
            "\n"
            "    def __add__(self, other):\n"
            "        if not any(other):\n"
            "            return self\n"
            "        elif not self.any and any(other):\n"
            "            return other\n"
            "        else:\n"
            "            tmp = array([])\n"
            "            for i in self.range:\n"
            "                tmp.append(self.array[i] + other[i])\n"
            "            return tmp\n"
            "\n"
            "    def __radd__(self, other):\n"
            "        if not any(other):\n"
            "            return self\n"
            "        elif not self.any and any(other):\n"
            "            return other\n"
            "        else:\n"
            "            tmp = array([])\n"
            "            for i in self.range:\n"
            "                tmp.append(other[i] + self.array[i])\n"
            "            return tmp\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = array([0, 1, 2])\n"
            "    b = array([0, 0, 0])\n"
            "    c = a + b\n"
            "\n"
            "    print('a:', a)\n"
            "    print('c:', c)\n"
            "    a[0] = 20\n"
            "    print('a:', a)\n"
            "    print('c:', c)\n"
        )
        self.write_markdown = (
            "* With that in mind, I argue that we want to keep them separate\n"
            "  * If we have separate variables, then we are almost certainly tracking them separately and want to keep them unique\n"
            "* Here I have used Python's `any()` built-in function to return one array if the other is all zeros\n"
            "  * It will return `self` if `other` is all zeros, and it will return `other` if `self` is all zeros\n"
            "* If we return the exact same array, then `c` is not unique from `a`\n"
            "  * Therefore if we update either, we update both which is not what we want in terms of usability\n"
            "* Further edits will expand on the previous state, not this one\n"
        )

    def topLevel7_Child5_text(self):
        self.write_code = (
            "class array:\n"
            "\n"
            "    def __init__(self, arr):\n"
            "\n"
            "        if not isinstance(arr, list):\n"
            "            arr = list(arr)\n"
            "\n"
            "        for i in arr:\n"
            "            if not isinstance(i, (int, float, complex)):\n"
            "                raise TypeError('All elements must be of type int, float, or complex')\n"
            "\n"
            "        self.array = arr\n"
            "        self.len   = len(arr)\n"
            "        self.range = range(self.len)\n"
            "\n"
            "    def append(self, val):\n"
            "        if isinstance(val, (int, float, complex)):\n"
            "            self.array.append(val)\n"
            "        else:\n"
            "            self.array.extend(val)\n"
            "\n"
            "    def __str__(self):\n"
            "        return str(self.array)\n"
            "\n"
            "    def __getitem__(self, item):\n"
            "        return self.array[item]\n"
            "\n"
            "    def __setitem__(self, key, value):\n"
            "        self.array[key] = value\n"
            "\n"
            "    def __add__(self, other):\n"
            "        if hasattr(other, '__getitem__'):\n"
            "            tmp = array([])\n"
            "            for i in self.range:\n"
            "                tmp.append(self.array[i] + other[i])\n"
            "            return tmp\n"
            "        else:\n"
            "            tmp = array([])\n"
            "            for i in self.range:\n"
            "                tmp.append(self.array[i] + other)\n"
            "            return tmp\n"
            "\n"
            "    def __radd__(self, other):\n"
            "        if hasattr(other, '__getitem__'):\n"
            "            tmp = array([])\n"
            "            for i in self.range:\n"
            "                tmp.append(other[i] + self.array[i])\n"
            "            return tmp\n"
            "        else:\n"
            "            tmp = array([])\n"
            "            for i in self.range:\n"
            "                tmp.append(other + self.array[i])\n"
            "            return tmp\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = array([0, 1, 2])\n"
            "    b = array([5, 5, 5])\n"
            "\n"
            "    print(a + b)\n"
            "    print(b + a)\n"
            "    print(a + 5)\n"
            "    print(5 + a)\n"
        )
        self.write_markdown = (
            "* Now that we know how we want to manage memory during our mathematical operations, let's look into improving our usability.\n"
            "  * Specifically, what if we want to add a single value to every element of our array?\n"
            "  * Currently we would get an indexing error when trying to index into other\n"
            "* We've already added this '__getitem__() Dunder method to our class\n"
            "* Since this is what Python looks for when indexing, so we know that if the other argument passed does not have that method, then it is likely a single value\n"
            "* Python has another built-in function called hasattr() (which also works for methods), so we can use to check if the argument has a specific method\n"
        )

    def topLevel7_Child6_text(self):
        self.write_code = (
            "class array:\n"
            "\n"
            "    def __init__(self, arr):\n"
            "\n"
            "        if not isinstance(arr, list):\n"
            "            arr = list(arr)\n"
            "\n"
            "        for i in arr:\n"
            "            if not isinstance(i, (int, float, complex)):\n"
            "                raise TypeError('All elements must be of type int, float, or complex')\n"
            "\n"
            "        self.array = arr\n"
            "        self.len   = len(arr)\n"
            "        self.range = range(self.len)\n"
            "\n"
            "    def append(self, val):\n"
            "        if isinstance(val, (int, float, complex)):\n"
            "            self.array.append(val)\n"
            "        else:\n"
            "            self.array.extend(val)\n"
            "\n"
            "    def __str__(self):\n"
            "        return str(self.array)\n"
            "\n"
            "    def __getitem__(self, item):\n"
            "        return self.array[item]\n"
            "\n"
            "    def __setitem__(self, key, value):\n"
            "        self.array[key] = value\n"
            "\n"
            "    def __len__(self):\n"
            "        return self.len\n"
            "\n"
            "    def __add__(self, other):\n"
            "        if hasattr(other, '__getitem__'):\n"
            "            if self.len != len(other):\n"
            "                raise SyntaxError('Type array can only be added to iterables of equal shape or single values')\n"
            "            else:\n"
            "                tmp = array([])\n"
            "                for i in self.range:\n"
            "                    tmp.append(self.array[i] + other[i])\n"
            "                return tmp\n"
            "        else:\n"
            "            tmp = array([])\n"
            "            for i in self.range:\n"
            "                tmp.append(self.array[i] + other)\n"
            "            return tmp\n"
            "\n"
            "    def __radd__(self, other):\n"
            "        if hasattr(other, '__getitem__'):\n"
            "            if self.len != len(other):\n"
            "                raise SyntaxError('Type array can only be added to arrays of equal size or single values')\n"
            "            else:\n"
            "                tmp = array([])\n"
            "                for i in self.range:\n"
            "                    tmp.append(other[i] + self.array[i])\n"
            "                return tmp\n"
            "        else:\n"
            "            tmp = array([])\n"
            "            for i in self.range:\n"
            "                tmp.append(other + self.array[i])\n"
            "            return tmp\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    a = array([1, 2, 3])\n"
            "    b = array([0, 0, 0, 0])\n"
            "    c = a + b\n"
        )
        self.write_markdown = (
            "* We have not taken steps to make sure that we are only adding arrays of the same size\n"
            "* We can add one more check to see if the lengths are equal, and then we can raise a `SyntaxError` if they are not the same\n"
            "* That was a lot just to create two methods to add arrays to arrays and arrays to single values...\n"
        )

    def topLevel7_Child7_text(self):
        self.write_code = '''\
from typing import Iterable


class array:

    def __init__(self, arr: int | float | complex | Iterable[int | float | complex]):
        """
        A class for element by element mathematical and boolean operations on one-dimensional arrays

        Args:
            arr (int | float | complex | Iterable[int  |  float  |  complex]): Value(s) to store in array

        Raises:
            TypeError: if not all elements in `arr` are of type: `int`, `float`, or `complex`.
        """

        if not isinstance(arr, list):
            arr = list(arr)

        for i in arr:
            if not isinstance(i, (int, float, complex)):
                raise TypeError('All elements must be of type int, float, or complex')

        self.array = arr
        self.len   = len(arr)
        self.range = range(self.len)

    def append(self, val):
        if isinstance(val, (int, float, complex)):
            self.array.append(val)
        else:
            self.array.extend(val)

    def __str__(self):
        return str(self.array)

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __add__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to iterables of equal shape or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(self.array[i] + other[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] + other)
            return tmp

    def __radd__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to arrays of equal size or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(other[i] + self.array[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(other + self.array[i])
            return tmp

    def __sub__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to iterables of equal shape or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(self.array[i] - other[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] - other)
            return tmp

    def __rsub__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to arrays of equal size or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(other[i] - self.array[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(other - self.array[i])
            return tmp

    def __mul__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to iterables of equal shape or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(self.array[i] * other[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] * other)
            return tmp

    def __rmul__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to arrays of equal size or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(other[i] * self.array[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(other * self.array[i])
            return tmp

    def __truediv__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to iterables of equal shape or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(self.array[i] / other[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] / other)
            return tmp

    def __rtruediv__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to arrays of equal size or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(other[i] / self.array[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(other / self.array[i])
            return tmp

    def __floordiv__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to iterables of equal shape or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(self.array[i] // other[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] // other)
            return tmp

    def __rfloordiv__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to arrays of equal size or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(other[i] / self.array[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(other / self.array[i])
            return tmp

    def __mod__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to iterables of equal shape or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(self.array[i] % other[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] % other)
            return tmp

    def __rmod__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to arrays of equal size or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(other[i] % self.array[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(other % self.array[i])
            return tmp

    def __pow__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to arrays of equal size or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(self.array[i] ** other[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] ** other)
            return tmp

    def __rpow__(self, other):
        if hasattr(other, '__getitem__'):
            if self.len != len(other):
                raise SyntaxError('Type array can only be added to arrays of equal size or single values')
            else:
                tmp = array([])
                for i in self.range:
                    tmp.append(other[i] ** self.array[i])
                return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(other ** self.array[i])
            return tmp

    def __lt__(self, other):
        if hasattr(other, '__getitem__'):
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] < other[i])
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] < other)
        return tmp

    def __le__(self, other):
        if hasattr(other, '__getitem__'):
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] <= other[i])
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] <= other)
        return tmp

    def __gt__(self, other):
        if hasattr(other, '__getitem__'):
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] > other[i])
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] > other)
        return tmp

    def __ge__(self, other):
        if hasattr(other, '__getitem__'):
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] >= other[i])
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] >= other)
        return tmp

    def __eq__(self, other):
        if hasattr(other, '__getitem__'):
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] == other[i])
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] == other)
        return tmp

    def __ne__(self, other):
        if hasattr(other, '__getitem__'):
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] != other[i])
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] != other)
        return tmp

    def __bool__(self):
        tmp = array([])
        for i in self.range:
            tmp.append(bool(self.array[i]))
        return tmp

    def __len__(self):
        return self.len


if __name__ == '__main__':

    a = array([1, 2, 3])
    b = array([4, 5, 6])

    print('a + b:', a + b)
    print('b + a:', b + a)
    print('a + 5:', a + 5)
    print('5 + a:', 5 + a)
    print()
    print('a - b:', a - b)
    print('b - a:', b - a)
    print('a - 5:', a - 5)
    print('5 - a:', 5 - a)
    print()
    print('a * b:', a * b)
    print('b * a:', b * a)
    print('a * 5:', a * 5)
    print('5 * a:', 5 * a)
    print()
    print('a / b:', a / b)
    print('b / a:', b / a)
    print('a / 5:', a / 5)
    print('5 / a:', 5 / a)
    print()
    print('a // b:', a // b)
    print('b // a:', b // a)
    print('a // 5:', a // 5)
    print('5 // a:', 5 // a)
    print()
    print('a % b:', a % b)
    print('b % a:', b % a)
    print('a % 5:', a % 5)
    print('5 % a:', 5 % a)
    print()
    print('a ** b:', a ** b)
    print('b ** a:', b ** a)
    print('a ** 5:', a ** 5)
    print('5 ** a:', 5 ** a)
    print()
    print('any:', any(a))
    print('all:', all(a))
    print()
    print('a < b:', a < b)
    print('b < a:', b < a)
    print('a < 5:', a < 5)
    print('a < 0:', a < 0)
    print()
    print('a <= b:', a <= b)
    print('b <= a:', b <= a)
    print('a <= 5:', a <= 5)
    print('a <= 0:', a <= 0)
    print()
    print('a > b:', a > b)
    print('b > a:', b > a)
    print('a > 5:', a > 5)
    print('a > 0:', a > 0)
    print()
    print('a >= b:', a >= b)
    print('b >= a:', b >= a)
    print('a >= 5:', a >= 5)
    print('a >= 0:', a >= 0)
    print()
    print('a == b:', a == b)
    print('b == a:', b == a)
    print('a == 5:', a == 5)
    print('a == 0:', a == 0)
    print()
    print('a != b:', a != b)
    print('b != a:', b != a)
    print('a != 5:', a != 5)
    print('a != 0:', a != 0)
'''
        self.write_markdown = (
            "* ...luckily the rest follow a similar trend but with minor changes to the ways we check the values of `self` and `other`\n"
            "* I've also added Type Hints and a Doc-string to make it more user-friendly\n"
            "* There's 318 lines of code just to control the basic functionality of our array\n"
            "  * And this is just for 1D Arrays!\n"
            "  * But now we can do all the element by element mathematical operations using Python's built-in operators\n"
        )

    # ==================================================================================================================
    #                                                                                             topLevel8 text methods
    # ==================================================================================================================
    def topLevel8_Child0_text(self):
        self.write_code = '''\
class Rectangle:

    class Point:

        def __init__(self, x, y):
            self.__p = (x, y)

        def __str__(self):
            return str(self.__p)

    def __init__(self, L, W):

        self.L = L
        self.W = W

        self.bottom_left  = self.Point(-0.5*W, -0.5*L)
        self.bottom_right = self.Point( 0.5*W, -0.5*L)
        self.top_right    = self.Point( 0.5*W,  0.5*L)
        self.top_left     = self.Point(-0.5*W,  0.5*L)

    def __str__(self):
        return f"""\\
LENGTH: {self.L}
WIDTH:  {self.W}
POINTS:
    Bottom Left:  {self.bottom_left}
    Bottom Right: {self.bottom_right}
    Top Right:    {self.top_right}
    Top Left:     {self.top_left}\\
"""

if __name__ == '__main__':

    r = Rectangle(4, 2)
    print(r)
    p = Rectangle.Point(0, 0)
'''
        self.write_markdown = (
            "* You can define classes that are within the scope of other classes\n"
            "* Here we have an outer class `Rectangle` and the inner class `Point`\n"
            "* Each class has their own `__init__()` constructor and `__str__()` method\n"
            "* We pass a length and width to the `Rectangle` class and it will calculate the locations of its four points\n"
            "* The inner class can be accessed by the outer class with the `self.` syntax similar to attributes and methods\n"
            "* We can access the `Point` class outside of the `Rectangle` class with `p = Rectangle.Point(0, 0)`\n"
        )

    def topLevel8_Child1a_text(self):
        self.write_code = (
            "import json\n"
            "\n"
            "\n"
            "# example dictionary to serialize with json\n"
            "d = {\n"
            "    'a': 0,\n"
            "    'b': 1.0,\n"
            "    'c': '2',\n"
            "    'd': True,\n"
            "    'e': None,\n"
            "    'f': {\n"
            "        'a': 0,\n"
            "        'b': 1.0,\n"
            "        'c': '2',\n"
            "        'd': True,\n"
            "        'e': None,\n"
            "    },\n"
            "    'g': [0, 1.0, '2', True, None],\n"
            "    7: (0, 1.0, '2', True, None),\n"
            "}\n"
            "\n"
            "\n"
            "# serialize dictionary to json file\n"
            "with open('serialization.json', 'w') as f:\n"
            "    json.dump(d, f, indent='\\t')\n"
        )
        self.write_markdown = (
            "* Object serialization means that we serialize an object to a series of bytes for later use\n"
            "  * Another way of describing this is that we are saving objects to files\n"
            "* JSON stands for JavaScript Object Notation and is a popular method of serialization because it saves data to plain text\n"
            "* Because the data is plain text, it makes it easy to serialize data for use between different programming languages\n"
            "* JSON is very restrictive in the types of data that can be included. You are limited to:\n"
            "  * Dictionaries\n"
            "  * Floats\n"
            "  * Integers\n"
            "  * Strings\n"
            "  * Booleans\n"
            "  * None (or Null)\n"
            "  * Arrays (in the form of Lists and Tuples)\n"
            "* Some things to note between the dictionary we created and the json file output\n"
            "  * Some of the data has been transformed into the JavaScript equivalent\n"
            "    * Booleans are lower case, `None` has become `null`\n"
            "  * The `7` integer key we used in our dictionary is now a string\n"
            "    * Keep that in mind if you are ever using loop variables as keys\n"
            '  * The tuple that we assigned to `7` is now square brackets, just like "g"\n'
        )

    def topLevel8_Child1b_text(self):
        self.write_code = (
            "import json\n"
            "\n"
            "\n"
            "# read json file and print type of 'h' key value\n"
            "with open('serialization.json', 'r') as f:\n"
            "    data = json.load(f)\n"
            "print(type(data['7']))\n"
            "print(type(data))\n"
        )
        self.write_markdown = (
            "* Let's see what happens when we load in this serialized JSON data\n"
            "  * Notice that we have to use a string of 7 for that key now\n"
            "  * The tuple that we created has been transformed to a list\n"
            '    * Tuples are "immutable" meaning that they cannot be edited once created\n'
            "    * We lost that immutability when we serialized to json\n"
            "  * `data` is a dictionary type\n"
            "    * There is no `json` data type, it is just a serialization protocol\n"
            "    * `data` is a dictionary because that is what we created, json will also load to a list or one of the other data types depending on the file contents\n"
            '      * Strings must be defined inside of ""\n'
        )

    def topLevel8_Child2a_text(self):
        self.write_code = (
            "import pickle\n"
            "\n"
            "\n"
            "# example class to serialize with pickle\n"
            "class serializeThis:\n"
            "\n"
            "    def __init__(self):\n"
            "        self.a = 0\n"
            "        self.b = 1.0\n"
            "        self.c = '1'\n"
            "        self.d = True\n"
            "        self.e = None\n"
            "        self.f = {\n"
            "            'a': 0,\n"
            "            'b': 1.0,\n"
            "            'c': '2',\n"
            "            'd': True,\n"
            "            'e': None,\n"
            "        }\n"
            "        self.g = [0, 1.0, '2', True, None]\n"
            "        self.h = (0, 1.0, '2', True, None)\n"
            "\n"
            "    def printA(self):\n"
            "        print('a:', self.a)\n"
            "\n"
            "\n"
            "# create and pickle an object of the class serializeThis\n"
            "obj = serializeThis()\n"
            "with open('serialization.p', 'wb') as f:\n"
            "    pickle.dump(obj, f)\n"
        )
        self.write_markdown = (
            "* `pickle` is another serialization module and this one is exclusive to Python\n"
            "* When you pickle vegetables, you process them and store them for later user\n"
            "  * That is where this module gets its name\n"
            "* Because `pickle` is Python-exclusive, you can serialize more than just the data types available to json\n"
            "  * You can even serialize objects from custom classes!\n"
            "* Here I have created a class with a similar structure as the dictionary in the JSON Serialization example\n"
            "  * I have included a method that will print the `a` attribute\n"
            "* The serialization process looks very similar to the process for json serialization\n"
            "  * Now we include a `b` when we write though because we are writing in binary\n"
        )

    def topLevel8_Child2b_text(self):
        self.write_code = (
            "import pickle\n"
            "from oopDemo import serializeThis\n"
            "\n"
            "# load serialized object, run method, pass obj2 to dir()\n"
            "with open('serialization.p', 'rb') as f:\n"
            "    obj2 = pickle.load(f)\n"
            "obj2.printA()\n"
            "print(type(obj2))\n"
            "print(dir(obj2))\n"
        )
        self.write_markdown = (
            "* Some items to note with pickle serialization\n"
            "  * The output is not in a human readable format\n"
            "    * We can see some words but overall we can derive nothing meaningful from this\n"
            "  * We can unpickle the file, and we still have access to the method defined in the class\n"
            "  * Even though we do not have an explicit call to the class, we still need to include it in our imports\n"
            "    * If I comment out the import line, and run the pickling of the class again, the unpickle will fail\n"
            "    * If I did not run the pickling again it would have loaded without issue because of information included in `__pycache__/`\n"
            "* Be careful to only unpickle data that you know is safe\n"
            "  * Someone could easily pickle malicious code\n"
            "* As of Python 3.8.2, `pickle` is faster than `JSON`\n"
        )

    # ==================================================================================================================
    #                                                                                             topLevel9 text methods
    # ==================================================================================================================
    def topLevel9_Child0_text(self):
        self.write_code = (
            "import sys\n"
            "from PyQt6.QtWidgets import *\n"
            "\n"
            "\n"
            "class Main(QMainWindow):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "\n"
            "        # window properties\n"
            "        self.setWindowTitle('Qt Demo')\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "\n"
            "    app = QApplication(sys.argv)\n"
            "    main = Main()\n"
            "    main.show()\n"
            "    sys.exit(app.exec())\n"
        )
        self.write_markdown = (
            "PyQt is a wrapper for the C++ Qt Framework. It allows users to create visually-appealing, powerful GUI Applications. Guides for PyQt almost exclusively use Object-Oriented Programming.\n"
            "To create a very basic GUI Application we must include the lines:\n"
            "   app = QApplication(sys.argv)\n"
            "   sys.exit(app.exec())\n"
            "Between these two lines we can initialize our program.\n"
            "\n"
            "We create the program by subclassing `QMainWindow`\n"
            "This program will create an empty window\n"
        )

    def topLevel9_Child1_text(self):
        self.write_code = (
            "import sys\n"
            "from PyQt6.QtWidgets import *\n"
            "\n"
            "\n"
            "class Main(QMainWindow):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "\n"
            "        # window properties\n"
            "        self.setWindowTitle('Qt Demo')\n"
            "\n"
            "        # main layout\n"
            "        widget = QWidget()\n"
            "        self.setCentralWidget(widget)\n"
            "        layout = QGridLayout()\n"
            "        widget.setLayout(layout)\n"
            "\n"
            "        # label with text\n"
            "        self.lbl = QLabel('Hello World!')\n"
            "        layout.addWidget(self.lbl)\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "\n"
            "    app = QApplication(sys.argv)\n"
            "    main = Main()\n"
            "    main.show()\n"
            "    sys.exit(app.exec())\n"
        )
        self.write_markdown = (
            "The structure of the QMainWindow is illustrated at: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMainWindow.html#qt-main-window-framework\n"
            "We will not cover all elements of `QMainWindow` in this demo; only `Central Widget` and `Menu Bar`\n"
            "Here we see how to set the window title and central widget\n"
            "We also see how to add a widget to the window\n"
        )

    def topLevel9_Child2_text(self):
        self.write_code = (
            "import sys\n"
            "from PyQt6.QtWidgets import *\n"
            "\n"
            "\n"
            "class Main(QMainWindow):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "\n"
            "        # window properties\n"
            "        self.setWindowTitle('Qt Demo')\n"
            "\n"
            "        # main layout\n"
            "        widget = QWidget()\n"
            "        self.setCentralWidget(widget)\n"
            "        layout = QGridLayout()\n"
            "        widget.setLayout(layout)\n"
            "\n"
            "        # left label counter\n"
            "        self.lbl_left = QLabel('0')\n"
            "        layout.addWidget(self.lbl_left)\n"
            "\n"
            "        # right label counter\n"
            "        self.lbl_right = QLabel('0')\n"
            "        layout.addWidget(self.lbl_right, 0, 1)\n"
            "\n"
            "        # counter button\n"
            "        self.btn = QPushButton('Count')\n"
            "        self.btn.pressed.connect(self.counterLeft)\n"
            "        self.btn.released.connect(self.counterRight)\n"
            "        layout.addWidget(self.btn, 1, 0, 1, 2)\n"
            "\n"
            "        # counter attributes\n"
            "        self.countLeft  = 0\n"
            "        self.countRight = 0\n"
            "\n"
            "    def counterLeft(self):\n"
            "\n"
            "        self.countLeft += 1\n"
            "        self.lbl_left.setText(str(self.countLeft))\n"
            "\n"
            "    def counterRight(self):\n"
            "\n"
            "        self.countRight += 1\n"
            "        self.lbl_right.setText(str(self.countRight))\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "\n"
            "    app = QApplication(sys.argv)\n"
            "    main = Main()\n"
            "    main.show()\n"
            "    sys.exit(app.exec())\n"
        )
        self.write_markdown = (
            "Qt works on the ideas of signals, not commands. In Tkinter when you program a button, you set the function to run when the user clicks the button. In Qt each element has different signals associated with it, and we can connect these signals to as many operations as we wish.\n"
            "In this demo we created two labels, and we link two different signals of the same button to update each one.\n"
            "We see that when we first click the button the label on the left will increment, and when we release the button the label on the right will increment.\n"
        )

    def topLevel9_Child3_text(self):
        self.write_code = (
            "import sys, time\n"
            "from PyQt6.QtWidgets import *\n"
            "\n"
            "\n"
            "class Main(QMainWindow):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "\n"
            "        # window properties\n"
            "        self.setWindowTitle('Qt Demo')\n"
            "\n"
            "        # main layout\n"
            "        widget = QWidget()\n"
            "        self.setCentralWidget(widget)\n"
            "        layout = QGridLayout()\n"
            "        widget.setLayout(layout)\n"
            "\n"
            "        # label with text\n"
            "        self.lbl = QLabel('0')\n"
            "        layout.addWidget(self.lbl)\n"
            "\n"
            "        # counter button\n"
            "        self.btn = QPushButton('Start Counting')\n"
            "        self.btn.released.connect(self.startCounting)\n"
            "        layout.addWidget(self.btn)\n"
            "        self.counting = False\n"
            "        self.count = 0\n"
            "\n"
            "    def startCounting(self):\n"
            "\n"
            "        self.btn.released.disconnect(self.startCounting)\n"
            "        self.btn.released.connect(self.stopCounting)\n"
            "        self.btn.setText('Stop Counting')\n"
            "\n"
            "        self.counting = True\n"
            "\n"
            "        while self.counting:\n"
            "            time.sleep(1)\n"
            "            self.count += 1\n"
            "            print(self.count)\n"
            "\n"
            "    def stopCounting(self):\n"
            "        self.btn.setText('Start Counting')\n"
            "        self.btn.released.disconnect(self.stopCounting)\n"
            "        self.btn.released.connect(self.startCounting)\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "\n"
            "    app = QApplication(sys.argv)\n"
            "    main = Main()\n"
            "    main.show()\n"
            "    sys.exit(app.exec())\n"
        )
        self.write_markdown = (
            "Signals can be disconnected too. In this script we release our previously linked signal with the `released` command.\n"
            "We then link to another method that will continuously count and update our label. The method will first disconnect the signal to itself and then connect the signal to the `stopCounting` method.\n"
            "\n"
            "This Window freezes though and we do not see anything being updated, but we are still printing out what the numbers should be set to, so what is going on?\n"
            "GUI Windows are very sensitive to thread management. The program itself is operating on the _main_ thread and any time we click a button or run a function/method, that is _also_ running on the main thread.\n"
            "This means that every operation we are doing is blocking our main thread from managing our GUI. If the main thread is blocked for long enough, then the GUI window appears to be frozen.\n"
            "\n"
            "Any long running operation needs to be transferred to a different thread. Qt has its own threading module that we can use to do this.\n"
        )

    def topLevel9_Child4_text(self):
        self.write_code = (
            "import time\n"
            "\n"
            "\n"
            "class longTask:\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "        self.counting = True\n"
            "        self.time = None\n"
            "        self.counter = 0\n"
            "\n"
            "    def count(self):\n"
            "        while self.counting:\n"
            "            time.sleep(1)\n"
            "            self.counter += 1\n"
            "            print(self.counter)\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "\n"
            "    task = longTask()\n"
            "    task.count()\n"
        )
        self.write_markdown = (
            "First we create a class in a script that is completely separate from any Qt Code.\n"
            "You could set this up in the same script, especially for something this simple, but in general this makes testing easier before implementing into the main code.\n"
            "\n"
            "We create the `self.counter` attribute rather than use a local variable because we know that we will need to access this information later in our main code.\n"
            "\n"
            "The `while` loop will be an infinite loop because we have not put in a mechanism to change the value of `self.counting` but that will change when we implement into the main code.\n"
        )

    def topLevel9_Child5_text(self):
        self.write_code = (
            "import sys, time\n"
            "from PyQt6.QtWidgets import *\n"
            "from PyQt6.QtCore import *\n"
            "\n"
            "\n"
            "class longTask(QObject):\n"
            "\n"
            "    progress = pyqtSignal(int)\n"
            "    finished = pyqtSignal()\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "        self.counting = True\n"
            "        self.time = None\n"
            "        self.counter = 0\n"
            "\n"
            "    def count(self):\n"
            "        while self.counting:\n"
            "            self.progress.emit(self.counter)\n"
            "            time.sleep(1)\n"
            "            self.counter += 1\n"
            "            # print(x)\n"
            "        self.finished.emit()\n"
            "\n"
            "\n"
            "class Main(QMainWindow):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "\n"
            "        # window properties\n"
            "        self.setWindowTitle('Qt Demo')\n"
            "\n"
            "        # main layout\n"
            "        widget = QWidget()\n"
            "        self.setCentralWidget(widget)\n"
            "        layout = QGridLayout()\n"
            "        widget.setLayout(layout)\n"
            "\n"
            "        # label with text\n"
            "        self.lbl = QLabel('0')\n"
            "        layout.addWidget(self.lbl)\n"
            "\n"
            "        # counter button\n"
            "        self.btn = QPushButton('Start Task')\n"
            "        self.btn.released.connect(self.startCounting)\n"
            "        layout.addWidget(self.btn)\n"
            "\n"
            "        # threading attributes\n"
            "        self.worker = None\n"
            "        self.thread = None\n"
            "\n"
            "    def startCounting(self):\n"
            "\n"
            "        self.btn.released.disconnect(self.startCounting)\n"
            "        self.btn.released.connect(self.stopCounting)\n"
            "        self.btn.setText('Stop Task')\n"
            "\n"
            "        self.worker = longTask()\n"
            "        self.thread = QThread(self)\n"
            "        self.worker.moveToThread(self.thread)\n"
            "\n"
            "        self.thread.started.connect(self.worker.count)\n"
            "        self.worker.finished.connect(self.thread.quit)\n"
            "        self.worker.finished.connect(self.worker.deleteLater)\n"
            "        self.worker.finished.connect(self.thread.deleteLater)\n"
            "        self.worker.progress.connect(self.updateLbl)\n"
            "\n"
            "        self.thread.start()\n"
            "\n"
            "    def stopCounting(self):\n"
            "        self.worker.counting = False\n"
            "        self.btn.setText('Start Task')\n"
            "        self.btn.released.disconnect(self.stopCounting)\n"
            "        self.btn.released.connect(self.startCounting)\n"
            "\n"
            "    def updateLbl(self, msg):\n"
            "        self.lbl.setText(str(msg))\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "\n"
            "    app = QApplication(sys.argv)\n"
            "    main = Main()\n"
            "    main.show()\n"
            "    sys.exit(app.exec())\n"
        )
        self.write_markdown = (
            "To implement this class into our main program we first have to edit our class that will run our long operation.\n"
            "We set it to subclass `QObject`, then create signals for this class that we will use to communicate with and send information to our main thread.\n"
            "We give an `int` type when we set up the `progress` signal so that we know we will be sending integers to our main thread with the `progress` signal.\n"
            "\n"
            "In our `startCounting` method, we still change our configuration to the button signals. From there we establish our long running task.\n"
            "\n"
            "We assign an attribute to an instance of our new class, and we create a separate thread to run it on using `QThread`, and then move the worker class to the new thread.\n"
            "\n"
            "We then link the signals for our operation. We link the `started` signal of our thread to the `count` method of our worker.\n"
            "When the worker emits the `finished` signal we need to `quit` the thread and delete both the thread and the worker.\n"
            "We also link the `progress` signal to a new method we named `updateLbl()` in our main class.\n"
            "\n"
            "`updateLbl()` will set the text of our label to the integer value it receives from our worker\n"
            "\n"
            "Errors that occur in other threads will not be made available to the user. Here we have this `print(x)` command in our long running task where `x` is undefined.\n"
            "If I run this code, we will not receive an error message. We have to make sure we catch all exceptions, and then transfer them to the main thread.\n"
        )

    def topLevel9_Child6_text(self):
        self.write_code = (
            "import sys, time\n"
            "from PyQt6.QtWidgets import *\n"
            "from PyQt6.QtCore import *\n"
            "\n"
            "\n"
            "class longTask(QObject):\n"
            "\n"
            "    progress = pyqtSignal(int)\n"
            "    finished = pyqtSignal()\n"
            "    error    = pyqtSignal(tuple)\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "        self.counting = True\n"
            "        self.time = None\n"
            "        self.counter = 0\n"
            "\n"
            "    def run(self):\n"
            "        try:\n"
            "            self.count()\n"
            "        except:\n"
            "            self.error.emit(sys.exc_info())\n"
            "\n"
            "    def count(self):\n"
            "        while self.counting:\n"
            "            self.progress.emit(self.counter)\n"
            "            time.sleep(1)\n"
            "            self.counter += 1\n"
            "        self.finished.emit()\n"
            "\n"
            "\n"
            "class Main(QMainWindow):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "\n"
            "        # window properties\n"
            "        self.setWindowTitle('Qt Demo')\n"
            "\n"
            "        # main layout\n"
            "        widget = QWidget()\n"
            "        self.setCentralWidget(widget)\n"
            "        layout = QGridLayout()\n"
            "        widget.setLayout(layout)\n"
            "\n"
            "        # label with text\n"
            "        self.lbl = QLabel('0')\n"
            "        layout.addWidget(self.lbl)\n"
            "\n"
            "        # counter button\n"
            "        self.btn = QPushButton('Start Task')\n"
            "        self.btn.released.connect(self.startCounting)\n"
            "        layout.addWidget(self.btn)\n"
            "\n"
            "        # threading attributes\n"
            "        self.worker = None\n"
            "        self.thread = None\n"
            "\n"
            "    def startCounting(self):\n"
            "\n"
            "        self.btn.released.disconnect(self.startCounting)\n"
            "        self.btn.released.connect(self.stopCounting)\n"
            "        self.btn.setText('Stop Task')\n"
            "\n"
            "        self.worker = longTask()\n"
            "        self.thread = QThread(self)\n"
            "        self.worker.moveToThread(self.thread)\n"
            "\n"
            "        self.thread.started.connect(self.worker.run)\n"
            "        self.worker.finished.connect(self.thread.quit)\n"
            "        self.worker.finished.connect(self.worker.deleteLater)\n"
            "        self.worker.finished.connect(self.thread.deleteLater)\n"
            "\n"
            "        self.worker.progress.connect(self.updateLbl)\n"
            "        self.worker.error.connect(self.error)\n"
            "\n"
            "        self.thread.start()\n"
            "\n"
            "    def stopCounting(self):\n"
            "        self.worker.counting = False\n"
            "        self.btn.setText('Start Task')\n"
            "        self.btn.released.disconnect(self.stopCounting)\n"
            "        self.btn.released.connect(self.startCounting)\n"
            "\n"
            "    def updateLbl(self, msg):\n"
            "        self.lbl.setText(str(msg))\n"
            "\n"
            "    @staticmethod\n"
            "    def error(err):\n"
            "        except_hook(err[0], err[1], err[2])\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "\n"
            "    def except_hook(exc_type, exc_value, tb):\n"
            "        sys.__excepthook__(exc_type, exc_value, tb)\n"
            "        main.close()\n"
            "        sys.exit(1)\n"
            "    sys.excepthook = except_hook\n"
            "\n"
            "    app = QApplication(sys.argv)\n"
            "    main = Main()\n"
            "    main.show()\n"
            "    sys.exit(app.exec())\n"
        )
        self.write_markdown = (
            "Under `if __name__ == '__main__'`, we create a function and override the default `excepthook` method of the `sys` module.\n"
            "This function will directly pass our error directly to the `__excepthook__` Dunder method of `sys`. It will then close our main window.\n"
            "\n"
            "We add a new method in our class `longTask` that will run our long operation and catch exceptions and send them to the main thread in a tuple.\n"
            "\n"
            "In our main class we create a new `staticmethod` that will send our error to our `except_hook` function that we created.\n"
        )

    def topLevel9_Child7_text(self):
        self.write_code = (
            "import sys, time\n"
            "from PyQt6.QtWidgets import *\n"
            "from PyQt6.QtCore import *\n"
            "from PyQt6.QtGui import *\n"
            "\n"
            "\n"
            "class longTask(QObject):\n"
            "\n"
            "    progress = pyqtSignal(int)\n"
            "    finished = pyqtSignal()\n"
            "    error    = pyqtSignal(tuple)\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "        self.counting = True\n"
            "        self.time = None\n"
            "        self.counter = 0\n"
            "\n"
            "    def run(self):\n"
            "        try:\n"
            "            self.count()\n"
            "        except:\n"
            "            self.error.emit(sys.exc_info())\n"
            "\n"
            "    def count(self):\n"
            "        while self.counting:\n"
            "            self.progress.emit(self.counter)\n"
            "            time.sleep(1)\n"
            "            self.counter += 1\n"
            "        self.finished.emit()\n"
            "\n"
            "\n"
            "class Main(QMainWindow):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "\n"
            "        # window properties\n"
            "        self.setWindowTitle('Qt Demo')\n"
            "\n"
            "        # main layout\n"
            "        widget = QWidget()\n"
            "        self.setCentralWidget(widget)\n"
            "        layout = QGridLayout()\n"
            "        widget.setLayout(layout)\n"
            "\n"
            "        # label with text\n"
            "        self.lbl = QLabel('0')\n"
            "        layout.addWidget(self.lbl)\n"
            "\n"
            "        # counter button\n"
            "        self.btn = QPushButton('Start Task')\n"
            "        self.btn.released.connect(self.startCounting)\n"
            "        layout.addWidget(self.btn)\n"
            "\n"
            "        # dropdown menu\n"
            "        menu = QComboBox()\n"
            "        menu.setPlaceholderText('Options')\n"
            "        menu.addItems(['Filled', 'Dropdown', 'Menu'])\n"
            "        layout.addWidget(menu)\n"
            "\n"
            "        # tab widget\n"
            "        tabs = QTabWidget()\n"
            "        tabs.setMovable(True)\n"
            "        layout.addWidget(tabs, 0, 1, 3, 2)\n"
            "\n"
            "        # image tab\n"
            "        imageTab = QWidget()\n"
            "        imageLayout = QHBoxLayout()\n"
            "        imageTab.setLayout(imageLayout)\n"
            "        imageLabel = QLabel()\n"
            "        imageLabel.setPixmap(QPixmap('image.jpg'))\n"
            "        imageLabel.setScaledContents(True)\n"
            "        imageLayout.addWidget(imageLabel)\n"
            "        tabs.addTab(imageTab, 'Image')\n"
            "\n"
            "        # text tab\n"
            "        textTab = QWidget()\n"
            "        textLayout = QVBoxLayout()\n"
            "        textTab.setLayout(textLayout)\n"
            "        tabText = QLabel('Tab Widget showing text')\n"
            "        textLayout.addWidget(tabText)\n"
            "        tabs.addTab(textTab, 'Text')\n"
            "\n"
            "        # line edit\n"
            "        self.line = QLineEdit()\n"
            "        self.line.setPlaceholderText('Enter text here')\n"
            "        layout.addWidget(self.line, 3, 0, 1, 3)\n"
            "\n"
            "        # check box\n"
            "        checkBox = QCheckBox('Check Box')\n"
            "        checkBox.setCheckState(Qt.CheckState.Checked)\n"
            "        layout.addWidget(checkBox)\n"
            "\n"
            "        # radio buttons\n"
            "        radioBtn1 = QRadioButton('Radio Button 1')\n"
            "        radioBtn1.setChecked(True)\n"
            "        radioBtn2 = QRadioButton('Radio Button 2')\n"
            "        layout.addWidget(radioBtn1, 4, 1)\n"
            "        layout.addWidget(radioBtn2, 4, 2)\n"
            "\n"
            "        # menu bar\n"
            "        menuBar = self.menuBar()\n"
            "        fileMenu = menuBar.addMenu('File')\n"
            "        menuBar.addMenu(fileMenu)\n"
            "\n"
            "        # file menu\n"
            "        act1 = QAction('These', self)\n"
            "        act2 = QAction('Do', self)\n"
            "        act3 = QAction('Nothing', self)\n"
            "        act4 = QAction('This Does', self)\n"
            "        act4.triggered.connect(self.printInput)\n"
            "        act4.setShortcut('Ctrl+p')\n"
            "        subMenu = fileMenu.addMenu('&More')\n"
            "\n"
            "        fileMenu.addAction(act1)\n"
            "        fileMenu.addAction(act2)\n"
            "        fileMenu.addAction(act3)\n"
            "        fileMenu.addSeparator()\n"
            "        fileMenu.addMenu(subMenu)\n"
            "\n"
            "        subMenu.addAction(act4)\n"
            "\n"
            "        # threading attributes\n"
            "        self.worker = None\n"
            "        self.thread = None\n"
            "\n"
            "    def startCounting(self):\n"
            "\n"
            "        self.btn.released.disconnect(self.startCounting)\n"
            "        self.btn.released.connect(self.stopCounting)\n"
            "        self.btn.setText('Stop Task')\n"
            "\n"
            "        self.worker = longTask()\n"
            "        self.thread = QThread(self)\n"
            "        self.worker.moveToThread(self.thread)\n"
            "\n"
            "        self.thread.started.connect(self.worker.run)\n"
            "        self.worker.finished.connect(self.thread.quit)\n"
            "        self.worker.finished.connect(self.worker.deleteLater)\n"
            "        self.worker.finished.connect(self.thread.deleteLater)\n"
            "\n"
            "        self.worker.progress.connect(self.updateLbl)\n"
            "        self.worker.error.connect(self.error)\n"
            "\n"
            "        self.thread.start()\n"
            "\n"
            "    def stopCounting(self):\n"
            "        self.worker.counting = False\n"
            "        self.btn.setText('Start Task')\n"
            "        self.btn.released.disconnect(self.stopCounting)\n"
            "        self.btn.released.connect(self.startCounting)\n"
            "\n"
            "    def updateLbl(self, msg):\n"
            "        self.lbl.setText(str(msg))\n"
            "\n"
            "    def printInput(self):\n"
            "        print(self.line.text())\n"
            "\n"
            "    @staticmethod\n"
            "    def error(err):\n"
            "        except_hook(err[0], err[1], err[2])\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "\n"
            "    def except_hook(exc_type, exc_value, tb):\n"
            "        sys.__excepthook__(exc_type, exc_value, tb)\n"
            "        main.close()\n"
            "        sys.exit(1)\n"
            "    sys.excepthook = except_hook\n"
            "\n"
            "    app = QApplication(sys.argv)\n"
            "    main = Main()\n"
            "    main.show()\n"
            "    sys.exit(app.exec())\n"
        )
        self.write_markdown = (
            "Here is a GUI Window that shows how to implement many common features used in Qt development.\n"
            "\n"
            "We still have our `longTask` class implemented the same way that we did in the previous code snippet.\n"
            "\n"
            "Here I have added the following:\n"
            "* A tab widget with the following tabs\n"
            "    * An image embedded in the tab\n"
            "    * A label displaying text\n"
            "* A dropdown menu with place holder text\n"
            "* A widget for user text input with place holder text\n"
            "* A check box\n"
            "* Two radio buttons\n"
            "    * Note that we do not need to give any command for Qt to know that only one of these radio buttons can be selected at a time\n"
            "* A menu bar filled with:\n"
            "    * Three actions that do nothing\n"
            "    * A sub menu with an action that prints the text in the user input line\n"
            "        * This also has a keyboard shortcut that is implemented with only one line\n"
            "\n"
            "You can see how Qt manages threads by starting the long, counting task and then using the input line and the `Ctll+p` command to print out the text without the operations delaying each other.\n"
        )

    def topLevel9_Child8_text(self):
        self.write_code = (
            "import sys, time\n"
            "from PyQt6.QtWidgets import *\n"
            "from PyQt6.QtCore import *\n"
            "from PyQt6.QtGui import *\n"
            "\n"
            "\n"
            "class longTask(QObject):\n"
            "\n"
            "    progress = pyqtSignal(int)\n"
            "    finished = pyqtSignal()\n"
            "    error    = pyqtSignal(tuple)\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "        self.counting = True\n"
            "        self.time = None\n"
            "        self.counter = 0\n"
            "\n"
            "    def run(self):\n"
            "        try:\n"
            "            self.count()\n"
            "        except:\n"
            "            self.error.emit(sys.exc_info())\n"
            "\n"
            "    def count(self):\n"
            "        while self.counting:\n"
            "            self.progress.emit(self.counter)\n"
            "            time.sleep(1)\n"
            "            self.counter += 1\n"
            "        self.finished.emit()\n"
            "\n"
            "\n"
            "class menu(QComboBox):\n"
            "\n"
            "    def __init__(self, placeholder, items):\n"
            "        super().__init__()\n"
            "        self.setPlaceholderText(placeholder)\n"
            "        self.addItems(items)\n"
            "\n"
            "\n"
            "class tabs(QTabWidget):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "        self.setMovable(True)\n"
            "\n"
            "\n"
            "class imageTab(QWidget):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "        layout = QHBoxLayout()\n"
            "        self.setLayout(layout)\n"
            "        lbl = QLabel()\n"
            "        lbl.setPixmap(QPixmap('image.jpg'))\n"
            "        lbl.setScaledContents(True)\n"
            "        layout.addWidget(lbl)\n"
            "\n"
            "\n"
            "class textTab(QWidget):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "        layout = QVBoxLayout()\n"
            "        self.setLayout(layout)\n"
            "        txt = QLabel('Tab Widget showing text')\n"
            "        layout.addWidget(txt)\n"
            "\n"
            "\n"
            "class line(QLineEdit):\n"
            "\n"
            "    def __init__(self, txt):\n"
            "        super().__init__()\n"
            "        self.setPlaceholderText(txt)\n"
            "\n"
            "\n"
            "class check(QCheckBox):\n"
            "\n"
            "    def __init__(self, txt):\n"
            "        super().__init__()\n"
            "        self.setText(txt)\n"
            "        self.setCheckState(Qt.CheckState.Checked)\n"
            "\n"
            "\n"
            "class Main(QMainWindow):\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "\n"
            "        # window properties\n"
            "        self.setWindowTitle('Qt Demo')\n"
            "\n"
            "        # main layout\n"
            "        widget = QWidget()\n"
            "        self.setCentralWidget(widget)\n"
            "        layout = QGridLayout()\n"
            "        widget.setLayout(layout)\n"
            "\n"
            "        # label with text\n"
            "        self.lbl = QLabel('0')\n"
            "        layout.addWidget(self.lbl)\n"
            "\n"
            "        # counter button\n"
            "        self.btn = QPushButton('Start Task')\n"
            "        self.btn.released.connect(self.startCounting)\n"
            "        layout.addWidget(self.btn)\n"
            "\n"
            "        # dropdown menu\n"
            "        self.menu = menu('Options', ['Filled', 'Dropdown', 'Menu'])\n"
            "        layout.addWidget(self.menu)\n"
            "\n"
            "        # tab widget\n"
            "        tabs = QTabWidget()\n"
            "        layout.addWidget(tabs, 0, 1, 3, 2)\n"
            "\n"
            "        # image tab\n"
            "        imgTab = imageTab()\n"
            "        tabs.addTab(imgTab, 'Image')\n"
            "\n"
            "        # text tab\n"
            "        txtTab = textTab()\n"
            "        tabs.addTab(txtTab, 'Text')\n"
            "\n"
            "        # line edit\n"
            "        self.line = line('Enter text here')\n"
            "        layout.addWidget(self.line, 3, 0, 1, 3)\n"
            "\n"
            "        # check box\n"
            "        checkBox = check('Check Box')\n"
            "        layout.addWidget(checkBox)\n"
            "\n"
            "        # radio buttons\n"
            "        radioBtn1 = QRadioButton('Radio Button 1')\n"
            "        radioBtn1.setChecked(True)\n"
            "        radioBtn2 = QRadioButton('Radio Button 2')\n"
            "        layout.addWidget(radioBtn1, 4, 1)\n"
            "        layout.addWidget(radioBtn2, 4, 2)\n"
            "\n"
            "        # menu bar\n"
            "        menuBar = self.menuBar()\n"
            "        fileMenu = menuBar.addMenu('File')\n"
            "        menuBar.addMenu(fileMenu)\n"
            "\n"
            "        # file menu\n"
            "        act1 = QAction('These', self)\n"
            "        act2 = QAction('Do', self)\n"
            "        act3 = QAction('Nothing', self)\n"
            "        act4 = QAction('This Does', self)\n"
            "        act4.triggered.connect(self.printInput)\n"
            "        act4.setShortcut('Ctrl+p')\n"
            "        subMenu = fileMenu.addMenu('&More')\n"
            "\n"
            "        fileMenu.addAction(act1)\n"
            "        fileMenu.addAction(act2)\n"
            "        fileMenu.addAction(act3)\n"
            "        fileMenu.addSeparator()\n"
            "        fileMenu.addMenu(subMenu)\n"
            "\n"
            "        subMenu.addAction(act4)\n"
            "\n"
            "        # threading attributes\n"
            "        self.worker = None\n"
            "        self.thread = None\n"
            "\n"
            "    def startCounting(self):\n"
            "\n"
            "        self.btn.released.disconnect(self.startCounting)\n"
            "        self.btn.released.connect(self.stopCounting)\n"
            "        self.btn.setText('Stop Task')\n"
            "\n"
            "        self.worker = longTask()\n"
            "        self.thread = QThread(self)\n"
            "        self.worker.moveToThread(self.thread)\n"
            "\n"
            "        self.thread.started.connect(self.worker.run)\n"
            "        self.worker.finished.connect(self.thread.quit)\n"
            "        self.worker.finished.connect(self.worker.deleteLater)\n"
            "        self.worker.finished.connect(self.thread.deleteLater)\n"
            "\n"
            "        self.worker.progress.connect(self.updateLbl)\n"
            "        self.worker.error.connect(self.error)\n"
            "\n"
            "        self.thread.start()\n"
            "\n"
            "    def stopCounting(self):\n"
            "        self.worker.counting = False\n"
            "        self.btn.setText('Start Task')\n"
            "        self.btn.released.disconnect(self.stopCounting)\n"
            "        self.btn.released.connect(self.startCounting)\n"
            "\n"
            "    def updateLbl(self, msg):\n"
            "        self.lbl.setText(str(msg))\n"
            "\n"
            "    def printInput(self):\n"
            "        print(self.line.text())\n"
            "\n"
            "    @staticmethod\n"
            "    def error(err):\n"
            "        except_hook(err[0], err[1], err[2])\n"
            "\n"
            "\n"
            "if __name__ == '__main__':\n"
            "\n"
            "    def except_hook(exc_type, exc_value, tb):\n"
            "        sys.__excepthook__(exc_type, exc_value, tb)\n"
            "        main.close()\n"
            "        sys.exit(1)\n"
            "    sys.excepthook = except_hook\n"
            "\n"
            "    app = QApplication(sys.argv)\n"
            "    main = Main()\n"
            "    main.show()\n"
            "    sys.exit(app.exec())\n"
        )
        self.write_markdown = (
            "This creates the same GUI Window as `qt-demo-7`, but creates subclasses for many of the GUI elements rather than setting their properties in the `__init__()` constructor.\n"
            "This is to further illustrate the interaction of these GUI Elements as objects. It also increases readability of the `__init__()` constructor of `class Main`.\n"
        )

    # ==================================================================================================================
    #                                                                                            update checkbox methods
    # ==================================================================================================================
    def update_topLevel0_checkbox(self):

        states = [
            self.topLevel0_Child0.checkState(0) == Qt.CheckState.Checked,
            self.topLevel0_Child1.checkState(0) == Qt.CheckState.Checked,
        ]

        if all(states):
            self.topLevel0.setCheckState(0, Qt.CheckState.Checked)
            self.progressDict["0"]["expanded"] = False
            self.progressDict["1"]["expanded"] = True
        elif any(states):
            self.topLevel0.setCheckState(0, Qt.CheckState.PartiallyChecked)
        else:
            self.topLevel0.setCheckState(0, Qt.CheckState.Unchecked)

    def update_topLevel1_checkbox(self):

        states = [
            self.topLevel1_Child0.checkState(0) == Qt.CheckState.Checked,
            self.topLevel1_Child1.checkState(0) == Qt.CheckState.Checked,
            self.topLevel1_Child2.checkState(0) == Qt.CheckState.Checked,
            self.topLevel1_Child3.checkState(0) == Qt.CheckState.Checked,
            self.topLevel1_Child4.checkState(0) == Qt.CheckState.Checked,
            self.topLevel1_Child5.checkState(0) == Qt.CheckState.Checked,
            self.topLevel1_Child6.checkState(0) == Qt.CheckState.Checked,
            self.topLevel1_Child7.checkState(0) == Qt.CheckState.Checked,
        ]

        if all(states):
            self.topLevel1.setCheckState(0, Qt.CheckState.Checked)
            self.progressDict["1"]["expanded"] = False
            self.progressDict["2"]["expanded"] = True
        elif any(states):
            self.topLevel1.setCheckState(0, Qt.CheckState.PartiallyChecked)
        else:
            self.topLevel1.setCheckState(0, Qt.CheckState.Unchecked)

    def update_topLevel2_checkbox(self):

        states = [
            self.topLevel2_Child0.checkState(0) == Qt.CheckState.Checked,
            self.topLevel2_Child1.checkState(0) == Qt.CheckState.Checked,
            self.topLevel2_Child2.checkState(0) == Qt.CheckState.Checked,
            self.topLevel2_Child3.checkState(0) == Qt.CheckState.Checked,
            self.topLevel2_Child4.checkState(0) == Qt.CheckState.Checked,
            self.topLevel2_Child5.checkState(0) == Qt.CheckState.Checked,
            self.topLevel2_Child6.checkState(0) == Qt.CheckState.Checked,
            self.topLevel2_Child7.checkState(0) == Qt.CheckState.Checked,
            self.topLevel2_Child8.checkState(0) == Qt.CheckState.Checked,
        ]

        if all(states):
            self.topLevel2.setCheckState(0, Qt.CheckState.Checked)
            self.progressDict["2"]["expanded"] = False
            self.progressDict["3"]["expanded"] = True
        elif any(states):
            self.topLevel2.setCheckState(0, Qt.CheckState.PartiallyChecked)
        else:
            self.topLevel2.setCheckState(0, Qt.CheckState.Unchecked)

    def update_topLevel3_checkbox(self):

        states = [
            self.topLevel3_Child0.checkState(0) == Qt.CheckState.Checked,
            self.topLevel3_Child1.checkState(0) == Qt.CheckState.Checked,
            self.topLevel3_Child2.checkState(0) == Qt.CheckState.Checked,
            self.topLevel3_Child3.checkState(0) == Qt.CheckState.Checked,
            self.topLevel3_Child4.checkState(0) == Qt.CheckState.Checked,
            self.topLevel3_Child5.checkState(0) == Qt.CheckState.Checked,
            self.topLevel3_Child6.checkState(0) == Qt.CheckState.Checked,
            self.topLevel3_Child7.checkState(0) == Qt.CheckState.Checked,
            self.topLevel3_Child8.checkState(0) == Qt.CheckState.Checked,
            self.topLevel3_Child9.checkState(0) == Qt.CheckState.Checked,
            self.topLevel3_Child10.checkState(0) == Qt.CheckState.Checked,
            self.topLevel3_Child11.checkState(0) == Qt.CheckState.Checked,
            self.topLevel3_Child12.checkState(0) == Qt.CheckState.Checked,
        ]

        if all(states):
            self.topLevel3.setCheckState(0, Qt.CheckState.Checked)
            self.progressDict["3"]["expanded"] = False
            self.progressDict["4"]["expanded"] = True
        elif any(states):
            self.topLevel3.setCheckState(0, Qt.CheckState.PartiallyChecked)
        else:
            self.topLevel3.setCheckState(0, Qt.CheckState.Unchecked)

    def update_topLevel4_checkbox(self):

        states = [
            self.topLevel4_Child0.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child1.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child2.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child3.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child4.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child5.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child6.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child7.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child8.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child9.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child10.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child11.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child12.checkState(0) == Qt.CheckState.Checked,
            self.topLevel4_Child13.checkState(0) == Qt.CheckState.Checked,
        ]

        if all(states):
            self.topLevel4.setCheckState(0, Qt.CheckState.Checked)
            self.progressDict["4"]["expanded"] = False
            self.progressDict["5"]["expanded"] = True
        elif any(states):
            self.topLevel4.setCheckState(0, Qt.CheckState.PartiallyChecked)
        else:
            self.topLevel4.setCheckState(0, Qt.CheckState.Unchecked)

    def update_topLevel5_checkbox(self):

        states = [
            self.topLevel5_Child0.checkState(0) == Qt.CheckState.Checked,
            self.topLevel5_Child1.checkState(0) == Qt.CheckState.Checked,
            self.topLevel5_Child2.checkState(0) == Qt.CheckState.Checked,
            self.topLevel5_Child3.checkState(0) == Qt.CheckState.Checked,
            self.topLevel5_Child4.checkState(0) == Qt.CheckState.Checked,
            self.topLevel5_Child5.checkState(0) == Qt.CheckState.Checked,
            self.topLevel5_Child6.checkState(0) == Qt.CheckState.Checked,
        ]

        if all(states):
            self.topLevel5.setCheckState(0, Qt.CheckState.Checked)
            self.progressDict["5"]["expanded"] = False
            self.progressDict["6"]["expanded"] = True
        elif any(states):
            self.topLevel5.setCheckState(0, Qt.CheckState.PartiallyChecked)
        else:
            self.topLevel5.setCheckState(0, Qt.CheckState.Unchecked)

    def update_topLevel6_checkbox(self):

        states = [
            self.topLevel6_Child0.checkState(0) == Qt.CheckState.Checked,
            self.topLevel6_Child1.checkState(0) == Qt.CheckState.Checked,
            self.topLevel6_Child2.checkState(0) == Qt.CheckState.Checked,
            self.topLevel6_Child3.checkState(0) == Qt.CheckState.Checked,
            self.topLevel6_Child4.checkState(0) == Qt.CheckState.Checked,
            self.topLevel6_Child5.checkState(0) == Qt.CheckState.Checked,
            self.topLevel6_Child6.checkState(0) == Qt.CheckState.Checked,
            self.topLevel6_Child7.checkState(0) == Qt.CheckState.Checked,
            self.topLevel6_Child8.checkState(0) == Qt.CheckState.Checked,
            self.topLevel6_Child9.checkState(0) == Qt.CheckState.Checked,
            self.topLevel6_Child10.checkState(0) == Qt.CheckState.Checked,
        ]

        if all(states):
            self.topLevel6.setCheckState(0, Qt.CheckState.Checked)
            self.progressDict["6"]["expanded"] = False
            self.progressDict["7"]["expanded"] = True
        elif any(states):
            self.topLevel6.setCheckState(0, Qt.CheckState.PartiallyChecked)
        else:
            self.topLevel6.setCheckState(0, Qt.CheckState.Unchecked)

    def update_topLevel7_checkbox(self):

        states = [
            self.topLevel7_Child0.checkState(0) == Qt.CheckState.Checked,
            self.topLevel7_Child1.checkState(0) == Qt.CheckState.Checked,
            self.topLevel7_Child2.checkState(0) == Qt.CheckState.Checked,
            self.topLevel7_Child3.checkState(0) == Qt.CheckState.Checked,
            self.topLevel7_Child4.checkState(0) == Qt.CheckState.Checked,
            self.topLevel7_Child5.checkState(0) == Qt.CheckState.Checked,
            self.topLevel7_Child6.checkState(0) == Qt.CheckState.Checked,
            self.topLevel7_Child7.checkState(0) == Qt.CheckState.Checked,
        ]

        if all(states):
            self.topLevel7.setCheckState(0, Qt.CheckState.Checked)
            self.progressDict["7"]["expanded"] = False
            self.progressDict["8"]["expanded"] = True
        elif any(states):
            self.topLevel7.setCheckState(0, Qt.CheckState.PartiallyChecked)
        else:
            self.topLevel7.setCheckState(0, Qt.CheckState.Unchecked)

    def update_topLevel8_checkbox(self):

        states = [
            self.topLevel8_Child0.checkState(0) == Qt.CheckState.Checked,
            self.topLevel8_Child1.checkState(0) == Qt.CheckState.Checked,
            self.topLevel8_Child2.checkState(0) == Qt.CheckState.Checked,
        ]

        if all(states):
            self.topLevel8.setCheckState(0, Qt.CheckState.Checked)
            self.progressDict["8"]["expanded"] = False
            self.progressDict["9"]["expanded"] = True
        elif any(states):
            self.topLevel8.setCheckState(0, Qt.CheckState.PartiallyChecked)
        else:
            self.topLevel8.setCheckState(0, Qt.CheckState.Unchecked)

    def update_topLevel9_checkbox(self):

        states = [
            self.topLevel9_Child0.checkState(0) == Qt.CheckState.Checked,
            self.topLevel9_Child1.checkState(0) == Qt.CheckState.Checked,
            self.topLevel9_Child2.checkState(0) == Qt.CheckState.Checked,
            self.topLevel9_Child3.checkState(0) == Qt.CheckState.Checked,
            self.topLevel9_Child4.checkState(0) == Qt.CheckState.Checked,
            self.topLevel9_Child5.checkState(0) == Qt.CheckState.Checked,
            self.topLevel9_Child6.checkState(0) == Qt.CheckState.Checked,
            self.topLevel9_Child7.checkState(0) == Qt.CheckState.Checked,
            self.topLevel9_Child8.checkState(0) == Qt.CheckState.Checked,
        ]

        if all(states):
            self.topLevel9.setCheckState(0, Qt.CheckState.Checked)
            self.progressDict["9"]["expanded"] = False
        elif any(states):
            self.topLevel9.setCheckState(0, Qt.CheckState.PartiallyChecked)
        else:
            self.topLevel9.setCheckState(0, Qt.CheckState.Unchecked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
