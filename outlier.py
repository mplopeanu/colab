def plot_outl(df,serie):
  mean_ = df[serie].mean()
  std_ = df[serie].std()
  ulimit = mean_+2*std_
  llimit = mean_-2*std_

  df['outl'] = df.apply(lambda row:
                        'red'
                        if row[serie] < (mean_-2*std_)
                        or row[serie] > (mean_+2*std_)
                        else 'blue',
                        axis=1)
  df['outl_size'] = df.apply(lambda row:
                        50
                        if row[serie] < (mean_-2*std_)
                        or row[serie] > (mean_+2*std_)
                        else 10,
                        axis=1)

  color_list = df['outl'].to_list()
  size_list = df['outl_size'].to_list()

  fig, ax = plt.subplots(figsize=(10,5))
  fig.set_dpi(150)

  #---
  ax.plot(df[serie], linestyle='--', linewidth=1, color='grey')
  ax.scatter(df.index, df[serie], label='Distante', linewidth=1, marker='o', facecolor=color_list, s=size_list)
  ax.axhline(df[serie].mean(), c='r', alpha=1, lw=1, ls='--')
  ax.axhline(ulimit, c='g', alpha=1, lw=1, ls='--')
  ax.axhline(llimit, c='g', alpha=1, lw=1, ls='--')


  m,s,b = ax.stem(df[serie], markerfmt='')
  s.set_alpha(0.25)
  s.set_linewidth(1)
  s.set_linestyle(':')
  #---
  ax.set_title('Line Plot with Outliers', fontsize=17, fontweight='bold', pad=20)
  # ax.set_title('Line Plot with Outliers')
  ax.grid(True, linestyle='--', linewidth=0.5)
  ax.set_ylim(df[serie].min() - 0.005, df[serie].max() + 0.005)

  ax.yaxis.set_major_formatter('{:.4f}'.format)

  for x,y,label in zip(df.index,df[serie],df.no):
    ax.annotate(label, (x,y), ha='center',textcoords='offset points', xytext=(0,7), fontsize=7)

  ax.legend(loc='best', fontsize=3, prop={'style':'italic'},
            title="Legendă:", title_fontproperties={'weight':'bold'})
