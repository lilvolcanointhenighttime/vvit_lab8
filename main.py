import psycopg2
import sys

from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._connect_to_db()

        self.setWindowTitle("Sсhedule")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        # Создаем объект QScrollArea и добавляем в него виджет
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.tabs)

        # Устанавливаем виджет с прокруткой в качестве главного виджета окна
        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(scroll_area)

        # self._create_shedule_tab("schedule")
        self._create_shedule_tab("Schedule")
        self._create_teachers_tab("Teachers")
        self._create_subjects_tab("Subjects")
        # self._create_teachers_tab("Subjects")
        # self._update_table()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="lab7",
                                     user="postgres",
                                     password="123",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_subjects_tab(self, tab_name):
        self.subjects_tab = QWidget()
        self.tabs.addTab(self.subjects_tab, tab_name)

        self.table_gbox1 = QGroupBox()

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shboxupdate = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shboxupdate)

        self.shbox1.addWidget(self.table_gbox1)

        self._create_subjects_table()

        self.update_shedule_button = QPushButton("Update")
        self.shboxupdate.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.subjects_tab.setLayout(self.svbox)

    def _create_teachers_tab(self, tab_name):
        self.teachers_tab = QWidget()
        self.tabs.addTab(self.teachers_tab, tab_name)

        self.table_gbox1 = QGroupBox()

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shboxupdate = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shboxupdate)

        self.shbox1.addWidget(self.table_gbox1)

        self._create_teachers_table()
        self._update_teachers()

        self.update_shedule_button = QPushButton("Update")
        self.shboxupdate.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.teachers_tab.setLayout(self.svbox)


    def _create_shedule_tab(self, tab_name):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, tab_name)

        self.table_gbox1 = QGroupBox("Monday")
        self.table_gbox2 = QGroupBox("Tuesday")
        self.table_gbox3 = QGroupBox("Wednesday")
        self.table_gbox4 = QGroupBox("Thursday")
        self.table_gbox5 = QGroupBox("Friday")
        self.table_gbox6 = QGroupBox("Saturday")
        self.table_gbox7 = QGroupBox("Sunday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()
        self.shbox4 = QHBoxLayout()
        self.shbox5 = QHBoxLayout()
        self.shbox6 = QHBoxLayout()
        self.shbox7 = QHBoxLayout()
        self.shboxupdate = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox4)
        self.svbox.addLayout(self.shbox5)
        self.svbox.addLayout(self.shbox6)
        self.svbox.addLayout(self.shbox7)
        self.svbox.addLayout(self.shboxupdate)

        self.shbox1.addWidget(self.table_gbox1)
        self.shbox2.addWidget(self.table_gbox2)
        self.shbox3.addWidget(self.table_gbox3)
        self.shbox4.addWidget(self.table_gbox4)
        self.shbox5.addWidget(self.table_gbox5)
        self.shbox6.addWidget(self.table_gbox6)
        self.shbox7.addWidget(self.table_gbox7)

        self._create_shedule_table()

        self.update_shedule_button = QPushButton("Update")
        self.shboxupdate.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)

    def _create_subjects_table(self):
        self.table13 = QTableWidget()
        self.table13.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table13.setColumnCount(1)
        self.table13.setHorizontalHeaderLabels(["Subject"])

        self._update_subjects()

        self.mvbox13 = QVBoxLayout()
        self.mvbox13.addWidget(self.table13)
        self.table_gbox1.setLayout(self.mvbox13)

        self.add_empty_record_button = QPushButton("Add Record")
        self.mvbox13.addWidget(self.add_empty_record_button)
        self.add_empty_record_button.clicked.connect(self._add_empty_record13)

    def _create_teachers_table(self):
        self.table12 = QTableWidget()
        self.table12.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table12.setColumnCount(2)
        self.table12.setHorizontalHeaderLabels(["Teacher", "Subject"])

        self._update_teachers()

        self.mvbox12 = QVBoxLayout()
        self.mvbox12.addWidget(self.table12)
        self.table_gbox1.setLayout(self.mvbox12)

        self.add_empty_record_button = QPushButton("Add Record")
        self.mvbox12.addWidget(self.add_empty_record_button)
        self.add_empty_record_button.clicked.connect(self._add_empty_record12)

    def _create_shedule_table(self):
        self.table1 = QTableWidget()
        self.table1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table1.setColumnCount(5)
        self.table1.setHorizontalHeaderLabels(["Subject", "Room_number", "Start_time", "Even_week", "Teacher"])


        self.table2 = QTableWidget()
        self.table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table2.setColumnCount(5)
        self.table2.setHorizontalHeaderLabels(["Subject", "Room_number", "Start_time", "Even_week", "Teacher"])

        self.table3 = QTableWidget()
        self.table3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table3.setColumnCount(5)
        self.table3.setHorizontalHeaderLabels(["Subject", "Room_number", "Start_time", "Even_week", "Teacher"])

        self.table4 = QTableWidget()
        self.table4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table4.setColumnCount(5)
        self.table4.setHorizontalHeaderLabels(["Subject", "Room_number", "Start_time", "Even_week", "Teacher"])

        self.table5 = QTableWidget()
        self.table5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table5.setColumnCount(5)
        self.table5.setHorizontalHeaderLabels(["Subject", "Room_number", "Start_time", "Even_week", "Teacher"])


        self.table6 = QTableWidget()
        self.table6.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table6.setColumnCount(5)
        self.table6.setHorizontalHeaderLabels(["Subject", "Room_number", "Start_time", "Even_week", "Teacher"])

        self.table7 = QTableWidget()
        self.table7.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table7.setColumnCount(5)
        self.table7.setHorizontalHeaderLabels(["Subject", "Room_number", "Start_time", "Even_week", "Teacher"])



        self._update_shedule()

        self.mvbox1 = QVBoxLayout()
        self.mvbox1.addWidget(self.table1)
        self.table_gbox1.setLayout(self.mvbox1)

        self.add_empty_record_button = QPushButton("Add Record")
        self.mvbox1.addWidget(self.add_empty_record_button)
        self.add_empty_record_button.clicked.connect(self._add_empty_record1)

        self.mvbox2 = QVBoxLayout()
        self.mvbox2.addWidget(self.table2)
        self.table_gbox2.setLayout(self.mvbox2)

        self.add_empty_record_button = QPushButton("Add Record")
        self.mvbox2.addWidget(self.add_empty_record_button)
        self.add_empty_record_button.clicked.connect(self._add_empty_record2)


        self.mvbox3 = QVBoxLayout()
        self.mvbox3.addWidget(self.table3)
        self.table_gbox3.setLayout(self.mvbox3)

        self.add_empty_record_button = QPushButton("Add Record")
        self.mvbox3.addWidget(self.add_empty_record_button)
        self.add_empty_record_button.clicked.connect(self._add_empty_record3)

        self.mvbox4 = QVBoxLayout()
        self.mvbox4.addWidget(self.table4)
        self.table_gbox4.setLayout(self.mvbox4)

        self.add_empty_record_button = QPushButton("Add Record")
        self.mvbox4.addWidget(self.add_empty_record_button)
        self.add_empty_record_button.clicked.connect(self._add_empty_record4)

        self.mvbox5 = QVBoxLayout()
        self.mvbox5.addWidget(self.table5)
        self.table_gbox5.setLayout(self.mvbox5)

        self.add_empty_record_button = QPushButton("Add Record")
        self.mvbox5.addWidget(self.add_empty_record_button)
        self.add_empty_record_button.clicked.connect(self._add_empty_record5)


        self.mvbox6 = QVBoxLayout()
        self.mvbox6.addWidget(self.table6)
        self.table_gbox6.setLayout(self.mvbox6)

        self.add_empty_record_button = QPushButton("Add Record")
        self.mvbox6.addWidget(self.add_empty_record_button)
        self.add_empty_record_button.clicked.connect(self._add_empty_record6)

        self.mvbox7 = QVBoxLayout()
        self.mvbox7.addWidget(self.table7)
        self.table_gbox7.setLayout(self.mvbox7)

        self.add_empty_record_button = QPushButton("Add Record")
        self.mvbox7.addWidget(self.add_empty_record_button)
        self.add_empty_record_button.clicked.connect(self._add_empty_record7)

    def _add_empty_record(self, table):

        rec = table.columnCount()
        print(rec)
        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                print(f'{j}')
                try:
                    if j == 0:

                        self.cursor.execute(
                        f"Update timetable set subject = '{table.item(i,j).text()}', room_number = '{table.item(i, j+1).text()}',  start_time = '{table.item(i, j+2).text()}', even_week = {table.item(i, j+3).text()}, teacher = '{table.item(i, j+4).text()}' Where day = 'Monday'")
                        self.conn.commit()
                        print("Запись успешно добавлена в базу данных.")
                except psycopg2.Error as e:
                    print("Ошибка при добавлении записи в базу данных:", e)
                    self.conn.rollback()


    def _add_empty_record13(self):
        self._add_empty_record(self.table13)

    def _add_empty_record12(self):
        self._add_empty_record(self.table12)

    def _add_empty_record1(self):
        self._add_empty_record(self.table1)

    def _add_empty_record2(self):
        self._add_empty_record(self.table2)

    def _add_empty_record3(self):
        self._add_empty_record(self.table3)

    def _add_empty_record4(self):
        self._add_empty_record(self.table4)

    def _add_empty_record5(self):
        self._add_empty_record(self.table5)

    def _add_empty_record6(self):
        self._add_empty_record(self.table6)

    def _add_empty_record7(self):
        self._add_empty_record(self.table7)

    def _update_subjects(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM subjects;")
        subjects = cursor.fetchall()
        self.table13.setRowCount(len(subjects))

        for i, subject in enumerate(subjects):
            for j, value in enumerate(subject):
                item = QTableWidgetItem(str(value))
                self.table13.setItem(i, j, item)

    def _update_teachers(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT t.full_name, t.subject FROM teachers t;")
        subjects = cursor.fetchall()
        self.table12.setRowCount(len(subjects))

        for i, subject in enumerate(subjects):
            for j, value in enumerate(subject):
                item = QTableWidgetItem(str(value))
                self.table12.setItem(i, j, item)

    def _update_shedule(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT t.subject, t.room_number, t.start_time, t.even_week, t.teacher FROM timetable t;")
        subjects = cursor.fetchall()
        self.table1.setRowCount(len(subjects))

        for i, subject in enumerate(subjects):
            for j, value in enumerate(subject):
                item = QTableWidgetItem(str(value))
                self.table1.setItem(i, j, item)


app = QApplication(sys.argv)
print(app)
win = MainWindow()
win.show()
sys.exit(app.exec_())