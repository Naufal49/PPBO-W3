class Koordinat2D:
    x = 0
    y = 0

    def _init_(self, x, y):  
        self.x = x
        self.y = y


class Koordinat3D(Koordinat2D):
    z = 0

    def _init_(self, x, y, z):  
        super()._init_(x, y)  
        self.z = z 

    def tampilkan_koord(self):  
        print(f'x = {self.x}')  
        print(f'y = {self.y}')
        print(f'z = {self.z}')

titik1 = Koordinat3D(1, 2, 3)  
titik1.tampilkan_koord()