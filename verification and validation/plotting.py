import plotly.graph_objs as go
from plotly.offline import plot

# Assuming you have lists or arrays containing epochs and corresponding accuracy values
epochs = [1, 2, 3, 4, 5]
accuracy = [0.85, 0.88, 0.90, 0.92, 0.93]

fig = go.Figure(data=go.Scatter(x=epochs, y=accuracy, mode='lines+markers'))
fig.update_layout(title='Epoch vs Accuracy', xaxis_title='Epochs', yaxis_title='Accuracy')
plot(fig, filename='epoch_vs_accuracy.html')
