


class Materiala:
    def __init__(self):
        print()

    def materialaEzabatu(self):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "DELETE FROM Ekipamendua WHERE materiala = 'Nike Air Zoom Pegasus 37';"
        cursor.execute(query)
        konexioa.commit()
        print("Ondo ezabatu da")