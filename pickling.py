import pickle

imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1, 'Pulling the Rug'),
          (2, 'Psycho'),
          (3, 'Mayhem'),
          (4, 'Kentish town Waltz')
          ))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
  pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
  pickle.dump(even, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
  pickle.dump(odd, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
  pickle.dump(2998303, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)

with open("imelda.pickle", "rb") as imelda_pickled:
  imelda2 = pickle.load(imelda_pickled)
  even_list = pickle.load(imelda_pickled)
  odd_list = pickle.load(imelda_pickled)
  x = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, tract_list = imelda2

print(album)
print(artist)
print(year)
for track in tract_list:
  track_number, track_title = track
  print(track_number, track_title)

print('=' * 40)

for i in even_list:
  print(i)

print('=' * 40)

for i in odd_list:
  print(i)

print(x)

# pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")
