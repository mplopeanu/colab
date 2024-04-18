def plot_outl(df, serie, prag=3):
  '''Graficul cu outliers al unei serii Pandas
  - Functia primeste ca parametri un `df` (df=) si o coloanala/linie din `df` (serie)
  - Functia poate fi argumentata cu nume

  Parametrii functiei:
  df=
    (str) numele df-ului
  serie=
    (str) numele seriei pentru care se afiseaza outliers
  prag=
    (int) parametru optional, ce furnizeaza valoarea de prag pentru care se calculeaza 'outliers'

  Return:
  Functia intoarce un grafic cu outliers pentru seria respectiva
  
  Exemplu de utilizare:
  plot_outl(df, 'dist', 2)
  '''
  mean_ = df[serie].mean()
  std_ = df[serie].std()
  llimit = mean_-prag*std_
  ulimit = mean_+prag*std_

  #   df['outl'] = df.apply(lambda row:
#                         'red'
#                         if row[serie] < (mean_-2*std_)
#                         or row[serie] > (mean_+2*std_)
#                         else 'blue',
#                         axis=1)
#   df['outl_size'] = df.apply(lambda row:
#                         50
#                         if row[serie] < (mean_-2*std_)
#                         or row[serie] > (mean_+2*std_)
#                         else 10,
#                         axis=1)

  df[f'outl_{serie}'] = df.apply(lambda row:
                        'red'
                        if row[serie] < llimit
                        or row[serie] > ulimit
                        else 'blue',
                        axis=1)
  df[f'outl_size_{serie}'] = df.apply(lambda row:
                        50              
                        if row[serie] < llimit
                        or row[serie] > ulimit
                        else 10,
                        axis=1)

  color_list = df[f'outl_{serie}'].to_list()
  size_list = df[f'outl_size_{serie}'].to_list()

  fig, ax = plt.subplots(figsize=(10,5))
  fig.set_dpi(150)

  #---
  ax.plot(df[serie], linestyle='--', linewidth=1, color='grey')
  ax.scatter(df.index, df[serie], label=serie, linewidth=1, marker='o', facecolor=color_list, s=size_list)
  ax.axhline(df[serie].mean(), c='r', alpha=1, lw=1, ls='--')
  ax.axhline(ulimit, c='g', alpha=1, lw=1, ls='--')
  ax.axhline(llimit, c='g', alpha=1, lw=1, ls='--')


  m,s,b = ax.stem(df[serie], markerfmt='')
  s.set_alpha(0.25)
  s.set_linewidth(1)
  s.set_linestyle(':')
  #---
  ax.set_title(f'Line Plot with Outliers (seria: "{serie}")', fontsize=17, fontweight='bold', pad=20)
  # ax.set_title('Line Plot with Outliers')
  ax.grid(True, linestyle='--', linewidth=0.5)
  ax.set_ylim(df[serie].min() - 0.005, df[serie].max() + 0.005)

  ax.yaxis.set_major_formatter('{:.4f}'.format)
