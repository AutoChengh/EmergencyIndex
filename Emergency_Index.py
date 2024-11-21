import pandas as pd
import numpy as np

def compute_Pc(x_A, y_A, x_B, y_B, h_A, h_B):
    delta_x = x_B - x_A
    delta_y = y_B - y_A
    sin_diff = np.sin(h_B - h_A)
    Pc = np.array([x_A, y_A]) + (delta_x * np.sin(h_B) - delta_y * np.cos(h_B)) / sin_diff * np.array([np.cos(h_A), np.sin(h_A)])
    return Pc

def compute_t_ac(x_A, y_A, x_B, y_B, h_A, h_B, v_A):
    delta_x = x_B - x_A
    delta_y = y_B - y_A
    sin_diff = np.sin(h_B - h_A)
    t_ac = (delta_x * np.sin(h_B) - delta_y * np.cos(h_B)) /(v_A * sin_diff)
    return t_ac

def compute_t_bc(x_A, y_A, x_B, y_B, h_A, h_B, v_B):
    delta_x = x_A - x_B
    delta_y = y_A - y_B
    sin_diff = np.sin(h_A - h_B)
    t_bc = (delta_x * np.sin(h_A) - delta_y * np.cos(h_A)) / (v_B * sin_diff)
    return t_bc

def compute_dac(w_A, h_A, h_B):
    numerator = w_A
    denominator = np.sqrt(1 - np.dot([np.cos(h_A), np.sin(h_A)], [np.cos(h_B), np.sin(h_B)])**2)
    return numerator / denominator

def compute_dbc(w_B, h_A, h_B):
    numerator = w_B
    denominator = np.sqrt(1 - np.dot([np.cos(h_A), np.sin(h_A)], [np.cos(h_B), np.sin(h_B)])**2)
    return numerator / denominator

def compute_A_bcC_i(Pc, dac, dbc, h_A, h_B, x_A, y_A, l_A, i):
    C = np.array([np.cos(h_A), np.sin(h_A)])
    if i == 1:
        return Pc - dbc / 2 * C + dac / 2 * np.array([np.cos(h_B), np.sin(h_B)]) - [x_A - l_A/2 * np.cos(h_A), y_A - l_A/2 * np.sin(h_A)]
    elif i == 2:
        return Pc + dbc / 2 * C + dac / 2 * np.array([np.cos(h_B), np.sin(h_B)]) - [x_A - l_A/2 * np.cos(h_A), y_A - l_A/2 * np.sin(h_A)]
    elif i == 3:
        return Pc - dbc / 2 * C - dac / 2 * np.array([np.cos(h_B), np.sin(h_B)]) - [x_A - l_A/2 * np.cos(h_A), y_A - l_A/2 * np.sin(h_A)]
    elif i == 4:
        return Pc + dbc / 2 * C - dac / 2 * np.array([np.cos(h_B), np.sin(h_B)]) - [x_A - l_A/2 * np.cos(h_A), y_A - l_A/2 * np.sin(h_A)]

def compute_B_bcC_j(Pc, dac, dbc, h_A, h_B, x_B, y_B, l_B, j):
    C = np.array([np.cos(h_B), np.sin(h_B)])
    if j == 1:
        return Pc - dbc / 2 * np.array([np.cos(h_A), np.sin(h_A)]) + dac / 2 * C - [x_B - l_B/2 * np.cos(h_B), y_B - l_B/2 * np.sin(h_B)]
    elif j == 2:
        return Pc + dbc / 2 * np.array([np.cos(h_A), np.sin(h_A)]) + dac / 2 * C - [x_B - l_B/2 * np.cos(h_B), y_B - l_B/2 * np.sin(h_B)]
    elif j == 3:
        return Pc - dbc / 2 * np.array([np.cos(h_A), np.sin(h_A)]) - dac / 2 * C - [x_B - l_B/2 * np.cos(h_B), y_B - l_B/2 * np.sin(h_B)]
    elif j == 4:
        return Pc + dbc / 2 * np.array([np.cos(h_A), np.sin(h_A)]) - dac / 2 * C - [x_B - l_B/2 * np.cos(h_B), y_B - l_B/2 * np.sin(h_B)]

