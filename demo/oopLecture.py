import sys, json, shutil, os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class Main(QMainWindow):

    # ==================================================================================================================
    #                                                                                                       init methods
    # ==================================================================================================================
    def __init__(self):
        super().__init__()

        # -----------------
        # window properties
        # -----------------
        self.setWindowTitle('OOP Lecture')
        self.layout = QGridLayout()
        self.setMinimumHeight(650)

        # ---------
        # shortcuts
        # ---------
        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')

        rstAct = QAction('Reset Lecture', self)
        rstAct.setShortcut('Ctrl+r')
        rstAct.triggered.connect(self.reset)
        fileMenu.addAction(rstAct)

        # ---------------------
        # functional attributes
        # ---------------------
        self.write_text    = ''
        self.write_comment = ''
        self.write_file = 'oopDemo.py'
        self.write_shared_file = ''

        # -------------------------
        # central widget and layout
        # -------------------------
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        # --------------------------
        # lecture progress json file
        # --------------------------
        self.progressFile = 'place.json'
        if not os.path.exists(self.progressFile):
            with open(self.progressFile) as f:
                json.dump({
                    "0": {
                        "expanded": True,
                        "children": {
                            "0": False,
                            "1": False,
                        }
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
                        }
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
                        }
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
                        }
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
                        }
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
                        }
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
                        }
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
                        }
                    },
                    "8": {
                        "expanded": False,
                        "children": {
                            "0": False,
                            "1": False,
                            "2": False,
                            "3": False,
                            "4": False,
                        }
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
                        }
                    },
                }, f, indent='\t')
        with open(self.progressFile, 'r') as f:
            self.progressDict = json.load(f)

        # ------------------------------
        # create tree and set properties
        # ------------------------------
        self.tree = QTreeWidget()
        self.tree.header().hide()
        self.tree.itemClicked.connect(self.itemSelected)
        self.layout.addWidget(self.tree)

        # ---------------
        # top level items
        # ---------------
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

        # --------------------
        # top level 0 children
        # --------------------
        self.topLevel0_Child0 = QTreeWidgetItem(self.topLevel0)
        self.topLevel0_Child1 = QTreeWidgetItem(self.topLevel0)

        # --------------------
        # top level 1 children
        # --------------------
        self.topLevel1_Child0 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child1 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child2 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child3 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child4 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child5 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child6 = QTreeWidgetItem(self.topLevel1)
        self.topLevel1_Child7 = QTreeWidgetItem(self.topLevel1)

        # --------------------
        # top level 2 children
        # --------------------
        self.topLevel2_Child0 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child1 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child2 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child3 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child4 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child5 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child6 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child7 = QTreeWidgetItem(self.topLevel2)
        self.topLevel2_Child8 = QTreeWidgetItem(self.topLevel2)

        # --------------------
        # top level 3 children
        # --------------------
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

        # --------------------
        # top level 4 children
        # --------------------
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

        # --------------------
        # top level 5 children
        # --------------------
        self.topLevel5_Child0 = QTreeWidgetItem(self.topLevel5)
        self.topLevel5_Child1 = QTreeWidgetItem(self.topLevel5)
        self.topLevel5_Child2 = QTreeWidgetItem(self.topLevel5)
        self.topLevel5_Child3 = QTreeWidgetItem(self.topLevel5)
        self.topLevel5_Child4 = QTreeWidgetItem(self.topLevel5)
        self.topLevel5_Child5 = QTreeWidgetItem(self.topLevel5)
        self.topLevel5_Child6 = QTreeWidgetItem(self.topLevel5)

        # --------------------
        # top level 6 children
        # --------------------
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

        # --------------------
        # top level 7 children
        # --------------------
        self.topLevel7_Child0 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child1 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child2 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child3 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child4 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child5 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child6 = QTreeWidgetItem(self.topLevel7)
        self.topLevel7_Child7 = QTreeWidgetItem(self.topLevel7)

        # --------------------
        # top level 8 children
        # --------------------
        self.topLevel8_Child0 = QTreeWidgetItem(self.topLevel8)
        self.topLevel8_Child1 = QTreeWidgetItem(self.topLevel8)
        self.topLevel8_Child2 = QTreeWidgetItem(self.topLevel8)

        # --------------------
        # top level 9 children
        # --------------------
        self.topLevel9_Child0 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child1 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child2 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child3 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child4 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child5 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child6 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child7 = QTreeWidgetItem(self.topLevel9)
        self.topLevel9_Child8 = QTreeWidgetItem(self.topLevel9)

        # ------------
        # init methods
        # ------------
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

        self.topLevel0.setText(0, 'How to set up a Class')
        self.topLevel0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel0.setExpanded(self.progressDict['0']['expanded'])
        self.tree.addTopLevelItem(self.topLevel0)

        self.topLevel1.setText(0, 'Class Attributes')
        self.topLevel1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.setExpanded(self.progressDict['1']['expanded'])
        self.tree.addTopLevelItem(self.topLevel1)

        self.topLevel2.setText(0, 'Methods')
        self.topLevel2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.setExpanded(self.progressDict['2']['expanded'])
        self.tree.addTopLevelItem(self.topLevel2)

        self.topLevel3.setText(0, '__init__() and Instance Attributes')
        self.topLevel3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.setExpanded(self.progressDict['3']['expanded'])
        self.tree.addTopLevelItem(self.topLevel3)

        self.topLevel4.setText(0, 'Subclassing')
        self.topLevel4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.setExpanded(self.progressDict['4']['expanded'])
        self.tree.addTopLevelItem(self.topLevel4)

        self.topLevel5.setText(0, 'Dunder Methods')
        self.topLevel5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.setExpanded(self.progressDict['5']['expanded'])
        self.tree.addTopLevelItem(self.topLevel5)

        self.topLevel6.setText(0, 'Objects, Objects, Everywhere')
        self.topLevel6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.setExpanded(self.progressDict['6']['expanded'])
        self.tree.addTopLevelItem(self.topLevel6)

        self.topLevel7.setText(0, 'Creating a new array data type')
        self.topLevel7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.setExpanded(self.progressDict['7']['expanded'])
        self.tree.addTopLevelItem(self.topLevel7)

        self.topLevel8.setText(0, 'Miscellaneous')
        self.topLevel8.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel8.setExpanded(self.progressDict['8']['expanded'])
        self.tree.addTopLevelItem(self.topLevel8)

        self.topLevel9.setText(0, 'PyQt6')
        self.topLevel9.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.setExpanded(self.progressDict['9']['expanded'])
        self.tree.addTopLevelItem(self.topLevel9)

    def initTopLevel0Children(self):

        self.topLevel0_Child0.setText(0, 'Basic Class')
        if self.progressDict['0']['children']['0']:
            self.topLevel0_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel0_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel0.addChild(self.topLevel0_Child0)

        self.topLevel0_Child1.setText(0, 'Initialize an object')
        if self.progressDict['0']['children']['1']:
            self.topLevel0_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel0_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel0.addChild(self.topLevel0_Child1)

        self.update_topLevel0_checkbox()

    def initTopLevel1Children(self):

        self.topLevel1_Child0.setText(0, 'Create a Class Attribute')
        if self.progressDict['1']['children']['0']:
            self.topLevel1_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child0)

        self.topLevel1_Child1.setText(0, 'Accessing Class Attributes')
        if self.progressDict['1']['children']['1']:
            self.topLevel1_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child1)

        self.topLevel1_Child2.setText(0, 'Memory Allocation 1')
        if self.progressDict['1']['children']['2']:
            self.topLevel1_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child2)

        self.topLevel1_Child3.setText(0, 'Memory Allocation 2')
        if self.progressDict['1']['children']['3']:
            self.topLevel1_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child3)

        self.topLevel1_Child4.setText(0, 'Memory Allocation 3')
        if self.progressDict['1']['children']['4']:
            self.topLevel1_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child4)

        self.topLevel1_Child5.setText(0, 'Memory Allocation 4')
        if self.progressDict['1']['children']['5']:
            self.topLevel1_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child5)

        self.topLevel1_Child6.setText(0, 'Memory Allocation 5')
        if self.progressDict['1']['children']['6']:
            self.topLevel1_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child6)

        self.topLevel1_Child7.setText(0, 'Private and Protected Attributes')
        if self.progressDict['1']['children']['7']:
            self.topLevel1_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel1_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel1.addChild(self.topLevel1_Child7)

        self.update_topLevel1_checkbox()

    def initTopLevel2Children(self):

        self.topLevel2_Child0.setText(0, 'Define a Method')
        if self.progressDict['2']['children']['0']:
            self.topLevel2_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child0)

        self.topLevel2_Child1.setText(0, 'Run a Method')
        if self.progressDict['2']['children']['1']:
            self.topLevel2_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child1)

        self.topLevel2_Child2.setText(0, 'Methods Operation 1')
        if self.progressDict['2']['children']['2']:
            self.topLevel2_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child2)

        self.topLevel2_Child3.setText(0, 'Methods Operation 2')
        if self.progressDict['2']['children']['3']:
            self.topLevel2_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child3)

        self.topLevel2_Child4.setText(0, 'Methods Operation 3')
        if self.progressDict['2']['children']['4']:
            self.topLevel2_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child4)

        self.topLevel2_Child5.setText(0, 'Methods Operation 4')
        if self.progressDict['2']['children']['5']:
            self.topLevel2_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child5)

        self.topLevel2_Child6.setText(0, 'Static Methods')
        if self.progressDict['2']['children']['6']:
            self.topLevel2_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child6)

        self.topLevel2_Child7.setText(0, 'Assigning New Methods')
        if self.progressDict['2']['children']['7']:
            self.topLevel2_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child7)

        self.topLevel2_Child8.setText(0, 'Private and Protected Methods')
        if self.progressDict['2']['children']['8']:
            self.topLevel2_Child8.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel2_Child8.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel2.addChild(self.topLevel2_Child8)

        self.update_topLevel2_checkbox()

    def initTopLevel3Children(self):

        self.topLevel3_Child0.setText(0, '__init__() 1')
        if self.progressDict['3']['children']['0']:
            self.topLevel3_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child0)

        self.topLevel3_Child1.setText(0, '__init__() 2')
        if self.progressDict['3']['children']['1']:
            self.topLevel3_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child1)

        self.topLevel3_Child2.setText(0, '__init__() 3')
        if self.progressDict['3']['children']['2']:
            self.topLevel3_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child2)

        self.topLevel3_Child3.setText(0, 'Instance Attributes')
        if self.progressDict['3']['children']['3']:
            self.topLevel3_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child3)

        self.topLevel3_Child4.setText(0, '__init__() 4')
        if self.progressDict['3']['children']['4']:
            self.topLevel3_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child4)

        self.topLevel3_Child5.setText(0, '__init__() 5')
        if self.progressDict['3']['children']['5']:
            self.topLevel3_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child5)

        self.topLevel3_Child6.setText(0, '__init__() 6')
        if self.progressDict['3']['children']['6']:
            self.topLevel3_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child6)

        self.topLevel3_Child7.setText(0, 'More Memory Allocation 1')
        if self.progressDict['3']['children']['7']:
            self.topLevel3_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child7)

        self.topLevel3_Child8.setText(0, 'More Memory Allocation 2')
        if self.progressDict['3']['children']['8']:
            self.topLevel3_Child8.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child8.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child8)

        self.topLevel3_Child9.setText(0, 'More Memory Allocation 3')
        if self.progressDict['3']['children']['9']:
            self.topLevel3_Child9.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child9.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child9)

        self.topLevel3_Child10.setText(0, 'More Memory Allocation 4')
        if self.progressDict['3']['children']['10']:
            self.topLevel3_Child10.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child10.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child10)

        self.topLevel3_Child11.setText(0, 'More Memory Allocation 5')
        if self.progressDict['3']['children']['11']:
            self.topLevel3_Child11.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child11.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child11)

        self.topLevel3_Child12.setText(0, 'More Memory Allocation 6')
        if self.progressDict['3']['children']['12']:
            self.topLevel3_Child12.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel3_Child12.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel3.addChild(self.topLevel3_Child12)

        self.update_topLevel3_checkbox()

    def initTopLevel4Children(self):

        self.topLevel4_Child0.setText(0, 'Basic Child Class 1')
        if self.progressDict['4']['children']['0']:
            self.topLevel4_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child0)

        self.topLevel4_Child1.setText(0, 'Basic Child Class 2')
        if self.progressDict['4']['children']['1']:
            self.topLevel4_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child1)

        self.topLevel4_Child2.setText(0, 'Basic Child Class 3')
        if self.progressDict['4']['children']['2']:
            self.topLevel4_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child2)

        self.topLevel4_Child3.setText(0, 'Basic Child Class 4')
        if self.progressDict['4']['children']['3']:
            self.topLevel4_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child3)

        self.topLevel4_Child4.setText(0, 'Inheritance 1')
        if self.progressDict['4']['children']['4']:
            self.topLevel4_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child4)

        self.topLevel4_Child5.setText(0, 'Inheritance 2')
        if self.progressDict['4']['children']['5']:
            self.topLevel4_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child5)

        self.topLevel4_Child6.setText(0, 'Inheritance 3')
        if self.progressDict['4']['children']['6']:
            self.topLevel4_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child6)

        self.topLevel4_Child7.setText(0, 'Child Methods 1')
        if self.progressDict['4']['children']['7']:
            self.topLevel4_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child7)

        self.topLevel4_Child8.setText(0, 'Child Methods 2')
        if self.progressDict['4']['children']['8']:
            self.topLevel4_Child8.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child8.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child8)

        self.topLevel4_Child9.setText(0, 'Protected vs. Private')
        if self.progressDict['4']['children']['9']:
            self.topLevel4_Child9.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child9.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child9)

        self.topLevel4_Child10.setText(0, 'Overriding __init__()')
        if self.progressDict['4']['children']['10']:
            self.topLevel4_Child10.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child10.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child10)

        self.topLevel4_Child11.setText(0, 'super().__init__()')
        if self.progressDict['4']['children']['11']:
            self.topLevel4_Child11.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child11.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child11)

        self.topLevel4_Child12.setText(0, 'Multilevel Inheritance')
        if self.progressDict['4']['children']['12']:
            self.topLevel4_Child12.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child12.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child12)

        self.topLevel4_Child13.setText(0, 'Multiple Inheritance')
        if self.progressDict['4']['children']['13']:
            self.topLevel4_Child13.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel4_Child13.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel4.addChild(self.topLevel4_Child13)

        self.update_topLevel4_checkbox()

    def initTopLevel5Children(self):

        self.topLevel5_Child0.setText(0, '__init__()')
        if self.progressDict['5']['children']['0']:
            self.topLevel5_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child0)

        self.topLevel5_Child1.setText(0, 'Printing an Object 1')
        if self.progressDict['5']['children']['1']:
            self.topLevel5_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child1)

        self.topLevel5_Child2.setText(0, 'Printing an Object 2')
        if self.progressDict['5']['children']['2']:
            self.topLevel5_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child2)

        self.topLevel5_Child3.setText(0, 'Adding Objects 1')
        if self.progressDict['5']['children']['3']:
            self.topLevel5_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child3)

        self.topLevel5_Child4.setText(0, 'Adding Objects 2')
        if self.progressDict['5']['children']['4']:
            self.topLevel5_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child4)

        self.topLevel5_Child5.setText(0, 'Adding Objects 3')
        if self.progressDict['5']['children']['5']:
            self.topLevel5_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child5)

        self.topLevel5_Child6.setText(0, 'Other Dunder Methods')
        if self.progressDict['5']['children']['6']:
            self.topLevel5_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel5_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel5.addChild(self.topLevel5_Child6)

        self.update_topLevel5_checkbox()

    def initTopLevel6Children(self):

        self.topLevel6_Child0.setText(0, 'And')
        if self.progressDict['6']['children']['0']:
            self.topLevel6_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child0)

        self.topLevel6_Child1.setText(0, 'I')
        if self.progressDict['6']['children']['1']:
            self.topLevel6_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child1)

        self.topLevel6_Child2.setText(0, 'Mean')
        if self.progressDict['6']['children']['2']:
            self.topLevel6_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child2)

        self.topLevel6_Child3.setText(0, 'Everywhere')
        if self.progressDict['6']['children']['3']:
            self.topLevel6_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child3)

        self.topLevel6_Child4.setText(0, 'Quiz 1')
        if self.progressDict['6']['children']['4']:
            self.topLevel6_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child4)

        self.topLevel6_Child5.setText(0, 'Quiz 2')
        if self.progressDict['6']['children']['5']:
            self.topLevel6_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child5)

        self.topLevel6_Child6.setText(0, 'Quiz 3')
        if self.progressDict['6']['children']['6']:
            self.topLevel6_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child6)

        self.topLevel6_Child7.setText(0, 'Quiz 4')
        if self.progressDict['6']['children']['7']:
            self.topLevel6_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child7)

        self.topLevel6_Child8.setText(0, 'Quiz 5')
        if self.progressDict['6']['children']['8']:
            self.topLevel6_Child8.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child8.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child8)

        self.topLevel6_Child9.setText(0, 'Quiz 6')
        if self.progressDict['6']['children']['9']:
            self.topLevel6_Child9.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child9.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child9)

        self.topLevel6_Child10.setText(0, 'Quiz 7')
        if self.progressDict['6']['children']['10']:
            self.topLevel6_Child10.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel6_Child10.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel6.addChild(self.topLevel6_Child10)

        self.update_topLevel6_checkbox()

    def initTopLevel7Children(self):

        self.topLevel7_Child0.setText(0, 'Lists 1')
        if self.progressDict['7']['children']['0']:
            self.topLevel7_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child0)

        self.topLevel7_Child1.setText(0, 'Lists 2')
        if self.progressDict['7']['children']['1']:
            self.topLevel7_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child1)

        self.topLevel7_Child2.setText(0, '"array" class 1')
        if self.progressDict['7']['children']['2']:
            self.topLevel7_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child2)

        self.topLevel7_Child3.setText(0, '"array" class 2')
        if self.progressDict['7']['children']['3']:
            self.topLevel7_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child3)

        self.topLevel7_Child4.setText(0, '"array" class 3')
        if self.progressDict['7']['children']['4']:
            self.topLevel7_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child4)

        self.topLevel7_Child5.setText(0, '"array" class 4')
        if self.progressDict['7']['children']['5']:
            self.topLevel7_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child5)

        self.topLevel7_Child6.setText(0, '"array" class 5')
        if self.progressDict['7']['children']['6']:
            self.topLevel7_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child6)

        self.topLevel7_Child7.setText(0, '"array" class 6')
        if self.progressDict['7']['children']['7']:
            self.topLevel7_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel7_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel7.addChild(self.topLevel7_Child7)

        self.update_topLevel7_checkbox()

    def initTopLevel8Children(self):

        self.topLevel8_Child0.setText(0, 'Inner Classes')
        if self.progressDict['8']['children']['0']:
            self.topLevel8_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel8_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel8.addChild(self.topLevel8_Child0)

        self.topLevel8_Child1.setText(0, 'JSON Serialization')
        if self.progressDict['8']['children']['1']:
            self.topLevel8_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel8_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel8.addChild(self.topLevel8_Child1)

        self.topLevel8_Child2.setText(0, 'Pickle Serialization')
        if self.progressDict['8']['children']['2']:
            self.topLevel8_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel8_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel8.addChild(self.topLevel8_Child2)

        self.update_topLevel8_checkbox()

    def initTopLevel9Children(self):

        self.topLevel9_Child0.setText(0, 'Create an Application')
        if self.progressDict['9']['children']['0']:
            self.topLevel9_Child0.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child0.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child0)

        self.topLevel9_Child1.setText(0, 'Add a Widget')
        if self.progressDict['9']['children']['1']:
            self.topLevel9_Child1.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child1.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child1)

        self.topLevel9_Child2.setText(0, 'Connect Button Signals')
        if self.progressDict['9']['children']['2']:
            self.topLevel9_Child2.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child2.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child2)

        self.topLevel9_Child3.setText(0, 'Long Running Task 1')
        if self.progressDict['9']['children']['3']:
            self.topLevel9_Child3.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child3.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child3)

        self.topLevel9_Child4.setText(0, 'Long Running Task 2')
        if self.progressDict['9']['children']['4']:
            self.topLevel9_Child4.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child4.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child4)

        self.topLevel9_Child5.setText(0, 'Long Running Task 3')
        if self.progressDict['9']['children']['5']:
            self.topLevel9_Child5.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child5.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child5)

        self.topLevel9_Child6.setText(0, 'Emit Error Signals to Main Thread')
        if self.progressDict['9']['children']['6']:
            self.topLevel9_Child6.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child6.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child6)

        self.topLevel9_Child7.setText(0, 'Other GUI Elements')
        if self.progressDict['9']['children']['7']:
            self.topLevel9_Child7.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child7.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child7)

        self.topLevel9_Child8.setText(0, 'Subclassing GUI Elements')
        if self.progressDict['9']['children']['8']:
            self.topLevel9_Child8.setCheckState(0, Qt.CheckState.Checked)
        else:
            self.topLevel9_Child8.setCheckState(0, Qt.CheckState.Unchecked)
        self.topLevel9.addChild(self.topLevel9_Child8)

        self.update_topLevel9_checkbox()

    # ==================================================================================================================
    #                                                                                                    rewrite methods
    # ==================================================================================================================
    def itemSelected(self, selection):

        # ---------------------------------
        # Section 0 - How to set up a Class
        # ---------------------------------
        if selection == self.topLevel0_Child0:
            if self.topLevel0_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel0_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['0']['children']['0'] = True
            self.update_topLevel0_checkbox()
            self.topLevel0_Child0_text()
            self.write_shared_file = 'scripts/section0_item0.py'
            self.writeText()
        elif selection == self.topLevel0_Child1:
            if self.topLevel0_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel0_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['0']['children']['1'] = True
            self.update_topLevel0_checkbox()
            self.topLevel0_Child1_text()
            self.write_shared_file = 'scripts/section0_item1.py'
            self.writeText()

        # ----------------------------
        # Section 1 - Class Attributes
        # ----------------------------
        elif selection == self.topLevel1_Child0:
            if self.topLevel1_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['1']['children']['0'] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child0_text()
            self.write_shared_file = 'scripts/section1_item0.py'
            self.writeText()
        elif selection == self.topLevel1_Child1:
            if self.topLevel1_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['1']['children']['1'] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child1_text()
            self.write_shared_file = 'scripts/section1_item1.py'
            self.writeText()
        elif selection == self.topLevel1_Child2:
            if self.topLevel1_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['1']['children']['2'] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child2_text()
            self.write_shared_file = 'scripts/section1_item2.py'
            self.writeText()
        elif selection == self.topLevel1_Child3:
            if self.topLevel1_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['1']['children']['3'] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child3_text()
            self.write_shared_file = 'scripts/section1_item3.py'
            self.writeText()
        elif selection == self.topLevel1_Child4:
            if self.topLevel1_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['1']['children']['4'] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child4_text()
            self.write_shared_file = 'scripts/section1_item4.py'
            self.writeText()
        elif selection == self.topLevel1_Child5:
            if self.topLevel1_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['1']['children']['5'] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child5_text()
            self.write_shared_file = 'scripts/section1_item5.py'
            self.writeText()
        elif selection == self.topLevel1_Child6:
            if self.topLevel1_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['1']['children']['6'] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child6_text()
            self.write_shared_file = 'scripts/section1_item6.py'
            self.writeText()
        elif selection == self.topLevel1_Child7:
            if self.topLevel1_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel1_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['1']['children']['7'] = True
            self.update_topLevel1_checkbox()
            self.topLevel1_Child7_text()
            self.write_shared_file = 'scripts/section1_item7.py'
            self.writeText()

        # -------------------
        # Section 2 - Methods
        # -------------------
        elif selection == self.topLevel2_Child0:
            if self.topLevel2_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['2']['children']['0'] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child0_text()
            self.write_shared_file = 'scripts/section2_item0.py'
            self.writeText()
        elif selection == self.topLevel2_Child1:
            if self.topLevel2_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['2']['children']['1'] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child1_text()
            self.write_shared_file = 'scripts/section2_item1.py'
            self.writeText()
        elif selection == self.topLevel2_Child2:
            if self.topLevel2_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['2']['children']['2'] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child2_text()
            self.write_shared_file = 'scripts/section2_item2.py'
            self.writeText()
        elif selection == self.topLevel2_Child3:
            if self.topLevel2_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['2']['children']['3'] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child3_text()
            self.write_shared_file = 'scripts/section2_item3.py'
            self.writeText()
        elif selection == self.topLevel2_Child4:
            if self.topLevel2_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['2']['children']['4'] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child4_text()
            self.write_shared_file = 'scripts/section2_item4.py'
            self.writeText()
        elif selection == self.topLevel2_Child5:
            if self.topLevel2_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['2']['children']['5'] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child5_text()
            self.write_shared_file = 'scripts/section2_item5.py'
            self.writeText()
        elif selection == self.topLevel2_Child6:
            if self.topLevel2_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['2']['children']['6'] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child6_text()
            self.write_shared_file = 'scripts/section2_item6.py'
            self.writeText()
        elif selection == self.topLevel2_Child7:
            if self.topLevel2_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['2']['children']['7'] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child7_text()
            self.write_shared_file = 'scripts/section2_item7.py'
            self.writeText()
        elif selection == self.topLevel2_Child8:
            if self.topLevel2_Child8.checkState(0) != Qt.CheckState.Checked:
                self.topLevel2_Child8.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['2']['children']['8'] = True
            self.update_topLevel2_checkbox()
            self.topLevel2_Child8_text()
            self.write_shared_file = 'scripts/section2_item8.py'
            self.writeText()

        # ----------------------------------------------
        # Section 3 - __init__() and Instance Attributes
        # ----------------------------------------------
        elif selection == self.topLevel3_Child0:
            if self.topLevel3_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['0'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child0_text()
            self.write_shared_file = 'scripts/section3_item0.py'
            self.writeText()
        elif selection == self.topLevel3_Child1:
            if self.topLevel3_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['1'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child1_text()
            self.write_shared_file = 'scripts/section3_item1.py'
            self.writeText()
        elif selection == self.topLevel3_Child2:
            if self.topLevel3_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['2'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child2_text()
            self.write_shared_file = 'scripts/section3_item2.py'
            self.writeText()
        elif selection == self.topLevel3_Child3:
            if self.topLevel3_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['3'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child3_text()
            self.write_shared_file = 'scripts/section3_item3.py'
            self.writeText()
        elif selection == self.topLevel3_Child4:
            if self.topLevel3_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['4'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child4_text()
            self.write_shared_file = 'scripts/section3_item4.py'
            self.writeText()
        elif selection == self.topLevel3_Child5:
            if self.topLevel3_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['5'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child5_text()
            self.write_shared_file = 'scripts/section3_item5.py'
            self.writeText()
        elif selection == self.topLevel3_Child6:
            if self.topLevel3_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['6'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child6_text()
            self.write_shared_file = 'scripts/section3_item6.py'
            self.writeText()
        elif selection == self.topLevel3_Child7:
            if self.topLevel3_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['7'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child7_text()
            self.write_shared_file = 'scripts/section3_item7.py'
            self.writeText()
        elif selection == self.topLevel3_Child8:
            if self.topLevel3_Child8.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child8.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['8'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child8_text()
            self.write_shared_file = 'scripts/section3_item8.py'
            self.writeText()
        elif selection == self.topLevel3_Child9:
            if self.topLevel3_Child9.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child9.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['9'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child9_text()
            self.write_shared_file = 'scripts/section3_item9.py'
            self.writeText()
        elif selection == self.topLevel3_Child10:
            if self.topLevel3_Child10.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child10.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['10'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child10_text()
            self.write_shared_file = 'scripts/section3_item10.py'
            self.writeText()
        elif selection == self.topLevel3_Child11:
            if self.topLevel3_Child11.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child11.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['11'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child11_text()
            self.write_shared_file = 'scripts/section3_item11.py'
            self.writeText()
        elif selection == self.topLevel3_Child12:
            if self.topLevel3_Child12.checkState(0) != Qt.CheckState.Checked:
                self.topLevel3_Child12.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['3']['children']['12'] = True
            self.update_topLevel3_checkbox()
            self.topLevel3_Child12_text()
            self.write_shared_file = 'scripts/section3_item12.py'
            self.writeText()

        # --------------------------------
        # Section 4 - Parents and Children
        # --------------------------------
        elif selection == self.topLevel4_Child0:
            if self.topLevel4_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['0'] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child0_text()
            self.write_shared_file = 'scripts/section4_item0.py'
            self.writeText()
        elif selection == self.topLevel4_Child1:
            if self.topLevel4_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['1'] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child1_text()
            self.write_shared_file = 'scripts/section4_item1.py'
            self.writeText()
        elif selection == self.topLevel4_Child2:
            if self.topLevel4_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['2'] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child2_text()
            self.write_shared_file = 'scripts/section4_item2.py'
            self.writeText()
        elif selection == self.topLevel4_Child3:
            if self.topLevel4_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['3'] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child3_text()
            self.write_shared_file = 'scripts/section4_item3.py'
            self.writeText()
        elif selection == self.topLevel4_Child4:
            if self.topLevel4_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['4'] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child4_text()
            self.write_shared_file = 'scripts/section4_item4.py'
            self.writeText()
        elif selection == self.topLevel4_Child5:
            if self.topLevel4_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['5'] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child5_text()
            self.write_shared_file = 'scripts/section4_item5.py'
            self.writeText()
        elif selection == self.topLevel4_Child6:
            if self.topLevel4_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['6'] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child6_text()
            self.write_shared_file = 'scripts/section4_item6.py'
            self.writeText()
        elif selection == self.topLevel4_Child7:
            if self.topLevel4_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['7'] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child7_text()
            self.write_shared_file = 'scripts/section4_item7.py'
            self.writeText()
        elif selection == self.topLevel4_Child8:
            if self.topLevel4_Child8.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child8.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['8'] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child8_text()
            self.write_shared_file = 'scripts/section4_item8.py'
            self.writeText()
        elif selection == self.topLevel4_Child9:
            if self.topLevel4_Child9.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child9.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['9'] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child9_text()
            self.write_shared_file = 'scripts/section4_item9.py'
            self.writeText()
        elif selection == self.topLevel4_Child10:
            if self.topLevel4_Child10.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child10.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['10'] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child10_text()
            self.write_shared_file = 'scripts/section4_item10.py'
            self.writeText()
        elif selection == self.topLevel4_Child11:
            if self.topLevel4_Child11.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child11.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['11'] = True
            self.update_topLevel4_checkbox()
            self.topLevel4_Child11_text()
            self.write_shared_file = 'scripts/section4_item11.py'
            self.writeText()
        elif selection == self.topLevel4_Child12:
            if self.topLevel4_Child12.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child12.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['12'] = True
            self.update_topLevel8_checkbox()
            self.topLevel4_Child12_text()
            self.write_shared_file = 'scripts/section4_item12.py'
            self.writeText()
        elif selection == self.topLevel4_Child13:
            if self.topLevel4_Child13.checkState(0) != Qt.CheckState.Checked:
                self.topLevel4_Child13.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['4']['children']['13'] = True
            self.update_topLevel8_checkbox()
            self.topLevel4_Child13_text()
            self.write_shared_file = 'scripts/section4_item13.py'
            self.writeText()

        # --------------------------
        # Section 5 - Dunder Methods
        # --------------------------
        elif selection == self.topLevel5_Child0:
            if self.topLevel5_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['5']['children']['0'] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child0_text()
            self.write_shared_file = 'scripts/section5_item0.py'
            self.writeText()
        elif selection == self.topLevel5_Child1:
            if self.topLevel5_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['5']['children']['1'] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child1_text()
            self.write_shared_file = 'scripts/section5_item1.py'
            self.writeText()
        elif selection == self.topLevel5_Child2:
            if self.topLevel5_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['5']['children']['2'] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child2_text()
            self.write_shared_file = 'scripts/section5_item2.py'
            self.writeText()
        elif selection == self.topLevel5_Child3:
            if self.topLevel5_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['5']['children']['3'] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child3_text()
            self.write_shared_file = 'scripts/section5_item3.py'
            self.writeText()
        elif selection == self.topLevel5_Child4:
            if self.topLevel5_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['5']['children']['4'] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child4_text()
            self.write_shared_file = 'scripts/section5_item4.py'
            self.writeText()
        elif selection == self.topLevel5_Child5:
            if self.topLevel5_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['5']['children']['5'] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child5_text()
            self.write_shared_file = 'scripts/section5_item5.py'
            self.writeText()
        elif selection == self.topLevel5_Child6:
            if self.topLevel5_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel5_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['5']['children']['6'] = True
            self.update_topLevel5_checkbox()
            self.topLevel5_Child6_text()
            self.write_shared_file = 'scripts/section5_item6.py'
            self.writeText()

        # ---------------------------------------
        # Section 6 - Object, Objects, Everywhere
        # ---------------------------------------
        elif selection == self.topLevel6_Child0:
            if self.topLevel6_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['6']['children']['0'] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child0_text()
            self.write_shared_file = 'scripts/section6_item0.py'
            self.writeText()
        elif selection == self.topLevel6_Child1:
            if self.topLevel6_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['6']['children']['1'] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child1_text()
            self.write_shared_file = 'scripts/section6_item1.py'
            self.writeText()
        elif selection == self.topLevel6_Child2:
            if self.topLevel6_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['6']['children']['2'] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child2_text()
            self.write_shared_file = 'scripts/section6_item2.py'
            self.writeText()
        elif selection == self.topLevel6_Child3:
            if self.topLevel6_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['6']['children']['3'] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child3_text()
            self.write_shared_file = 'scripts/section6_item3.py'
            self.writeText()
        elif selection == self.topLevel6_Child4:
            if self.topLevel6_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['6']['children']['4'] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child4_text()
            self.write_shared_file = 'scripts/section6_item4.py'
            self.writeText()
        elif selection == self.topLevel6_Child5:
            if self.topLevel6_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['6']['children']['5'] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child5_text()
            self.write_shared_file = 'scripts/section6_item5.py'
            self.writeText()
        elif selection == self.topLevel6_Child6:
            if self.topLevel6_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['6']['children']['6'] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child6_text()
            self.write_shared_file = 'scripts/section6_item6.py'
            self.writeText()
        elif selection == self.topLevel6_Child7:
            if self.topLevel6_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['6']['children']['7'] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child7_text()
            self.write_shared_file = 'scripts/section6_item7.py'
            self.writeText()
        elif selection == self.topLevel6_Child8:
            if self.topLevel6_Child8.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child8.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['6']['children']['8'] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child8_text()
            self.write_shared_file = 'scripts/section6_item8.py'
            self.writeText()
        elif selection == self.topLevel6_Child9:
            if self.topLevel6_Child9.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child9.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['6']['children']['9'] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child9_text()
            self.write_shared_file = 'scripts/section6_item9.py'
            self.writeText()
        elif selection == self.topLevel6_Child10:
            if self.topLevel6_Child10.checkState(0) != Qt.CheckState.Checked:
                self.topLevel6_Child10.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['6']['children']['10'] = True
            self.update_topLevel6_checkbox()
            self.topLevel6_Child10_text()
            self.write_shared_file = 'scripts/section6_item10.py'
            self.writeText()

        # ----------------------------------------
        # Section 7 - Create a new array data type
        # ----------------------------------------
        elif selection == self.topLevel7_Child0:
            if self.topLevel7_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['7']['children']['0'] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child0_text()
            self.write_shared_file = 'scripts/section7_item0.py'
            self.writeText()
        elif selection == self.topLevel7_Child1:
            if self.topLevel7_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['7']['children']['1'] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child1_text()
            self.write_shared_file = 'scripts/section7_item1.py'
            self.writeText()
        elif selection == self.topLevel7_Child2:
            if self.topLevel7_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['7']['children']['2'] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child2_text()
            self.write_shared_file = 'scripts/section7_item2.py'
            self.writeText()
        elif selection == self.topLevel7_Child3:
            if self.topLevel7_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['7']['children']['3'] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child3_text()
            self.write_shared_file = 'scripts/section7_item3.py'
            self.writeText()
        elif selection == self.topLevel7_Child4:
            if self.topLevel7_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['7']['children']['4'] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child4_text()
            self.write_shared_file = 'scripts/section7_item4.py'
            self.writeText()
        elif selection == self.topLevel7_Child5:
            if self.topLevel7_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['7']['children']['5'] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child5_text()
            self.write_shared_file = 'scripts/section7_item5.py'
            self.writeText()
        elif selection == self.topLevel7_Child6:
            if self.topLevel7_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['7']['children']['6'] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child6_text()
            self.write_shared_file = 'scripts/section7_item6.py'
            self.writeText()
        elif selection == self.topLevel7_Child7:
            if self.topLevel7_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel7_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['7']['children']['7'] = True
            self.update_topLevel7_checkbox()
            self.topLevel7_Child7_text()
            self.write_shared_file = 'scripts/section7_item7.py'
            self.writeText()

        # -------------------------
        # Section 8 - miscellaneous
        # -------------------------
        elif selection == self.topLevel8_Child0:
            if self.topLevel8_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel8_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['8']['children']['0'] = True
            self.update_topLevel8_checkbox()
            self.topLevel8_Child0_text()
            self.write_shared_file = 'scripts/section8_item0.py'
            self.writeText()
        elif selection == self.topLevel8_Child1:
            if self.topLevel8_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel8_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['8']['children']['1'] = True
            self.update_topLevel8_checkbox()

            self.topLevel8_Child1a_text()
            self.write_shared_file = 'scripts/section8_item1a.py'
            self.writeText()

            self.topLevel8_Child1b_text()
            self.write_shared_file = 'scripts/section8_item1b.py'
            self.write_file = 'oopDemo-b.py'
            self.writeText()
            self.write_file = 'oopDemo.py'
        elif selection == self.topLevel8_Child2:
            if self.topLevel8_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel8_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['8']['children']['2'] = True
            self.update_topLevel8_checkbox()

            self.topLevel8_Child2a_text()
            self.write_shared_file = 'scripts/section8_item2a.py'
            self.writeText()

            self.topLevel8_Child2b_text()
            self.write_shared_file = 'scripts/section8_item2b.py'
            self.write_file = 'oopDemo-b.py'
            self.writeText()
            self.write_file = 'oopDemo.py'

        # -----------------
        # Section 9 - PyQt6
        # -----------------
        elif selection == self.topLevel9_Child0:
            if self.topLevel9_Child0.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child0.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['9']['children']['0'] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child0_text()
            self.write_shared_file = 'scripts/section9_item0.py'
            self.writeText()
        elif selection == self.topLevel9_Child1:
            if self.topLevel9_Child1.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child1.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['9']['children']['1'] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child1_text()
            self.write_shared_file = 'scripts/section9_item1.py'
            self.writeText()
        elif selection == self.topLevel9_Child2:
            if self.topLevel9_Child2.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child2.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['9']['children']['2'] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child2_text()
            self.write_shared_file = 'scripts/section9_item2.py'
            self.writeText()
        elif selection == self.topLevel9_Child3:
            if self.topLevel9_Child3.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child3.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['9']['children']['3'] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child3_text()
            self.write_shared_file = 'scripts/section9_item3.py'
            self.writeText()
        elif selection == self.topLevel9_Child4:
            if self.topLevel9_Child4.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child4.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['9']['children']['4'] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child4_text()
            self.write_shared_file = 'scripts/section9_item4.py'
            self.writeText()
        elif selection == self.topLevel9_Child5:
            if self.topLevel9_Child5.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child5.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['9']['children']['5'] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child5_text()
            self.write_shared_file = 'scripts/section9_item5.py'
            self.writeText()
        elif selection == self.topLevel9_Child6:
            if self.topLevel9_Child6.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child6.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['9']['children']['6'] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child6_text()
            self.write_shared_file = 'scripts/section9_item6.py'
            self.writeText()
        elif selection == self.topLevel9_Child7:
            if self.topLevel9_Child7.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child7.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['9']['children']['7'] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child7_text()
            self.write_shared_file = 'scripts/section9_item7.py'
            self.writeText()
        elif selection == self.topLevel9_Child8:
            if self.topLevel9_Child8.checkState(0) != Qt.CheckState.Checked:
                self.topLevel9_Child8.setCheckState(0, Qt.CheckState.Checked)
                self.progressDict['9']['children']['8'] = True
            self.update_topLevel9_checkbox()
            self.topLevel9_Child8_text()
            self.write_shared_file = 'scripts/section9_item8.py'
            self.writeText()

    def writeText(self):
        os.makedirs('scripts/', exist_ok=True)
        with open(self.write_file, 'w') as f:
            f.write(self.write_text)
        with open(self.write_shared_file, 'w') as f:
            f.write(f"{self.write_text}\n\n{self.write_comment}")
        with open(self.progressFile, 'w') as f:
            json.dump(self.progressDict, f, indent='\t')

    def reset(self):
        if os.path.exists('scripts/'):
            shutil.rmtree('scripts/', ignore_errors=True)
        with open('place-default.json', 'r') as f:
            self.progressDict = json.load(f)
        with open(self.progressFile, 'w') as f:
            json.dump(self.progressDict, f, indent='\t')
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
        self.write_text = '''\
class ExampleA:
    pass
'''
        self.write_comment = '''\
# * Let's set up the most simple Class we can
# * This class does nothing and has no information associated with it
# * How do we initialize an Object (or Instance) of this Class?
'''

    def topLevel0_Child1_text(self):
        self.write_text = '''\
class ExampleA:
    pass


if __name__ == '__main__':
    a = ExampleA()
    print(isinstance(a, ExampleA))
'''
        self.write_comment = '''\
# * All we have to do in Python is call this class as shown
# * Here is a built-in function that can be useful:
#   * `isinstance(<var>, <class>)` will return a boolean value if a given variable is an instance of the given class
# * We can see that `isinstance()` returns `True` so `a` is an instance of our class `ExampleA`
# * Now that we know how the basics of using a class, let's make them actually do something
'''

    # ==================================================================================================================
    #                                                                                             topLevel1 text methods
    # ==================================================================================================================
    def topLevel1_Child0_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5
'''
        self.write_comment = '''\
# * Here is how we create a Class Attribute
#   * Looks almost exactly the same as creating a variable
# * Now `x` is an Attribute of the Class `ExampleA`
# * How can our main script access `x`?
'''

    def topLevel1_Child1_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5


if __name__ == '__main__':
    print(ExampleA.x)

    a = ExampleA()
    print(a.x)
'''
        self.write_comment = '''\
# * We have two ways of accessing Class Attributes:
#   * We can access it by `<class name>.<attribute name>`
#   * Or we can create an instance of the class and access it by `<instance variable>.<attribute name>`
# * A very important aspect of Object-Oriented Programming in Python is understanding how Python is managing memory
#   * Let's see how Python is allocating memory for these objects
'''

    def topLevel1_Child2_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5


if __name__ == '__main__':
    a = ExampleA()
    print(id(a) == id(ExampleA))
'''
        self.write_comment = '''\
# * Python has this interesting built in `id()` function
# * This function returns the memory address of whatever is passed to it

# POLL: True or False: An instance of this class has the same memory address as the class itself

# Answer: False

# Explanation: The class will have a location in memory, but it is essentially acting as a blueprint to create unique instances
'''

    def topLevel1_Child3_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5


if __name__ == '__main__':
    a = ExampleA()
    print(id(a.x) == id(ExampleA.x))
'''
        self.write_comment = '''\
# * What about the memory address of the `x` attribute of this instance and directly accessing the `x` attribute?

# POLL: True or False: The `x` attribute of the object and the class will have the same memory address

# Answer: True

# Explanation: the attribute has a different memory address than the class and the object, and it has not changed
'''

    def topLevel1_Child4_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5


if __name__ == '__main__':
    a = ExampleA()
    a.x = 10
    print(id(a.x) == id(ExampleA.x))
'''
        self.write_comment = '''\
# * Now what will happen if I change the value of `x` for the instance of `ExampleA`?

# POLL: True or False: Changing the value of the `x` attribute will change the memory address of the attribute

# Answer: False

# Explanation: A memory location won't hold two sets of information, so it must move to a different memory location to hold the new value of `a.x`
'''

    def topLevel1_Child5_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5


if __name__ == '__main__':
    a = ExampleA()
    a.x = 5
    print(id(a.x) == id(ExampleA.x))
'''
        self.write_comment = '''\
# * What happens if I set `a.x` to a value, but it is the same value as the default in the class?

# POLL: True or False: Setting the `x` attribute to its original value will not change the memory address

# Answer: True

# Explanation: The value of the attribute does not change so Python will not change the memory address of the attribute
'''

    def topLevel1_Child6_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5


if __name__ == '__main__':
    a = ExampleA()
    a.x = 10
    a.x = 5
    print(id(a.x) == id(ExampleA.x))
'''
        self.write_comment = '''\
# * What happens if we set `a.x` to a different value and the set it back to the original value?

# POLL: True or False: Setting the attribute back to the original value will restore its original memory address

# Answer: True

# Explanation: There is already a location in memory for the original value of `a.x` so Python will return it to the same address
'''

    def topLevel1_Child7_text(self):
        self.write_text = '''\
class ExampleA:

    _x = 5
    __y = 10


if __name__ == '__main__':
    a = ExampleA()
    print('a._x', a._x)
    # print('a.__y', a.__y)
'''
        self.write_comment = '''\
# * If we want to create a Protected Attribute in Python we can add a single `_` prefix to the attribute name
# * We can still access this outside of the class but PyCharm does not like letting us do this
# * We can let PyCharm add a new method with a `property` decorator that returns the value of the protected attribute
#   * Now we are still getting the value of the `x` attribute, but we are not accessing the protected attribute directly
#   * This seems like a lot of extra work to add a seemingly unnecessary workaround, but this allows us to adhere to the Encapsulation Principle of Object-Oriented Programming
# * To make a Private Attribute we simply add a `__` prefix to the attribute name
#   * We can not access this attribute at all when our scope is outside the class
#   * Now we can set the visibility of our information and choose what we share outside the scope of the object following the Principle of Encapsulation
# * We will get into the differences between Private and Protected attributes in the `Parents and Children` section
'''

    # ==================================================================================================================
    #                                                                                             topLevel2 text methods
    # ==================================================================================================================
    def topLevel2_Child0_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def printX(self):
        print(self.x)
'''
        self.write_comment = '''\
# Attributes are analogous to variables, and Methods are analogous to functions. Methods are special in that they have access to all attributes and other methods of the same class

# * Here we see how to create a method
# * As I just mentioned, methods are analogous to functions and they are defined
# * The key aspect to remember for methods is that you still have to pass this
# * This is the first time we have seen `self` so far, and it is very
#   * `self` is how an object refers to...itself within the class
#   * Passing `self` to a method may seem somewhat redundant but doing so is what gives the method access to all attributes and other methods of the class
# * How do we access/run a method of a class?

'''

    def topLevel2_Child1_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def printX(self):
        print(self.x)


if __name__ == '__main__':
    a = ExampleA()
    a.printX()
'''
        self.write_comment = '''\
# * If we are going to run a method we first have to create an instance of the class
# * Then we run it with the syntax `<instance name>.<method name>()`
# * What can we do with methods?
'''

    def topLevel2_Child2_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def updateX(self):
        self.x = 10


if __name__ == '__main__':
    a = ExampleA()
    print(a.x)
    a.updateX()
    print(a.x)
'''
        self.write_comment = '''\
# * We can use methods to modify attributes of the object like this
'''

    def topLevel2_Child3_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def updateX(self, val):
        self.x = val


if __name__ == '__main__':
    a = ExampleA()
    print(a.x)
    a.updateX(10)
    print(a.x)
'''
        self.write_comment = '''\
# * We can pass outside values into a method
'''

    def topLevel2_Child4_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def printX(self):
        print(self.x)

    def updateX(self, val):
        self.x = val
        self.printX()


if __name__ == '__main__':
    a = ExampleA()
    print(a.x)
    a.updateX(10)
'''
        self.write_comment = '''\
# * Methods can call other methods of the class
'''

    def topLevel2_Child5_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def getX(self):
        return self.x


if __name__ == '__main__':
    a = ExampleA()
    print(a.getX())
'''
        self.write_comment = '''\
# * Methods can also return values outside the class
# * This is another way that Objects interact with each other and also another way to access attributes, _even private and protected attributes_
'''

    def topLevel2_Child6_text(self):
        self.write_text = '''\
class ExampleA:

    @staticmethod
    def printHW():
        print('Hello World!')


if __name__ == '__main__':
    ExampleA.printHW()
'''
        self.write_comment = '''\
# * Static methods are a special kind of method that do not have access to the class attributes and other methods but still belong to the class
# * Notice that we no longer pass `self` as an argument into the method
#   * This is why we pass it to other methods even though it seems redundant
# * One interesting aspect of static methods is that we can access them without creating an instance of the class
'''

    def topLevel2_Child7_text(self):
        self.write_text = '''\
import numpy as np


class ExampleA:

    arr = np.array


if __name__ == '__main__':
    a = ExampleA()
    arr = a.arr([0, 1, 2, 3])
    print(type(arr))
    print(id(a.arr) == id(np.array))
'''
        self.write_comment = '''\
# * You can assign outside functions or methods to an attribute like this
# * Also notice that doing this does not change the memory address of the function
'''

    def topLevel2_Child8_text(self):
        self.write_text = '''\
class ExampleA:

    __x = 5
    __y = 10

    def _printX(self):
        print('__x', self.__x)

    def __printY(self):
        print('__y', self.__y)

    def print_params(self):
        self._printX()
        self.__printY()


if __name__ == '__main__':
    a = ExampleA()
    a._printX()
    # a.__printY()
    # a.print_params()
'''
        self.write_comment = '''\
# * Using the same syntax as private and protected attributes, we can create private and protected methods with the `_` and `__` prefix convention
# * Notice that both attributes here are Private Attributes
# * We can run a protected method from outside the class with no issue, but PyCharm is here to let us know that it is a protected method, and we should not do that
# * Similarly to private attributes, we do not have access to private methods outside the class
# * However, we can create a public method that can be accessed outside the class and has access to all protected and private information of the class
# * Remember back to the `Abstraction` Principle of Object-Oriented Programming
#   * We create Public methods that allow interaction with our object, but we hide the internal mechanisms of the object that we want to remain hidden
'''

    # ==================================================================================================================
    #                                                                                             topLevel3 text methods
    # ==================================================================================================================
    def topLevel3_Child0_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        pass
'''
        self.write_comment = '''\
# Now that we know how to create Class Attributes and Methods, we can get into the real nitty-gritty of classes; starting with a special method named `__init__()`
# * Here is what it will look like when we define `__init__()`
# * It does not look any different from any other method except for the double underscores
# * We still pass `self` as the first argument
# * So how do we run this `__init__()` method?
'''

    def topLevel3_Child1_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        print('Hello World!')


if __name__ == '__main__':
    a = ExampleA()
'''
        self.write_comment = '''\
# * Turns out we don't have to worry about it!
# * When we _initialize_ an object, Python will run the `__init__()` method automatically
# * But when does Python run `__init__()`?
'''

    def topLevel3_Child2_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        print(self.x)

    x = 5


if __name__ == '__main__':
    a = ExampleA()
'''
        self.write_comment = '''\
# * After all Class Attributes and other methods have been initialized too
# * `__init__()` can still access the `x` attribute even though it is defined above `x`
# * All methods and class attributes will be compiled during the initialization process before `__init__()` is executed
# * All this time I have been saying _Class_ attribute because there is another type of attribute called the Instance Attribute
'''

    def topLevel3_Child3_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        self.y = 10


if __name__ == '__main__':
    a = ExampleA()
    print('x:', a.x)
    print('y:', a.y)
    # print('x:', ExampleA.x)
    # print('y:', ExampleA.y)
'''
        self.write_comment = '''\
# * Here we are defining another attribute `y` in the `__init__()` method
# * They are accessed the same way as class attributes
# * What makes Instance Attributes different from Class Attributes?
#   * For starters, we _have_ to create an instance of this class to access the attribute
#   * We can not run this commented out line because `y` is an _Instance_ attribute
# * Let's see what else we can do with the `__init__()` method
'''

    def topLevel3_Child4_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self, value):
        self.x = value


if __name__ == '__main__':
    a = ExampleA(5)
    print(a.x)
'''
        self.write_comment = '''\
# * If we want to initialize an object with a value we can pass it into `__init__()` like this
# * Since we never directly call the `__init__()` method, this is how Python handles these passed values
# * This is another key difference between Instance and Class Attributes
#   * Class Attributes will be the same for all objects initialized from the class, unless intentionally changed
#   * Instance Attributes do not necessarily have to be the same
'''

    def topLevel3_Child5_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.initX()

    def initX(self):
        self.x = 5


if __name__ == '__main__':
    a = ExampleA()
    print(a.x)
'''
        self.write_comment = '''\
# * Like other methods, `__init__()` can call other methods
# * If the class I am writing has many attributes or needs to perform many actions during construction, I like to move some initialization procedure to other methods for readability
'''

    def topLevel3_Child6_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        pass

    def setX(self):
        self.x = 5


if __name__ == '__main__':
    a = ExampleA()
    print(a.x)
'''
        self.write_comment = '''\
# * A note on best practices
# * All attributes that the class will use should be in `__init__()` so that a new reader knows all attribute of the class from only inspecting `__init__()`
# * This also contributes to better usability
#   * If an attribute only gets defined in another method, and we forget to call that method then it will not exist
#   * PyCharm will not give us any error except for telling us that `self.x` should be added to `__init__()`
'''

    def topLevel3_Child7_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5


if __name__ == '__main__':
    a = ExampleA()
    id_a = id(a)
    a.x = 10
    print(id_a == id(a))
'''
        self.write_comment = '''\
# * What happens when we change an attribute of this instance; will the memory address change?

# POLL: True or False: Changing the value of an Instance Attribute will _not_ change the memory address of the object

# Answer: True

# Explanation: We are only changing an attribute of this object. Python does not need to create an entirely new object in memory just because of this small change so the memory address will remain the same.
'''

    def topLevel3_Child8_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5
        print('Hello World!')


if __name__ == '__main__':
    a = ExampleA()
    b = a
    print(id(a) == id(b))
'''
        self.write_comment = '''\
# * Let's create an instance of a class, and then assign another variable as equal to the first instance
# * Do we think that Python is going to run `__init__()` again? Will `a` and `b` have memory address?

# POLL: What will the printed output of this script?

# Answer: Hello World!\\nTrue

# Explanation: Assigning `b` as equal to `a` does not run `__init__()` again, and they will have the same memory address
'''

    def topLevel3_Child9_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5
        print('Hello World!')


if __name__ == '__main__':
    a = ExampleA()
    b = a
    b.x = 10
'''
        self.write_comment = '''\
# * What about if we change the `x` attribute of `b`?

# POLL: What will the printed output of this script?

# Answer: Hello World!

# Explanation: Just changing the instance attribute will not run `__init__()` again
'''

    def topLevel3_Child10_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        print('Hello World!')


if __name__ == '__main__':
    a = ExampleA()
    b = a
    b.x = 10
'''
        self.write_comment = '''\
# * What if we change a Class Attribute instead? Will that run `__init__()` again?

# POLL: What will the printed output of this script?

# Answer: Hello World!

# Explanation: No. Changing any attribute of `b` will not run `__init__()` again
'''

    def topLevel3_Child11_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5


if __name__ == '__main__':
    a = ExampleA()
    b = a
    b.x = 10
    print(id(a) == id(b))
'''
        self.write_comment = '''\
# * Let's compare the memory addresses of `a` and `b`
# * We create and instance of our class, set `b` equal to `a`, then change `b.x`

# POLL: What will the output be?

# Answer: True

# What is going on here? We only changed the `x` attribute of `b`, not `a`. And I told you earlier that a memory address is not going to hold two sets of information, so that would mean that `a.x` must be equal to `10`, right?
'''

    def topLevel3_Child12_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5


if __name__ == '__main__':
    a = ExampleA()
    b = a
    b.x = 10
    print(a.x)
'''
        self.write_comment = '''\
# * It _is_ equal to 10!
#   * But we didn't change `a.x` so what is going on?
# * It turns out that by declaring `a = ExampleA()` what we are really doing is telling Python:
#   * "When I use the variable `a`, I am referring to something at a specific memory address"
# * Then, when we say that `b = a`, we are telling Python that `b` refers to the same memory address as `a`
# * So if we modify _any_ attribute of either `a` or `b`, we are modifying that attribute in both!
# * This can be useful if you understand what is going on and soooooooooo frustrating when you don't and have to learn this on your own
# * Now that we understand core fundamentals of classes, let's start looking at some more advanced aspects of OOP
'''

    # ==================================================================================================================
    #                                                                                             topLevel4 text methods
    # ==================================================================================================================
    def topLevel4_Child0_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        self.y = 10

    def printX(self):
        print(self.x)

    def printY(self):
        print(self.y)


class ExampleB(ExampleA):
    pass


if __name__ == '__main__':
    b = ExampleB()
'''
        self.write_comment = '''\
# * Here we have defined two classes, `ExampleA` and `ExampleB`
# * `ExampleB`  is considered a Child of the Parent class, `ExampleA`
#   * This relationship is also referred to as superclass and subclass, or base class and derived class
#   * I will also use subclass as a verb; such as `ExampleB` is subclassing `ExampleA`
# * We create an instance of `ExampleB` the same as we would any other class, but what is going on with `ExampleB`?
'''

    def topLevel4_Child1_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        self.y = 10

    def printX(self):
        print(self.x)

    def printY(self):
        print(self.y)


class ExampleB(ExampleA):
    pass


if __name__ == '__main__':
    b = ExampleB()
    print(isinstance(b, ExampleB))
'''
        self.write_comment = '''\
# * We set the variable `b` to be an instance of `ExampleB` so the return of `isinstance()` here will obviously be `True`
'''

    def topLevel4_Child2_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        self.y = 10

    def printX(self):
        print(self.x)

    def printY(self):
        print(self.y)


class ExampleB(ExampleA):
    pass


if __name__ == '__main__':
    b = ExampleB()
    print(isinstance(b, ExampleA))
'''
        self.write_comment = '''\
# * Is it an instance of `ExampleA` though?

# POLL: True or False: `b` is an instance of `ExampleA`

# Answer: True
'''

    def topLevel4_Child3_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        self.y = 10

    def printX(self):
        print(self.x)

    def printY(self):
        print(self.y)


class ExampleB(ExampleA):
    pass


if __name__ == '__main__':
    a = ExampleA()
    print(isinstance(a, ExampleB))
'''
        self.write_comment = '''\
# * Are instances of parent classes also instances of their children?

# POLL: True or False: `a` is an instance of `ExampleB`

# Answer: False
'''

    def topLevel4_Child4_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        self.y = 10

    def printX(self):
        print(self.x)

    def printY(self):
        print(self.y)


class ExampleB(ExampleA):
    pass


if __name__ == '__main__':
    b = ExampleB()
    print(b.x)
'''
        self.write_comment = '''\
# * Child classes inherit all Class Attributes and methods of their parent
# * When we run this script, it will print `5` because `ExampleB` has inherited the `x` class attribute
'''

    def topLevel4_Child5_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        self.y = 10

    def printX(self):
        print(self.x)

    def printY(self):
        print(self.y)


class ExampleB(ExampleA):
    pass


if __name__ == '__main__':
    b = ExampleB()
    print(b.y)
'''
        self.write_comment = '''\
# * We do not have an `__init__()` method in `ExampleB` though
# * Does `b` have a `y` attribute?

# POLL: What will be the output of this script?

# Answer: 10

# Explanation: `ExampleB` inherits the `__init__()` method from `ExampleA` so it will still run when we create an instance of `ExampleB`
'''

    def topLevel4_Child6_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        self.y = 10

    def printX(self):
        print(self.x)

    def printY(self):
        print(self.y)


class ExampleB(ExampleA):
    pass


if __name__ == '__main__':
    b = ExampleB()
    b.printX()
    b.printY()
'''
        self.write_comment = '''\
# * As mentioned earlier, child classes inherit all methods from their parent so `ExampleB` has the `printX()` and `printY()` methods
# * All of this so far is fine, but we still have not done anything with `ExampleB`
#   * It is still exactly like `ExampleA` so what is the point of creating a child class?
'''

    def topLevel4_Child7_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        self.y = 10

    def printX(self):
        print(self.x)

    def printY(self):
        print(self.y)


class ExampleB(ExampleA):

    def printSumXY(self):
        print(self.x + self.y)


if __name__ == '__main__':
    b = ExampleB()
    b.printSumXY()
'''
        self.write_comment = '''\
# * For starters, we can create new methods in the child class
# * In `ExampleB` here we have this `printSumXY()` method that prints the sum of the `x` and `y` attributes
'''

    def topLevel4_Child8_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        self.y = 10

    def printX(self):
        print(self.x)

    def printY(self):
        print(self.y)


class ExampleB(ExampleA):

    def printAddXY(self):
        print(self.x + self.y)


if __name__ == '__main__':
    a = ExampleA()
    a.printAddXY()
'''
        self.write_comment = '''\
# * What about if we create an instance of `ExampleA` and run the `printSumXY() ` method?

# POLL: What will the output of this script be?

# Answer: AttributeError

# Explanation: Parents do not have access to methods or attributes of the child class
'''

    def topLevel4_Child9_text(self):
        self.write_text = '''\
class ExampleA:

    _x = 5
    __y = 10

    def _printX(self):
        print('__x', self._x)

    def __printY(self):
        print('__y', self.__y)


class ExampleB(ExampleA):

    def print_params(self):
        self._printX()
        self.__printY()
        # print('__y', self.__y)


if __name__ == '__main__':
    b = ExampleB()
    b._printX()
    # b.print_params()
'''
        self.write_comment = '''\
# * Now that we are on Inheritance, we can finally demonstrate the difference between Protected and Private attributes and methods
# * Note that we have one protected and one private attribute and method in our parent class
# * Our child class only defines one public method
# * If we try to run this protected method on an instance of our child class...
#   * ...it runs without issue
#   * `ExampleB` has inherited the protected methods and attributes and still tracks it as protected
# * Now let's run the `print_params` public method of our child class...
#   * ...and we see that we get an `AttributeError` trying to access the private method
#   * This is the difference between Protected and Private
#   * Child classes will still inherit Protected methods but will not inherit Private ones
# * If we change the `__printY` method in our parent class to be Protected...
#   * Then we see that we can also access the new `_printY` method, and we can even access the Private attribute of our parent class
#   * But if we were to try to access the Private attribute directly in the child class with this commented out line in our `print_params` public method...
#   * ...then we get an `AttributeError` because the Private Attribute is not accessible directly by the child class
#   * If we move the `_printY` method to the child class, we still get the `AttributeError`
#   * This is a kind of tricky aspect about inheriting attributes and methods
#     * If we are inheriting a method that can access a private method of the parent class that will still work, even though the child class does not have direct access to that attribute
'''

    def topLevel4_Child10_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        self.y = 10

    def printX(self):
        print(self.x)

    def printY(self):
        print(self.y)


class ExampleB(ExampleA):

    def __init__(self):
        pass


if __name__ == '__main__':
    b = ExampleB()
    print(b.y)
'''
        self.write_comment = '''\
# * If we want `ExampleB` to have its own `__init__()` method, we are free to do so

# POLL: What will the output of this script be?

# Answer: AttributeError

# Explanation: Here we are _overriding_ the parent method and this is the only aspect of the Polymorphism Principle of Object-Oriented Programming that is
# implemented by default in Python. Since we have overridden the `__init__()` method, Python will no longer run  the `__init__()` method of `ExampleA` when
# we create an instance of `ExampleB` unless we do something special.
'''

    def topLevel4_Child11_text(self):
        self.write_text = '''\
class ExampleA:

    x = 5

    def __init__(self):
        self.y = 10

    def printX(self):
        print(self.x)

    def printY(self):
        print(self.y)


class ExampleB(ExampleA):

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    b = ExampleB()
    print(b.y)
'''
        self.write_comment = '''\
# * We can access the parent from the child with this `super()` call
# * So when we add this `super().__init__()` call to the child `__init__()` method, we are telling Python to run the parent `__init__()` method and then continue with the rest of this `__init__()` method
# * Now if we run this script, we see that `b` does have the `y` attribute
# * We have seen this `__init__()` method quite a bit now, and you maybe be wondering what is going on with the name of it
#   * `__init__()` is only one of a specific kind of methods called `Dunder Methods`
'''

    def topLevel4_Child12_text(self):
        self.write_text = '''\
class A:

    def __init__(self):
        print('A.__init__()')


class B(A):

    def __init__(self):
        print('B.__init__()')
        super().__init__()


class C(B):

    def __init__(self):
        print('C.__init__()')
        super().__init__()
        print('Done')


if __name__ == '__main__':
    c = C()
    print()
    print(isinstance(c, C))
    print(isinstance(c, B))
    print(isinstance(c, A))
'''
        self.write_comment = '''\
# * Multilevel Inheritance is kind of like setting up a chain of inheritance with classes
# * In this example, `class C` inherits from `class B` which inherits from `class A`
# * We can see from the printed output that when we create an instance of `C`, we:
#   * Call the `__init__()` method of `B`,
#   * which calls the `__init__()` method of `A` before we finish the initialization of `C`
# * We also see the our instance of `C` is also an instance of `class B` and `class A` we would expect
'''

    def topLevel4_Child13_text(self):
        self.write_text = '''\
class A:

    def __init__(self):
        self.x = 5

    def printX(self):
        print(self.x)


class B:

    def __init__(self):
        self.y = 10

    def printY(self):
        print(self.y)


class C:

    def __init__(self):
        self.z = 15

    def printZ(self):
        print(self.z)


class D(A, B):

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    d = D()
    d.printX()
    # d.printY()
    # print(d.z)
    # d.printZ()
'''
        self.write_comment = '''\
# * Child classes can have multiple parents
# * For now in this example ignore the `class C`, we will cover that one later
# * We see that `class D` inherits from `class A` and `class B`
# * When we run this code, we see that has indeed inherited the `printX()` method from `class A` and ran `class A`'s `__init__()` method with the `super()` call
# * What if we try to run the `printY()` method from `class B`?

# POLL: What will the output of this script be?
# a. 10
# b. AttributeError: 'D' object has no attribute 'printY'
# c. AttributeError: 'D' object has no attribute 'y'

# Answer: C. AttributeError: 'D' object has no attribute 'y'

# Explanation: We inherit the `printY()` method, but `super()` only runs the `__init__()` method of `A`

# * How can we run the `__init__()` method of `B`? We have to do it manually by adding `B.__init__(self)` to the `__init__()` method of `class D`
# * Now if we try to run the `printY` method, we see that `D` does have the attribute `y`
# * For a moment, this may not seem like we are truly inheriting from `class B`, but remember that we still inherit the methods of `class B`
#   * We can add `C.__init__(self)` and now our `class D` will have access to the `z` attribute, but not the `printZ()` method because we did not inherit from `class C`
# * If we also subclass `class C`, then we will have access to the `printZ()` method
'''

    # ==================================================================================================================
    #                                                                                             topLevel5 text methods
    # ==================================================================================================================
    def topLevel5_Child0_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5


if __name__ == '__main__':
    a = ExampleA()
    print(a.x)
'''
        self.write_comment = '''\
# * Dunder methods get their name from the double underscores at the beginning and end of the method name
# * There is nothing inherently special about Dunder methods, they get defined the same way as other methods but with a different naming scheme
# * The reason they have any importance at all is that many of Python's built-in functions and operators know to call these Dunder methods
# * The reason they were given double underscores is to make them more difficult to override
#   * You have to go out of your way a bit to be able to override them which makes Python's operation more stable
# * So what are some other Dunder methods and how are they used?

# * We've already seen `__init__()` in operation
# * Python knows to look for an `__init__()` method when creating an instance of a class
'''

    def topLevel5_Child1_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5


if __name__ == '__main__':
    a = ExampleA()
    print(a)
'''
        self.write_comment = '''\
# * If we print an Object then we might get something like this
# * We see that it is an object of `__main__.ExampleA` and we have the memory address of the object
# * This is not really useful for anything though, so why don't we help out `print()`?
'''

    def topLevel5_Child2_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5

    def __str__(self):
        return 'An instance of class ExampleA'


if __name__ == '__main__':
    a = ExampleA()
    print(a)
'''
        self.write_comment = '''\
# * In Python, `print()` is actually calling the `__str__()` Dunder method of the class
# * `__str__()` has to return a string, otherwise we will get a `TypeError`
# * Now if we run this script, we can get an output that is more informative
'''

    def topLevel5_Child3_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5

    def __add__(self, other):
        return self.x + other


if __name__ == '__main__':
    a = ExampleA()
    print(a + 5)
'''
        self.write_comment = '''\
# * Another common built-in operation is `+`
# * The `+` operator calls the `__add__()` Dunder method of the object
# * If we tried to add objects together that did not have `__add__()` defined, we would get a `TypeError`
'''

    def topLevel5_Child4_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5

    def __add__(self, other):
        return self.x + other


if __name__ == '__main__':
    a = ExampleA()
    print(5 + a)
'''
        self.write_comment = '''\
# * What if we swap the order of `5` and `a`?

# POLL: What is the printed output of this script?

# Answer: TypeError

# Explanation: `5` is not an object so it does not have a `__add__()` method, and we need a different Dunder method when `a` is in the second place
'''

    def topLevel5_Child5_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5

    def __add__(self, other):
        return self.x + other

    def __radd__(self, other):
        return self.x + other


if __name__ == '__main__':
    a = ExampleA()
    print(5 + a)
'''
        self.write_comment = '''\
# * This `__radd__()` method is called when we need to add in the reverse direction. For adding two numbers it does not seem necessary but...
'''

    def topLevel5_Child6_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5

    def __str__(self):
        return 'An instance of class ExampleA'

    def __add__(self, other):
        return self.x + other

    def __radd__(self, other):
        return other + self.x

    def __sub__(self, other):
        return self.x - other

    def __rsub__(self, other):
        return other - self.x

    def __mul__(self, other):
        return self.x * other

    def __rmul__(self, other):
        return  other * self.x

    def __truediv__(self, other):
        return self.x / other

    def __floordiv__(self, other):
        return self.x // other

    def __mod__(self, other):
        return self.x % other

    def __pow__(self, other):
        return self.x ** other

    def __lt__(self, other):
        return self.x < other

    def __le__(self, other):
        return self.x <= other

    def __eq__(self, other):
        return self.x == other

    def __ne__(self, other):
        return self.x != other

    def __gt__(self, other):
        return self.x > other

    def __ge__(self, other):
        return self.x >= other

    def __bool__(self):
        return bool(self.x)

    def __len__(self):
        return 1


if __name__ == '__main__':
    a = ExampleA()
    print(a)
    print('a + 5:', a + 5)
    print('5 + a:', 5 + a)
    print('a - 2:', a - 2)
    print('2 - a:', 2 - a)
    print('a * 2:', a * 2)
    print('2 * a:', 2 * a)
    print('a / 2:', a / 2)
    print('a // 2:', a // 2)
    print('a % 2:', a % 2)
    print('a ** 2:', a ** 2)
    print('a < 5:', a < 5)
    print('a <= 5:', a <= 5)
    print('a == 5:', a == 5)
    print('a != 5:', a != 5)
    print('a > 5:', a > 5)
    print('a >= 5:', a >= 5)
    print('bool(a)', bool(a))
    print('len(a)', len(a))
'''
        self.write_comment = '''\
# * ...it makes sense for other mathematical operations
# * Every basic mathematical operation in Python is controlled by these Dunder Methods
# * Even Boolean comparisons are controlled by Dunder methods
# * This is not every Dunder method that Python uses
# * Now you may have noticed that there is something strange going on here which is that the `__add__()` Dunder method has a `+` in it
#   * Is this `+` behaving differently? No it's not. It is calling the `__add__()` method of the `x` attribute
#   * But for that to be true, that means that the `x` attribute has to be an instance of some class, right?
'''

    # ==================================================================================================================
    #                                                                                             topLevel6 text methods
    # ==================================================================================================================
    def topLevel6_Child0_text(self):
        self.write_text = '''\
class ExampleA:

    def __init__(self):
        self.x = 5


if __name__ == '__main__':
    a = ExampleA()
    print(dir(a.x))
'''
        self.write_comment = '''\
# * That's exactly what it is
# * The `x` attribute is an instance of the `int` class
# * Python has this neat built-in `dir()` function
#   * This function will return a list of all methods and attributes of the object that is passed to it
#   * Now we can see the structure of Python's built-in `int` class
'''

    def topLevel6_Child1_text(self):
        self.write_text = '''\
x = 5

print(isinstance(x, int))
print(type(x))
'''
        self.write_comment = '''\
# * Every time we create a variable, we are creating an instance of a class
# * All the data types that you are familiar with like integers, floats, lists, etc. are all classes
# * The `isinstance()` function checks if a variable is an instance of a class
# * The `type()` function basically just returns the name of the class that the object is initialized from
#   * And note that it is also printing out `class` here
'''

    def topLevel6_Child2_text(self):
        self.write_text = '''\
x = 5

print(dir(x))
'''
        self.write_comment = '''\
# * Just like when we used the `dir()` built-in function on the attribute `x`, we can use it on this variable `x` and see the same attributes and methods of the integer class
'''

    def topLevel6_Child3_text(self):
        self.write_text = '''\
x = 5
y = 10

print(x + y)
'''
        self.write_comment = '''\
# * In this script we end up creating three instances of the `int` class
# * By adding `x` and `y` together we call the `__add__()` Dunder method of `x`
# * And when we print, we are calling the `__str__()` method of the object resulting from the summation
# * _Everything_ in Python is an object which means that if anyone asks if you are an Object-Oriented programmer, you can _technically_ say yes because you work with Python
#   * They are really asking if you know how to create your own classes and objects, so you should wait until the end of this course, and _then_ you can say yes
'''

    def topLevel6_Child4_text(self):
        self.write_text = '''\
x = 5
y = 6.315
z = x + y
'''
        self.write_comment = '''\
# POLL: Not including objects in the base classes, how many unique objects are created by this script?

# Answer: 3
'''

    def topLevel6_Child5_text(self):
        self.write_text = '''\
x = 5
y = 0
z = x + y
'''
        self.write_comment = '''\
# POLL: Not including objects in the base classes, how many unique objects are created by this script?

# Answer: 2

# Explanation: `x` and `y` are both unique objects but because the value of `y` is `0`, `x` and `z` are actually the same object
#   * We can add `print(id(x) == id(z))` to verify this
'''

    def topLevel6_Child6_text(self):
        self.write_text = '''\
x = 5
y = x + 0
'''
        self.write_comment = '''\
# POLL: Not including objects in the base classes, how many unique objects are created by this script?

# Answer: 1

# Explanation: `0` is not an object here, and because we are adding `0` to an integer, `y` will be identical to `x`
#   * We can add `print(id(x) == id(y))` to verify this
'''

    def topLevel6_Child7_text(self):
        self.write_text = '''\
x = 5
y = 10 + 25
'''
        self.write_comment = '''\
# POLL: Not including objects in the base classes, how many unique objects are created by this script?

# Answer: 3

# Explanation: 10 is an object
'''

    def topLevel6_Child8_text(self):
        self.write_text = '''\
x = 1
y = 1
'''
        self.write_comment = '''\
# POLL: Not including objects in the base classes, how many unique objects are created by this script?

# Answer: 1

# Explanation: even though we initialize two different variables, since they are the same value Python will assign them the same memory address
#   * Again, we can check this using `print(id(x) == id(y))`
'''

    def topLevel6_Child9_text(self):
        self.write_text = '''\
x = 4
y = 4.178

"Demo script"
'''
        self.write_comment = '''\
# POLL: Not including objects in the base classes, how many unique objects are created by this script?

# Answer: 3

# Explanation: The string is also an object, even though it does not get assigned to a variable
'''

    def topLevel6_Child10_text(self):
        self.write_text = '''\
def Foo(aX, aY):
    return aX + aY


x = 3
y = 4

z = Foo(x, y)
'''
        self.write_comment = '''\
# POLL: Not including objects in the base classes, how many unique objects are created by this script?

# Answer: 4

# Explanation: This one is tricky because some might not be sure if `aX` and `aY` have different memory addresses in the function scope
#   * They do _not_ have unique addresses but even this is not the only trick
#   * `Foo` is _also_ an object; it is an instance of the `function` class
#     * `print(type(Foo))`
#   * Methods are also instances of the `function` class
'''

    # ==================================================================================================================
    #                                                                                             topLevel7 text methods
    # ==================================================================================================================
    def topLevel7_Child0_text(self):
        self.write_text = '''\
arr  = [1, 2, 3]
arr += [4, 5, 6]
print(arr)
'''
        self.write_comment = '''\
# * Now that we understand how Python is operating at a lower level, we have the power to do some interesting things with classes
# * There is a version of Python called MicroPython that is used on microcontrollers
# * This is kind of like a lite version of Python because it does not have access to all the existing Python modules
#   * Disappointingly, this includes `numpy`
#   * As you probably know, `numpy` is very good at mathematical operations on arrays so not having access to this module can be difficult
#   * Why don't we create a class that manages a 1D Array and works with the basic mathematical operations in Python?

# * Lists would be a good starting point, but they are obviously not exclusive to numbers, so they do not use the mathematical operators for math
# * For instance, `+` does not add the elements of this list together, it combines the two lists into one
#   * It is functioning like the `extend()` method of the `list` class
'''

    def topLevel7_Child1_text(self):
        self.write_text = '''\
arr  = [1, 2, 3]
arr *= [4, 5, 6]
print(arr)
'''
        self.write_comment = '''\
# * And if we tried to multiply these two lists together we get a `TypeError`
# * We can still use lists, but we need to change their behavior when using Python's operators
'''

    def topLevel7_Child2_text(self):
        self.write_text = '''\
class array:

    def __init__(self, arr):

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
        tmp = array([])
        for i in self.range:
            tmp.append(self.array[i] + other[i])
        return tmp

    def __radd__(self, other):
        tmp = array([])
        for i in self.range:
            tmp.append(other[i] + self.array[i])
        return tmp


if __name__ == '__main__':
    a = array([0, 1, 2])
    b = array([3, 4, 5])

    print(a + b)
'''
        self.write_comment = '''\
# * A lot just showed up at once, so let's break this down method by method
# * We create a class named `array`
#   * We will be using lists to store our numbers, so we could have subclassed `list`, but we would be overriding so much that it would probably hinder us to do that
#   * And we would inherit attributes and methods we do not need so we would end up using more memory than we need which is not great on microcontrollers
# * In the `__init__()` method we are passing in the `arr` argument, then converting it to a list if required
#   * We then iterate through every element in the `arr` argument to make sure it is a number, or else we raise a `TypeError`
#   * Then we assign `arr` to an attribute, get its length, and then create a range that we will use in our other methods
# * We define the `append` behavior of this `array` class
#   * We are only going to be working with one dimensional arrays for the demo so we will add them to the end of the array
#   * We could have done 2D arrays but that would just increase the complexity
# * We define the `__str__()` method to give ourselves a nice print statement
# * We define `__getitem__()` and `__setitem__()` so that we can index into the array and assign new values to specific elements
# * Then we have our `__add__()` and `__radd__()` methods, so we can add arrays together
# * We _could_ add a type check for `other` to make sure it is compatible, but if it is not compatible Python will already handle that
#   * Best to keep our class as light as possible if we are going to use it with a microcontroller
'''

    def topLevel7_Child3_text(self):
        self.write_text = '''\
class array:

    def __init__(self, arr):

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
        tmp = array([])
        for i in self.range:
            tmp.append(self.array[i] + other[i])
        return tmp

    def __radd__(self, other):
        tmp = array([])
        for i in self.range:
            tmp.append(other[i] + self.array[i])
        return tmp


if __name__ == '__main__':
    a = array([0, 1, 2])
    b = array([0, 0, 0])
    c = a + b

    print('a:', a)
    print('c:', c)
    print(id(a) == id(c))
'''
        self.write_comment = '''\
# * But what happens when we try to add an array of zeros to an existing array?
#   * `a` and `c` have identical contents, but not the same memory address
# * This is because in our `__add__()` and `__radd__()` methods we are creating entirely new instances of our class and then appending values to it
# * All of the questions about how Python manages memory has led to this. Do we want our array class to keep `a` and `c` as unique objects?

# POLL: True or False: The individual elements of `a` and `c` share the same memory address. (Will this loop print out all `True` or all `False`?)

# Answer: A. True

# Explanation: We change the address of the class overall, but the address of the individual elements remain the same, meaning we are not heavily consuming more memory.
# Even though "a" and "c" have identical elements that share memory, they are still unique arrays and we can manipulate them individually.
'''

    def topLevel7_Child4_text(self):
        self.write_text = '''\
class array:

    def __init__(self, arr):

        if not isinstance(arr, list):
            arr = list(arr)

        for i in arr:
            if not isinstance(i, (int, float, complex)):
                raise TypeError('All elements must be of type int, float, or complex')

        self.array = arr
        self.len   = len(arr)
        self.range = range(self.len)
        self.any   = any(arr)

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
        if not any(other):
            return self
        elif not self.any and any(other):
            return other
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(self.array[i] + other[i])
            return tmp

    def __radd__(self, other):
        if not any(other):
            return self
        elif not self.any and any(other):
            return other
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(other[i] + self.array[i])
            return tmp


if __name__ == '__main__':
    a = array([0, 1, 2])
    b = array([0, 0, 0])
    c = a + b

    print('a:', a)
    print('c:', c)
    a[0] = 20
    print('a:', a)
    print('c:', c)
'''
        self.write_comment = '''\
# * With that in mind, I argue that we want to keep them separate
#   * If we have separate variables, then we are almost certainly tracking them separately and want to keep them unique
# * Here I have used Python's `any()` built-in function to return one array if the other is all zeros
#   * It will return `self` if `other` is all zeros, and it will return `other` if `self` is all zeros
# * If we return the exact same array, then `c` is not unique from `a`
#   * Therefore if we update either, we update both which is not what we want in terms of usability
# * Further edits will expand on the previous state, not this one
'''

    def topLevel7_Child5_text(self):
        self.write_text = '''\
class array:

    def __init__(self, arr):

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
            tmp = array([])
            for i in self.range:
                tmp.append(other[i] + self.array[i])
            return tmp
        else:
            tmp = array([])
            for i in self.range:
                tmp.append(other + self.array[i])
            return tmp


if __name__ == '__main__':
    a = array([0, 1, 2])
    b = array([5, 5, 5])

    print(a + b)
    print(b + a)
    print(a + 5)
    print(5 + a)
'''
        self.write_comment = '''\
# * Now that we know how we want to manage memory during our mathematical operations, let's look into improving our usability.
#   * Specifically, what if we want to add a single value to every element of our array?
#   * Currently we would get an indexing error when trying to index into other
# * We've already added this '__getitem__() Dunder method to our class
# * Since this is what Python looks for when indexing, so we know that if the other argument passed does not have that method, then it is likely a single value
# * Python has another built-in function called hasattr() (which also works for methods), so we can use to check if the argument has a specific method'''

    def topLevel7_Child6_text(self):
        self.write_text = '''\
class array:

    def __init__(self, arr):

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

    def __len__(self):
        return self.len

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


if __name__ == '__main__':
    a = array([1, 2, 3])
    b = array([0, 0, 0, 0])
    c = a + b
'''
        self.write_comment = '''\
# * We have not taken steps to make sure that we are only adding arrays of the same size
# * We can add one more check to see if the lengths are equal, and then we can raise a `SyntaxError` if they are not the same
# * That was a lot just to create two methods to add arrays to arrays and arrays to single values...
'''

    def topLevel7_Child7_text(self):
        self.write_text = '''\
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
        self.write_comment = '''\
# * ...luckily the rest follow a similar trend but with minor changes to the ways we check the values of `self` and `other`
# * I've also added Type Hints and a Doc-string to make it more user-friendly
# * There's 318 lines of code just to control the basic functionality of our array
#   * And this is just for 1D Arrays!
#   * But now we can do all the element by element mathematical operations using Python's built-in operators
'''

    # ==================================================================================================================
    #                                                                                             topLevel8 text methods
    # ==================================================================================================================
    def topLevel8_Child0_text(self):
        self.write_text = '''\
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
        self.write_comment = '''\
# * You can define classes that are within the scope of other classes
# * Here we have an outer class `Rectangle` and the inner class `Point`
# * Each class has their own `__init__()` constructor and `__str__()` method
# * We pass a length and width to the `Rectangle` class and it will calculate the locations of its four points
# * The inner class can be accessed by the outer class with the `self.` syntax similar to attributes and methods
# * We can access the `Point` class outside of the `Rectangle` class with `p = Rectangle.Point(0, 0)`
'''

    def topLevel8_Child1a_text(self):
        self.write_text = '''\
import json


# -----------------------------------------
# example dictionary to serialize with json
# -----------------------------------------
d = {
    'a': 0,
    'b': 1.0,
    'c': '2',
    'd': True,
    'e': None,
    'f': {
        'a': 0,
        'b': 1.0,
        'c': '2',
        'd': True,
        'e': None,
    },
    'g': [0, 1.0, '2', True, None],
    7: (0, 1.0, '2', True, None),
}


# ---------------------------------
# serialize dictionary to json file
# ---------------------------------
with open('serialization.json', 'w') as f:
    json.dump(d, f, indent='\\t')
'''
        self.write_comment = '''\
# * Object serialization means that we serialize an object to a series of bytes for later use
#   * Another way of describing this is that we are saving objects to files
# * JSON stands for JavaScript Object Notation and is a popular method of serialization because it saves data to plain text
# * Because the data is plain text, it makes it easy to serialize data for use between different programming languages
# * JSON is very restrictive in the types of data that can be included. You are limited to:
#   * Dictionaries
#   * Floats
#   * Integers
#   * Strings
#   * Booleans
#   * None (or Null)
#   * Arrays (in the form of Lists and Tuples)
# * Some things to note between the dictionary we created and the json file output
#   * Some of the data has been transformed into the JavaScript equivalent
#     * Booleans are lower case, `None` has become `null`
#   * The `7` integer key we used in our dictionary is now a string
#     * Keep that in mind if you are ever using loop variables as keys
#   * The tuple that we assigned to `7` is now square brackets, just like "g"
'''

    def topLevel8_Child1b_text(self):
        self.write_text = '''\
import json


# ----------------------------------------------
# read json file and print type of 'h' key value
# ----------------------------------------------
with open('serialization.json', 'r') as f:
    data = json.load(f)
print(type(data['7']))
print(type(data))
'''
        self.write_comment = '''\
# * Let's see what happens when we load in this serialized JSON data
#   * Notice that we have to use a string of 7 for that key now
#   * The tuple that we created has been transformed to a list
#     * Tuples are "immutable" meaning that they cannot be edited once created
#     * We lost that immutability when we serialized to json
#   * `data` is a dictionary type
#     * There is no `json` data type, it is just a serialization protocol
#     * `data` is a dictionary because that is what we created, json will also load to a list or one of the other data types depending on the file contents
#       * Strings must be defined inside of ""
'''

    def topLevel8_Child2a_text(self):
        self.write_text = '''\
import pickle


# --------------------------------------
# example class to serialize with pickle
# --------------------------------------
class serializeThis:

    def __init__(self):
        self.a = 0
        self.b = 1.0
        self.c = '1'
        self.d = True
        self.e = None
        self.f = {
            'a': 0,
            'b': 1.0,
            'c': '2',
            'd': True,
            'e': None,
        }
        self.g = [0, 1.0, '2', True, None]
        self.h = (0, 1.0, '2', True, None)

    def printA(self):
        print('a:', self.a)


# ------------------------------------------------------
# create and pickle an object of the class serializeThis
# ------------------------------------------------------
obj = serializeThis()
with open('serialization.p', 'wb') as f:
    pickle.dump(obj, f)
'''
        self.write_comment = '''\
# * `pickle` is another serialization module and this one is exclusive to Python
# * When you pickle vegetables, you process them and store them for later user
#   * That is where this module gets its name
# * Because `pickle` is Python-exclusive, you can serialize more than just the data types available to json
#   * You can even serialize objects from custom classes!
# * Here I have created a class with a similar structure as the dictionary in the JSON Serialization example
#   * I have included a method that will print the `a` attribute
# * The serialization process looks very similar to the process for json serialization
#   * Now we include a `b` when we write though because we are writing in binary
'''

    def topLevel8_Child2b_text(self):
        self.write_text = '''\
import pickle
from oopDemo import serializeThis

# ------------------------------------------------------
# load serialized object, run method, pass obj2 to dir()
# ------------------------------------------------------
with open('serialization.p', 'rb') as f:
    obj2 = pickle.load(f)
obj2.printA()
# print(type(obj2))
# print(dir(obj2))
'''
        self.write_comment = '''\
# * Some items to note with pickle serialization
#   * The output is not in a human readable format
#     * We can see some words but overall we can derive nothing meaningful from this
#   * We can unpickle the file, and we still have access to the method defined in the class
#   * Even though we do not have an explicit call to the class, we still need to include it in our imports
#     * If I comment out the import line, and run the pickling of the class again, the unpickle will fail
#     * If I did not run the pickling again it would have loaded without issue because of information included in `__pycache__/`
# * Be careful to only unpickle data that you know is safe
#   * Someone could easily pickle malicious code
# * As of Python 3.8.2, `pickle` is faster than `JSON`
'''

    # ==================================================================================================================
    #                                                                                             topLevel9 text methods
    # ==================================================================================================================
    def topLevel9_Child0_text(self):
        self.write_text = '''\
import sys
from PyQt6.QtWidgets import *


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        # -----------------
        # window properties
        # -----------------
        self.setWindowTitle('Qt Demo')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
'''
        self.write_comment = '''\
# PyQt is a wrapper for the C++ Qt Framework. It allows users to create visually-appealing, powerful GUI Applications. Guides for PyQt almost exclusively use Object-Oriented Programming.
# To create a very basic GUI Application we must include the lines:
#    app = QApplication(sys.argv)
#    sys.exit(app.exec())
# Between these two lines we can initialize our program.

# We create the program by subclassing `QMainWindow`
# This program will create an empty window
'''

    def topLevel9_Child1_text(self):
        self.write_text = '''\
import sys
from PyQt6.QtWidgets import *


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        # -----------------
        # window properties
        # -----------------
        self.setWindowTitle('Qt Demo')

        # -----------
        # main layout
        # -----------
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QGridLayout()
        widget.setLayout(layout)

        # ---------------
        # label with text
        # ---------------
        self.lbl = QLabel('Hello World!')
        layout.addWidget(self.lbl)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
'''
        self.write_comment = '''\
# The structure of the QMainWindow is illustrated at: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMainWindow.html#qt-main-window-framework
# We will not cover all elements of `QMainWindow` in this demo; only `Central Widget` and `Menu Bar`
# Here we see how to set the window title and central widget
# We also see how to add a widget to the window
'''

    def topLevel9_Child2_text(self):
        self.write_text = '''\
import sys
from PyQt6.QtWidgets import *


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        # -----------------
        # window properties
        # -----------------
        self.setWindowTitle('Qt Demo')

        # -----------
        # main layout
        # -----------
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QGridLayout()
        widget.setLayout(layout)

        # ------------------
        # left label counter
        # ------------------
        self.lbl_left = QLabel('0')
        layout.addWidget(self.lbl_left)

        # -------------------
        # right label counter
        # -------------------
        self.lbl_right = QLabel('0')
        layout.addWidget(self.lbl_right, 0, 1)

        # --------------
        # counter button
        # --------------
        self.btn = QPushButton('Count')
        self.btn.pressed.connect(self.counterLeft)
        self.btn.released.connect(self.counterRight)
        layout.addWidget(self.btn, 1, 0, 1, 2)

        # ------------------
        # counter attributes
        # ------------------
        self.countLeft  = 0
        self.countRight = 0

    def counterLeft(self):

        self.countLeft += 1
        self.lbl_left.setText(str(self.countLeft))

    def counterRight(self):

        self.countRight += 1
        self.lbl_right.setText(str(self.countRight))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
'''
        self.write_comment = '''\
# Qt works on the ideas of signals, not commands. In Tkinter when you program a button, you set the function to run when the user clicks the button. In Qt each element has different signals associated with it, and we can connect these signals to as many operations as we wish.
# In this demo we created two labels, and we link two different signals of the same button to update each one.
# We see that when we first click the button the label on the left will increment, and when we release the button the label on the right will increment.
'''

    def topLevel9_Child3_text(self):
        self.write_text = '''\
import sys, time
from PyQt6.QtWidgets import *


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        # -----------------
        # window properties
        # -----------------
        self.setWindowTitle('Qt Demo')

        # -----------
        # main layout
        # -----------
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QGridLayout()
        widget.setLayout(layout)

        # ---------------
        # label with text
        # ---------------
        self.lbl = QLabel('0')
        layout.addWidget(self.lbl)

        # --------------
        # counter button
        # --------------
        self.btn = QPushButton('Start Counting')
        self.btn.released.connect(self.startCounting)
        layout.addWidget(self.btn)
        self.counting = False
        self.count = 0

    def startCounting(self):

        self.btn.released.disconnect(self.startCounting)
        self.btn.released.connect(self.stopCounting)
        self.btn.setText('Stop Counting')

        self.counting = True

        while self.counting:
            time.sleep(1)
            self.count += 1
            print(self.count)

    def stopCounting(self):
        self.btn.setText('Start Counting')
        self.btn.released.disconnect(self.stopCounting)
        self.btn.released.connect(self.startCounting)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
'''
        self.write_comment = '''\
# Signals can be disconnected too. In this script we release our previously linked signal with the `released` command.
# We then link to another method that will continuously count and update our label. The method will first disconnect the signal to itself and then connect the signal to the `stopCounting` method.

# This Window freezes though and we do not see anything being updated, but we are still printing out what the numbers should be set to, so what is going on?
# GUI Windows are very sensitive to thread management. The program itself is operating on the _main_ thread and any time we click a button or run a function/method, that is _also_ running on the main thread.
# This means that every operation we are doing is blocking our main thread from managing our GUI. If the main thread is blocked for long enough, then the GUI window appears to be frozen.

# Any long running operation needs to be transferred to a different thread. Qt has its own threading module that we can use to do this.
'''

    def topLevel9_Child4_text(self):
        self.write_text = '''\
import time


class longTask:

    def __init__(self):
        super().__init__()
        self.counting = True
        self.time = None
        self.counter = 0

    def count(self):
        while self.counting:
            time.sleep(1)
            self.counter += 1
            print(self.counter)


if __name__ == '__main__':

    task = longTask()
    task.count()
'''
        self.write_comment = '''\
# First we create a class in a script that is completely separate from any Qt Code.
# You could set this up in the same script, especially for something this simple, but in general this makes testing easier before implementing into the main code.

# We create the `self.counter` attribute rather than use a local variable because we know that we will need to access this information later in our main code.

# The `while` loop will be an infinite loop because we have not put in a mechanism to change the value of `self.counting` but that will change when we implement into the main code.
'''

    def topLevel9_Child5_text(self):
        self.write_text = '''\
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class longTask(QObject):

    progress = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.counting = True
        self.time = None
        self.counter = 0

    def count(self):
        while self.counting:
            self.progress.emit(self.counter)
            time.sleep(1)
            self.counter += 1
            # print(x)
        self.finished.emit()


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        # -----------------
        # window properties
        # -----------------
        self.setWindowTitle('Qt Demo')

        # -----------
        # main layout
        # -----------
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QGridLayout()
        widget.setLayout(layout)

        # ---------------
        # label with text
        # ---------------
        self.lbl = QLabel('0')
        layout.addWidget(self.lbl)

        # --------------
        # counter button
        # --------------
        self.btn = QPushButton('Start Task')
        self.btn.released.connect(self.startCounting)
        layout.addWidget(self.btn)
        # --------------------
        # threading attributes
        # --------------------
        self.worker = None
        self.thread = None

    def startCounting(self):

        self.btn.released.disconnect(self.startCounting)
        self.btn.released.connect(self.stopCounting)
        self.btn.setText('Stop Task')

        self.worker = longTask()
        self.thread = QThread(self)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.count)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.updateLbl)

        self.thread.start()

    def stopCounting(self):
        self.worker.counting = False
        self.btn.setText('Start Task')
        self.btn.released.disconnect(self.stopCounting)
        self.btn.released.connect(self.startCounting)

    def updateLbl(self, msg):
        self.lbl.setText(str(msg))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
'''
        self.write_comment = '''\
# To implement this class into our main program we first have to edit our class that will run our long operation.
# We set it to subclass `QObject`, then create signals for this class that we will use to communicate with and send information to our main thread.
# We give an `int` type when we set up the `progress` signal so that we know we will be sending integers to our main thread with the `progress` signal.

# In our `startCounting` method, we still change our configuration to the button signals. From there we establish our long running task.

# We assign an attribute to an instance of our new class, and we create a separate thread to run it on using `QThread`, and then move the worker class to the new thread.

# We then link the signals for our operation. We link the `started` signal of our thread to the `count` method of our worker.
# When the worker emits the `finished` signal we need to `quit` the thread and delete both the thread and the worker.
# We also link the `progress` signal to a new method we named `updateLbl()` in our main class.

# `updateLbl()` will set the text of our label to the integer value it receives from our worker

# Errors that occur in other threads will not be made available to the user. Here we have this `print(x)` command in our long running task where `x` is undefined.
# If I run this code, we will not receive an error message. We have to make sure we catch all exceptions, and then transfer them to the main thread.
'''

    def topLevel9_Child6_text(self):
        self.write_text = '''\
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class longTask(QObject):

    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error    = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.counting = True
        self.time = None
        self.counter = 0

    def run(self):
        try:
            self.count()
        except:
            self.error.emit(sys.exc_info())

    def count(self):
        while self.counting:
            self.progress.emit(self.counter)
            time.sleep(1)
            self.counter += 1
        self.finished.emit()


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        # -----------------
        # window properties
        # -----------------
        self.setWindowTitle('Qt Demo')

        # -----------
        # main layout
        # -----------
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QGridLayout()
        widget.setLayout(layout)

        # ---------------
        # label with text
        # ---------------
        self.lbl = QLabel('0')
        layout.addWidget(self.lbl)

        # --------------
        # counter button
        # --------------
        self.btn = QPushButton('Start Task')
        self.btn.released.connect(self.startCounting)
        layout.addWidget(self.btn)

        # --------------------
        # threading attributes
        # --------------------
        self.worker = None
        self.thread = None

    def startCounting(self):

        self.btn.released.disconnect(self.startCounting)
        self.btn.released.connect(self.stopCounting)
        self.btn.setText('Stop Task')

        self.worker = longTask()
        self.thread = QThread(self)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.thread.deleteLater)

        self.worker.progress.connect(self.updateLbl)
        self.worker.error.connect(self.error)

        self.thread.start()

    def stopCounting(self):
        self.worker.counting = False
        self.btn.setText('Start Task')
        self.btn.released.disconnect(self.stopCounting)
        self.btn.released.connect(self.startCounting)

    def updateLbl(self, msg):
        self.lbl.setText(str(msg))

    @staticmethod
    def error(err):
        except_hook(err[0], err[1], err[2])


if __name__ == '__main__':

    def except_hook(exc_type, exc_value, tb):
        sys.__excepthook__(exc_type, exc_value, tb)
        main.close()
        sys.exit(1)
    sys.excepthook = except_hook

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
'''
        self.write_comment = '''\
# Under `if __name__ == '__main__'`, we create a function and override the default `excepthook` method of the `sys` module.
# This function will directly pass our error directly to the `__excepthook__` Dunder method of `sys`. It will then close our main window.

# We add a new method in our class `longTask` that will run our long operation and catch exceptions and send them to the main thread in a tuple.

# In our main class we create a new `staticmethod` that will send our error to our `except_hook` function that we created.
'''

    def topLevel9_Child7_text(self):
        self.write_text = '''\
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class longTask(QObject):

    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error    = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.counting = True
        self.time = None
        self.counter = 0

    def run(self):
        try:
            self.count()
        except:
            self.error.emit(sys.exc_info())

    def count(self):
        while self.counting:
            self.progress.emit(self.counter)
            time.sleep(1)
            self.counter += 1
        self.finished.emit()


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        # -----------------
        # window properties
        # -----------------
        self.setWindowTitle('Qt Demo')

        # -----------
        # main layout
        # -----------
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QGridLayout()
        widget.setLayout(layout)

        # ---------------
        # label with text
        # ---------------
        self.lbl = QLabel('0')
        layout.addWidget(self.lbl)

        # --------------
        # counter button
        # --------------
        self.btn = QPushButton('Start Task')
        self.btn.released.connect(self.startCounting)
        layout.addWidget(self.btn)

        # -------------
        # dropdown menu
        # -------------
        menu = QComboBox()
        menu.setPlaceholderText('Options')
        menu.addItems(['Filled', 'Dropdown', 'Menu'])
        layout.addWidget(menu)

        # ----------
        # tab widget
        # ----------
        tabs = QTabWidget()
        tabs.setMovable(True)
        layout.addWidget(tabs, 0, 1, 3, 2)

        # ---------
        # image tab
        # ---------
        imageTab = QWidget()
        imageLayout = QHBoxLayout()
        imageTab.setLayout(imageLayout)
        imageLabel = QLabel()
        imageLabel.setPixmap(QPixmap('image.jpg'))
        imageLabel.setScaledContents(True)
        imageLayout.addWidget(imageLabel)
        tabs.addTab(imageTab, 'Image')

        # --------
        # text tab
        # --------
        textTab = QWidget()
        textLayout = QVBoxLayout()
        textTab.setLayout(textLayout)
        tabText = QLabel('Tab Widget showing text')
        textLayout.addWidget(tabText)
        tabs.addTab(textTab, 'Text')

        # ---------
        # line edit
        # ---------
        self.line = QLineEdit()
        self.line.setPlaceholderText('Enter text here')
        layout.addWidget(self.line, 3, 0, 1, 3)

        # ---------
        # check box
        # ---------
        checkBox = QCheckBox('Check Box')
        checkBox.setCheckState(Qt.CheckState.Checked)
        layout.addWidget(checkBox)

        # -------------
        # radio buttons
        # -------------
        radioBtn1 = QRadioButton('Radio Button 1')
        radioBtn1.setChecked(True)
        radioBtn2 = QRadioButton('Radio Button 2')
        layout.addWidget(radioBtn1, 4, 1)
        layout.addWidget(radioBtn2, 4, 2)

        # --------
        # menu bar
        # --------
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')
        menuBar.addMenu(fileMenu)

        # ---------
        # file menu
        # ---------
        act1 = QAction('These', self)
        act2 = QAction('Do', self)
        act3 = QAction('Nothing', self)
        act4 = QAction('This Does', self)
        act4.triggered.connect(self.printInput)
        act4.setShortcut('Ctrl+p')
        subMenu = fileMenu.addMenu('&More')

        fileMenu.addAction(act1)
        fileMenu.addAction(act2)
        fileMenu.addAction(act3)
        fileMenu.addSeparator()
        fileMenu.addMenu(subMenu)

        subMenu.addAction(act4)

        # --------------------
        # threading attributes
        # --------------------
        self.worker = None
        self.thread = None

    def startCounting(self):

        self.btn.released.disconnect(self.startCounting)
        self.btn.released.connect(self.stopCounting)
        self.btn.setText('Stop Task')

        self.worker = longTask()
        self.thread = QThread(self)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.thread.deleteLater)

        self.worker.progress.connect(self.updateLbl)
        self.worker.error.connect(self.error)

        self.thread.start()

    def stopCounting(self):
        self.worker.counting = False
        self.btn.setText('Start Task')
        self.btn.released.disconnect(self.stopCounting)
        self.btn.released.connect(self.startCounting)

    def updateLbl(self, msg):
        self.lbl.setText(str(msg))

    def printInput(self):
        print(self.line.text())

    @staticmethod
    def error(err):
        except_hook(err[0], err[1], err[2])


if __name__ == '__main__':

    def except_hook(exc_type, exc_value, tb):
        sys.__excepthook__(exc_type, exc_value, tb)
        main.close()
        sys.exit(1)
    sys.excepthook = except_hook

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
'''
        self.write_comment = '''\
# Here is a GUI Window that shows how to implement many common features used in Qt development.

# We still have our `longTask` class implemented the same way that we did in the previous code snippet.

# Here I have added the following:
# * A tab widget with the following tabs
#     * An image embedded in the tab
#     * A label displaying text
# * A dropdown menu with place holder text
# * A widget for user text input with place holder text
# * A check box
# * Two radio buttons
#     * Note that we do not need to give any command for Qt to know that only one of these radio buttons can be selected at a time
# * A menu bar filled with:
#     * Three actions that do nothing
#     * A sub menu with an action that prints the text in the user input line
#         * This also has a keyboard shortcut that is implemented with only one line

# You can see how Qt manages threads by starting the long, counting task and then using the input line and the `Ctll+p` command to print out the text without the operations delaying each other.
'''

    def topLevel9_Child8_text(self):
        self.write_text = '''\
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class longTask(QObject):

    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error    = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.counting = True
        self.time = None
        self.counter = 0

    def run(self):
        try:
            self.count()
        except:
            self.error.emit(sys.exc_info())

    def count(self):
        while self.counting:
            self.progress.emit(self.counter)
            time.sleep(1)
            self.counter += 1
        self.finished.emit()


class menu(QComboBox):

    def __init__(self, placeholder, items):
        super().__init__()
        self.setPlaceholderText(placeholder)
        self.addItems(items)


class tabs(QTabWidget):

    def __init__(self):
        super().__init__()
        self.setMovable(True)


class imageTab(QWidget):

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        lbl = QLabel()
        lbl.setPixmap(QPixmap('image.jpg'))
        lbl.setScaledContents(True)
        layout.addWidget(lbl)


class textTab(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        txt = QLabel('Tab Widget showing text')
        layout.addWidget(txt)


class line(QLineEdit):

    def __init__(self, txt):
        super().__init__()
        self.setPlaceholderText(txt)


class check(QCheckBox):

    def __init__(self, txt):
        super().__init__()
        self.setText(txt)
        self.setCheckState(Qt.CheckState.Checked)


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        # -----------------
        # window properties
        # -----------------
        self.setWindowTitle('Qt Demo')

        # -----------
        # main layout
        # -----------
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QGridLayout()
        widget.setLayout(layout)

        # ---------------
        # label with text
        # ---------------
        self.lbl = QLabel('0')
        layout.addWidget(self.lbl)

        # --------------
        # counter button
        # --------------
        self.btn = QPushButton('Start Task')
        self.btn.released.connect(self.startCounting)
        layout.addWidget(self.btn)

        # -------------
        # dropdown menu
        # -------------
        self.menu = menu('Options', ['Filled', 'Dropdown', 'Menu'])
        layout.addWidget(self.menu)

        # ----------
        # tab widget
        # ----------
        tabs = QTabWidget()
        layout.addWidget(tabs, 0, 1, 3, 2)

        # ---------
        # image tab
        # ---------
        imgTab = imageTab()
        tabs.addTab(imgTab, 'Image')

        # --------
        # text tab
        # --------
        txtTab = textTab()
        tabs.addTab(txtTab, 'Text')

        # ---------
        # line edit
        # ---------
        self.line = line('Enter text here')
        layout.addWidget(self.line, 3, 0, 1, 3)

        # ---------
        # check box
        # ---------
        checkBox = check('Check Box')
        layout.addWidget(checkBox)

        # -------------
        # radio buttons
        # -------------
        radioBtn1 = QRadioButton('Radio Button 1')
        radioBtn1.setChecked(True)
        radioBtn2 = QRadioButton('Radio Button 2')
        layout.addWidget(radioBtn1, 4, 1)
        layout.addWidget(radioBtn2, 4, 2)

        # --------
        # menu bar
        # --------
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')
        menuBar.addMenu(fileMenu)

        # ---------
        # file menu
        # ---------
        act1 = QAction('These', self)
        act2 = QAction('Do', self)
        act3 = QAction('Nothing', self)
        act4 = QAction('This Does', self)
        act4.triggered.connect(self.printInput)
        act4.setShortcut('Ctrl+p')
        subMenu = fileMenu.addMenu('&More')

        fileMenu.addAction(act1)
        fileMenu.addAction(act2)
        fileMenu.addAction(act3)
        fileMenu.addSeparator()
        fileMenu.addMenu(subMenu)

        subMenu.addAction(act4)

        # --------------------
        # threading attributes
        # --------------------
        self.worker = None
        self.thread = None

    def startCounting(self):

        self.btn.released.disconnect(self.startCounting)
        self.btn.released.connect(self.stopCounting)
        self.btn.setText('Stop Task')

        self.worker = longTask()
        self.thread = QThread(self)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.thread.deleteLater)

        self.worker.progress.connect(self.updateLbl)
        self.worker.error.connect(self.error)

        self.thread.start()

    def stopCounting(self):
        self.worker.counting = False
        self.btn.setText('Start Task')
        self.btn.released.disconnect(self.stopCounting)
        self.btn.released.connect(self.startCounting)

    def updateLbl(self, msg):
        self.lbl.setText(str(msg))

    def printInput(self):
        print(self.line.text())

    @staticmethod
    def error(err):
        except_hook(err[0], err[1], err[2])


if __name__ == '__main__':

    def except_hook(exc_type, exc_value, tb):
        sys.__excepthook__(exc_type, exc_value, tb)
        main.close()
        sys.exit(1)
    sys.excepthook = except_hook

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
'''
        self.write_comment = '''\
This creates the same GUI Window as `qt-demo-7`, but creates subclasses for many of the GUI elements rather than setting their properties in the `__init__()` constructor.
# This is to further illustrate the interaction of these GUI Elements as objects. It also increases readability of the `__init__()` constructor of `class Main`.
'''

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
            self.progressDict['0']['expanded'] = False
            self.progressDict['1']['expanded'] = True
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
            self.progressDict['1']['expanded'] = False
            self.progressDict['2']['expanded'] = True
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
            self.progressDict['2']['expanded'] = False
            self.progressDict['3']['expanded'] = True
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
            self.progressDict['3']['expanded'] = False
            self.progressDict['4']['expanded'] = True
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
            self.progressDict['4']['expanded'] = False
            self.progressDict['5']['expanded'] = True
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
            self.progressDict['5']['expanded'] = False
            self.progressDict['6']['expanded'] = True
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
            self.progressDict['6']['expanded'] = False
            self.progressDict['7']['expanded'] = True
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
            self.progressDict['7']['expanded'] = False
            self.progressDict['8']['expanded'] = True
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
            self.progressDict['8']['expanded'] = False
            self.progressDict['9']['expanded'] = True
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
            self.progressDict['9']['expanded'] = False
        elif any(states):
            self.topLevel9.setCheckState(0, Qt.CheckState.PartiallyChecked)
        else:
            self.topLevel9.setCheckState(0, Qt.CheckState.Unchecked)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
