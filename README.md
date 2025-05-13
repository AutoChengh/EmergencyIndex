# Emergency Index (EI): A two-dimensional surrogate safety measure considering vehicles' interaction depth
Surrogate Safety Measures (SSMs) such as Time-to-Collision (TTC) are classic metrics that align with people's intuitive understanding of safety and have now become essential standards for assessing autonomous vehicles' safety.
- However, are there moments when you're unsure how to calculate TTC? For instance, during merging events or multi-angle conflict scenarios at complex intersections?
- Do you ever feel that the TTC calculation logic may be too simplistic for safety assessment? For example, in the situations shown in the Figure 1, is the risk truly the same?

<p align="center">
  <img src="assets/The_shortcoming_of_TTC.png" alt="animated" width="65%" height="65%"/>
</p>
<p align="center"><em>Figure 1: TTC-based indicators can measure the intensity of collision avoidance along the current closure direction. However, in 2D scenarios, evasive maneuvers are not limited to actions along the current closure direction. Evasive actions may involve various possibilities, such as lateral or combined maneuvers, which TTC-based indicators struggle to quantify effectively</em></p>

Don't worry! We will provide you with a new SSM—**Emergency Index (EI)**, which is applicable to various forms of conflicts in a 2D plane. It can assess more granular levels of risk and, like TTC, has an intuitive physical meaning.

Compared to previous indicators, we have considered a new dimension. EI utilizes the concept of Interaction Depth (InDepth), defined as the maximum depth at which two vehicles are projected to intrude into each other's safety region, representing the necessary adjustments for pre-collision states. The physical significance of EI lies in the rate of change in InDepth required for evasive actions, offering unique insights into crash avoidance strategies. Additionally, we propose a conflict detection model to comprehensively screen potential conflict vehicles.

<p align="center">
  <img src="assets/EI_framework.png" alt="animated" width="95%" height="95%"/>
</p>
<p align="center"><em>Figure 2: The framework of EI</em></p>

## News
- 🚀 **(2025/5)** Our new work [**MEI**] (https://github.com/AutoChengh/MEI)(Modified Emergency Index) is now open!

## Features
- **Identify Conflicting Vehicles**: For each vehicle and timestamp, the tool identifies nearby vehicles with potential conflicts.
- **Compute Safety Metrics**: Calculates TDM, InDepth, and EI for each conflicting vehicle pair.
- **Comprehensive Outputs**: Generates a CSV file containing the original data and four new columns:
  - `Q_Veh_ID`: IDs of vehicles in potential conflict.
  - `TDM (s)`: Time-to-Depth-Maximum, indicating remaining time for evasive actions.
  - `InDepth (m)`: Maximum depth of intrusion into each other's safety region.
  - `EI (m/s)`: Emergency Index, representing the intensity of evasive actions required.

## Input Data Format
The script requires a CSV file where each row corresponds to a vehicle's state at a specific timestamp. The following columns are expected:

| **Column Name**   | **Description**                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| **Time (s)**       | Timestamp (100 Hz sampling rate in the example data).                          |
| **Position X (m)** | X-coordinate of the vehicle's centroid position.                               |
| **Position Y (m)** | Y-coordinate of the vehicle's centroid position.                               |
| **Velocity (m/s)** | Speed of the vehicle in meters per second.                                     |
| **Heading**        | Heading angle of the vehicle in radians (-3.14 to 3.14).                       |
| **Length (m)**     | Length of the vehicle in meters.                                               |
| **Width (m)**      | Width of the vehicle in meters.                                                |
| **Vehicle ID**     | Unique ID for each vehicle.                                                    |

### Example Input File
The input file should follow the structure below:

| Time (s) | Position X (m) | Position Y (m) | Velocity (m/s) | Heading | Length (m) | Width (m) | Vehicle ID |
|----------|----------------|----------------|----------------|---------|------------|-----------|------------|
| 0.0      | 5.0            | 10.0           | 12.0           | 0.785   | 4.5        | 1.8       | 1          |
| 0.0      | 15.0           | 20.0           | 10.0           | 1.570   | 4.5        | 1.8       | 2          |

## Output Data Format
The processed file will retain the original columns and append the following four new columns:

| **Column Name**    | **Description**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| **Q_Veh_ID**        | IDs of vehicles in potential conflict with the subject vehicle.                |
| **TDM (s)**         | Time-to-Depth-Maximum, indicating remaining time for evasive actions.          |
| **InDepth (m)**     | Maximum depth of intrusion into each other's safety region.                    |
| **EI (m/s)**        | Emergency Index, representing the intensity of evasive actions required.       |

### Example Output File
| Time (s) | Position X (m) | ... | Q_Veh_ID | TDM (s)  | InDepth (m) | EI (m/s)  |
|----------|----------------|-----|----------|----------|-------------|-----------|
| 0.0      | 5.0            | ... | 2        | 1.2      | 0.3         | 1.5       |
| 0.0      | 15.0           | ... |          |          |             |           |

## Library Requirements
This script requires the following Python libraries:
- `pandas`
- `numpy`

Any version of these libraries should work.

## Usage
### 1. Prepare Your Environment

Step 1: Set up conda environment

```bash
# Create conda env
conda create -n EI python=3.10 pandas numpy -y
conda activate EI
```
Step: 2 Clone this git repo in an appropriate folder

```bash
git clone git@github.com:AutoChengh/EmergencyIndex.git
```

### 2. Prepare Your CSV Files

Prepare **CSV files** containing vehicle data as described in the Input Data Format section. Save the file in the [data folder](data/), or adjust the script's file path as needed.

### 3. Run the Script
Run the script using the following command:
```bash
python Emergency_Index.py
```
### 4. Adjust Parameters (Optional)
You can modify the following parameters in the command:

```bash
python Emergency_Index.py --D_0 'Your value' --D_safe 'Your_value'
```

  - `D_0`: Distance range of interest (default: 100)
  - `D_safe`:  Safe distance threshold (default: 0)

### 5. Check the Results
The processed file will be saved in the data folder (or the specified output path). The new file will include the calculated Q_Veh_ID, TDM (s), InDepth (m), and EI (m/s) columns.

## Author
Developed by Hao Cheng. For questions or feedback, feel free to contact me at chengh22@mails.tsinghua.edu.cn.
