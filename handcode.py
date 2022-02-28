#!/usr/bin/python3

'''
Reads the 150MB+ file named 'all_gazepoints_max_invalid_per_subject10%.txt'
and splits the gazepoint data into individual CSVs (based on which film the
gazepoints data is associated with) named 'film_gazepoints.csv'.
'''

import pandas as pd

def read_txt_into_df():
  '''
  Reads the 150MB+ file named 'all_gazepoints_max_invalid_per_subject10%.txt'
  into a Pandas DataFrame.

  Inputs
    None
  Returns
    pd.DF containing data from file
  '''
  txt_filename = 'all_gazepoints_max_invalid_per_subject10%.txt'
  df = pd.read_csv(txt_filename, delim_whitespace=True)
  print(df.info())
  return df

def find_movie_names(df):
  '''
  From a DataFrame containing a 'film' column, returns all the unique films.

  Inputs
    df <Pandas.DataFrame>

  Returns
    numpy array containing our unique films
  '''
  return df.film.unique()

def write_gaze_to_film_file(df, list_of_movies):
  '''
  For all of the gazepoint data, splits into individual files based on which
  film it came from.

  Inputs
    df <Pandas.DataFrame>
    list_of_movies <numpy.array>

  Returns
    None.
  '''
  for movie in list_of_movies:
    single_movie_gazepoints = df[df['film'] == movie]
    movie_filename = movie + '_gazepoints.csv'
    single_movie_gazepoints.to_csv(movie_filename)

def main():
  '''
  Reads the 150MB+ file named 'all_gazepoints_max_invalid_per_subject10%.txt'
  and splits the gazepoints data into different files for each film.
  '''
  all_gazepoints = read_txt_into_df()
  movie_names = find_movie_names(all_gazepoints)
  write_gaze_to_film_file(all_gazepoints, movie_names)


if __name__ == '__main__':
  main()
