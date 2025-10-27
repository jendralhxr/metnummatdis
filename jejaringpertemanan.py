import networkx as nx

G = nx.Graph()
# G.add_node(1)
# G.add_edge(1, 1)  # self-loop
# nx.draw(G, with_labels=True)

def draw_graph(graph):
    node_colors = nx.get_node_attributes(graph, "color").values()
    edge_colors = nx.get_edge_attributes(graph, "color").values()
    # plt.figure(figsize=(width/12,height/12))
    nx.draw(
        graph,
        # nodes' param
        with_labels=True,
        node_size= 20,
        node_color=node_colors,
        font_size=8,
        # edges' param
        edge_color=edge_colors,
    )


mahasiswa = [
"Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena", 
"Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia", 
"Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya", 
"Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi", 
"Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar", 
"Kiky", "Sofia", "Varid", "Gaitsa"]
G.add_nodes_from(mahasiswa)

sekelompok= [
        ("Raveena", "Amelia"), ("Raveena", "Yuniar"), ("Yuniar", "Amelia"),
        ("Hizkia", "Maria"), ("Hizkia", "Sofia"), ("Sofia", "Maria"),
        ("Naufal", "Laudya"), ("Naufal", "Febriani"), ("Febriani", "Laudya"),
        ("Kenzy", "Wildan"), ("Wildan", "Hafiyyan"), ("Kenzy", "Hafiyyan"),
        ("Alimun", "Dany"), ("Dany", "Indra"), ("Indra", "Alimun"),
        ("Esthi", "Kiky"), ("Kiky", "Selvy"), ("Selvy", "Esthi"),
        ("Adrian", "Izzati"), ("Izzati", "Fanny"), ("Fanny", "Adrian"),
        ("Aquina", "Diva"), ("Diva", "Maya"), ("Maya", "Aquina"),
        ("Diah", "Gendis"), ("Gendis", "Angel"), ("Angel", "Diah"),
        ("Ophyng", "Aisyah"), ("Aisyah", "Naia"), ("Naia", "Ophyng"),
        ("Adinda", "Varid"), ("Varid", "Gaitsa"), ("Gaitsa", "Adinda"),
        ("Auliya", "Carissa"), ("Carissa", "Erik"), ("Erik", "Auliya"),
        ("Madina", "Via"), ("Maulida", "Madina"), ("Via", "Alfani"), 
        ("Madina", "Alfani"), ("Maulida", "Via"), ("Maulida", "Alfani")        
        ]

G.add_edges_from(sekelompok, color='red')

# asal daerah
akamsi = ["Yuniar", "Via", "Raveena", "Kenzy", "Esthi", "Alimun", "Amelia", 
          "Indra", "Madina", "Maulida", "Kiky"
    ]
jabodetabek = ["Sofia", "Maria", "Fanny", "Gaitsa", "Aisyah"]
platP= ["Angel", "Yuniar", ]
platS= ["Naia", "Izzati"]
platM= ["Dany", "Alimun"]
platN= ["Amelia", "Alfani"]
platAx= ["Adrian", "Raveena", "Selvy", "Fanny"]  

# 
sekos= ["Aisyah", "Naia"]

himasada= ["Dany", "Amelia", "Yuniar", "Kiky", "Esthi", "Raveena", "Naia", 
           "Wildan", "Selvy", "Via", "Madina", "Alfani", "Maulida"]

BEMfakultas= ["Indra", "Hafiyyan", "Varid", "Carissa", "Raveena"]

warkopbening= ["Raveena", "Yuniar", "Wildan", "Dany", "Maulida", "Izzati"]

skincaredanmakeup = ["Hizkia", "Kiky", "Yuniar", "Raveena", "Sofia", "Amelia"]

makanbareng = []

# lengkapi, koreksi, tambahkan sendiri klaster pertemanannya
# gunakan warna edge yang berbeda untuk tiap jenis klaster pertemanan
# buat fungsi untuk membuat koneksi pertemanan secara iteratif untuk anggota klaster

# Analisis
# 1) cari 3 orang yang konektivitasnya paling banyak
# 2) cari pasangan-pasangan yang paling jauh koneksinya
# 3a) bridge person. nx.betweenness_centrality(G)
# 3b) cari bridge person dengan koneksi paling sedikit 

########### tambahan dari prodi #####
SURVEI KEPUASAN TENGAH SEMESTER! 📣

Kepada seluruh Mahasiswa/i Program Studi Sains Data UPN "Veteran" Jawa Timur,
Kami mengundang partisipasi Anda dalam Survei Kepuasan Tengah Semester Ganjil 2025/2026. 📝
Tujuan survei ini adalah mengevaluasi kualitas proses pembelajaran (8 minggu berjalan) sebagai bahan perbaikan berkelanjutan (continuous improvement) dan penjaminan mutu prodi. 🚀

Partisipasi bersifat anonim dan suara Anda sangat penting! Mohon berikan jawaban jujur dengan skala penilaian 1–5. ⭐
Isi survei sekarang: ➡️ bit.ly/SETPP2526


































 

