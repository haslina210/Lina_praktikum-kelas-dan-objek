# mendefinisikan kelas
# nama file : Tugas2Lingkaran.py

class Lingkaran(object):
   def __init__(self, p, r):
      self.phi = p
      self.jarijari = r      
   def hitungKeliling(self):
      return self.phi * self.jarijari * 2

def main():
   # membuat objek pertama
   ling1 = Lingkaran(3.14, 9)

   # menggunakan objek pertama
   print('Objek ling1')
   print('phi\t: ', ling1.phi)
   print('jari\t: ', ling1.jarijari)
   print('Keliling\t= ', ling1.hitungKeliling())

   # membuat objek kedua
   ling2 = Lingkaran(3.14, 14)

   # menggunakan objek kedua
   print("\nObjek kotak2")
   print("phi\t: ", ling2.phi)
   print("jari\t: ", ling2.jarijari)
   print("Keliling\t= ", ling2.hitungKeliling())

if __name__ == "__main__":
   main()
