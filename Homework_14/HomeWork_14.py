"""
� ������������ ���� ���� ����� (���������).
������ ���� ����� ����� ��������������:
���
����
��������    (int �� 1 �� 100. ��������� �������� 100)
����        (int �� 1 �� 10. ��������� �������� 1)
��������    (int �� 1 �� 10. ��������� �������� 1)
��������    (int �� 1 �� 10. ��������� �������� 1)
"""


class Units:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.dexterity = 1
        self.intelligence = 1

    def healing(self):