def compute_theta_B_prime(v_A, h_A, v_B, h_B):
    velocity_diff = np.array([v_B * np.cos(h_B) - v_A * np.cos(h_A), v_B * np.sin(h_B) - v_A * np.sin(h_A)])
    theta_B_prime = velocity_diff / np.linalg.norm(velocity_diff)
    return theta_B_prime

def compute_D_t1(x_A, y_A, x_B, y_B, theta_B_prime):
    delta = np.array([x_B - x_A, y_B - y_A])
    D_t1 = np.linalg.norm(delta - np.dot(delta, theta_B_prime) * theta_B_prime)
    return D_t1

def compute_D_B_prime(x_A, y_A, x_B, y_B, theta_B_prime):
    delta = np.array([x_B - x_A, y_B - y_A])
    D_B_prime = -np.dot(delta, theta_B_prime)
    return D_B_prime

def compute_v_B_prime_norm(v_A, h_A, v_B, h_B):
    v_B_prime = np.array([v_B * np.cos(h_B) - v_A * np.cos(h_A), v_B * np.sin(h_B) - v_A * np.sin(h_A)])
    return np.linalg.norm(v_B_prime)

def compute_TDM(x_A, y_A, x_B, y_B, theta_B_prime, v_A, h_A, v_B, h_B):
    D_B_prime = compute_D_B_prime(x_A, y_A, x_B, y_B, theta_B_prime)
    v_B_prime_norm = compute_v_B_prime_norm(v_A, h_A, v_B, h_B)
    TDM = D_B_prime / v_B_prime_norm
    return TDM, D_B_prime, v_B_prime_norm

def compute_AA_l_A_w_A(x_A, y_A, h_A, l_A, w_A):
    cos_h_A, sin_h_A = np.cos(h_A), np.sin(h_A)
    AA1 = np.array([l_A / 2 * cos_h_A - w_A / 2 * -sin_h_A, l_A / 2 * sin_h_A - w_A / 2 * cos_h_A])
    AA2 = np.array([l_A / 2 * cos_h_A + w_A / 2 * -sin_h_A, l_A / 2 * sin_h_A + w_A / 2 * cos_h_A])
    AA3 = np.array([-l_A / 2 * cos_h_A - w_A / 2 * -sin_h_A, -l_A / 2 * sin_h_A - w_A / 2 * cos_h_A])
    AA4 = np.array([-l_A / 2 * cos_h_A + w_A / 2 * -sin_h_A, -l_A / 2 * sin_h_A + w_A / 2 * cos_h_A])
    return AA1, AA2, AA3, AA4

def compute_BB_l_B_w_B(x_B, y_B, h_B, l_B, w_B):
    cos_h_B, sin_h_B = np.cos(h_B), np.sin(h_B)
    BB1 = np.array([l_B / 2 * cos_h_B - w_B / 2 * -sin_h_B, l_B / 2 * sin_h_B - w_B / 2 * cos_h_B])
    BB2 = np.array([l_B / 2 * cos_h_B + w_B / 2 * -sin_h_B, l_B / 2 * sin_h_B + w_B / 2 * cos_h_B])
    BB3 = np.array([-l_B / 2 * cos_h_B - w_B / 2 * -sin_h_B, -l_B / 2 * sin_h_B - w_B / 2 * cos_h_B])
    BB4 = np.array([-l_B / 2 * cos_h_B + w_B / 2 * -sin_h_B, -l_B / 2 * sin_h_B + w_B / 2 * cos_h_B])
    return BB1, BB2, BB3, BB4

