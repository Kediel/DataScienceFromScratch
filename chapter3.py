# Visualizing data
from __future__ import division
from collections import Counter
from collections import defaultdict
from matplotlib import pyplot as plt

# Chapter data
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
mentions = [500, 505]
years2 = [2013, 2014]
variance     = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]


def simple_line_chart():

    # Create a line chart, years on x-axis, gdp on y-axis
    plt.plot(years, gdp, color = "green", marker = "o", linestyle = "solid")

    # Add a title
    plt.title("Nominal GDP")

    # Add a label to the y-axis
    plt.ylabel("Billions of $")
    plt.show()

def simple_bar_chart():

    # Bars are by default width 0.8, so we'll add 0.1 to the left coordinates
    # So that each bar is centered
    xs = [i + 0.1 for i, _ in enumerate(movies)]

    # Plot bars with left x-coordinates [xs], heights [num_oscrars]
    plt.bar(xs, num_oscars)

    plt.ylabel("# of Academy Awards")
    plt.title("My Favorite Movies")

    # Label x-axis with movie names at bar centers
    plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
    plt.show()

def make_histogram():

    decile = lambda grade: grade // 10 * 10
    histogram = Counter(decile(grade) for grade in grades)

    plt.bar([x - 4 for x in histogram.keys()], histogram.values(), 8) # Shift each bar to the left by 4
    plt.axis([-5, 105, 0 ,5])       # x-axis from -5 to 105, y-axis from 0 to 5

    plt.xticks([10 * i for i in range(11)])
    plt.xlabel("Decile")
    plt.ylabel("# of Students")
    plt.title("Distribution of Exam 1 Grades")
    plt.show()

def misleading_y_axis(mislead = True):

    plt.bar([2012.6, 2013.6], mentions, 0.8)
    plt.xticks(years2)
    plt.ylabel("# of times I heard someone say 'data science'")

    # If you don't do this, matplotlib will label the x-axis 0, 1
    # and then add a +2.013e3 off in the corner (bad matplotlib ^.^)
    plt.ticklabel_format(useOffset = False)

    # Misleading y-axis only shows the part above 500
    if mislead:
        # misleading y-axis only shows the part above 500
        plt.axis([2012.5, 2014.5, 499, 506])
        plt.title("Look at the 'Huge' Increase!")
    else:
        plt.axis([2012.5, 2014.5, 0, 550])
        plt.title("Not So Huge Anymore.")
    plt.show()

def several_line_charts():

    total_error = [x + y for x, y in zip(variance, bias_squared)]
    xs = [i for i, _ in enumerate(variance)]

    # We can make multiple calls to plt.plot to show the multiple series on the same chart
    plt.plot(xs, variance,  "g-", label = "variance")   # Green solid line
    plt.plot(xs, bias_squared, "r-.", label="bias^2")  # Red dot-dashed line
    plt.plot(xs, total_error, "b:", label="total error")  # Blue dotted line

    # Because we've assigned labels to each series we can get a legend for free
    # loc=9 means "top center"
    plt.legend(loc=9)
    plt.xlabel("model complexity")
    plt.title("The Bias-Variance Tradeoff")
    plt.show()

def scatterplots():

    plt.scatter(friends, minutes)

    # Label each point
    for label, friend_count, minute_count in zip(labels, friends, minutes):

        plt.annotate(label,
                     xy =(friend_count, minute_count),  # Put the label with its point but slightly offset
                     xytext=(5, -5),
                     textcoords="offset points")

    plt.title("Daily Minutes vs. Number of Friends")
    plt.xlabel("# of friends")
    plt.ylabel("Daily minutes spent on the site")
    plt.show()

def scatterplot_axes(equal_axes = False):

        plt.scattter(test_1_grades, test_2_grades)
        plt.title("Axes aren't comparable")
        plt.xlabel("Test 1 grade")
        plt.ylabel("Test 2 grade")
        plt.show()

def pie_chart():
    plt.pie([0.95, 0.05], labels=["Uses pie charts", "Knows better"])

    # make sure pie is a circle and not an oval
    plt.axis("equal")
    plt.show()

if __name__ == "__main__":

    # Test each function/method
    simple_line_chart()
    simple_bar_chart()
    make_histogram()
    misleading_y_axis(True)
    misleading_y_axis(False)
    several_line_charts()
    scatterplots()
    scatterplot_axes(True)
    scatterplot_axes(False)
    pie_chart()