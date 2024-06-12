from bar_kesehatan import KesehatanBar

class Character:
    def __init__(self, nama: str, kesehatan: int, senjata) -> None:
        self.nama = nama
        self.kesehatan = kesehatan
        self.kesehatan_max = kesehatan
        self.senjata = senjata
    
    def serangan(self, target) -> None:
        target.kesehatan -= self.senjata.kekuatan
        target.kesehatan = max(target.kesehatan, 0)
        target.bar_kesehatan.update()
        print(f"{self.nama} menyerang {target.nama} dengan {self.senjata.nama}, menyebabkan {self.senjata.kekuatan} kerusakan")
        
class pahlawan(Character):
    def __init__(self, nama: str, kesehatan: int, senjata) -> None:
        super().__init__(nama, kesehatan, senjata)
        self.default_senjata = self.senjata
        self.bar_kesehatan = KesehatanBar(self, color="green")
    
    def equip(self, senjata) -> None:
        self.senjata = senjata
        print(f"{self.nama} menggunakan {self.senjata.nama}!")
    
    def drop(self) -> None:
        print(f"{self.nama} menurunkan {self.senjata.nama}!")
        self.senjata = self.default_senjata
        
class Musuh(Character):
    def __init__(self, nama: str, kesehatan: int, senjata) -> None:
        super().__init__(nama, kesehatan, senjata)
        self.bar_kesehatan = KesehatanBar(self, color="red")
