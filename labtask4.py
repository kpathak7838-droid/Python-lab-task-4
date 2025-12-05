import pandas as pd            # for reading CSV
import matplotlib.pyplot as plt  # for charts

# -----------------------------
# Task 1: Load the Dataset
# -----------------------------
print("Loading dataset...")
data = pd.read_csv("temperature.csv")     # Make sure the file is in the same folder
print("\nFirst 10 rows:")
print(data.head(10))                      # show first 10 rows

# -----------------------------
# Task 2: Data Cleaning
# -----------------------------
print("\nChecking missing values:")
print(data.isnull().sum())                # count missing values

# Filling missing temperature with average value 

if data['temperature'].isnull().sum() > 0:
    avg_temp = data['temperature'].mean()
    print("Mean temperature used:", avg_temp)
    data['temperature'].fillna(avg_temp, inplace=True)
else:
    print("No missing values, so mean is not needed.")


print("\nAfter cleaning (missing values removed):")
print(data.isnull().sum())


# -----------------------------
# Task 3: Line Plot
# -----------------------------
print("\nCreating line plot...")

plt.figure()                                 # new graph
plt.plot(data['date'], data['temperature'])  # simple line plot
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Over Time")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("line_plot.png")                 # save image
plt.close()

print("Saved as line_plot.png")

# -----------------------------
# Task 4: Bar Chart
# -----------------------------
print("\nCreating bar chart...")

# Convert date column to month name (easy group)
data['date'] = pd.to_datetime(data['date'])
data['month'] = data['date'].dt.month_name()

monthly_avg = data.groupby('month')['temperature'].mean()

plt.figure()
monthly_avg.plot(kind='bar')                 # simple bar chart
plt.xlabel("Month")
plt.ylabel("Average Temperature")
plt.title("Average Monthly Temperature")

plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()

print("Saved as bar_chart.png")

print("\nAll tasks completed successfully!")
# Bonus
plt.figure()
plt.scatter(data['date'], data['temperature'])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Scatter Plot of Temperature")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.close()
