# mendefinisikan kelas
# nama file : Tugas1Lingkaran.py

class Lingkaran(object):
   def __init__(py, p, r):
      py.phi = p
      py.jarijari = r      
   def hitungLuas(py):
      return py.phi * py.jarijari **2

def main():
   # membuat objek pertama
   Lingkaran1 = Lingkaran(3.14, 7)

   # menggunakan objek pertama
   print('Objek ling1')
   print('phi\t: ', Lingkaran1.phi)
   print('jari\t: ', Lingkaran1.jarijari)
   print('Luas\t= ', Lingkaran1.hitungLuas())

   # membuat objek kedua
   Lingkaran2 = Lingkaran(3.14, 10)

   # menggunakan objek kedua
   print("\nObjek Lingkaran2")
   print("phi\t: ", Lingkaran2.phi)
   print("jari\t: ", Lingkaran2.jarijari)
   print("Luas\t= ", Lingkaran2.hitungLuas())

if __name__ == "__main__":
   main()
