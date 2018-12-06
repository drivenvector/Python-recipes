# Adding count in % in the bar charts
# For adding count on top of bar charts, modify the code given here: https://stackoverflow.com/questions/31749448/how-to-add-percentages-on-top-of-bars-in-seaborn
ax = haberman['survival_status'].value_counts().plot(kind='bar', figsize=(10,7),
                                         fontsize=13);
ax.set_alpha(0.8)
ax.set_title("Patients Survived vs Not Survived", fontsize=18)
ax.set_ylabel("Count", fontsize=18);
#ax.set_yticks([0, 5, 10, 15, 20])
ax.set_xticklabels(['Survived','Not Survived'], rotation=0, fontsize=11)

# create a list to collect the plt.patches data
totals = []

# find the values and append to list
for i in ax.patches:
    totals.append(i.get_height())

# set individual bar lables using above list
total = sum(totals)

# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    #ax.text(i.get_x()-.03, i.get_height()+.5, \
     #       str(round((i.get_height()/total)*100, 2))+'%', fontsize=15,
      #          color='dimgrey')
    ax.text(i.get_x()+.12, i.get_height()-14, \
            str(round((i.get_height()/total)*100, 2))+'%', fontsize=22,
                color='white')
                
                