def compute_d_A(x_A, y_A, h_A, l_A, w_A, theta_B_prime):
    AA1, AA2, AA3, AA4 = compute_AA_l_A_w_A(x_A, y_A, h_A, l_A, w_A)
    d_A1 = np.linalg.norm(AA1 - np.dot(AA1, theta_B_prime) * theta_B_prime)
    d_A2 = np.linalg.norm(AA2 - np.dot(AA2, theta_B_prime) * theta_B_prime)
    d_A3 = np.linalg.norm(AA3 - np.dot(AA3, theta_B_prime) * theta_B_prime)
    d_A4 = np.linalg.norm(AA4 - np.dot(AA4, theta_B_prime) * theta_B_prime)
    return max(d_A1, d_A2, d_A3, d_A4)

def compute_d_B(x_B, y_B, h_B, l_B, w_B, theta_B_prime):
    BB1, BB2, BB3, BB4 = compute_BB_l_B_w_B(x_B, y_B, h_B, l_B, w_B)
    d_B1 = np.linalg.norm(BB1 - np.dot(BB1, theta_B_prime) * theta_B_prime)
    d_B2 = np.linalg.norm(BB2 - np.dot(BB2, theta_B_prime) * theta_B_prime)
    d_B3 = np.linalg.norm(BB3 - np.dot(BB3, theta_B_prime) * theta_B_prime)
    d_B4 = np.linalg.norm(BB4 - np.dot(BB4, theta_B_prime) * theta_B_prime)
    return max(d_B1, d_B2, d_B3, d_B4)

def compute_MFD(D_t1, d_A, d_B):
    return D_t1 - (d_A + d_B)

