import pandas as pd
import numpy as np
import pickle
import warnings
import matplotlib.pylab as plt
import seaborn as sns

def plot_graphic(path_direct):
	path_result = '../Качество расшифровки/Качество расшифровки - результаты/Результаты по качеству расш/'
	data_roads_ct = pd.read_excel(path_result + path_direct)
	arr_for_plot = data_roads_ct[data_roads_ct.index=='Сумма'].values[0][1:-3]
	columns_name = data_roads_ct.columns[1:-3]
	arr_fin_plot = []
	arr_name_col = []
	for i in range(len(arr_for_plot)):
		if (i+1)%3==0:
			arr_fin_plot.append(arr_for_plot[i])
			arr_name_col.append(columns_name[i-2])
	arr_fin_plot = np.asarray(arr_fin_plot)
	arr_name_col = np.asarray(arr_name_col)
	con = np.concatenate([arr_fin_plot.reshape(-1,1), arr_name_col.reshape(-1,1)], axis=1)
	data_frame_road = pd.DataFrame(con, columns=['OTN', 'NAME_ROAD'])
	data_frame_road.OTN = data_frame_road.OTN.values.astype(float)
	rel = data_frame_road[['NAME_ROAD', 'OTN']].sort_values(by='OTN', ascending=False)
	genres = rel.NAME_ROAD
	plt.rcParams.update(plt.rcParamsDefault)

	colors = sns.color_palette("summer", len(rel))
	plt.figure(figsize=(12,8))
	ax = sns.barplot(y = 'NAME_ROAD', x = 'OTN', data=rel, orient='h', palette=colors)
	ax.set_xlabel(xlabel='Подтверждение вины машиниста за нарушение', fontsize=16)
	ax.set_ylabel(ylabel='Региональные дирекции тяги', fontsize=16)
	ax.set_title(label='Качество расследования нарушений, выявленных при расшифровке носителей информации', fontsize=18, 
             y=1.03, fontweight='semibold')
	ax.set_yticklabels(labels = genres, fontsize=14)
	plt.show();