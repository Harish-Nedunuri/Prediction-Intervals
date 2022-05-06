

# Visualization
import matplotlib.pyplot as  plt
def plot_array(data):
    plt.figure()
    plt.plot(data["actual"])
    plt.show()
    
def plot_prediction_intervals(upper,lower,mid):
    plt.figure()
    plt.plot(upper)
    plt.plot(mid)
    plt.plot(lower)
    plt.show()
    
    




