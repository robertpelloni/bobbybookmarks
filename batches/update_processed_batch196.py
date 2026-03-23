import sqlite3

data = [
    ('https://www.google.com/search?aqs=edge.0.0i67j0i512l7.383j0j1&ie=UTF-8&oq=Cynomorium&q=cynomorium&sec_act=d&sourceid=chrome', 'Guides & Industry Trends', 'Cynomorium (Maltese Mushroom)', 'A parasitic desert plant used historically in traditional medicine as an aphrodisiac and "Yang tonic" to improve stamina and digestive health.', 'botany, supplements, traditional-medicine, cynomorium, aphrodisiac', 'Traditional "Yang tonic," sexual health/libido support, fatigue reduction, antioxidant properties.'),
    ('https://www.google.com/search?aqs=edge.0.0i433i512j0i512l4j0i131i433i512j0i512l2.159j0j1&ie=UTF-8&oq=Fadogia+Agrestis&q=fadogia+agrestis&sec_act=sr&sourceid=chrome&sxsrf=ADLYWILnWF3oH6jH_FpbbQpNvlGblW3ecg:1735575079653', 'Guides & Industry Trends', 'Fadogia Agrestis', 'A West African shrub popular in biohacking communities for its traditional use as an aphrodisiac and its potential to support testosterone levels.', 'botany, supplements, biohacking, testosterone, fadogia', 'Testosterone support potential, libido enhancement, athletic recovery supplement, traditional anti-inflammatory use.'),
    ('https://www.google.com/search?aqs=edge.0.0i512l2j0i22i30l2j0i22i30i457j0i22i30l2j0i390.479j0j1&ie=UTF-8&oq=Deer+Antler+Velvet+Powder&q=deer+antler+velvet+powder&sec_act=d&sourceid=chrome', 'Guides & Industry Trends', 'Deer Antler Velvet Powder', 'A supplement derived from the pre-calcified cartilaginous tissue of deer antlers, rich in IGF-1 growth factors and joint-supporting compounds.', 'supplements, biohacking, recovery, igf-1, joint-health', 'Natural IGF-1 source, glucosamine/chondroitin content, athletic performance recovery, immune system support.'),
    ('https://www.google.com/search?aqs=edge.0.0i512l3j0i457i512j0i512l2j0i390l2j69i64.471j0j1&ie=UTF-8&oq=Gorontula+Fruit&q=gorontula+fruit&sourceid=chrome', 'Guides & Industry Trends', 'Gorontula Fruit', 'A sweet, chewy fruit native to Northern Nigeria known as "African Chewing Gum," traditionally prized for supporting female reproductive health and fertility.', 'botany, supplements, traditional-medicine, women-health, nutrition', 'Vaginal hydration/lubrication support, fertility/hormone balance traditions, high dietary fiber, antioxidant/Vitamin C density.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf, score in [(d[0], d[1], d[2], d[3], d[4], d[5], 10) for d in data]:
    cursor.execute('''
        INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level, innovation_score)
        VALUES (?, ?, ?, ?, ?, ?, 'borg', ?)
        ON CONFLICT(url) DO UPDATE SET
            category=excluded.category,
            short_description=excluded.short_description,
            long_description=excluded.long_description,
            tags=excluded.tags,
            main_features=excluded.main_features,
            research_level='borg',
            innovation_score=excluded.innovation_score
    ''', (url, cat, sd, ld, tags, mf, score))
conn.commit()
conn.close()
print('Successfully injected batch 156.')