from direct.showbase.ShowBase import ShowBase

class GameTokoKue(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Memuat model 3D (panda adalah model bawaan untuk tes)
        self.kue = self.loader.loadModel("models/panda")
        self.kue.reparentTo(self.render)
        self.kue.setScale(0.25, 0.25, 0.25)
        self.kue.setPos(0, 10, 0) # Posisi kue di etalase

        # Mengatur posisi kamera
        self.camera.setPos(0, 0, 0)
        
        # Tambahkan fungsi interaksi mouse di sini nanti
        print("Toko Kue 3D siap dibangun!")

game = GameTokoKue()
game.run()
