# https://stackoverflow.com/a/55650457/3187537
def make_labels(ax, boxplot):

    # Grab the relevant Line2D instances from the boxplot dictionary
    iqr = boxplot['boxes'][0]
    caps = boxplot['caps']
    med = boxplot['medians'][0]
    fly = boxplot['fliers'][0]
    avg = boxplot['means'][0]
    # The x position of the median line
    xpos = med.get_xdata()
    
    # Lets make the text have a horizontal offset which is some 
    # fraction of the width of the box
    xoff = 0.10 * (xpos[1] - xpos[0])

    # The x position of the labels
    xlabel = xpos[1] + xoff

    # The median is the y-position of the median line
    #print(med)
    median = med.get_ydata()[1]
    #print(median)
    
    # The mean 
    mean = avg.get_ydata()[1]
   
    # The 25th and 75th percentiles are found from the
    # top and bottom (max and min) of the box
    pc25 = iqr.get_ydata().min()
    pc75 = iqr.get_ydata().max()

    # The caps give the vertical position of the ends of the whiskers
    capbottom = caps[0].get_ydata()[0]
    captop = caps[1].get_ydata()[0]

    # Make some labels on the figure using the values derived above
    ax.text(xlabel, median,
            'Median = {:.2f}'.format(median), va='center')
    ax.text(xlabel, pc25,
            '25th percentile = {:.2f}'.format(pc25), va='center')
    ax.text(xlabel, pc75,
            '75th percentile = {:.2f}'.format(pc75), va='center')
    ax.text(xlabel, capbottom,
            'Min. value = {:.2f}'.format(capbottom), va='center')
    ax.text(xlabel, captop,
            'Max. value = {:.2f}'.format(captop), va='center')
    ax.text(xlabel, mean,
             'Avg. value = {:.2f}'.format(mean), va='center')
    #ax.text(xlabel, avg,
            # 'Avg. value = ', avg, va='center')

    # Many fliers, so we loop over them and create a label for each one
    #for flier in fly.get_ydata():
        #ax.text(1 + xoff, flier,
                #'Flier = {:6.3g}'.format(flier), va='center')
            
# Make the figure
red_diamond = dict(markerfacecolor='r', marker='D')
fig3, ax3 = plt.subplots(figsize=(16, 10))
ax3.set_title('Distribution of charges')

# Create the boxplot and store the resulting python dictionary
my_boxes = ax3.boxplot(dataframe['charges'], flierprops=red_diamond, showmeans=True, meanline = True)

# Call the function to make labels
make_labels(ax3, my_boxes)

plt.show()
