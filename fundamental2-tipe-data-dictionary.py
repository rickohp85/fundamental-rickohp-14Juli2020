"""
TIPE DATA DICTIONARY
"""

kamus = {}
kamus_jawa_inggris = {'siji':'one', 'loro':'two', 'telu':'three', 'papat':'four'}
print(kamus_jawa_inggris)

print('\nDATA INI DIKIRIMKAN SERVER GOJEK UNTUK MEMBERIKAN INFO DRIVER DI SEKITAR PEMAKAI APLIKASI')
data_dari_server_gojek = {
    'tanggal' : '2020-07-24',
    'driver_list' : [{'nama' : 'Paijo', 'jarak' : '10'},
                     {'nama' : 'Tukijo', 'jarak' : '25'},
                     {'nama' : 'Poniman', 'jarak' : '34'},
                     {'nama' : 'Sarijo', 'jarak' : '47'}]
}
print(data_dari_server_gojek)
print(f"Driver di sekitar sini{data_dari_server_gojek['driver_list']}")
print(f"Driver di sekitar sini Pak {data_dari_server_gojek['driver_list'][1]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][1]['jarak']} meter")
