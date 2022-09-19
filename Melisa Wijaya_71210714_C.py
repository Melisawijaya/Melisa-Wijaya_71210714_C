import json

jml_mhsw = int(input("Masukan Jumlah Mahasiswa Baru : "))

for i in range (jml_mhsw):
    data_mhsw = dict()
    bio_mhsw = dict()
    hobi_mhsw = dict()
    list_hobi = []
    nama_mhsw = str(input("Masukan Nama Anda : "))
    data_mhsw[nama_mhsw] = bio_mhsw
    jml_hobi = int(input("Masukan Jumlah Hobi : "))
    
    for j in range (jml_hobi):
         input_hobi = str(input("Masukan Hobi ke-" + str(j+1) + " : "))
         list_hobi.append(input_hobi)
         
    hobi_mhsw["Hobi"] = list_hobi
    pres_mhsw = str(input("Masukan Prestasi Anda : "))
    hobi_mhsw["Prestasi"] = pres_mhsw
    bio_mhsw["BioData"] = hobi_mhsw
    
    with open("datamahasiswa.json", "a") as file:
        json.dump(data_mhsw,file)
    
    print("=== Data Berhasil Dimasukkan ===")
    
    
    
    # data_mhsw[nama_mhsw] = dict()
    # biodata_mhsw = dict()
    # biodata_mhsw["Hobi"] = list_hobi.append(input_hobi)
    