def main(file_path, output_file, D_0, π, γ, D_safe):
    df = pd.read_csv(file_path)

    df['P1_Veh_ID'] = ''
    df['P2_Veh_ID'] = ''
    df['Q_Veh_ID'] = ''

    df['TDM (s)'] = ''
    df['InDepth (m)'] = ''
    df['EI (m/s)'] = ''

    # Iterate over each row for calculation
    for i, row in df.iterrows():
        x_A, y_A, v_A, h_A, l_A, w_A = row.iloc[1:7]
        same_time_rows = df[(df[df.columns[0]] == row.iloc[0]) & (df.index != i)]

        P11_potential_indices = []
        P11_indices = []
        P12_potential_indices = []
        P12_indices = []
        P1_vehicle_ids = []

        P2_indices = []
        P2_vehicle_ids = []

        Q_vehicle_ids = []

        for j, same_time_row in same_time_rows.iterrows():
            x_B, y_B, v_B, h_B, l_B, w_B = same_time_row.iloc[1:7]
            vehicle_id_B = same_time_row['Vehicle ID']

            delta_x = x_B - x_A
            delta_y = y_B - y_A
            norm_delta = np.sqrt(delta_x ** 2 + delta_y ** 2)
            if norm_delta != 0:
                unit_vector = np.array([delta_x / norm_delta, delta_y / norm_delta])
                velocity_diff = np.array([v_B * np.cos(h_B) - v_A * np.cos(h_A), v_B * np.sin(h_B) - v_A * np.sin(h_A)])
                v_B_r = -np.dot(unit_vector, velocity_diff)
            else:
                v_B_r = 0

            v_B_r = round(v_B_r, 2)
            if v_B_r > 0:
                P2_indices.append(j)
                P2_vehicle_ids.append(vehicle_id_B)

            D = np.sqrt(delta_x ** 2 + delta_y ** 2)

            condition1 = D < D_0
            condition2 = (abs(h_B - h_A) <= γ) or (abs(h_B - h_A + π) <= γ) or (abs(h_B - h_A - π) <= γ) or (abs(abs(h_B - h_A) - π) <= γ)

            if condition1 and condition2:
                P12_potential_indices.append(j)
            elif condition1:
                P11_potential_indices.append(j)

        df.at[i, 'P2_Veh_ID'] = ';'.join(map(str, P2_vehicle_ids))

        for j in P11_potential_indices:
            same_time_row = df.iloc[j]
            x_B, y_B, v_B, h_B, l_B, w_B = same_time_row.iloc[1:7]

            Pc = compute_Pc(x_A, y_A, x_B, y_B, h_A, h_B)
            dac = compute_dac(w_A, h_A, h_B)
            dbc = compute_dbc(w_B, h_A, h_B)

            condition_i = any(np.dot([np.cos(h_A), np.sin(h_A)], compute_A_bcC_i(Pc, dac, dbc, h_A, h_B, x_A, y_A, l_A, i)) > 0 for i in range(1, 5))
            condition_j = any(np.dot([np.cos(h_B), np.sin(h_B)], compute_B_bcC_j(Pc, dac, dbc, h_A, h_B, x_B, y_B, l_B, j)) > 0 for j in range(1, 5))

            if condition_i and condition_j:
                P11_indices.append(j)

        for j in P12_potential_indices:
            same_time_row = df.iloc[j]

            x_B, y_B, v_B, h_B, l_B, w_B = same_time_row.iloc[1:7]
            delta_x = x_B - x_A
            delta_y = y_B - y_A

            P_1221 = np.dot([delta_x, delta_y], [np.cos(h_A), np.sin(h_A)])
            P_1222 = np.dot([-delta_x, -delta_y], [np.cos(h_B), np.sin(h_B)])
            P_1223 = np.abs(delta_x * np.cos(h_A) + delta_y * (-np.sin(h_A))) - (l_A + l_B) / 2
            P_123 = np.abs(delta_x * np.sin(h_A) - delta_y * np.cos(h_A)) - (w_A + w_B) / 2
            if (P_1221 >= 0 or P_1222 >= 0 or P_1223 <= 0) and P_123 <= 0:
                P12_indices.append(j)

        P1_indices = list(set(P11_indices) | set(P12_indices))
        for j in P1_indices:
            vehicle_id_B = df.iloc[j]['Vehicle ID']
            P1_vehicle_ids.append(vehicle_id_B)
        df.at[i, 'P1_Veh_ID'] = ';'.join(map(str, P1_vehicle_ids))

        Q_indices = list(set(P2_indices) & set(P1_indices))
        for j in Q_indices:
            vehicle_id_B = df.iloc[j]['Vehicle ID']
            Q_vehicle_ids.append(vehicle_id_B)
        df.at[i, 'Q_Veh_ID'] = ';'.join(map(str, Q_vehicle_ids))

        TDM_values = []
        InDepth_values = []
        EI_values = []

        for j in Q_indices:
            same_time_row = df.iloc[j]
            x_B, y_B, v_B, h_B, l_B, w_B = same_time_row.iloc[1:7]
            theta_B_prime = compute_theta_B_prime(v_A, h_A, v_B, h_B)
            D_t1 = compute_D_t1(x_A, y_A, x_B, y_B, theta_B_prime)
            TDM, D_B_prime, v_B_prime_norm = compute_TDM(x_A, y_A, x_B, y_B, theta_B_prime, v_A, h_A, v_B, h_B)
            d_A = compute_d_A(x_A, y_A, h_A, l_A, w_A, theta_B_prime)
            d_B = compute_d_B(x_B, y_B, h_B, l_B, w_B, theta_B_prime)

            MFD = compute_MFD(D_t1, d_A, d_B)
            InDepth = D_safe - MFD
            EI = InDepth / TDM

            if 0 < TDM < 5 and InDepth > -5 and EI > -10:
                TDM_values.append(round(TDM, 2))
                InDepth_values.append(round(InDepth, 2))
                EI_values.append(round(EI, 2))

        df.at[i, 'TDM (s)'] = ','.join(map(str, TDM_values))
        df.at[i, 'InDepth (m)'] = ','.join(map(str, InDepth_values))
        df.at[i, 'EI (m/s)'] = ','.join(map(str, EI_values))

    df.to_csv(output_file, index=False)
    print(f"finish：{output_file}")


if __name__ == "__main__":
    file_path = "data/Case1_angle_conflict_raw_input.csv"
    output_file = "data/Case1_angle_conflict_EI_output.csv"
    D_0 = 100  # The distance range of interest
    π = 3.14159
    γ = 0.01396  # If the angle difference between two vehicles is less than γ, it is considered a parallel situation (used in Condition P1)
    D_safe = 0  # D_safe is temporarily set to 0
    main(file_path, output_file, D_0, π, γ, D_safe)
