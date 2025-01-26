# ООП-моделі для об’єктів
## Клас для роботи з клапанами
class Valve:
    """
        Клас для роботи з характеристиками клапанів.

        Attributes:
            name (str): Назва клапана.
            article_number (str): Номер статті клапана.
    """
    def __init__(self, name: str, article_number: str):
        """
                Ініціалізує Valve з назвою та номером статті.

                Args:
                    name (str): Назва клапана.
                    article_number (str): Номер статті клапана.
        """
        self.name = name
        self.article_number = article_number