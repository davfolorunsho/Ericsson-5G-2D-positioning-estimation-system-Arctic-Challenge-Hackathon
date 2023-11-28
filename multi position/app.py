from flask import Flask, render_template, request
import numpy as np
from scipy.optimize import least_squares
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get uploaded files
    bs_file = request.files['bs_data']
    toa_file = request.files['toa_data']

    # Read data from uploaded CSV files
    bs_positions = np.genfromtxt(bs_file, delimiter=',')
    toa_data = np.genfromtxt(toa_file, delimiter=',')

    # Check if the checkbox for showing all positions is selected
    show_all_positions = 'show_all_positions' in request.form

    # Perform position estimation
    estimated_positions = perform_position_estimation(bs_positions, toa_data, show_all_positions)

    # Plot the results
    plot_path = plot_results(bs_positions, estimated_positions)

    # Render the HTML template with the plot
    return render_template('result.html', plot_path=plot_path, show_all_positions=show_all_positions)

def perform_position_estimation(bs_positions, toa_data, show_all_positions):
    # Number of base stations and time instants
    N_BS = bs_positions.shape[1]
    T = toa_data.shape[0]

    # Function to compute residuals for least squares optimization
    def residuals(params, anchors, toa_measurements):
        x, y = params
        d = np.sqrt((anchors[0, :] - x)**2 + (anchors[1, :] - y)**2)
        return d - toa_measurements

    # Least squares optimization for each time instant
    estimated_positions = np.zeros((T, 2))

    for t in range(T):
        reference_bs = bs_positions[:, 0]
        toa_diff = toa_data[t, :] - toa_data[t, 0]
        initial_position = reference_bs
        result = least_squares(residuals, initial_position, args=(bs_positions, toa_diff))
        estimated_positions[t, :] = result.x

    if not show_all_positions:
        # If not showing all positions, keep only the last estimated position
        estimated_positions = estimated_positions[-1:]

    return estimated_positions

def plot_results(bs_positions, estimated_positions):
    plt.figure(figsize=(8, 6))
    plt.scatter(bs_positions[0, :], bs_positions[1, :], marker='o', label='Base Stations', color='blue')

    if estimated_positions.shape[0] > 1:
        # If there are multiple estimated positions, plot them all
        plt.scatter(estimated_positions[:, 0], estimated_positions[:, 1], marker='x', label='Estimated Positions', color='red')
    else:
        # If there is only one estimated position, plot it
        plt.scatter(estimated_positions[0, 0], estimated_positions[0, 1], marker='x', label='Estimated Position', color='red')

    plt.title('2D Position Estimation')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.legend()
    plt.grid(True)

    # Save the plot to a BytesIO object
    img_bytes = BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    plt.close()

    # Convert BytesIO to base64 for HTML embedding
    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')

    return f'data:image/png;base64,{img_base64}'

if __name__ == '__main__':
    app.run(debug=True)
