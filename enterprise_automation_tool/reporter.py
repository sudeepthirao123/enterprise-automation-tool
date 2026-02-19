import matplotlib.pyplot as plt

def generate_report(data):
    print(data)

    plt.figure()
    plt.bar(data['Category'], data['Total'])
    plt.title('Sales by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Sales')
    plt.savefig('report.png')
    print("Visualization saved as report.png")